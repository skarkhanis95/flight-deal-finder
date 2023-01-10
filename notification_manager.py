import smtplib
MY_EMAIL = "sid624576@gmail.com"
PASSWORD = "lvjqygevlfcuarph"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self,message, to):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            subject = "CHEAP FLIGHT ALERT"
            msg = f"Subject: {subject} \n\n {message}"
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to, msg=msg)
            print("Mail Sent!")