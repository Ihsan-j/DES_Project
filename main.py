from utils import (
    text_to_binary,
    binary_to_text,
    hex_to_binary,
    binary_to_hex,
    pad_plaintext,
    unpad_plaintext
)
from key_generation import generate_round_keys
from des_rounds import encrypt


def decrypt_block(block, keys):
    return encrypt(block, keys[::-1])


def encrypt_message(text, key):
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters")
    
    key_bin = text_to_binary(key)
    keys = generate_round_keys(key_bin)
    padded_text = pad_plaintext(text)
    
    result = ""
    for i in range(0, len(padded_text), 8):
        block_bin = text_to_binary(padded_text[i:i+8])
        result += encrypt(block_bin, keys)
    
    return binary_to_hex(result)


def decrypt_message(cipher_hex, key):
    # Validate hex input
    if not all(c in '0123456789ABCDEFabcdef' for c in cipher_hex):
        raise ValueError("Ciphertext must be in hexadecimal format")
    
    key_bin = text_to_binary(key)
    keys = generate_round_keys(key_bin)
    binary = hex_to_binary(cipher_hex)
    
    result = ""
    for i in range(0, len(binary), 64):
        if i + 64 <= len(binary):
            result += decrypt_block(binary[i:i+64], keys)
    
    return unpad_plaintext(binary_to_text(result))


def test():
    test_cases = [
        ("Hello123", "SECRET12"),
        ("Hi", "12345678"),
        ("Test", "PASSWORD"),
        ("A", "12345678"),
        ("", "12345678")
    ]
    
    print("\n" + "="*50)
    print("TEST RESULTS")
    print("="*50)
    
    for plaintext, key in test_cases:
        try:
            cipher = encrypt_message(plaintext, key)
            decrypted = decrypt_message(cipher, key)
            status = "✓ PASS" if plaintext == decrypted else "✗ FAIL"
            print(f"\nText: '{plaintext}'")
            print(f"Cipher: {cipher}")
            print(f"Result: '{decrypted}'")
            print(status)
        except Exception as e:
            print(f"\n'{plaintext}' with key '{key}': ERROR - {e}")
        print("-" * 40)


def main():
    while True:
        print("\n" + "=" * 50)
        print("DES Encryption/Decryption Tool")
        print("=" * 50)
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Test")
        print("4. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            text = input("Text to encrypt: ")
            key = input("Key (8 chars exactly): ")
            if len(key) != 8:
                print("Error: Key must be exactly 8 characters!")
                continue
            try:
                result = encrypt_message(text, key)
                print(f"\nEncrypted (HEX): {result}")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == "2":
            cipher = input("Ciphertext (HEX): ").strip()
            key = input("Key (8 chars exactly): ")
            if len(key) != 8:
                print("Error: Key must be exactly 8 characters!")
                continue
            try:
                result = decrypt_message(cipher, key)
                print(f"\nDecrypted text: {result}")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == "3":
            test()
        
        elif choice == "4":
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()