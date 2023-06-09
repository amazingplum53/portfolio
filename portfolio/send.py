from os import environ
from mailjet_rest import Client
from django.conf import settings
from base64 import b64encode


def file_encode(file_path):

    with open(file_path, "rb") as f:

        return b64encode(f.read())
    

def send_email(
    to, subject, _from = "portfolio" + settings.BASE_EMAIL_SENDER, html_content = " ",
    cc = [], bcc = [], attachments = []
):

    recipient = "matthewpaulh@hotmail.co.uk"

    app_key = environ["email application key"]

    secret_key = environ["email secret key"]

    email_client = Client(auth = (app_key, secret_key), version = 'v3.1')

    data = {'Messages': []}

    for recipient in to:
            
        data["Messages"].append(
            {
                "From": {
                    "Email": _from,
                    "Name": "Matthew Hill"
                },

                "To": [
                    {
                        "Email": recipient,
                        "Name": "You"
                    }
                ],

                "Cc": [
                    {
                        "Email": contact,
                    } for contact in cc
                ],

                "Bcc": [
                    {
                        "Email": contact,
                    } for contact in bcc
                ],

                "Attachments": [
                    {
                        "ContentType": a["ContentType"],
                        "Filename": a["Filename"],
                        "Base64Content": file_encode(a["Filepath"])
                    } for a in attachments
                ],

                "Subject": subject,
                "TextPart": "",
                "HTMLPart": html_content
            }
        )

    if len(data["Messages"]) > 0:

        result = email_client.send.create(data=data)

        if result.status_code == 200:

            return True

    return False
