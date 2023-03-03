import sendgrid
import requests
import re
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
import yahoo_fin.stock_info as stock_info

#date time is important as I have learned many api's will call for a date or time key
import datetime


#Here I have assigned all my variables, hopefully in a fashion that is easy to understand and reads like a story
user_stock = input('Enter the stock tic: ')
apple_price = stock_info.get_live_price('aapl')
game_stop_price = stock_info.get_live_price('gme')
user_stock_price = stock_info.get_live_price(user_stock)
set_price = input('Enter the price you would like to be notified for: ')

#Here I have created a function for my email notification utilizing the Sendgrid API

def Email_Notification():
    #I have included my API-Key which I would usually not give away as it could allow others to make charges onto your account
    response = sendgrid.SendGridAPIClient('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')
    #this is where you can input your approved and authenticated domain
    from_email = Email("Demondboone@gmail.com")  
    #the to email variable will be assigned to the recipient email
    to_email = To("demondboone@gmail.com")  
    subject = "Act Fast - Your Stock Just Reached Your Priecpoint!"
    content = Content("Your Stock Has Reached Its Point!")
    mail = Mail(from_email, to_email, subject, content)
    #this will convert the mail variable into a json
    mail_json = mail.get()
    # this sends an HTTP POST request to /mail/send
    response = response.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)

#My while loop will ensure that the yfinance module continues to scrap the information 
#when the conditions are met my email function will run and the email notification will be sent
while int(set_price) >= int(user_stock_price):
        Email_Notification()
        break
