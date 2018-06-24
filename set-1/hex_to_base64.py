import sys

def hex_to_base64(message):
    return message.decode('hex').encode('base64')

if __name__ == '__main__':
    print hex_to_base64(sys.argv[1])
