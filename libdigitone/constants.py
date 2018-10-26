# TODO: PICKLE THIS SHIT

TAGS = (
        'KICK', 'SNAR', 'DEEP', 'BRAS', 'STRI', 'PERC', 'HHAT', 'CYMB', 'EVOL', 'EXPR',
        'BASS', 'LEAD', 'PAD', 'TXTR', 'CRD', 'SFX', 'ARP', 'METL', 'ACOU', 'ATMO',
        'NOIS', 'GLCH', 'HARD', 'SOFT', 'DARK', 'BRGT', 'UNTG', 'EPIC', 'FAIL', 'LOOP',
        'MINE', 'FAV'
       )

TAG_LOOK = {
            '0': {
                  b'1': [TAGS[23]],
                  b'2': [TAGS[31]],
                  b'3': [TAGS[23], TAGS[31]]
                 },
            '1': {
                  b'4': [TAGS[7]],
                  b'8': [TAGS[15]],
                  b'c': [TAGS[7], TAGS[15]]
                 },
            '2': {
                  b'1': [TAGS[28]],
                  b'2': [TAGS[29]],
                  b'3': [TAGS[28], TAGS[29]],
                  b'4': [TAGS[30]],
                  b'5': [TAGS[30], TAGS[28]],
                  b'6': [TAGS[29], TAGS[30]],
                  b'7': [TAGS[28], TAGS[29], TAGS[30]]
                 },
            '3': {
                  b'1': [TAGS[24]],
                  b'2': [TAGS[25]],
                  b'3': [TAGS[24], TAGS[25]],
                  b'4': [TAGS[26]],
                  b'5': [TAGS[24], TAGS[26]],
                  b'6': [TAGS[25], TAGS[26]],
                  b'7': [TAGS[24], TAGS[25], TAGS[26]],
                  b'8': [TAGS[27]],
                  b'9': [TAGS[24], TAGS[27]],
                  b'a': [TAGS[25], TAGS[27]],
                  b'b': [TAGS[24], TAGS[25], TAGS[27]],
                  b'c': [TAGS[26], TAGS[27]],
                  b'd': [TAGS[24], TAGS[25], TAGS[27]],
                  b'e': [TAGS[24], TAGS[26], TAGS[27]],
                  b'f': [TAGS[24], TAGS[25], TAGS[26], TAGS[27]]
                 },
            '4': {
                  b'1': [TAGS[20]],
                  b'2': [TAGS[21]],
                  b'3': [TAGS[20], TAGS[21]],
                  b'4': [TAGS[22]],
                  b'5': [TAGS[20], TAGS[22]],
                  b'6': [TAGS[21], TAGS[22]],
                  b'7': [TAGS[20], TAGS[21], TAGS[22]]
                 },
            '5': {
                  b'1': [TAGS[16]],
                  b'2': [TAGS[17]],
                  b'3': [TAGS[16], TAGS[17]],
                  b'4': [TAGS[18]],
                  b'5': [TAGS[16], TAGS[18]],
                  b'6': [TAGS[25], TAGS[26]],
                  b'7': [TAGS[16], TAGS[17], TAGS[18]],
                  b'8': [TAGS[19]],
                  b'9': [TAGS[16], TAGS[19]],
                  b'a': [TAGS[17], TAGS[19]],
                  b'b': [TAGS[16], TAGS[17], TAGS[19]],
                  b'c': [TAGS[18], TAGS[19]],
                  b'd': [TAGS[16], TAGS[17], TAGS[19]],
                  b'e': [TAGS[16], TAGS[18], TAGS[19]],
                  b'f': [TAGS[16], TAGS[17], TAGS[18], TAGS[19]]
                 },
            '6': {
                  b'1': [TAGS[12]],
                  b'2': [TAGS[13]],
                  b'3': [TAGS[12], TAGS[13]],
                  b'4': [TAGS[14]],
                  b'5': [TAGS[12], TAGS[14]],
                  b'6': [TAGS[13], TAGS[14]],
                  b'7': [TAGS[12], TAGS[13], TAGS[14]]
                 },
            '7': {
                  b'1': [TAGS[8]],
                  b'2': [TAGS[9]],
                  b'3': [TAGS[8], TAGS[9]],
                  b'4': [TAGS[10]],
                  b'5': [TAGS[8], TAGS[10]],
                  b'6': [TAGS[25], TAGS[26]],
                  b'7': [TAGS[8], TAGS[9], TAGS[10]],
                  b'8': [TAGS[11]],
                  b'9': [TAGS[8], TAGS[11]],
                  b'a': [TAGS[9], TAGS[11]],
                  b'b': [TAGS[8], TAGS[9], TAGS[11]],
                  b'c': [TAGS[10], TAGS[11]],
                  b'd': [TAGS[8], TAGS[9], TAGS[11]],
                  b'e': [TAGS[8], TAGS[10], TAGS[11]],
                  b'f': [TAGS[8], TAGS[9], TAGS[10], TAGS[11]]
                 },
            '8': {
                  b'1': [TAGS[4]],
                  b'2': [TAGS[5]],
                  b'3': [TAGS[4], TAGS[5]],
                  b'4': [TAGS[6]],
                  b'5': [TAGS[4], TAGS[6]],
                  b'6': [TAGS[5], TAGS[6]],
                  b'7': [TAGS[4], TAGS[5], TAGS[6]]
                 },
            '9': {
                  b'1': [TAGS[0]],
                  b'2': [TAGS[1]],
                  b'3': [TAGS[0], TAGS[1]],
                  b'4': [TAGS[2]],
                  b'5': [TAGS[0], TAGS[2]],
                  b'6': [TAGS[25], TAGS[26]],
                  b'7': [TAGS[0], TAGS[1], TAGS[2]],
                  b'8': [TAGS[3]],
                  b'9': [TAGS[0], TAGS[3]],
                  b'a': [TAGS[1], TAGS[3]],
                  b'b': [TAGS[0], TAGS[1], TAGS[3]],
                  b'c': [TAGS[2], TAGS[3]],
                  b'd': [TAGS[0], TAGS[1], TAGS[3]],
                  b'e': [TAGS[0], TAGS[2], TAGS[3]],
                  b'f': [TAGS[0], TAGS[1], TAGS[2], TAGS[3]]
                }
              }

# TODO: Finish and check Parameter Mapping
# Parameters do not currently contain the modulation routing parameters and are most likely
# contributing to the bytes valued at 40 throughout the patch data. Will need to redo the entire
# parameter dump file with the correct values.

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
        'pb_dest3', 'pb_dest4', 'pb_amt1', 'pb_amt2', 'pb_amt3', 'pb_amt4', 'mod_dest1', 'mod_dest2', 'mod_dest3',
        'mod_dest4', 'mod_amt1', 'mod_amt2', 'mod_amt3', 'mod_amt4', 'breath_dest1', 'breath_dest2', 'breath_dest3',
        'breath_dest4', 'breath_amt1', 'breath_amt2', 'breath_amt3', 'breath_amt4', 'after_dest1', 'after_dest2',
        'after_dest3', 'after_dest4', 'after_amt1', 'after_amt2', 'after_amt3', 'after_amt4'

        )

PARAM_LOOK = {
                'algorithm': ['0x28'], 'c': ['0x2b'], 'a': ['0x2d'], 'b': ['0x29', '0x2f', '0x30'], 'harm': ['0x32'],
                'dtun': ['0x34'], 'fdbk': ['0x36'], 'mix': ['0x38'], 'a_attack': ['0x3f'], 'a_decay': ['0x42'],
                'a_end': ['0x44'], 'a_level': ['0x46'], 'b_attack': ['0x48'], 'b_decay': ['0x4b'], 'b_end': ['0x4d'],
                'b_level': ['0x4f'], 'a_delay': ['0x52'], 'a_trig': ['0x54'], 'a_reset': ['0x56'],
                'phase_reset': ['0x3b'], 'b_delay': ['0x58'], 'b_trig': ['0x5b'], 'b_reset': ['0x5d'],
                'filt_attack': ['0x7d'], 'filt_dec': ['0x7f'], 'filt_sustain': ['0x82'], 'filt_release': ['0x84'],
                'filt1_freq': ['0x76'], 'filt1_reso': ['0x78'], 'filt1_type': ['0x74'], 'filt_env': ['0x7b'],
                'filt2_base': ['0x86'], 'filt2_width': ['0x88'], 'amp_attack': ['0x8b'], 'amp_decay': ['0x8d'],
                'amp_sustain': ['0x8f'], 'amp_release': ['0x92'], 'drive': ['0x94'], 'pan': ['0x96'], 'vol': ['0x98'],
                'chorus': ['0x9f'], 'delay': ['0x9d'], 'reverb': ['0x9b'], 'amp_reset': ['0xa2'], 'lfo1_dest': ['0x12'],
                'lfo1_wave': ['0x16'], 'lfo1_spd': ['0x1', '0x4', '0x5'], 'lfo1_depth': ['0x21', '0x24', '0x25'],
                'lfo2_dest': ['0x14'], 'lfo2_wave': ['0x18'], 'lfo2_spd': ['0x1', '0x6', '0x7'],
                'lfo2_depth': ['0x21', '0x26', '0x27'], 'lfo1_mult': ['0x8'], 'lfo1_fade': ['0xd'],
                'lfo1_phase': ['0x1b'], 'lfo1_mode': ['0x1f'], 'lfo2_mult': ['0xb'], 'lfo2_fade': ['0xf'],
                'lfo2_phase': ['0x1d'], 'lfo2_mode': ['0x22'], 'arp_toggle': ['0xec'], 'arp_speed': ['0xed'],
                'arp_range': ['0xee'], 'arp_note_length': ['0xef'], 'arp_offset01': ['0xf1', '0xf4'],
                'arp_offset02': ['0xf1', '0xf5'], 'arp_offset03': ['0xf1', '0xf6'], 'arp_offset04': ['0xf1', '0xf7'],
                'arp_offset05': ['0xf1', '0xf8'], 'arp_offset06': ['0xf9', '0xfa'], 'arp_offset07': ['0xf9', '0xfb'],
                'arp_offset08': ['0xf9', '0xfc'], 'arp_offset09': ['0xf9', '0xfd'], 'arp_offset10': ['0xf9', '0xfe'],
                'arp_offset11': ['0xf9', '0xff'], 'arp_offset12': ['0xf9', '0x100'], 'arp_offset13': ['0x101', '0x102'],
                'arp_offset14': ['0x101', '0x103'], 'arp_offset15': ['0x101', '0x104'],
                'arp_offset16': ['0x101', '0x104', '0x105'], 'arp_length': ['0xf0', '0x104'],
                'arp_step01': ['0xf3', '0x104'], 'arp_step02': ['0xf3', '0x104'], 'arp_step03': ['0xf3', '0x104'],
                'arp_step04': ['0xf3', '0x104'], 'arp_step05': ['0xf3', '0x104'], 'arp_step06': ['0xf3', '0x104'],
                'arp_step07': ['0xf3', '0x104'], 'arp_step08': ['0xf1', '0x104'], 'arp_step09': ['0xf2', '0x104'],
                'arp_step10': ['0xf2', '0x104'], 'arp_step11': ['0xf2', '0x104'], 'arp_step12': ['0xf2', '0x104'],
                'arp_step13': ['0xf2', '0x104'], 'arp_step14': ['0xf2', '0x104'], 'arp_step15': ['0xf2', '0x104'],
                'arp_step16': ['0xf1', '0x104'], 'key_scale_a': ['0x107'], 'key_scale_b1': ['0x108'],
                'key_scale_b2': ['0x10a'], 'filt_track': ['0x10b'], 'vel_vol': ['0xbb'], 'pitch_bend': ['0x10d'],
                'octave': ['0x10e'], 'pb_dest1': ['0xc7'], 'pb_dest2': ['0xca'], 'pb_dest3': ['0xcc'],
                'pb_dest4': ['0xce'], 'pb_amt1': ['0xc1', '0xc6'], 'pb_amt2': ['0xc1', '0xc8'],
                'pb_amt3': ['0xc9', '0xcb'], 'pb_amt4': ['0xc9', '0xcd'], 'mod_dest1': ['0xbe'],
                'mod_dest2': ['0xc0'], 'mod_dest3': ['0xc3'], 'mod_dest4': ['0xc5'], 'mod_amt1': ['0xbd', '0xb9'],
                'mod_amt2': ['0xb9', '0xbf'], 'mod_amt3': ['0xc1', '0xc2'], 'mod_amt4': ['0xc1', '0xc4'],
                'breath_dest1': [], 'breath_dest2': [], 'breath_dest3': [], 'breath_dest4': [], 'breath_amt1': [],
                'breath_amt2': [], 'breath_amt3': [], 'breath_amt4': [], 'after_dest1': [], 'after_dest2': [],
                'after_dest3': [], 'after_dest4': [], 'after_amt1': [], 'after_amt2': [], 'after_amt3': [],
                'after_amt4': []
            }

SYSEX_BEGIN = b'f0'+b'00'+b'20'+b'3c'+b'0d'+b'00'+b'53'+b'01'+b'01'
