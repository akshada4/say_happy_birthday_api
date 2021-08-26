from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def sendMessage(sender_name, celebrant_name, number):
    message = sender_name + ' says: happy birthday, ' + celebrant_name 
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token) 
     
    message = client.messages.create(
                              messaging_service_sid=os.getenv("MESSAGING_SID"),  
                              body=message,      
                              to=number
                          ) 