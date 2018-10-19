from constants import TAG_LOOK, PARAM, PARAM_LOOK
from binascii import hexlify, unhexlify
import logging

logging.basicConfig(format='%(asctime)s :: %(levelname)s :> %(message)s', level=logging.DEBUG)


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
        self.prefix = patch[:int(0x0A)]
        self.unspec = patch[int(0x0a):int(0x12)]
        self.tags = patch[int(0x12):int(0x18)]
        self.name = patch[int(0x18):int(0x29)]
        self.data = patch[int(0x29):int(0x14e)]
        self.eom = patch[int(0x14e):]

    def tag_list(self):
        tag_msg = b''.join(self.tags[0:1] + self.tags[2:]).decode('utf-8')
        _tags = []

        for i in range(len(tag_msg)):
            if tag_msg[i] in TAG_LOOK[str(i)].keys():
                _tags = _tags + TAG_LOOK[str(i)][tag_msg[i]]

        return _tags

    def param_list(self):
        for para in PARAM:
            if len(PARAM_LOOK[para]) > 4:
                param_data = b''
                for byte in PARAM_LOOK[para].split():
                    param_data += self.data[int(byte, 16) - int(0x29)]
            else:
               param_data = self.data[int(PARAM_LOOK[para], 16) - int(0x29)]

            logging.debug('{}: {}'.format(para, param_data))

    def name_to_string(self):
        name = unhexlify(b''.join(self.name)).decode('utf-8').strip('\x00')
        return name


if __name__ == '__main__':
    with open('../blank_patch.syx', 'rb') as sysex:
        patches = hexlify(sysex.read())
        patch = Sound(patches)
        # print('Prefix:  {}'.format(patch.prefix))
        print('Name:    {}'.format(patch.name_to_string()))
        print('Tags:    {}'.format(patch.tag_list()))
        print('Data:    {}'.format(patch.data))
        print('EOM:     {}'.format(patch.eom))