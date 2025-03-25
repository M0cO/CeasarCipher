logo = """
  /$$$$$$                                                   
 /$$__  $$                                                  
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$       /$$__  $$ |____  $$ /$$_____/ |____  $$ /$$__  $$
| $$      | $$$$$$$$  /$$$$$$$|  $$$$$$   /$$$$$$$| $$  \__/
| $$    $$| $$_____/ /$$__  $$ \____  $$ /$$__  $$| $$      
|  $$$$$$/|  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$      
 \______/  \_______/ \_______/|_______/  \_______/|__/      
                                                            
                                                            
                                                            
  /$$$$$$  /$$           /$$                                
 /$$__  $$|__/          | $$                                
| $$  \__/ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       
| $$      | $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$      
| $$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/      
| $$    $$| $$| $$  | $$| $$  | $$| $$_____/| $$            
|  $$$$$$/| $$| $$$$$$$/| $$  | $$|  $$$$$$$| $$            
 \______/ |__/| $$____/ |__/  |__/ \_______/|__/            
              | $$                                          
              | $$                                          
              |__/                                          
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(original_text, shift_amount):
    cipher_text = ""
    cipher_text2 = ""
    if direction == 'encode':
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)# always makes sure we stay within alphabet
                cipher_text += alphabet[shifted_position]
        print(f"Results:{cipher_text}")
    else:
        for letter in original_text:
            if letter not in alphabet:
                cipher_text2 += letter #if character inputted is not in the alphabet, it will insert the character inputted in cipher_text2.
            else:
                back_words = alphabet.index(letter) - shift_amount
                back_words %= len(alphabet)
                cipher_text2 += alphabet[back_words]
        print(f"Results:{cipher_text2}")

ceasar(original_text=text, shift_amount=shift)


want_continue = input("Do you want to encrypt/decode something else? Type 'yes' or 'no'")

while want_continue == 'yes':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(original_text=text, shift_amount=shift)
    want_continue = input("Do you want to encrypt/decode something else? Type 'yes' or 'no'")
else:
    print("come back again")
