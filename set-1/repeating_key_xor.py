def repeating_key_xor(message, key):
    return ''.join(chr(ord(c) ^ ord(key[index % len(key)])) for index, c in enumerate(message))

if __name__ == '__main__':
    message = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    key = 'ICE'    
    result = repeating_key_xor(message.decode('ascii'), key.decode('ascii')).encode('hex')
    assert result == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    print result