TAGS = (
        'KICK', 'SNAR', 'DEEP', 'BRAS', 'STRI', 'PERC', 'HHAT', 'CYMB', 'EVOL', 'EXPR',
        'BASS', 'LEAD', 'PAD', 'TXTR', 'CRD', 'SFX', 'ARP', 'METL', 'ACOU', 'ATMO',
        'NOIS', 'GLCH', 'HARD', 'SOFT', 'DARK', 'BRGT', 'UNTG', 'EPIC', 'FAIL', 'LOOP',
        'MINE', 'FAV'
       )

TAG_LOOKUP = {
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

PARAMETERS = ('algorithm', 'c', 'a', 'b', 'harm', 'dtun', 'fdbk', 'mix', 'a_attack', 'a_decay',
              'a_end','a_level', 'b_attack', 'b_decay', 'b_end', 'b_level','a_delay', 'a_trig',
              'a_reset', 'phase_reset', 'b_delay', 'b_trig', 'b_reset', 'filt_attack', 'filt_dec',
              'filt_sustain', 'filt_release', 'filt1_freq', 'filt1_reso', 'filt1_type', 'filt_env',
              'filt2_base', 'filt2_width', 'amp_attack', 'amp_decay', 'amp_sustain', 'amp_release',
              'drive','pan', 'vol', 'chorus', 'delay', 'reverb', 'amp_reset', 'lfo1_dest',
              'lfo1_wave', 'lfo1_spd', 'lfo1_depth', 'lfo2_dest', 'lfo2_wave', 'lfo2_spd',
              'lfo2_depth', 'lfo1_mult', 'lfo1_fade', 'lfo1_phase', 'lfo1_mode', 'lfo2_mult',
              'lfo2_fade', 'lfo2_phase', 'lfo2_mode', 'arp_toggle', 'arp_speed', 'arp_range',
              'arp_note_length', 'arp_offset01', 'arp_offset02', 'arp_offset03', 'arp_offset04',
              'arp_offset05', 'arp_offset06', 'arp_offset07', 'arp_offset08', 'arp_offset09',
              'arp_offset10', 'arp_offset11', 'arp_offset12', 'arp_offset13', 'arp_offset14',
              'arp_offset15','arp_offset16', 'arp_length', 'arp_step01', 'arp_step02', 'arp_step03',
              'arp_step04', 'arp_step05', 'arp_step06', 'arp_step07', 'arp_step08', 'arp_step09',
              'arp_step10', 'arp_step11', 'arp_step12', 'arp_step13', 'arp_step14', 'arp_step15',
              'arp_step1'
              )

# 'key_scale_a', 'key_scale_b1', 'key_scale_b2', 'filt_keytrack', 'velocity_vol', 'octave', 'pitchbend',
# 'velocity_dest1', 'velocity_dest2', 'velocity_dest3', 'velocity_dest4', 'velocity_amt1', 'velocity_amt2',
# 'velocity_amt3'. 'velocity_amt4', 'modwheel_dest1', 'modwheel_dest2', 'modwheel_dest3', 'modwheel_dest4',
# 'modwheel_amt1', 'modwheel_amt2', 'modwheel_amt3', modwheel_amt4', 'breath_dest1', 'breath_dest2', breath_dest3',
# 'breath_dest4', 'breath_amt1', 'breath_amt2', 'breath_amt3', 'breath_amt4', 'after_dest1', 'after_dest2',
# 'after_dest3', 'after_dest4', 'after_amt1', 'after_amt2', 'after_amt3', 'after_amt4'

SYSEX_BEGIN = b'f0'+b'00'+b'20'+b'3c'+b'0d'+b'00'+b'53'+b'01'+b'01'
