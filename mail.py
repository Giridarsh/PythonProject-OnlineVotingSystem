#import RPi.GPIO as GPIO
import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_mail(gmail_user ,gmail_pwd,TO,message="python test"):
        FROM= gmail_user
        time.sleep(1)
        msg = MIMEMultipart()
        time.sleep(1)
        msg['Subject'] =message
        time.sleep(1)
        
        try:
                
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                print ("Enter the server")
                server.ehlo()
                print ("Acknowledgement Completed")
                server.starttls()
                print ("Security Layer")
                server.login(gmail_user, gmail_pwd)
                print ("Login Successfully")
                server.sendmail(FROM, TO, msg.as_string())
                print ("Message sending")
                server.close()
                print ('Successfully sent the mail')
        except:
                print ("Sorry... Failed to send mail")
                

##if __name__=="__main__":
##        send_mail("  @gmail.com","*********","  @gmail.com","Test","img.jpg")
