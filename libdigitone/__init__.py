import sound
import sysex
import logging

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :> %(message)s', level=logging.DEBUG)

    file = '../blank_patch.syx'
    sysex = sysex.parse(sysex.decode(file))
    patch = sound.Sound(sysex)
    logging.debug('Name:    {}'.format(patch.name_to_string()))
    logging.debug('Tags:    {}'.format(patch.tag_list()))
    logging.debug('Data:    {}'.format(patch.param_to_dict()))
    logging.debug('Algo     {}'.format(patch.param('algorithm')))
    logging.debug('EOM:     {}'.format(patch.eom))