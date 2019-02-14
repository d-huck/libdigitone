import libdigitone as dt
import logging
import argparse
import time
import threading # imported for threading in monitor arguement


def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--listen', action='store_true', help='Turns on verbose output')
    parser.add_argument('-m', '--monitor', action='store_true', help='Monitor for parameter changes')
    parser.add_argument('-r', '--request', dest='request', action='store',
                        help='Send a request to the digitone. Requires REQUEST argument to specify request type')
    parser.add_argument('-c', '--close', action='store_true')
    parser.add_argument('-d', '--data', action='store_true')
    parser.add_argument('-t', '--dtun', action='store_true', help='displays the dtun parameters in three columns')
    parser.add_argument('-p', '--parameter', dest='parameter', help='follows a single parameter change')
    global args
    args = parser.parse_args()

    logging.basicConfig(format='[ %(levelname)s ] :: > %(message)s', level=logging.DEBUG)


def main():
    if args.listen:
        try:
            for message in dt.listen():
                patch = dt.Sound(message)
                # logging.info('Prefix:  {}'.format(patch.prefix))
                # logging.info('Meta:    {}'.format(patch.meta))
                # logging.info('Message: {}'.format(patch.meta[1]))
                # logging.info('Name:    {}'.format(patch.name_to_string()))
                # logging.info('Tags:    {}'.format(patch.tag_list))
                logging.info('Data:    '
                             '  {}'.format(patch.param('pb_amt1')))
                # logging.info('EOM:     {}\n'.format(patch.eom))
        except KeyboardInterrupt:
            dt.listen().throw(GeneratorExit)

    elif args.request:
        while True:
            dt.request(args.request)
            time.sleep(.01)

    elif args.dtun:
        dt.request('patch')
        logging.debug('LISTENING FOR DTUN')
        for message in dt.listen():
            dt.request('patch')
            patch = dt.Sound(message)
            number = 653.34

            if 'patch_old' not in locals():
                patch_old = patch.data
            else:
                if patch.data != patch_old:
                    decimal = int(((99 / 127) * int(patch.data[int(0x25)], 16)))
                    msb = int(patch.data[int(0x2f)], 16)
                    if patch.data[int(0x30)] == b'08':
                        number = (((2 * msb) + 1) - 128) + (decimal / 100)
                        # if number < 0:
                        print('{}: {}\t{}: {}\t {}: {}\t\t {:.2f}'.format('0x29', patch.data[int(0x29)],
                                                                          '0x2f', patch.data[int(0x2f)],
                                                                          '0x30', patch.data[int(0x30)],
                                                                          number))
                    else:
                        number = ((2 * msb) - 128) + (decimal / 100)
                        print('{}: {}\t{}: {}\t {}: {}\t\t {:.2f}'.format('0x29', patch.data[int(0x29)],
                                                                          '0x2f', patch.data[int(0x2f)],
                                                                          '0x30', patch.data[int(0x30)],
                                                                          number))


                patch_old = patch.data
            time.sleep(.01)

    elif args.parameter:
        param = args.parameter

    elif args.parameter:
        param = args.parameter
        if param in dt.PARAM_LOOK.keys():
            logging.debug("Listening for {}".format(param))
            dt.request('patch')
            for message in dt.listen():
                patch = dt.Sound(message)
                if 'patch_old' not in locals():
                    patch_old = patch.data
                else:
                    if patch.data != patch_old:

                        if len(dt.PARAM_LOOK[param]) == 1:
                            print('{}: {}'.format(param,
                                                  int(patch.data[int(dt.PARAM_LOOK[param][0], 16)], 16)))

                        elif len(dt.PARAM_LOOK[param]) == 3:
                            neg_bit = dt.PARAM_LOOK[param][0]
                            neg_byte = '{:08b}'.format(int(patch.data[int(dt.PARAM_LOOK[param][1], 16)], 16))
                            value = int(patch.data[int(dt.PARAM_LOOK[param][2], 16)], 16)

                            if neg_byte[neg_bit] == '0':
                                print(param + ': ', value)
                            else:
                                print(param + ': ', value - 128)

                        elif len(dt.PARAM_LOOK[param]) == 4:
                            # TODO: refactor code. Check LFO first, then B as they are the outliers.
                            #       since harm and
                            flag_bit = dt.PARAM_LOOK[param][0]
                            flag_byte = '{:08b}'.format(int(patch.data[int(dt.PARAM_LOOK[param][1], 16)], 16))
                            msb_value = int(patch.data[int(dt.PARAM_LOOK[param][2], 16)], 16)
                            lsb_value = int(patch.data[int(dt.PARAM_LOOK[param][3], 16)], 16)
                            if param == 'harm':
                                msb_value = msb_value - 63
                                if flag_byte[flag_bit] == '0':
                                    lsb_value = int((50 / 127) * lsb_value)
                                    print('{:.2f}'.format(msb_value + (lsb_value / 100)))
                                else:
                                    lsb_value = int((50/ 127) * lsb_value + 50)
                                    print('{:.2f}'.format(msb_value + (lsb_value / 100)))
                            elif param == 'b':
                                # TODO: figure out how to represent the 'b' parameter in a meaningful way

                                # lsb_value = (64/127) * lsb_value
                                msb_value = msb_value * 128
                                if flag_byte[flag_bit] == '1':
                                    lsb_value = int((lsb_value + 127) * (64/127))
                                else:
                                    lsb_value = int((64/127) * lsb_value)
                                value = int(((msb_value) + lsb_value))
                                # print(lsb_value, msb_value, value)
                                print('{}, {}, {}, {}: {}'.format(flag_byte[-1], msb_value, lsb_value, value,
                                                                  dt.PARAM_B[value]))


                            elif 'lfo' in param:
                                lsb_value = (100/127) * lsb_value
                                if flag_byte[flag_bit] == '0':
                                    msb_value = (msb_value * 2) - 128
                                else:
                                    msb_value = (msb_value * 2) - 127
                                print('{:.2f}'.format(msb_value + (lsb_value / 100)))

                            else:
                                if flag_byte[flag_bit] == '0':
                                    lsb_value = int((50 / 127) * lsb_value)
                                    print('{:.2f}'.format(msb_value + (lsb_value / 100)))
                                else:
                                    lsb_value = int((50/ 127) * lsb_value + 50)
                                    print('{:.2f}'.format(msb_value + (lsb_value / 100)))
                        else:
                            print('how the fuck did you even get here? None of the parameters should even have this'
                                  'many byte locations. Check yo goddamn dictionary')
                    patch_old = patch.data
                dt.request('patch')
                time.sleep(0.05)
        else:
            logging.error("Nah, {} is not a valid parameter.".format(param))

        dt.request('patch')

    elif args.monitor:
        dt.request('patch')
        for message in dt.listen():
            dt.request('patch')
            patch = dt.Sound(message)

            if 'patch_old' not in locals():
                patch_old = patch.data
            else:
                for i in range(len(patch.data)):
                    if patch.data[i] != patch_old[i]:
                        print('{}: {}'.format(hex(i), patch.data[i]))
                patch_old = patch.data
            time.sleep(.05)

    elif args.close:
        dt.sysex.listen().throw(KeyboardInterrupt)
    
    elif args.data:
        parameters = dt.constants.PARAM_LOOK
        for param in parameters.keys():
            if len(parameters[param]) == 2:
                print('{}: {}'.format(param, parameters[param]))

    else:
        sysex = dt.decode('data/factory.syx')
        message = dt.parse(sysex)
        for msg in message:
            patch = dt.Sound(msg)
            logging.info('Prefix:  {}'.format(patch.prefix))
            # logging.info('Meta:    {}'.format(patch.meta))
            # logging.info('Message: {}'.format(patch.meta[1]))
            logging.info('Name:    {}'.format(patch.name_to_string()))
            logging.info('Tags:    {}'.format(patch.tag_list))
            # logging.info('DATA:    {}'.format(patch.))
            logging.info('Data:    {}'.format(patch.param_to_dict))
            # logging.info('B        {}'.format(patch.param('b')))
            # logging.info('EOM:     {}\n'.format(patch.eom))
    

if __name__ == '__main__':
    setup()
    main()