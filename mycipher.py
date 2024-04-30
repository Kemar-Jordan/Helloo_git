import sys

def caeser_cipher(text,shift):
    encoded = []
    for char in text:
        if char.isalpha():
            shifted = ord(char.upper()) + shift
            if shifted > ord('Z'):
                shifted -=26
            encoded.append(chr(shifted))
    return ''.join(encoded)

def format_output(encoded_text):
    output = []
    for i in range(0,len(encoded_text),5):
        output.append(encoded_text[i:i + 5])
    for i in range(0,len(output),10):
        print(' '.join(output[i:i + 10]))

if __name__ == "__main__":
    if len(sys.argv) not in [2,3]:
        print("Usage: python caeser_cipher.py <shift> [input_file]")
        sys.exit(1)

    shift = int(sys.argv[1])
    if len(sys.argv) == 3:
        with open(sys.argv[2], 'r') as file:
            input_text = file.read().strip()
    else:
        input_text = sys.stdin.read().strip()
    encoded_text = caeser_cipher(input_text, shift)
    format_output(encoded_text)
