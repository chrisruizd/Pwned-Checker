# Pwned-Checker
This program checks if a password or email have ever been compromised in a data breach.

This program uses SHA-1 to hash the password, and using the first 5 characters of the hashed password, it searches for all the compromised passwords in the data set that have the same first 5 hashed characters. Then, it returns the list and searches for the specific entered password. That way the password is not sent exactly as it is through the internet, protecting the user's password.
The website displays if the password has been hacked, followed by a count of how many times it appears in the data set, and if not found, the website displays that the password is not compromised.


PownedOrNot and Complete Pyhton Developer in 2022 ZTM course used as sources of learning for this project

