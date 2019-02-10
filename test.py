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
                    if patch.data[int(0x31)] == b'08':
                        decimal = int(((50 / 127) * int(patch.data[int(0x35)], 16)) + 50)
                        number = int(patch.data[int(0x34)], 16) + (decimal / 100)
                        print('{}: {}\t{}: {}\t {}: {}\t\t {:.2f}'.format('0x35', patch.data[int(0x35)],
                                                                          '0x34', patch.data[int(0x34)],
                                                                          '0x31', patch.data[int(0x31)],
                                                                          number))
                    else:
                        decimal = int((50 / 127) * int(patch.data[int(0x35)], 16))
                        number = int(patch.data[int(0x34)], 16) + (decimal / 100)
                        print('{}: {}\t{}: {}\t {}: {}\t\t {:.2f}'.format('0x35', patch.data[int(0x35)],
                                                                          '0x34', patch.data[int(0x34)],
                                                                          '0x31', patch.data[int(0x31)],
                                                                          number))


                patch_old = patch.data
            time.sleep(.01)

    elif args.parameter:
        if args.parameter in dt.PARAM_LOOK.keys():
            logging.debug("Listening for {}".format(args.parameter))
            dt.request('patch')
            for message in dt.listen():
                patch = dt.Sound(message)
                if 'patch_old' not in locals():
                    patch_old = patch.data
                else:
                    if patch.data != patch_old:
                        # print(len(dt.PARAM_LOOK[args.parameter]))
                        if len(dt.PARAM_LOOK[args.parameter]) == 1:
                            print('{}: {}'.format(args.parameter,
                                                  int(patch.data[int(dt.PARAM_LOOK[args.parameter][0], 16)], 16)))
                        #
                        # elif len(dt.PARAM_LOOK[args.parameter]) == 3:
                        #     pass
                        #
                        # elif len(dt.PARAM_LOOK[args.parameter]) == 4:
                        #     pass
                    patch_old = patch.data
                dt.request('patch')
                time.sleep(0.05)
        else:
            logging.error("Nah, {} is not a valid parameter.".format(args.parameter))

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
            # logging.info('Prefix:  {}'.format(patch.prefix))
            # logging.info('Meta:    {}'.format(patch.meta))
            # logging.info('Message: {}'.format(patch.meta[1]))
            logging.info('Name:    {}'.format(patch.name_to_string()))
            logging.info('Tags:    {}'.format(patch.tag_list))
            logging.info('Data:    {}'.format(patch.param_to_dict))
            # logging.info('B        {}'.format(patch.param('b')))
            # logging.info('EOM:     {}\n'.format(patch.eom))
    

if __name__ == '__main__':
    setup()
    main()