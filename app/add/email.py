from datetime import datetime
from flask_mail import Message
from app.main import mail
import time

def send_email(timestamp, recipient):
    date = datetime.fromtimestamp(timestamp)
    message = {
        "first": f"Your appointment has been set for {date}",
        "second": "Your appointment has started",
        "third": "You have missed your appointment"

    }
    msg = Message("Appointment info", sender="singleodin234@gmail.com",
    recipients = [recipient]

    )
    msg1 = Message("Appointment info", sender="singleodin234@gmail.com",
    recipients = [recipient]

    )

    msg2 = Message("Appointment info", sender="singleodin234@gmail.com",
    recipients = [recipient]

    )

    msg.body = message["first"]
    mail.send(msg)
    msg1.body = message["second"]
    mail.send(msg1)
    msg2.body = message["third"]
    mail.send(msg2)


