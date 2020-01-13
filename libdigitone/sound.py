from .constants import *
from binascii import unhexlify
import logging


class Sound:

    def __init__(self, patch):
        """ Breaks a patch into it's component sections.

        :param patch: Expects a single patch as a full sysex patch message.
        """

        # Check data type
        if patch[int(0x14f):int(0x151)] != [b'02', b'48']:
            logging.debug(patch[int(0x150):int(0x152)])
            raise TypeError("This is not the correct patch size! Data is probably corrupt")

        # Separate the key component sections of the patch
        self.prefix = patch[:int(0x05)]
        self.meta = patch[int(0x05):int(0x0a)]
        self.unspec = patch[int(0x0a):int(0x12)]
        self.tags = patch[int(0x12):int(0x18)]
        self.name = patch[int(0x18):int(0x29)]
        self.data = patch[int(0x29):int(0x14e)]
        self.eom = patch[int(0x14e):]

    @property
    def tag_list(self):
        """ Label the tags on a particular sound into human readable format

        :return: list of tags associated with the patch
        """

        tag_msg = b''.join(self.tags[0:1] + self.tags[2:]).decode('utf-8')
        _tags = []
        for i in range(len(tag_msg)):
            if tag_msg[i] in TAG_LOOK[str(i)].keys():
                _tags = _tags + TAG_LOOK[str(i)][tag_msg[i]]

        return _tags

    # TODO: What exactly is this good for again?
    def param_list(self):
        """ Scan the parameter locations and return a human readable value
            for each of the parameters.

        :return: human readable strings of the parameter values
        """

        for para in PARAM:
            param_data = b''
            for byte in PARAM_LOOK[para].split():
                param_data += self.data[int(byte, 16)]

            # logging.debug('{}: {}'.format(para, param_data))

    @property
    def param_to_dict(self):
        """ Create a dictionary with all of the parameter values.

        :return: dictionary of the parameter values
        """

        param_data = {}
        for para in PARAM:
            param_data[para] = self.param(para)

        return param_data

    def param(self, parameter):
        """ Return the value of a single parameter.

        :parameter: which parameter to retrieve a value from
        :return: the value of an individual parameter
        """

        # for param in PARAM:
        if len(PARAM_LOOK[parameter]) == 1:
            return int(self.data[int(PARAM_LOOK[parameter][0], 16)], 16)

        elif len(PARAM_LOOK[parameter]) == 3:
            neg_bit = PARAM_LOOK[parameter][0]
            neg_byte = '{:08b}'.format(int(self.data[int(PARAM_LOOK[parameter][1], 16)], 16))
            value = int(self.data[int(PARAM_LOOK[parameter][2], 16)], 16)
            if neg_byte[neg_bit] == '0':
                return value
            else:
                return value - 128
        # 3-byte parameters. 'b', 'lfo' and 'harm' behave differently than other functions
        elif len(PARAM_LOOK[parameter]) == 4:
            flag_bit = PARAM_LOOK[parameter][0]
            flag_byte = '{:08b}'.format(int(self.data[int(PARAM_LOOK[parameter][1], 16)], 16))
            msb_value = int(self.data[int(PARAM_LOOK[parameter][2], 16)], 16)
            lsb_value = int(self.data[int(PARAM_LOOK[parameter][3], 16)], 16)

            if parameter == 'b':
                msb_value = msb_value * 128
                if flag_byte[flag_bit] == '1':
                    lsb_value = int((lsb_value + 127) * (64 / 127))
                else:
                    lsb_value = int((64 / 127) * lsb_value)
                return int(((msb_value) + lsb_value))

            elif 'lfo' in parameter:
                lsb_value = (100 / 127) * lsb_value
                if flag_byte[flag_bit] == '0':
                    msb_value = (msb_value * 2) - 128
                else:
                    msb_value = (msb_value * 2) - 127
                return round(msb_value + (lsb_value/100), 2)

            elif parameter == 'harm':
                msb_value = msb_value - 63
                if flag_byte[flag_bit] == '0':
                    lsb_value = int((50 / 127) * lsb_value)
                    return round(msb_value + (lsb_value / 100))
                else:
                    lsb_value = int((50 / 127) * lsb_value + 50)
                    return round(msb_value + (lsb_value / 100))

            # every other 3-byte function
            else:
                if flag_byte[flag_bit] == '0':
                    lsb_value = int((50 / 127) * lsb_value)
                    return round(msb_value + (lsb_value / 100))
                else:
                    lsb_value = int((50 / 127) * lsb_value + 50)
                    return round(msb_value + (lsb_value / 100))

    def name_to_string(self):
        """ Convert the name section into a human readable string

        :return: the name of a patch as a human readable string
        """

        name = unhexlify(b''.join(self.name)).decode('utf-8').strip('\x00')
        return name


if __name__ == '__main__':
    print(TAG_LOOK, TAGS, PARAM, PARAM_LOOK)
