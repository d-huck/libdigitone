from constants import SYSEX_BEGIN


def parse(filename):
    with open(filename, 'rb') as file:
        sysex = hexlify(file.read())
        
        messages = []
        for message in sysex.split(SYSEX_BEGIN):

            # filter out the the first split
            if len(message) > 20:
                messages.append(SYSEX_BEGIN + message)

        for message in range(len(messages)):
            messages[message] = [messages[message][i:i + 2] for i in range(0, len(messages[message]), 2)]
        
        return messages