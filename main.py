import argparse
from Crypto.Cipher import DES

def arguments() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--website", required=True,  help="Name of Website")
    parser.add_argument("-e", "--email", required=True, help="Email ID")
    parser.add_argument("-k", "--key", required=True, help="Password key to generate password")

    return parser

def pad(text):
    n = len(text) - len(text) % 8 + 8
    return text + (b' ' * (n - len(text)))

def main():

    args = arguments().parse_args()

    key = args.key.encode()
    website = args.website.encode()
    email = args.email.encode()

    text1 = website + email

    des = DES.new(key, DES.MODE_ECB)

    padded_text = pad(text1)
    encrypted_text = des.encrypt(padded_text)

    print("Password: ", ''.join(str(encrypted_text).split("\\x")))
    print("Email: ", des.decrypt(encrypted_text))

if __name__ == "__main__":
    main()
