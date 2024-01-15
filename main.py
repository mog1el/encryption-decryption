import os
import random

key = open("key.txt", "a")
if os.stat("key.txt").st_size == 0:
    if_key = input("Looks like you don't have a key. Should I generate a new one? (Y/N)")
    if if_key == "Y":
        print("Generating a new key")
        new_key = random.randint(1024, 4058)
        key.write(str(new_key))
        print("Key generated")
    else:
        exit("Exiting the code then")

bina = []
with open("key.txt", 'rb') as file:
    byte = file.read(1)
    while byte:
        binary_representation = bin(byte[0])[2:]
        bina.append(binary_representation)
        byte = file.read(1)
print(bina)
steps = 1
encrypted_message = []
if os.stat("encrypted.txt").st_size == 0:
    print("I see that you don't have a message that you want to decrypt")
    print("What message would you like to encrypt? (without numbers and special characters)")
    message_encryption = str(input())
    #in the future I'm going to make this encryption more random by including in the key something to automate translating letters to numbers
    for i in range(len(message_encryption)):
        if message_encryption[i].lower() == "a":
            encrypted_message.append("7")
        elif message_encryption[i].lower() == "b":
            encrypted_message.append("14")
        elif message_encryption[i].lower() == "c":
            encrypted_message.append("5")
        elif message_encryption[i].lower() == "d":
            encrypted_message.append("13")
        elif message_encryption[i].lower() == "e":
            encrypted_message.append("20")
        elif message_encryption[i].lower() == "f":
            encrypted_message.append("22")
        elif message_encryption[i].lower() == "g":
            encrypted_message.append("12")
        elif message_encryption[i].lower() == "h":
            encrypted_message.append("21")
        elif message_encryption[i].lower() == "i":
            encrypted_message.append("24")
        elif message_encryption[i].lower() == "j":
            encrypted_message.append("6")
        elif message_encryption[i].lower() == "k":
            encrypted_message.append("23")
        elif message_encryption[i].lower() == "l":
            encrypted_message.append("25")
        elif message_encryption[i].lower() == "m":
            encrypted_message.append("18")
        elif message_encryption[i].lower() == "n":
            encrypted_message.append("10")
        elif message_encryption[i].lower() == "o":
            encrypted_message.append("11")
        elif message_encryption[i].lower() == "p":
            encrypted_message.append("3")
        elif message_encryption[i].lower() == "q":
            encrypted_message.append("9")
        elif message_encryption[i].lower() == "r":
            encrypted_message.append("8")
        elif message_encryption[i].lower() == "s":
            encrypted_message.append("15")
        elif message_encryption[i].lower() == "t":
            encrypted_message.append("26")
        elif message_encryption[i].lower() == "u":
            encrypted_message.append("19")
        elif message_encryption[i].lower() == "v":
            encrypted_message.append("2")
        elif message_encryption[i].lower() == "w":
            encrypted_message.append("16")
        elif message_encryption[i].lower() == "x":
            encrypted_message.append("17")
        elif message_encryption[i].lower() == "y":
            encrypted_message.append("4")
        elif message_encryption[i].lower() == "z":
            encrypted_message.append("1")
    encrypted_message = [bin(int(x))[2:] for x in encrypted_message]
    encrypted_message = [s.zfill(6) for s in encrypted_message]
    def xor_strings(str1, str2):
        return ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(str1, str2))
    for i in range (len(encrypted_message)):
        step = i%4
        result_list = [xor_strings(s1, s2) for s1, s2 in zip(encrypted_message[i], bina[step])]
        print(bina[step])
        encrypted_message[i] = ''.join(result_list)
    for i in range (len(encrypted_message)):
        encrypted_message[i] = int(encrypted_message[i], 2)
    with open("encrypted.txt", "a") as file:
        encrypted_message = ''.join(map(str, encrypted_message))
        file.write(encrypted_message)