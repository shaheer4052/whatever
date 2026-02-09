import string

alphabet = string.ascii_lowercase + " " 
shift = 3
shifted_alphabet = alphabet[shift:] + alphabet[:shift]

encrypt_dict = {a: s for a, s in zip(alphabet, shifted_alphabet)}
decrypt_dict = {s: a for s, a in zip(shifted_alphabet, alphabet)}

mode = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()
user_input = input("Enter your message: ").lower()

if mode == 'E':
    mapping = encrypt_dict
else:
    mapping = decrypt_dict

secret_msg = ""

for char in user_input:
    # Use 'mapping' here so it works for both E and D!
    new_char = mapping.get(char, char)
    secret_msg += new_char

print(f"\nFinal Result: {secret_msg}")