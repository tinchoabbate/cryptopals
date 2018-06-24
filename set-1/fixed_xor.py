import sys

def fixed_xor(message, mask):
    # Message and mask should have same length
    output = ''
    for (c1, c2) in zip(message, mask):
        output += chr(ord(c1) ^ ord(c2))
    return output

if __name__ == '__main__':
    print fixed_xor(sys.argv[1].decode('hex'), sys.argv[2].decode('hex')).encode('hex')
