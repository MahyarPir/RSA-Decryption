
"""
RSA Decryption Program by Mahyar Pirayesh
"""

import ast

def decrypt_with_ascii():  # With ASCII codes
    print(f"RSA Decryption using ASCII by Mahyar Pirayesh")
    p1 = int(input("What is YOUR prime? "))
    N = int(input("What is the product of the primes (N)? "))
    e = int(input("What is the encryption key shared by the other party? "))
    message = ast.literal_eval(input("Please write a list of each encrypted number corresponding to each letter; Please write in this form --> [W, X, Y, Z] : "))  # We turn the inputted string into an actual list, which is the reason for the ast import

    # Our ASCII Dictionary
    asciiDict = {i: chr(i) for i in range(128)}

    # We define the other prime, Z, and find our decryption key with the info given
    p2 = N / p1  # Calculate p2
    Z = (p1 - 1) * (p2 - 1)
    for x in range(2, 1000000000000):  # Finds our decryption key using Z and e with brute force
        d = (1 + x * Z)/e
        if d.is_integer():
            d = int(d)
            break  # We stop when we find an integer d

    # Decryption process is repeated for every letter in order to decipher
    decrypted_list = []
    for item in message:
        decrypted_list.append(str(int(((int(item))**d)%N)))  # m = c^d (mod N)

    # We now turn the numbers corresponding to each letter (according to ASCII) into letters and prints out our sentence!
    decrypted_message = ""
    for item in decrypted_list:
        try:
          decrypted_message = decrypted_message + asciiDict[(int(item))]
        except:
          print(f"The number {(int(item)**int(e))%int(N)} does not correspond to any ASCII Character, so it has been excluded from the sentence.")
    return(f"Decrypted message: {decrypted_message}") # Voila, done!


# We actually call the function now
print(decrypt_with_ascii())
