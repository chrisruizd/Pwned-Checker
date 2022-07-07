
from unittest import result
import requests
import hashlib
import sys
from flask import Flask, render_template, url_for, request, redirect
import csv

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res
  
def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)  # passing first 5 characters of the pasw
  return get_password_leaks_count(response, tail)
  
def main(password):
  count = pwned_api_check(password)
  if count:
    flag = 1
    return (f'{password} was found {count} times... you should probably change your password!')
  else:
    return (f'{password} was NOT found. Carry on!')
  

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('login.html')
    print()

@app.route('/checked', methods=['POST', 'GET'])
def psw_checked():
  password = request.form['password'] #putting password entered by user into a variable, request.args is for get, request.form is for post
  print('\n'+password + '\n')
  print(type(password))
  result= main(password)  
  return render_template('checked.html', result=result)

if __name__ == '__main__':
  app.run(debug=True)  



