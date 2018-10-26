import libdigitone as dt
import logging
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--listen', action="store_true", help='Turns on verbose output')
parser.add_argument('-m', '--monitor', action="store_true", help='Monitor for parameter changes')
parser.add_argument('-r', '--request', dest="request", action="store")

args = parser.parse_args()

logging.basicConfig(format='%(asctime)s :: %(levelname)s :> %(message)s', level=logging.INFO)

if args.listen:
    for message in dt.sysex.listen():
        patch = dt.sound.Sound(message)
        logging.debug('Prefix:  {}'.format(patch.prefix))
        logging.debug('Meta:    {}'.format(patch.meta))
        logging.debug('Message: {}'.format(patch.meta[1]))
        logging.debug('Name:    {}'.format(patch.name_to_string()))
        logging.debug('Tags:    {}'.format(patch.tag_list()))
        logging.debug('Data:    {}'.format(patch.param_to_dict()))
        logging.debug('B        {}'.format(patch.param('b')))
        logging.debug('EOM:     {}\n'.format(patch.eom))

elif args.request:
    dt.sysex.request(args.request)

# TODO: Write monitor script that will detect changed parameters
elif args.monitor:
    for message in dt.sysex.listen():
        patch = dt.sound.Sound(message)
        # print(patch.data)
        if 'patch_old' not in locals():
            patch_old = patch.data
        else:
            for i in range(len(patch.data)):
                if patch.data[i] != patch_old[i]:
                    print('{}: {}'.format(hex(i), patch.data[i]))
            patch_old = patch.data
        time.sleep(.01)
        dt.sysex.request('patch')


else:
    message = dt.decode('blank_patch.syx')
    bytes_ = dt.parse(message)
    logging.debug(bytes_)
    patch = dt.Sound(bytes_)
    logging.debug('Prefix:  {}'.format(patch.prefix))
    logging.debug('Meta:    {}'.format(patch.meta))
    logging.debug('Message: {}'.format(patch.meta[1]))
    logging.debug('Name:    {}'.format(patch.name_to_string()))
    logging.debug('Tags:    {}'.format(patch.tag_list()))
    logging.debug('Data:    {}'.format(patch.param_to_dict()))
    logging.debug('B        {}'.format(patch.param('b')))
    logging.debug('EOM:     {}\n'.format(patch.eom))