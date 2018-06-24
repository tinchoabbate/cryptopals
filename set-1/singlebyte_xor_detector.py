from singlebyte_xor import singlebyte_xor
from os import path

def singlebyte_xor_detector(data_path):
    with open(path.join(path.dirname(__file__), data_path), 'r') as input_file:
        # Take the best result for each line
        results = []
        for line in input_file:
            results.append(singlebyte_xor(line.rstrip('\n').decode('hex'))[0])
        # Order results by score and return the best one
        return sorted(results, key=lambda pair: pair[1], reverse=True)[0][0]


if __name__ == '__main__':
    data_path = 'data/4.txt'
    print singlebyte_xor_detector(data_path)
    # Now that the party is jumping
    
