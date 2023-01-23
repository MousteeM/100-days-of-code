from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(message, shift_amount, direction):
    endText = ''
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'decode':
                newPosition = position - shift_amount
            elif direction == 'encode':
                newPosition = position + shift_amount
            newLetter = alphabet[newPosition]
            endText += newLetter
        else:
            endText += char
    print(f'The {instruction}d text is {endText}')


cipherText = True
while cipherText:
    instruction = input("Type 'encode' to encrypt, and 'decode' to decrypt:\n")
    text = input(f"Enter the message you would like to {instruction}:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 25
        
    caeser(message=text, shift_amount=shift, direction=instruction)
    
    goAgain = input("Would you like to go again? 'yes' or 'no'\n")
    if goAgain == 'no':
        cipherText = False
