# Pwned-Checker
This program checks if a password or email have ever been hacked

This program uses SHA-1 to hash the pasword, that way your password is not send exactly as it is throug the internet.
Additionally, it only send the first 5 characters of your password, hashed
When a password hash with the same first 5 characters is found, it displays the suffix of every hash beginning with the specified prefix, followed by a count of how many times it appears in the data set and if not found, the password does not exist in the data set
It returns a list with every password that begins with the same 5 hashed characters as your password
Then the program searches in the returned list for any match in the passwords that contain the first 5 character, but now in your actual computer, making
it more secure.

# PownedOrNot and Complete Pyhton Developer in 2022 ZTM course used as sources of learning for this project

# Steps
- Website setup, design
- Get input from user
- Crate the hash: SHA-1 hash, doing it entirelly in the client so the info does not need to trave throug internet
- Split the hash
- ???
- Look at the result list
- clean data: separate hashed passwords from appearances, split by ":"
- serach your specific password in the list
- Create a new web path with the printed info
