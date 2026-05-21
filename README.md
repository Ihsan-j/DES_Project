# DES Encryption/Decryption Implementation in Python

A complete implementation of the Data Encryption Standard (DES) algorithm in pure Python. This project demonstrates the inner workings of DES including all rounds, S-boxes, key generation, and the Feistel network structure.

## 📋 Overview

This project implements the DES (Data Encryption Standard) algorithm from scratch using Python. It provides a command-line interface for encrypting and decrypting messages using 8-character keys. The implementation follows the standard DES specification including initial/final permutations, 16 rounds of Feistel network, and round key generation.

## ✨ Features

- **Complete DES Implementation**: Full implementation of DES algorithm including:
  - Initial and final permutations (IP/FP)
  - 16 rounds of Feistel network
  - Expansion permutation (32-bit → 48-bit)
  - 8 S-boxes for substitution
  - P-box permutation
  - Round key generation with PC-1 and PC-2 permutations

- **Command-Line Interface**:
  - Encrypt messages to hexadecimal ciphertext
  - Decrypt hexadecimal ciphertext back to plaintext
  - Automated testing with predefined test cases
  - Input validation for keys and ciphertext

- **Block Cipher Mode**: ECB (Electronic Codebook) mode with 8-byte block padding

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (pure Python implementation)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/des-implementation.git
cd des-implementation
Run the program:

bash
python main.py
💻 Usage
Main Menu
When you run the program, you'll see:

text
==================================================
DES Encryption/Decryption Tool
==================================================
1. Encrypt
2. Decrypt
3. Test
4. Exit

Choice:
Encryption
Select option 1 and provide:

Text: The message to encrypt (any text)

Key: Exactly 8 characters (e.g., "SECRET12")

Example:

text
Choice: 1
Text to encrypt: Hello World!
Key (8 chars exactly): PASSWORD

Encrypted (HEX): 77E645767536B30D
Decryption
Select option 2 and provide:

Ciphertext (HEX): The hexadecimal ciphertext from encryption

Key: The same 8-character key used for encryption

Example:

text
Choice: 2
Ciphertext (HEX): 77E645767536B30D
Key (8 chars exactly): PASSWORD

Decrypted text: Hello World!
Testing
Select option 3 to run automated tests:

Tests multiple plaintext/key combinations

Verifies encryption/decryption works correctly

Shows PASS/FAIL results for each test case

📁 Project Structure
text
des-implementation/
│
├── main.py              # Main CLI interface and user interaction
├── des_rounds.py        # DES round operations and Feistel network
├── feistel.py           # Feistel function (expansion, S-box, P-box)
├── key_generation.py    # Round key generation from 64-bit key
├── utils.py             # Utility functions (binary conversion, padding, permutations)
└── README.md            # Project documentation
🔧 How It Works
Encryption Process
Key Processing:

8-character key (64 bits) is converted to binary

PC-1 permutation reduces to 56 bits

16 round keys (48 bits each) are generated using left shifts and PC-2

Block Processing:

Plaintext is padded to multiple of 8 bytes

Each 64-bit block undergoes:

Initial permutation (IP)

16 rounds of Feistel network

Final permutation (FP)

Feistel Function (per round):

Right half (32 bits) is expanded to 48 bits

XOR with round key (48 bits)

S-box substitution (48 → 32 bits)

P-box permutation (32 bits)

Decryption Process
Decryption uses the same process but with round keys applied in reverse order (keys[::-1]).

📊 DES Parameters
Parameter	Size	Description
Block Size	64 bits	Processes data in 8-byte blocks
Key Size	64 bits	8-character key (56 effective bits)
Rounds	16	Number of Feistel network rounds
Round Key Size	48 bits	Generated from original key
S-boxes	8	Each maps 6 bits → 4 bits
🧪 Test Cases
The program includes automated tests for:

Regular text messages

Single characters

Empty strings

Various key combinations

All test cases verify that encryption followed by decryption returns the original plaintext.

⚠️ Limitations
Educational Purpose Only: This implementation is for learning and should not be used for real-world security

ECB Mode: Electronic Codebook mode is not secure for patterns in data

No Padding Scheme: Uses simple null-byte padding (not PKCS#7)

Single Block: Designed for educational understanding, not production use

🔐 Security Note
DES is considered insecure for modern applications due to its 56-bit effective key length, which can be brute-forced. This implementation is intended for:

Educational purposes

Understanding cryptographic algorithms

Learning about Feistel networks and S-boxes

For real-world applications, consider using AES (Advanced Encryption Standard).

🤝 Contributing
Contributions are welcome! Feel free to:

Report bugs

Suggest improvements

Submit pull requests

📝 License
This project is open source and available under the MIT License.

👨‍💻 Author
Ashenafi Bancha
Elham Jemal
Feruza Hassen
Ihsan Jemal

🙏 Acknowledgments
The original DES specification (FIPS PUB 46-3)

Claude Shannon's work on confusion and diffusion

The cryptographic community for educational resources

📖 References
DES Specification (FIPS PUB 46-3)

The DES Algorithm Illustrated

Note: This is an educational implementation. For production use, please use established cryptographic libraries like cryptography or pycryptodome.

text

This README provides:
- Clear project description and features
- Installation and usage instructions
- Technical details about the DES implementation
- Project structure explanation
- Limitations and security notes
- Professional formatting for GitHub

You can customize the author name, GitHub repository URL, and add any additional details specific to your project.