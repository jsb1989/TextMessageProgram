import os
from twilio.rest import Client

account_num=input("Enter account SID number: ");
account_token=input("Enter account token:")
client=Client(account_num,account_token)

from_phone=input("Enter you twilio phone number: ")
to_phone=input("Enter the phone number you are sending the message to: ")
your_message=input("Enter the message you are sending: ")

message=client.messages \
	.create(
		body=your_message,
		from_="+"+from_phone,
		to="+"+to_phone
	)
