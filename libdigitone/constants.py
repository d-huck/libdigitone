# TODO: PICKLE THIS SHIT

TAGS = (
        'KICK', 'SNAR', 'DEEP', 'BRAS', 'STRI', 'PERC', 'HHAT', 'CYMB', 'EVOL', 'EXPR',
        'BASS', 'LEAD', 'PAD', 'TXTR', 'CRD', 'SFX', 'ARP', 'METL', 'ACOU', 'ATMO',
        'NOIS', 'GLCH', 'HARD', 'SOFT', 'DARK', 'BRGT', 'UNTG', 'EPIC', 'FAIL', 'LOOP',
        'MINE', 'FAV'
       )

# TODO: Change TAG_LOOK to bit location lookup a la 2-byte parameters
TAG_LOOK = {
            '0': {
                  '1': [TAGS[23]],
                  '2': [TAGS[31]],
                  '3': [TAGS[23], TAGS[31]]
                 },
            '1': {
                  '4': [TAGS[7]],
                  '8': [TAGS[15]],
                  'c': [TAGS[7], TAGS[15]]
                 },
            '2': {
                  '1': [TAGS[28]],
                  '2': [TAGS[29]],
                  '3': [TAGS[28], TAGS[29]],
                  '4': [TAGS[30]],
                  '5': [TAGS[30], TAGS[28]],
                  '6': [TAGS[29], TAGS[30]],
                  '7': [TAGS[28], TAGS[29], TAGS[30]]
                 },
            '3': {
                  '1': [TAGS[24]],
                  '2': [TAGS[25]],
                  '3': [TAGS[24], TAGS[25]],
                  '4': [TAGS[26]],
                  '5': [TAGS[24], TAGS[26]],
                  '6': [TAGS[25], TAGS[26]],
                  '7': [TAGS[24], TAGS[25], TAGS[26]],
                  '8': [TAGS[27]],
                  '9': [TAGS[24], TAGS[27]],
                  'a': [TAGS[25], TAGS[27]],
                  'b': [TAGS[24], TAGS[25], TAGS[27]],
                  'c': [TAGS[26], TAGS[27]],
                  'd': [TAGS[24], TAGS[25], TAGS[27]],
                  'e': [TAGS[24], TAGS[26], TAGS[27]],
                  'f': [TAGS[24], TAGS[25], TAGS[26], TAGS[27]]
                 },
            '4': {
                  '1': [TAGS[20]],
                  '2': [TAGS[21]],
                  '3': [TAGS[20], TAGS[21]],
                  '4': [TAGS[22]],
                  '5': [TAGS[20], TAGS[22]],
                  '6': [TAGS[21], TAGS[22]],
                  '7': [TAGS[20], TAGS[21], TAGS[22]]
                 },
            '5': {
                  '1': [TAGS[16]],
                  '2': [TAGS[17]],
                  '3': [TAGS[16], TAGS[17]],
                  '4': [TAGS[18]],
                  '5': [TAGS[16], TAGS[18]],
                  '6': [TAGS[17], TAGS[18]],
                  '7': [TAGS[16], TAGS[17], TAGS[18]],
                  '8': [TAGS[19]],
                  '9': [TAGS[16], TAGS[19]],
                  'a': [TAGS[17], TAGS[19]],
                  'b': [TAGS[16], TAGS[17], TAGS[19]],
                  'c': [TAGS[18], TAGS[19]],
                  'd': [TAGS[16], TAGS[17], TAGS[19]],
                  'e': [TAGS[16], TAGS[18], TAGS[19]],
                  'f': [TAGS[16], TAGS[17], TAGS[18], TAGS[19]]
                 },
            '6': {
                  '1': [TAGS[12]],
                  '2': [TAGS[13]],
                  '3': [TAGS[12], TAGS[13]],
                  '4': [TAGS[14]],
                  '5': [TAGS[12], TAGS[14]],
                  '6': [TAGS[13], TAGS[14]],
                  '7': [TAGS[12], TAGS[13], TAGS[14]]
                 },
            '7': {
                  '1': [TAGS[8]],
                  '2': [TAGS[9]],
                  '3': [TAGS[8], TAGS[9]],
                  '4': [TAGS[10]],
                  '5': [TAGS[8], TAGS[10]],
                  '6': [TAGS[9], TAGS[10]],
                  '7': [TAGS[8], TAGS[9], TAGS[10]],
                  '8': [TAGS[11]],
                  '9': [TAGS[8], TAGS[11]],
                  'a': [TAGS[9], TAGS[11]],
                  'b': [TAGS[8], TAGS[9], TAGS[11]],
                  'c': [TAGS[10], TAGS[11]],
                  'd': [TAGS[8], TAGS[9], TAGS[11]],
                  'e': [TAGS[8], TAGS[10], TAGS[11]],
                  'f': [TAGS[8], TAGS[9], TAGS[10], TAGS[11]]
                 },
            '8': {
                  '1': [TAGS[4]],
                  '2': [TAGS[5]],
                  '3': [TAGS[4], TAGS[5]],
                  '4': [TAGS[6]],
                  '5': [TAGS[4], TAGS[6]],
                  '6': [TAGS[5], TAGS[6]],
                  '7': [TAGS[4], TAGS[5], TAGS[6]]
                 },
            '9': {
                  '1': [TAGS[0]],
                  '2': [TAGS[1]],
                  '3': [TAGS[0], TAGS[1]],
                  '4': [TAGS[2]],
                  '5': [TAGS[0], TAGS[2]],
                  '6': [TAGS[1], TAGS[2]],
                  '7': [TAGS[0], TAGS[1], TAGS[2]],
                  '8': [TAGS[3]],
                  '9': [TAGS[0], TAGS[3]],
                  'a': [TAGS[1], TAGS[3]],
                  'b': [TAGS[0], TAGS[1], TAGS[3]],
                  'c': [TAGS[2], TAGS[3]],
                  'd': [TAGS[0], TAGS[1], TAGS[3]],
                  'e': [TAGS[0], TAGS[2], TAGS[3]],
                  'f': [TAGS[0], TAGS[1], TAGS[2], TAGS[3]]
                }
              }

PARAM = (
        'algorithm', 'c', 'a', 'b', 'harm', 'dtun', 'fdbk', 'mix', 'a_attack', 'a_decay', 'a_end', 'a_level',
        'b_attack', 'b_decay', 'b_end', 'b_level', 'a_delay', 'a_trig', 'a_reset', 'phase_reset', 'b_delay', 'b_trig',
        'b_reset', 'filt_attack', 'filt_dec', 'filt_sustain', 'filt_release', 'filt1_freq', 'filt1_reso',
        'filt1_type', 'filt_env', 'filt2_base', 'filt2_width', 'amp_attack', 'amp_decay', 'amp_sustain', 'amp_release',
        'drive', 'pan', 'vol', 'chorus', 'delay', 'reverb', 'amp_reset', 'lfo1_dest', 'lfo1_wave', 'lfo1_spd',
        'lfo1_depth', 'lfo2_dest', 'lfo2_wave', 'lfo2_spd', 'lfo2_depth', 'lfo1_mult', 'lfo1_fade', 'lfo1_phase',
        'lfo1_mode', 'lfo2_mult', 'lfo2_fade', 'lfo2_phase', 'lfo2_mode', 'arp_toggle', 'arp_speed', 'arp_range',
        'arp_note_length', 'arp_offset01', 'arp_offset02', 'arp_offset03', 'arp_offset04', 'arp_offset05',
        'arp_offset06', 'arp_offset07', 'arp_offset08', 'arp_offset09', 'arp_offset10', 'arp_offset11', 'arp_offset12',
        'arp_offset13', 'arp_offset14', 'arp_offset15', 'arp_offset16', 'arp_length', 'arp_step01', 'arp_step02',
        'arp_step03', 'arp_step04', 'arp_step05', 'arp_step06', 'arp_step07', 'arp_step08', 'arp_step09', 'arp_step10',
        'arp_step11', 'arp_step12', 'arp_step13', 'arp_step14', 'arp_step15', 'arp_step16', 'key_scale_a',
        'key_scale_b1', 'key_scale_b2', 'filt_track', 'vel_vol', 'pitch_bend', 'octave', 'pb_dest1', 'pb_dest2',
        'pb_dest3', 'pb_dest4', 'pb_amt1', 'pb_amt2', 'pb_amt3', 'pb_amt4', 'vel_dest1', 'vel_dest2', 'vel_dest3',
        'vel_dest4', 'vel_amt1', 'vel_amt2', 'vel_amt3', 'vel_amt4', 'mod_dest1', 'mod_dest2', 'mod_dest3', 'mod_dest4',
        'mod_amt1', 'mod_amt2', 'mod_amt3', 'mod_amt4', 'breath_dest1', 'breath_dest2', 'breath_dest3', 'breath_dest4',
        'breath_amt1', 'breath_amt2', 'breath_amt3', 'breath_amt4', 'after_dest1', 'after_dest2', 'after_dest3',
        'after_dest4', 'after_amt1', 'after_amt2', 'after_amt3', 'after_amt4'

        )

PARAM_LOOK = {
                'algorithm': ['0x28'],
                'c': ['0x2b'],
                'a': ['0x2d'],
                'fdbk': ['0x36'],
                'mix': ['0x38'],
                'a_attack': ['0x3f'],
                'a_decay': ['0x42'],
                'a_end': ['0x44'],
                'a_level': ['0x46'],
                'b_attack': ['0x48'],
                'b_decay': ['0x4b'],
                'b_end': ['0x4d'],
                'b_level': ['0x4f'],
                'a_delay': ['0x52'],
                'a_trig': ['0x54'],
                'a_reset': ['0x56'],
                'phase_reset': ['0x3b'],
                'b_delay': ['0x58'],
                'b_trig': ['0x5b'],
                'b_reset': ['0x5d'],
                'filt_attack': ['0x7d'],
                'filt_dec': ['0x7f'],
                'filt_sustain': ['0x82'],
                'filt_release': ['0x84'],
                'filt1_type': ['0x74'],
                'filt2_base': ['0x86'],
                'filt2_width': ['0x88'],
                'amp_attack': ['0x8b'],
                'amp_decay': ['0x8d'],
                'amp_sustain': ['0x8f'],
                'pan': ['0x96'],
                'amp_reset': ['0xa2'],
                'lfo1_dest': ['0x12'],  # destination values start at b'11' LFO2 dest values start lower
                                        # since LFO params are a destination source
                'lfo1_wave': ['0x16'],
                'lfo2_dest': ['0x14'],
                'lfo2_wave': ['0x18'],
                'lfo1_mult': ['0x8'],
                'lfo1_fade': ['0xd'],
                'lfo1_phase': ['0x1b'],
                'lfo1_mode': ['0x1f'],
                'lfo2_mult': ['0xb'],
                'lfo2_fade': ['0xf'],
                'lfo2_phase': ['0x1d'],
                'lfo2_mode': ['0x22'],
                'arp_toggle': ['0xec'],
                'arp_speed': ['0xed'],
                'arp_range': ['0xee'],
                'arp_note_length': ['0xef'],
                'arp_length': ['0xf0'],

                # Arp step toggle uses same scheme as the tags

                'arp_step01': ['0xf3'],  # b'01'
                'arp_step02': ['0xf3'],  # b'02'
                'arp_step03': ['0xf3'],  # b'04'
                'arp_step04': ['0xf3'],  # b'08'
                'arp_step05': ['0xf3'],  # b'10'
                'arp_step06': ['0xf3'],  # b'20'
                'arp_step07': ['0xf3'],  # b'40'
                'arp_step08': ['0xf1'],  # b'20'
                'arp_step09': ['0xf2'],  # b'01'
                'arp_step10': ['0xf2'],  # b'02'
                'arp_step11': ['0xf2'],  # b'04'
                'arp_step12': ['0xf2'],  # b'08'
                'arp_step13': ['0xf2'],  # b'10'
                'arp_step14': ['0xf2'],  # b'20'
                'arp_step15': ['0xf2'],  # b'40'
                'arp_step16': ['0xf1'],  # b'40'
                'key_scale_a': ['0x107'],
                'key_scale_b1': ['0x108'],
                'key_scale_b2': ['0x10a'],
                'filt_track': ['0x10b'],
                'vel_vol': ['0xbb'],
                'pitch_bend': ['0x10d'],
                'octave': ['0x10e'],
                'pb_dest1': ['0xc7'],
                'pb_dest2': ['0xca'],
                'pb_dest3': ['0xcc'],
                'pb_dest4': ['0xce'],
                'vel_dest1': ['0xbe'],
                'vel_dest2': ['0xc0'],
                'vel_dest3': ['0xc3'],
                'vel_dest4': ['0xc5'],
                'mod_dest1': ['0xd0'],
                'mod_dest2': ['0xd3'],
                'mod_dest3': ['0xd5'],
                'mod_dest4': ['0xd7'],
                'breath_dest1': ['0xda'],
                'breath_dest2': ['0xdc'],
                'breath_dest3': ['0xde'],
                'breath_dest4': ['0xe0'],
                'after_dest1': ['0xe3'],
                'after_dest2': ['0xe5'],
                'after_dest3': ['0xe7'],
                'after_dest4': ['0xea'],

                # Two Byte Parameters
                # List structure: [ NEG_SIGN_BIT, NEG_SIGN_LOC, VALUE_LOC ]

                'arp_offset01': [3, '0xf1', '0xf4'],    # 0xf1: b'10'
                'arp_offset02': [4, '0xf1', '0xf5'],    # 0xf1: b'08'
                'arp_offset03': [5, '0xf1', '0xf6'],    # 0xf1: b'04'
                'arp_offset04': [6, '0xf1', '0xf7'],    # 0xf1: b'02'
                'arp_offset05': [7, '0xf1', '0xf8'],    # 0xf1: b'01'
                'arp_offset06': [1, '0xf9', '0xfa'],    # 0xf9: b'40'
                'arp_offset07': [2, '0xf9', '0xfb'],    # 0xf9: b'20'
                'arp_offset08': [3, '0xf9', '0xfc'],    # 0xf9: b'10'
                'arp_offset09': [4, '0xf9', '0xfd'],    # 0xf9: b'08'
                'arp_offset10': [5, '0xf9', '0xfe'],    # 0xf9: b'04'
                'arp_offset11': [6, '0xf9', '0xff'],    # 0xf9: b'02'
                'arp_offset12': [7, '0xf9', '0x100'],   # 0xf9: b'01'
                'arp_offset13': [1, '0x101', '0x102'],  # 0x101: b'40'
                'arp_offset14': [2, '0x101', '0x103'],  # 0x101: b'20'
                'arp_offset15': [3, '0x101', '0x104'],  # 0x101: b'10'
                'arp_offset16': [4, '0x101', '0x105'],  # 0x101: b'08'
                'pb_amt1': [5, '0xc1', '0xc6'],         # 0xc1: b'04'
                'pb_amt2': [7, '0xc1', '0xc8'],         # 0xc1: b'01'
                'vel_amt3': [1, '0xc1', '0xc2'],        # 0xc1: b'40'
                'vel_amt4': [3, '0xc1', '0xc4'],        # 0xc1: b'10'
                'pb_amt3': [2, '0xc9', '0xcb'],         # 0xc9: b'20'
                'pb_amt4': [4, '0xc9', '0xcd'],         # 0xc9: b'08'
                'mod_amt1': [6, '0xc9', '0xcf'],        # 0xc9: b'02'
                'vel_amt1': [4, '0xb9', '0xbd'],        # 0xb9: b'08'
                'vel_amt2': [6, '0xb9', '0xbf'],        # 0xb9: b'02'
                'breath_amt1': [7, '0xd1', '0xd8'],     # 0xd1: b'01'
                'mod_amt2': [1, '0xd1', '0xd2'],        # 0xd1: b'40'
                'mod_amt3': [3, '0xd1', '0xd4'],        # 0xd1: b'10'
                'mod_amt4': [5, '0xd1', '0xd6'],        # 0xd1: b'04'
                'breath_amt2': [2, '0xd9', '0xdb'],     # 0xd9: b'20'
                'breath_amt3': [4, '0xd9', '0xdd'],     # 0xd9: b'08'
                'breath_amt4': [6, '0xd9', '0xdf'],     # 0xd9: b'02'
                'after_amt1': [1, '0xe1', '0xe2'],      # 0xe1: b'40'
                'after_amt2': [3, '0xe1', '0xe4'],      # 0xe1: b'10'
                'after_amt3': [5, '0xe1', '0xe6'],      # 0xe1: b'04'
                'after_amt4': [7, '0xe1', '0xe8'],      # 0xe1: b'01'

                # Three Byte Parameters
                # This is divided into three different parts.

                # List structure: [ FLAG_BIT, FLAG_LOC, VALUE_MSB, VALUE_LSB]
                # In the following parameters, the sentinal value is used to divide the LSB into two sections, 0-50
                # and 51-99. This maps the value of the LSB from 0-127 to 0-50. The LSB goes after the decimal point as
                # it is displayed on the screen of the digitone.

                'dtun': [4, '0x31', '0x34', '0x35'],
                'filt1_freq': [6, '0x71', '0x76', '0x77'],
                'filt1_reso': [1, '0x78', '0x79', '0x7a'],
                'filt_env': [3, '0x79', '0x7b', '0x7c'],
                'amp_release': [2, '0x91', '0x92', '0x93'],  # Extremely odd. 0x93 does not render on param screen
                'drive': [4, '0x91', '0x94', '0x95'],
                'vol': [1, '0x99', '0x98', '0x9a'],
                'chorus': [7, '0x99', '0x9f', '0xa0'],
                'delay': [5, '0x99', '0x9d', '0x9e'],
                'reverb': [3, '0x99', '0x9b', '0x9c'],
                'lfo1_spd': [4, '0x1', '0x4', '0x5'],
                'lfo2_spd': [6, '0x1', '0x6', '0x7'],
                'harm': [2, '0x31', '0x32', '0x33'],  # maps from -26 to 26. Subtract 63 from MSB

                # FLAG_BIT changes the MSB. If Formula is (2 * MSB) - 128. If MSB is high add 1 to the formula. LSB maps
                # from 0 - 99. Not sure why the wouldn't just make the FLAG_BIT a negative sign. Seems much simpler

                'lfo1_depth': [4, '0x21', '0x24', '0x25'],
                'lfo2_depth': [6, '0x21', '0x26', '0x27'],

                # TODO: B is some kind of goddamn edgelord and needs to be dealt with
                #
                # This is very annoying. 0x30 is LSB. The MSB and FLAG_BYTE are multipliers on top of it. The MSB counts
                # from 0 to 2. Not sure of the mapping as of yet, but 0x29: 1 0x30: 5.00 / 1.00 on the Digitone. This
                # appears to be a mapping of 0 - 63. However, a table of values will need to generated
                'b': [7, '0x29', '0x2f', '0x30']

            }

SYSEX_BEGIN = b'f0'+b'00'+b'20'+b'3c'+b'0d'+b'00'+b'53'+b'01'+b'01'

PARAM_B = [
    '0.25 \ 0.25',
'00.25 \ 0.25',
'00.50 \ 0.25',
'00.75 \ 0.25',
'01.00 \ 0.25',
'02.00 \ 0.25',
'03.00 \ 0.25',
'04.00 \ 0.25',
'05.00 \ 0.25',
'06.00 \ 0.25',
'07.00 \ 0.25',
'08.00 \ 0.25',
'09.00 \ 0.25',
'10.00 \ 0.25',
'11.00 \ 0.25',
'12.00 \ 0.25',
'13.00 \ 0.25',
'14.00 \ 0.25',
'15.00 \ 0.25',
'16.00 \ 0.25',

    '00.25 \ 0.50',
    '00.50 \ 0.50',
    '00.75 \ 0.50',
    '01.00 \ 0.50',
    '02.00 \ 0.50',
    '03.00 \ 0.50',
    '04.00 \ 0.50',
    '05.00 \ 0.50',
    '06.00 \ 0.50',
    '07.00 \ 0.50',
    '08.00 \ 0.50',
    '09.00 \ 0.50',
    '10.00 \ 0.50',
    '11.00 \ 0.50',
    '12.00 \ 0.50',
    '13.00 \ 0.50',
    '14.00 \ 0.50',
    '15.00 \ 0.50',
    '16.00 \ 0.50',

    '00.25 \ 0.75',
    '00.50 \ 0.75',
    '00.75 \ 0.75',
    '01.00 \ 0.75',
    '02.00 \ 0.75',
    '03.00 \ 0.75',
    '04.00 \ 0.75',
    '05.00 \ 0.75',
    '06.00 \ 0.75',
    '07.00 \ 0.75',
    '08.00 \ 0.75',
    '09.00 \ 0.75',
    '10.00 \ 0.75',
    '11.00 \ 0.75',
    '12.00 \ 0.75',
    '13.00 \ 0.75',
    '14.00 \ 0.75',
    '15.00 \ 0.75',
    '16.00 \ 0.75',

    '00.25 \ 1.00',
    '00.50 \ 1.00',
    '00.75 \ 1.00',
    '01.00 \ 1.00',
    '02.00 \ 1.00',
    '03.00 \ 1.00',
    '04.00 \ 1.00',
    '05.00 \ 1.00',
    '06.00 \ 1.00',
    '07.00 \ 1.00',
    '08.00 \ 1.00',
    '09.00 \ 1.00',
    '10.00 \ 1.00',
    '11.00 \ 1.00',
    '12.00 \ 1.00',
    '13.00 \ 1.00',
    '14.00 \ 1.00',
    '15.00 \ 1.00',
    '16.00 \ 1.00',

    '00.25 \ 2.00',
    '00.50 \ 2.00',
    '00.75 \ 2.00',
    '01.00 \ 2.00',
    '02.00 \ 2.00',
    '03.00 \ 2.00',
    '04.00 \ 2.00',
    '05.00 \ 2.00',
    '06.00 \ 2.00',
    '07.00 \ 2.00',
    '08.00 \ 2.00',
    '09.00 \ 2.00',
    '10.00 \ 2.00',
    '11.00 \ 2.00',
    '12.00 \ 2.00',
    '13.00 \ 2.00',
    '14.00 \ 2.00',
    '15.00 \ 2.00',
    '16.00 \ 2.00',

    '00.25 \ 3.00',
    '00.50 \ 3.00',
    '00.75 \ 3.00',
    '01.00 \ 3.00',
    '02.00 \ 3.00',
    '03.00 \ 3.00',
    '04.00 \ 3.00',
    '05.00 \ 3.00',
    '06.00 \ 3.00',
    '07.00 \ 3.00',
    '08.00 \ 3.00',
    '09.00 \ 3.00',
    '10.00 \ 3.00',
    '11.00 \ 3.00',
    '12.00 \ 3.00',
    '13.00 \ 3.00',
    '14.00 \ 3.00',
    '15.00 \ 3.00',
    '16.00 \ 3.00',

    '00.25 \ 4.00',
    '00.50 \ 4.00',
    '00.75 \ 4.00',
    '01.00 \ 4.00',
    '02.00 \ 4.00',
    '03.00 \ 4.00',
    '04.00 \ 4.00',
    '05.00 \ 4.00',
    '06.00 \ 4.00',
    '07.00 \ 4.00',
    '08.00 \ 4.00',
    '09.00 \ 4.00',
    '10.00 \ 4.00',
    '11.00 \ 4.00',
    '12.00 \ 4.00',
    '13.00 \ 4.00',
    '14.00 \ 4.00',
    '15.00 \ 4.00',
    '16.00 \ 4.00',

    '00.25 \ 5.00',
    '00.50 \ 5.00',
    '00.75 \ 5.00',
    '01.00 \ 5.00',
    '02.00 \ 5.00',
    '03.00 \ 5.00',
    '04.00 \ 5.00',
    '05.00 \ 5.00',
    '06.00 \ 5.00',
    '07.00 \ 5.00',
    '08.00 \ 5.00',
    '09.00 \ 5.00',
    '10.00 \ 5.00',
    '11.00 \ 5.00',
    '12.00 \ 5.00',
    '13.00 \ 5.00',
    '14.00 \ 5.00',
    '15.00 \ 5.00',
    '16.00 \ 5.00',

    '00.25 \ 6.00',
    '00.50 \ 6.00',
    '00.75 \ 6.00',
    '01.00 \ 6.00',
    '02.00 \ 6.00',
    '03.00 \ 6.00',
    '04.00 \ 6.00',
    '05.00 \ 6.00',
    '06.00 \ 6.00',
    '07.00 \ 6.00',
    '08.00 \ 6.00',
    '09.00 \ 6.00',
    '10.00 \ 6.00',
    '11.00 \ 6.00',
    '12.00 \ 6.00',
    '13.00 \ 6.00',
    '14.00 \ 6.00',
    '15.00 \ 6.00',
    '16.00 \ 6.00',

    '00.25 \ 7.00',
    '00.50 \ 7.00',
    '00.75 \ 7.00',
    '01.00 \ 7.00',
    '02.00 \ 7.00',
    '03.00 \ 7.00',
    '04.00 \ 7.00',
    '05.00 \ 7.00',
    '06.00 \ 7.00',
    '07.00 \ 7.00',
    '08.00 \ 7.00',
    '09.00 \ 7.00',
    '10.00 \ 7.00',
    '11.00 \ 7.00',
    '12.00 \ 7.00',
    '13.00 \ 7.00',
    '14.00 \ 7.00',
    '15.00 \ 7.00',
    '16.00 \ 7.00',

    '00.25 \ 8.00',
    '00.50 \ 8.00',
    '00.75 \ 8.00',
    '01.00 \ 8.00',
    '02.00 \ 8.00',
    '03.00 \ 8.00',
    '04.00 \ 8.00',
    '05.00 \ 8.00',
    '06.00 \ 8.00',
    '07.00 \ 8.00',
    '08.00 \ 8.00',
    '09.00 \ 8.00',
    '10.00 \ 8.00',
    '11.00 \ 8.00',
    '12.00 \ 8.00',
    '13.00 \ 8.00',
    '14.00 \ 8.00',
    '15.00 \ 8.00',
    '16.00 \ 8.00',

    '00.25 \ 9.00',
    '00.50 \ 9.00',
    '00.75 \ 9.00',
    '01.00 \ 9.00',
    '02.00 \ 9.00',
    '03.00 \ 9.00',
    '04.00 \ 9.00',
    '05.00 \ 9.00',
    '06.00 \ 9.00',
    '07.00 \ 9.00',
    '08.00 \ 9.00',
    '09.00 \ 9.00',
    '10.00 \ 9.00',
    '11.00 \ 9.00',
    '12.00 \ 9.00',
    '13.00 \ 9.00',
    '14.00 \ 9.00',
    '15.00 \ 9.00',
    '16.00 \ 9.00',

    '00.25 \ 10.00',
    '00.50 \ 10.00',
    '00.75 \ 10.00',
    '01.00 \ 10.00',
    '02.00 \ 10.00',
    '03.00 \ 10.00',
    '04.00 \ 10.00',
    '05.00 \ 10.00',
    '06.00 \ 10.00',
    '07.00 \ 10.00',
    '08.00 \ 10.00',
    '09.00 \ 10.00',
    '10.00 \ 10.00',
    '11.00 \ 10.00',
    '12.00 \ 10.00',
    '13.00 \ 10.00',
    '14.00 \ 10.00',
    '15.00 \ 10.00',
    '16.00 \ 10.00',

    '00.25 \ 11.00',
    '00.50 \ 11.00',
    '00.75 \ 11.00',
    '01.00 \ 11.00',
    '02.00 \ 11.00',
    '03.00 \ 11.00',
    '04.00 \ 11.00',
    '05.00 \ 11.00',
    '06.00 \ 11.00',
    '07.00 \ 11.00',
    '08.00 \ 11.00',
    '09.00 \ 11.00',
    '10.00 \ 11.00',
    '11.00 \ 11.00',
    '12.00 \ 11.00',
    '13.00 \ 11.00',
    '14.00 \ 11.00',
    '15.00 \ 11.00',
    '16.00 \ 11.00',

    '00.25 \ 12.00',
    '00.50 \ 12.00',
    '00.75 \ 12.00',
    '01.00 \ 12.00',
    '02.00 \ 12.00',
    '03.00 \ 12.00',
    '04.00 \ 12.00',
    '05.00 \ 12.00',
    '06.00 \ 12.00',
    '07.00 \ 12.00',
    '08.00 \ 12.00',
    '09.00 \ 12.00',
    '10.00 \ 12.00',
    '11.00 \ 12.00',
    '12.00 \ 12.00',
    '13.00 \ 12.00',
    '14.00 \ 12.00',
    '15.00 \ 12.00',
    '16.00 \ 12.00',

    '00.25 \ 13.00',
    '00.50 \ 13.00',
    '00.75 \ 13.00',
    '01.00 \ 13.00',
    '02.00 \ 13.00',
    '03.00 \ 13.00',
    '04.00 \ 13.00',
    '05.00 \ 13.00',
    '06.00 \ 13.00',
    '07.00 \ 13.00',
    '08.00 \ 13.00',
    '09.00 \ 13.00',
    '10.00 \ 13.00',
    '11.00 \ 13.00',
    '12.00 \ 13.00',
    '13.00 \ 13.00',
    '14.00 \ 13.00',
    '15.00 \ 13.00',
    '16.00 \ 13.00',

    '00.25 \ 14.00',
    '00.50 \ 14.00',
    '00.75 \ 14.00',
    '01.00 \ 14.00',
    '02.00 \ 14.00',
    '03.00 \ 14.00',
    '04.00 \ 14.00',
    '05.00 \ 14.00',
    '06.00 \ 14.00',
    '07.00 \ 14.00',
    '08.00 \ 14.00',
    '09.00 \ 14.00',
    '10.00 \ 14.00',
    '11.00 \ 14.00',
    '12.00 \ 14.00',
    '13.00 \ 14.00',
    '14.00 \ 14.00',
    '15.00 \ 14.00',
    '16.00 \ 14.00',

    '00.25 \ 15.00',
    '00.50 \ 15.00',
    '00.75 \ 15.00',
    '01.00 \ 15.00',
    '02.00 \ 15.00',
    '03.00 \ 15.00',
    '04.00 \ 15.00',
    '05.00 \ 15.00',
    '06.00 \ 15.00',
    '07.00 \ 15.00',
    '08.00 \ 15.00',
    '09.00 \ 15.00',
    '10.00 \ 15.00',
    '11.00 \ 15.00',
    '12.00 \ 15.00',
    '13.00 \ 15.00',
    '14.00 \ 15.00',
    '15.00 \ 15.00',
    '16.00 \ 15.00',

    '00.25 \ 16.00',
    '00.50 \ 16.00',
    '00.75 \ 16.00',
    '01.00 \ 16.00',
    '02.00 \ 16.00',
    '03.00 \ 16.00',
    '04.00 \ 16.00',
    '05.00 \ 16.00',
    '06.00 \ 16.00',
    '07.00 \ 16.00',
    '08.00 \ 16.00',
    '09.00 \ 16.00',
    '10.00 \ 16.00',
    '11.00 \ 16.00',
    '12.00 \ 16.00',
    '13.00 \ 16.00',
    '14.00 \ 16.00',
    '15.00 \ 16.00',
    '16.00 \ 16.00'

]
