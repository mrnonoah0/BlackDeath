try:
    import requests
    import os
    import time
except Exception as e:  
    input(e)

def MailSpam():
    MailSpam = input("Enter the email to spam: ")
    SpamAmount = int(input("Enter the amount of spam emails to send (max 100): "))

    