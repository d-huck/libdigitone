import parser
import sound
import logging

if __name__ == '__main__':
    # logging.basicConfig(format='%(asctime)s :: %(levelname)s :> %(message)s', level=logging.INFO)

    file = '../blank_patch.syx'
    sysex = parser.parse(file)
    patch = sound.Sound(sysex)
    logging.debug('Name:    {}'.format(patch.name_to_string()))
    logging.debug('Tags:    {}'.format(patch.tag_list()))
    patch.param_list()
    logging.debug('EOM:     {}'.format(patch.eom))