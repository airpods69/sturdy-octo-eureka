# Pass-Gen

## About

A password generator which is just an encryption but hey atleast you won't have to remember your passwords!
For every key + email + website combination, the output is always the same, ie Your password.

## How does it work
- For inputs we have
	1. Key -> hard limited to 8 characters.
	2. Website -> The website name.
	3. Email -> The email address for which you need the password

- These inputs are fed into the program which has some magical skills that even I don't understand (DES encryption :D) and returns a set of characters or as I call it, Password.

This is how it should look like in practice
```shell
python main.py -w testwebsite -e test@mail.com -k testkey1
Password:  b'[b5O#1e8e50f316f9 3p1a9503e4Ej+${bbp289r98xdcc4'
Email:  b'testwebsitetest@mail.com        '
```

