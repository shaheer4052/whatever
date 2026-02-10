# Caesar encrypted and decrypted message generator
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
print("Thanks for using the Caesar Cipher App!")

#________________________   BANK ACCOUNT _________________________________
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.name}'s balance is {self.balance}")


acc1 = BankAccount("Ali", 5000)
acc2 = BankAccount("Sara")

acc1.deposit(1000)
acc2.deposit(300)
acc1.withdraw(2000)

acc1.show_balance()
acc2.show_balance()
