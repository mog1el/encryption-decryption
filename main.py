import os
import random

def xor_strings(str1, str2):
    return ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(str1, str2))

key = open("key.txt", "a")
if os.stat("key.txt").st_size == 0:
    if_key = input("Looks like you don't have a key. Should I generate a new one? (Y/N)")
    if if_key == "Y":
        print("Generating a new key")
        new_key = random.randint(999999, 999999999)
        key.write(str(new_key))
        print("Key generated")
    else:
        exit("Exiting the code then")
key.close()

bina = []
with open("key.txt", 'rb') as file:
    byte = file.read(1)
    while byte:
        binary_representation = bin(byte[0])[2:]
        bina.append(binary_representation)
        byte = file.read(1)
steps = 1
encrypted_message = []
if os.stat("encrypted.txt").st_size == 0:
    print("I see that you don't have a message that you want to decrypt")
    print("What message would you like to encrypt? (without numbers)")
    message_encryption = str(input())
    #in the future I'm going to make this encryption more random by including in the key something to automate translating letters to numbers
    #if you want to add your own chars, feel free to just add them to this and the next dictionary (I'll do it both into one dictionary in the future)
    char_to_number = {
        'a': '7', 'b': '14', 'c': '5', 'd': '13', 'e': '20',
        'f': '22', 'g': '12', 'h': '21', 'i': '24', 'j': '6',
        'k': '23', 'l': '25', 'm': '18', 'n': '10', 'o': '11',
        'p': '3', 'q': '9', 'r': '8', 's': '15', 't': '26',
        'u': '19', 'v': '2', 'w': '16', 'x': '17', 'y': '4',
        'z': '1', ' ': '27', ',': '28', '.': '29', '?': '30', '!': '31'
    }
    for char in message_encryption:
        encrypted_message.append(char_to_number[char.lower()])
    encrypted_message = [bin(int(x))[2:] for x in encrypted_message]
    encrypted_message = [s.zfill(6) for s in encrypted_message]
    for i in range (len(encrypted_message)):
        step = i % len(bina)
        if i < len(encrypted_message) and step < len(bina):
            result_list = [xor_strings(s1, s2) for s1, s2 in zip(encrypted_message[i], bina[step])]
            encrypted_message[i] = ''.join(result_list)
    for i in range (len(encrypted_message)):
        encrypted_message[i] = int(encrypted_message[i], 2)
    with open("encrypted.txt", "a") as file:
        encrypted_message = ''.join(map(str, encrypted_message))
        file.write(encrypted_message)
else:
    print("Decrypting message...")
    decrypted_message = []
    message_decryption = []
    with open("encrypted.txt", "r") as file:
        file_content = file.read().strip()
    message_decryption = [int(file_content[i:i+2]) for i in range(0, len(file_content), 2)]
    message_decryption = [bin(int(x))[2:] for x in message_decryption]
    for i in range (len(message_decryption)):
        step = i % len(bina)
        result_list = [xor_strings(s1, s2) for s1, s2 in zip(message_decryption[i], bina[step])]
        message_decryption[i] = ''.join(result_list)
    for i in range (len(message_decryption)):
        message_decryption[i] = int(message_decryption[i], 2)
    number_to_char = {
        '7': 'a', '14': 'b', '5': 'c', '13': 'd', '20': 'e',
        '22': 'f', '12': 'g', '21': 'h', '24': 'i', '6': 'j',
        '23': 'k', '25': 'l', '18': 'm', '10': 'n', '11': 'o',
        '3': 'p', '9': 'q', '8': 'r', '15': 's', '26': 't',
        '19': 'u', '2': 'v', '16': 'w', '17': 'x', '4': 'y',
        '1': 'z', '27': ' ', '28': ',', '29': '.', '30': '?', '31': '!'
    }
    for number in message_decryption:
        if str(number) in number_to_char:
            decrypted_message.append(number_to_char[str(number)])
    decrypted_message = ''.join(decrypted_message)
    print("Decrytpted message is:", decrypted_message)
