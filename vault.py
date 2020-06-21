#!/usr/bin/python

#Load some libs
import sys
import random

#Function for requesting the user to input a secret key
def ask_key():
    key = input("Please enter key:\n")
    seed = ""

    for i in key: #Iterate over each character and convert to ascii decimal value
        seed += str(ord(i)) #Concatenate up each ascii value into a single string
    print("Using key", seed,"\n")
    random.seed(a=seed) #Use the concatenated string as a seed for random
    cipher = random.randint(1,255) #Create a random integer 1-255

    return(cipher)
 
#Function for encrypting data
def encrypt():
    cipher = ask_key() #Run function to get user input for key
    my_file = open(sys.argv[2], "r") #Open up the file with a secret message
    
    my_data = ""
    for i in my_file.read(): #Iterate over each character
        my_data += str(ord(i)) #Concatenate the ascii decimal value of each character
        my_data += " " #Add spaces in between
    
    n = 0
    encoded = ""
    encode_step_1 = ""
    encode_step_2 = cipher
    length = len(my_data.split())
    
    for i in range(0, length):
        encode_step_1 = ""
        encode_step_1 += str(my_data.split(" ")[n]) #Iterate over each ascii value set
        encode_step_2 = int(cipher) #I do a lot of casting like this due to the kind of operations I run
        encode_step_2 += int(encode_step_1) #Add up the cipher and the ascii value to make a new (sometimes not ascii) value
        encoded += str(encode_step_2) #Concatenate up into a single string of numbers
        encoded += " "
        n+=1

    output_file = open(sys.argv[3], "w") #Open a new file to be saved
    output_file.write(encoded) #Write the encoded string to the new file
    output_file.close() #Close the file

    print("Done!")

    return(encoded)

#Function for decrypting data
def decrypt():
    cipher = int(ask_key())
    my_data = ""
    n = 0
    decode_step_1 = 0
    decoded = ""
    
    my_file = open(sys.argv[2], "r")

    for i in my_file.read():
        my_data += i 

    length = len(my_data.split())
    for i in range(0,length):
        decode_step_1 = 0
        decode_step_1 = abs(int(my_data.split(" ")[n]) - cipher)
        for x in str(decode_step_1).split(" "):
            decoded += chr(decode_step_1)
        n += 1

    print(decoded)
    return(decoded)

#Check for user input and run appropriate function
if len(sys.argv) != 1:
    if sys.argv[1] == "--encrypt" or sys.argv[1] == "-e":
        if len(sys.argv) == 4:
            encrypt()
        elif len(sys.argv) == 3:
            print("Missing output file")
        else:
            print("Missing file to encrypt")
            exit(1)
    elif sys.argv[1] == "--decrypt" or sys.argv[1] == "-d":
        if len(sys.argv) == 3:
            decrypt()
        else:
            print("Missing file to decrypt")
            exit(1)
    elif ((sys.argv[1] == "-h") or (sys.argv[1] == "--help")):
        print("Usage: vault {--encypt | -e} INFILE OUTFILE\n       vault {--decrypt | -d} INFILE")
    else:
        print("vault requires an argument!")
        print("Try 'vault -h for more information.")
else:
        print("vault requires an argument!")
        print("Try 'vault -h for more information.")
