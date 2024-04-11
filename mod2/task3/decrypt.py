import re
import sys


def decrypt_efficient(message):
    stack = []

    i = 0
    while i < len(message):
        if message[i] == '.':
            if i + 1 < len(message) and message[i + 1] == '.':
                if stack:
                    stack.pop()
                i += 2
                continue
            else:
                i += 1
                continue
        else:
            stack.append(message[i])
        i += 1

    return ''.join(stack)


def decrypt_regex(message):
    while True:
        m = re.search('\.\.', message)
        if not m:
            break
        message = message[:max(0, m.start() - 1)] + message[m.end():]

    while True:
        m = re.search('\.', message)
        if not m:
            break
        message = message[: m.start()] + message[m.end():]

    return message


if __name__ == '__main__':
    input_message = sys.stdin.read().replace('\n', '')
    print(decrypt_efficient(input_message))
