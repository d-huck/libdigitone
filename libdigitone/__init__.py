import parser
import sound

if __name__ == '__main__':
    file = '../blank_patch.syx'
    sysex = parser.parse(file)
    patch = sound.Sound(sysex)
    print('Name:    {}'.format(patch.name_to_string()))
    print('Tags:    {}'.format(patch.tag_list()))
    print('Data:    {}'.format(patch.data))
    print('EOM:     {}'.format(patch.eom))