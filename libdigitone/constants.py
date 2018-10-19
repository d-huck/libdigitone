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


# Parameters do not currently contain the modulation routing parameters and are most likely
# contributing to the bytes valued at 40 throughout the patch data. Will need to redo the entire
# parameter dump file with the correct values.

PARAM = (
        'algorithm', 'c', 'a', 'b', 'harm', 'dtun', 'fdbk', 'mix', 'a_attack', 'a_decay', 'a_end','a_level',
        'b_attack', 'b_decay', 'b_end', 'b_level','a_delay', 'a_trig','a_reset', 'phase_reset', 'b_delay', 'b_trig',
        'b_reset', 'filt_attack', 'filt_dec',  'filt_sustain', 'filt_release', 'filt1_freq', 'filt1_reso',
        'filt1_type', 'filt_env', 'filt2_base', 'filt2_width', 'amp_attack', 'amp_decay', 'amp_sustain', 'amp_release',
        'drive','pan', 'vol', 'chorus', 'delay', 'reverb', 'amp_reset', 'lfo1_dest', 'lfo1_wave', 'lfo1_spd',
        'lfo1_depth', 'lfo2_dest', 'lfo2_wave', 'lfo2_spd', 'lfo2_depth', 'lfo1_mult', 'lfo1_fade', 'lfo1_phase',
        'lfo1_mode', 'lfo2_mult',   'lfo2_fade', 'lfo2_phase', 'lfo2_mode', 'arp_toggle', 'arp_speed', 'arp_range',
        'arp_note_length', 'arp_offset01', 'arp_offset02', 'arp_offset03', 'arp_offset04', 'arp_offset05',
        'arp_offset06', 'arp_offset07', 'arp_offset08', 'arp_offset09','arp_offset10', 'arp_offset11', 'arp_offset12',
        'arp_offset13', 'arp_offset14','arp_offset15','arp_offset16', 'arp_length', 'arp_step01', 'arp_step02',
        'arp_step03', 'arp_step04', 'arp_step05', 'arp_step06', 'arp_step07', 'arp_step08', 'arp_step09', 'arp_step10',
        'arp_step11', 'arp_step12', 'arp_step13', 'arp_step14', 'arp_step15', 'arp_step1', 'key_scale_a', 'key_scale_b1',
        'key_scale_b2', 'filt_keytrack', 'velocity_vol', 'octave', 'pitchbend', 'velocity_dest1', 'velocity_dest2',
        'velocity_dest3', 'velocity_dest4', 'velocity_global', 'velocity_amt1', 'velocity_amt2', 'velocity_amt3',
        'velocity_amt4', 'modwheel_dest1', 'modwheel_dest2', 'modwheel_dest3', 'modwheel_dest4', 'modwheel_global',
        'modwheel_amt1', 'modwheel_amt2', 'modwheel_amt3', 'modwheel_amt4', 'breath_dest1', 'breath_dest2',
        'breath_dest3', 'breath_dest4', 'breath_global', 'breath_amt1', 'breath_amt2', 'breath_amt3', 'breath_amt4',
        'after_dest1', 'after_dest2', 'after_dest3', 'after_dest4', 'after_global', 'after_amt1', 'after_amt2',
        'after_amt3', 'after_amt4'
        )

PARAM_LOOK = {
            'algorithm': '0x51', 'c': '0x54', 'a': '0x56', 'b': '0x59 0x58 0x52', 'harm': '0x5b', 'dtun': '0x5d',
            'fdbk': '0x5f', 'mix': '0x61', 'a_attack': '0x68', 'a_decay': '0x6b', 'a_end': '0x6d', 'a_level': '0x6f',
            'b_attack': '0x71', 'b_decay': '0x74', 'b_end': '0x76', 'b_level': '0x78', 'a_delay': '0x7b',
            'a_trig': '0x7d', 'a_reset': '0x7f', 'phase_reset': '0x64', 'b_delay': '0x81', 'b_trig': '0x84',
            'b_reset': '0x86', 'filt_attack': '0xa6', 'filt_dec': '0xa8', 'filt_sustain': '0xab',
            'filt_release': '0xad', 'filt1_freq': '0x9f', 'filt1_reso': '0xa1', 'filt1_type': '0x9d',
            'filt_env': '0xa4', 'filt2_base': '0xaf', 'filt2_width': '0xb1', 'amp_attack': '0xb4',
            'amp_decay': '0xb6', 'amp_sustain': '0xb8', 'amp_release': '0xbb', 'drive': '0xbd', 'pan': '0xbf',
            'vol': '0xc1', 'chorus': '0xc8', 'delay': '0xc6', 'reverb': '0xc4', 'amp_reset': '0xcb',
            'lfo1_dest': '0x3b', 'lfo1_wave': '0x3f', 'lfo1_spd': '0x2e 0x2d 0x2a', 'lfo1_depth': '0x4e 0x4d 0x4a',
            'lfo2_dest': '0x3d', 'lfo2_wave': '0x41', 'lfo2_spd': '0x30 0x2f 0x2a', 'lfo2_depth': '0x50 0x4f 0x4a',
            'lfo1_mult': '0x31', 'lfo1_fade': '0x36', 'lfo1_phase': '0x44', 'lfo1_mode': '0x48', 'lfo2_mult': '0x34',
            'lfo2_fade': '0x38', 'lfo2_phase': '0x46', 'lfo2_mode': '0x4b', 'arp_toggle': '0x115',
            'arp_speed': '0x116', 'arp_range': '0x117', 'arp_note_length': '0x118', 'arp_offset01': '0x11d 0x11a',
            'arp_offset02': '0x11e 0x11a', 'arp_offset03': '0x11f 0x11a', 'arp_offset04': '0x120 0x11a',
            'arp_offset05': '0x121 0x11a', 'arp_offset06': '0x123 0x122', 'arp_offset07': '0x124 0x122',
            'arp_offset08': '0x125 0x122', 'arp_offset09': '0x126 0x122', 'arp_offset10': '0x127 0x122',
            'arp_offset11': '0x128 0x122', 'arp_offset12': '0x129 0x122', 'arp_offset13': '0x12b 0x12a',
            'arp_offset14': '0x12c 0x12a', 'arp_offset15': '0x12d 0x12a', 'arp_offset16': '0x12e 0x12d 0x12a',
            'arp_length': '0x12d 0x119', 'arp_step01': '0x12d 0x11c', 'arp_step02': '0x12d 0x11c',
            'arp_step03': '0x12d 0x11c', 'arp_step04': '0x12d 0x11c', 'arp_step05': '0x12d 0x11c',
            'arp_step06': '0x12d 0x11c', 'arp_step07': '0x12d 0x11c', 'arp_step08': '0x12d 0x11a',
            'arp_step09': '0x12d 0x11b', 'arp_step10': '0x12d 0x11b', 'arp_step11': '0x12d 0x11b',
            'arp_step12': '0x12d 0x11b', 'arp_step13': '0x12d 0x11b', 'arp_step14': '0x12d 0x11b',
            'arp_step15': '0x12d 0x11b', 'arp_step1': '0x12d 0x11a'
            }



SYSEX_BEGIN = b'f0'+b'00'+b'20'+b'3c'+b'0d'+b'00'+b'53'+b'01'+b'01'
