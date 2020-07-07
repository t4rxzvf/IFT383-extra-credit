# IFT383-extra-credit
### Usage  
`vault [--key-from-stdin] {--encypt | -e} INFILE OUTFILE`  
`vault [--key-from-stdin] {--decrypt | -d} INFILE`
  
### Overview
  This is a Python script for encrypting and decrypting ascii text using a simple cipher. There are three main parts to the script- requesting the user to input a key, encrypting, and decrypting text.  
  
  Getting the key is a farly simple function. Once the user enters in a secret word or phrase, the function will then convert each character into its ascii equivalent. Once this is done, that ascii equivalent of the secret key is used as a seed for the random function to generate a pseudo-random integer 1-255. The encryption part takes in the secret file provided and converts it into a list of ascii vaules (simiar to the key function). The resulting list is taken and each item has the secret cipher added to it (the random 1-255 integer). This changes each value of the list into a different value. This is then written to the provided OUTFILE argument. Decrypting is the revese of encrypting. The encrypted file is read in as a list, the list is manipulated by subtracting the (read in and calculated) secret key value. Afterwards each character is converted from the decimal ascii value into the original alphanumeric text and writted to the terminal. 
  
  In testing the script, I started with the key creation part. I wanted a way to easily create a cipher that was just complex enough to work but not as crazy as more secure methods. I initially stared with using the entire integer ascii representation of the key.  However, this would quickly turn a sentence or two into a list of giant numbers that would grow as quickly as the sentence was long. I decided upon simply using the key as a seed value for selecting a random integer 1-255. This would allow me to randomly select an ascii value based off a known seed (the user key). The next hurdle was the actual process of encrypting (and decrypting) the input. I had a bit of a tough time dealing with the loop and arithmetic of converting the input file.

  If I had to give myself some advice before starting this project it would have been to look into Python objects.  I had completed this two weeks ago before we had gotten to Python classes and objects.  I think that would have been fun to try and implement OOP for this project.
