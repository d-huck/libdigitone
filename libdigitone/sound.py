from .constants import *
from binascii import unhexlify
import logging

# TODO: Pickle dictionaries and such
#
#       After the libraries get finalized in the doc, they should be pickled
#       and opened as a dictionary where they are needed instead of holding them
#       inside of a .py file, plaintext.


class Sound:

    def __init__(self, patch):
        """ Breaks a patch into it's component sections.

        :param patch: Expects a single patch as a full sysex patch message.
        """

        # Check data type
        if patch[int(0x150):int(0x152)] != [b'02', b'49']:
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

    def param_list(self):
        """ Scan the parameter locations and return a human readable value
            for each of the parameters.

        :return: human readable strings of the parameter values
        """

        # TODO: Parsing of parameter data that uses 2 or three bytes

        for para in PARAM:
            param_data = b''
            for byte in PARAM_LOOK[para].split():
                param_data += self.data[int(byte, 16)]

            logging.debug('{}: {}'.format(para, param_data))

    @property
    def param_to_dict(self):
        """ Create a dictionary with all of the parameter values.

        :return: dictionary of the parameter values
        """
        # TODO: Parsing of parameter data that uses 2 or three bytes

        param_data = {}
        for para in PARAM:
            param_data[para] = []
            for byte in PARAM_LOOK[para]:
                param_data[para].append(self.data[int(byte, 16)])

        return param_data

    def param(self, parameter):
        """ Return the value of a single parameter.

        :param parameter: which parameter to retrieve a value from
        :return: the value of an individual parameter
        """

        values = []
        for byte in PARAM_LOOK[parameter]:
            values.append(self.data[int(byte, 16)])

        return values

    # TODO: Figure out what the fuck I was thinking here...
    def param_(self, parameter):
        pass

    def name_to_string(self):
        """ Convert the name section into a human readable string

        :return: the name of a patch as a human readable string
        """

        name = unhexlify(b''.join(self.name)).decode('utf-8').strip('\x00')
        return name


if __name__ == '__main__':
    print(TAG_LOOK, TAGS, PARAM, PARAM_LOOK)
