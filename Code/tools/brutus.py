import put

'''
import random
import string
import itertools
# import tqdm
import time

characters = string.printable[:95]
char_length = 8

def passwd_gen(char_length):
    init_pass = ""
    while len(init_pass) < char_length:
        init_pass += random.choice(characters)
    return init_pass

def brute_force(passwd, alphabet):
    start = time.time()
    passwd_tuple = tuple(passwd)
    char_list = [[char for char in alphabet]] * len(passwd)
    args = [char for char in char_list]
    
    for combination in itertools.product(*args):
        if combination == passwd_tuple:
            print(f"found {passwd_tuple}")
    stop = time.time()
'''

def brutus():
    print('This tool has not been implemented yet.')
    put.user_input()