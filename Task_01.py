def caesar_cipher(text, shift):

  result = ""
  for char in text:
    if char.isalpha():
      if char.isupper():
        start = ord('A')
      else:
        start = ord('a')

      new_index = (ord(char) - start + shift) % 26 + start
      result += chr(new_index)
    else:
      result += char
  return result

def main():
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      text = input("Enter the text to encrypt: ")
      shift = int(input("Enter the shift value: "))
      encrypted_text = caesar_cipher(text, shift)
      print("Encrypted text:", encrypted_text)
    elif choice == 2:
      text = input("Enter the text to decrypt: ")
      shift = int(input("Enter the shift value: "))
      decrypted_text = caesar_cipher(text, -shift)
      print("Decrypted text:", decrypted_text)
    elif choice == 3:
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()