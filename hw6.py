'''
Created on 10/29/22
@author:   Aryaman Srivastava
Pledge:    I pledge my honor that I will abide by the Stevens Honor System

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def compress(S):
    """takes a binary string of length 64 and returns a binary string which is a run-length encoding of the input string"""
    if S == "":
        return ""
    else:
        numZero = count(S, "0", MAX_RUN_LENGTH)
        S = S[numZero:]
        numBinaryZero = numToBinary(numZero, COMPRESSED_BLOCK_SIZE)
        if len(S) != 0:
            numOne = count(S, "1", MAX_RUN_LENGTH)
            S = S[numOne:]
            numBinaryOne = numToBinary(numOne, COMPRESSED_BLOCK_SIZE)
        else:
            numBinaryOne = ""
        return numBinaryZero + numBinaryOne + compress(S)

def uncompress(C):
    """takes a binary string which is a run-length encoding and returns the original binary string that was put through run-length encoding"""
    if C == "":
        return ""
    else:
        numZero = binaryToNum(C[:COMPRESSED_BLOCK_SIZE])
        C = C[COMPRESSED_BLOCK_SIZE:]
        numOne = binaryToNum(C[:COMPRESSED_BLOCK_SIZE])
        C = C[COMPRESSED_BLOCK_SIZE:]
        return "0"*numZero + "1"*numOne + uncompress(C)

def compression(S):
    """returns ratio of compressed size of given string S to original size of S"""
    return len(compress(S))/len(S)
"""
    The largest number of bits that my compress algorithm could possibly use to encode a 64-bit string is 1024 bits because after this amount, my function reaches the maximum recursion depth, and thus
    a Recursion Error is thrown and the program stops. Any number of bits below this amount, however, my program will still work and produce an output. 
"""



"""
    I ran 4 tests on my compression function, with the following images, the Penguin, the Smile, the Five, An image of only white blocks, and an image of alternating white and black blocks.
    The Penguin had a ratio of 1.484375, the smile had a ratio of 1.328125, the five had a ratio of 1.015625, the image of only white blocks had a ratio of 0.390625 and the image of alternating
    black and white blocks had a ratio of 5.0. 
    What I noticed is that with images with longer consecutive blocks of one color tended to have smaller ratios, while images with smaller consecutive blocks of color tended to have larger ratios.
    This indicates that compression is most effective with images that have long sections of blocks/bits of the same color. 
"""



"""
    Such an algorithm cannot exist as certain images will have very short consecutive blocks of the same color. In other words, the compression algorithm might be compressing the string representing some images into say, "1 black, 1 white, 1 black" repeated. In this case,
    the compressed string will actually be larger than the original string representing the image.
"""

def count(S, char, k):
    """returns the maximum number of consecutive characters(char) in a given string S that can also be expressed in the maximum number of bits for a compressed block size"""
    if S == "" or k == 0:
        return 0
    elif S[0] == char:
        return 1 + count(S[1:], char, k-1)
    else:
        return 0 
    
def numToBinary(n, k):
    """returns the binary representation of a given value using k bits"""
    if k == 0:
        return ''
    if n == 0:
        return '0' + numToBinary(n, k-1)
    elif n%2 != 0:
        return numToBinary(n//2, k-1) + '1'
    else:
        return numToBinary(n//2, k-1) + '0'

def binaryToNum(s):
    """returns the value which is represented by the binary string s"""
    if s == '':
        return 0
    elif int(s[-1]) == 0:
        return 2*binaryToNum(s[:-1]) 
    else:
        return 2*binaryToNum(s[:-1]) + 1

