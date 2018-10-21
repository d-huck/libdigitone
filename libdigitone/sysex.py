from . import constants
from binascii import hexlify

import mido

# TODO: PICKLE THIS SHIT
SYSEX_BEGIN = constants.SYSEX_BEGIN


def decode(filename):
    with open(filename, 'rb') as file:
        sysex = hexlify(file.read())
        return sysex


# TODO: encode sysex data to send to digitone


def encode(sysex, filename):
    pass


def parse(sysex):
    """

    :param sysex: sysex message to parse; expects a string
    :return: list of sysex messages, parsed into lists of individual bytes
    """
    messages = []
    for message in sysex.split(SYSEX_BEGIN):

        # filter out the the first split
        if len(message) > 20:
            messages.append(SYSEX_BEGIN + message)

    if len(messages) > 1:
        for message in range(len(messages)):
            messages[message] = [messages[message][i:i + 2] for i in range(0, len(messages[message]), 2)]
    else:
        messages = [messages[0][i:i + 2] for i in range(0, len(messages[0]), 2)]

    return messages


# TODO: function to combine several sysex messages after processing


def combine():
    pass


# TODO: request/send individual sysex messages to digitone


def request(message, track=0):
    outport = mido.open_output('Elektron Digitone Digitone out 1')
    if message == 'patch':
        msg_array = [int('0x00', 16), int('0x20', 16), int('0x3c', 16), int('0x0d', 16), int('0x00', 16),
                     int('0x6B', 16), int('0x01', 16), int('0x01', 16), 0, int('0x00', 16),
                     int('0x00', 16), int('0x00', 16), int('0x05', 16)]
        msg = mido.Message('sysex', data=msg_array)
        outport.send(msg)


def listen():
    """

    :return:
    """
    inport = mido.open_input('Elektron Digitone Digitone in 1')
    for msg in inport:
        try:
            if msg.type == 'sysex':
                msg = bytes(msg.hex(), 'utf-8').split()
                yield msg

        except KeyboardInterrupt:
            inport.close()
            break


def send(messages):
    inport = mido.open_output('Elektron Digitone Digitone out 1')


if __name__ == '__main__':
    pass
