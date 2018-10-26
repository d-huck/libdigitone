from .constants import *
from binascii import hexlify, unhexlify

import mido

# TODO: PICKLE THIS SHIT
# SYSEX_BEGIN = constants.SYSEX_BEGIN


def decode(filename):
    """ Decodes sysex file and converts to bytestring

    :param filename: expects binary .syx file from the digitone
    :return: hexlified byte string representing binary file
    """
    with open(filename, 'rb') as file:
        sysex = hexlify(file.read())
        return sysex


# TODO: encode sysex data to send to digitone


def encode(sysex, filename='digi_out.syx'):
    """

    :param sysex: sysex byte string
    :param filename: desired output binary .syx file name
    """
    with open(filename, 'wb') as file:
        sysex = unhexlify(sysex)
        file.write(sysex)

    file.close()


def parse(sysex):
    """ Takes a sysex message and parses it into a list of bytes

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


def combine(sysex):

    # Check if the input is a list of list or simply a list
    if type(sysex[0]) == list:
        for i in range(len(sysex)):
            sysex[i] = b''.join(sysex[i])

    sysex_out = b''.join(sysex)
    return sysex_out


# TODO: request/send individual sysex messages to digitone


def request(message, track=0):
    """ Request a sysex dump from the Digitone

    :param message: type of message to be required. Currently supports:
                        patch
    :param track: Which track or pattern to request. Currently defaults to 0
    :return: None
    """
    outport = mido.open_output('Elektron Digitone Digitone out 1')
    if message == 'patch':
        msg_array = [int('0x00', 16), int('0x20', 16), int('0x3c', 16), int('0x0d', 16), int('0x00', 16),
                     int('0x6B', 16), int('0x01', 16), int('0x01', 16), 0, int('0x00', 16),
                     int('0x00', 16), int('0x00', 16), int('0x05', 16)]
        msg = mido.Message('sysex', data=msg_array)
        outport.send(msg)


def listen():
    """ Listens for sysex messages from the digitone. Stays open as a loop

        TODO: Currently does not exit gracefully. Need to find better way

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
