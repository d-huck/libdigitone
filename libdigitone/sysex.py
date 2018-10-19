from constants import SYSEX_BEGIN
from binascii import hexlify


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

# TODO: request/send individual sysex messages to digitone


def request():
    pass


def send():
    pass

