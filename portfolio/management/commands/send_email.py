from django.core.management.base import BaseCommand
from os import environ
from mailjet_rest import Client
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        recipient = "matthewpaulh@hotmail.co.uk"

        app_key = environ["email application key"]

        secret_key = environ["email secret key"]

        email_client = Client(auth=(app_key, secret_key), version='v3.1')

        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "contact" + settings.BASE_EMAIL_SENDER,
                        "Name": "Me"
                    },
                    "To": [
                        {
                            "Email": recipient,
                            "Name": "You"
                        }
                    ],
                    "Subject": "My first Mailjet Email!",
                    "TextPart": "Greetings from Mailjet!",
                    "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
                }
            ]
        }

        result = email_client.send.create(data=data)
        print(result.status_code)
        print(result.json())