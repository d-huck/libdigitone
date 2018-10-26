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
    global args
    args = parser.parse_args()

    logging.basicConfig(format='[ %(levelname)s ] :: > %(message)s', level=logging.DEBUG)


def main():
    if args.listen:
        try:
            for message in dt.sysex.listen():
                patch = dt.sound.Sound(message)
                # logging.info('Prefix:  {}'.format(patch.prefix))
                # logging.info('Meta:    {}'.format(patch.meta))
                # logging.info('Message: {}'.format(patch.meta[1]))
                # logging.info('Name:    {}'.format(patch.name_to_string()))
                # logging.info('Tags:    {}'.format(patch.tag_list))
                # logging.info('Data:    {}'.format(patch.param_to_dict()))
                logging.info('pb_amt1:   {}'.format(patch.param('pb_amt1')))
                # logging.info('EOM:     {}\n'.format(patch.eom))
        except KeyboardInterrupt:
            dt.sysex.listen().throw(GeneratorExit)

    elif args.request:
        while True:
            dt.sysex.request(args.request)
            time.sleep(.01)

    elif args.monitor:
        for message in dt.sysex.listen():
            patch = dt.sound.Sound(message)
            if 'patch_old' not in locals():
                patch_old = patch.data
            else:
                for i in range(len(patch.data)):
                    if patch.data[i] != patch_old[i]:
                        print('{}: {}'.format(hex(i), patch.data[i]))
                patch_old = patch.data
            time.sleep(.01)
            # dt.sysex.request('patch')

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
            logging.info('Data:    {}\n'.format(patch.param_to_dict()))
            # logging.info('B        {}'.format(patch.param('b')))
            # logging.info('EOM:     {}\n'.format(patch.eom))
    

if __name__ == '__main__':
    setup()
    main()