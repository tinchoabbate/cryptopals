import sys
from helpers import get_freq_score

def singlebyte_xor(encrypted_message):
    """
    Decrypts the given message using a bruteforcing XOR single-byte decipher.
    It returns a list of tuples in the form (message, score), descendently ordered by score.
    """
    
    decrypted_messages = []
    scores = []
    for key in range(2**8): # 1 byte
        message = ''.join(chr(ord(c) ^ key) for c in encrypted_message)
        decrypted_messages.append(message)
        scores.append(get_freq_score(message))
    
    return sorted(zip(decrypted_messages, scores), key=lambda pair: pair[1], reverse=True)


if __name__ == '__main__':
    print singlebyte_xor(sys.argv[1].decode('hex'))[0][0]
    # "Cooking MC's like a pound of bacon"
