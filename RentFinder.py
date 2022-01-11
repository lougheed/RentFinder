import requests
import smtplib, ssl
from bs4 import BeautifulSoup
import sys
sys.path.insert(0, '/Users/Root/Desktop/Python')
from GmailConfig import*  #all 3 lines used to import password hosted in another file for secure handleing of credentials.
from datetime import date
from email.mime.text import MIMEText

def SendMail(DataOutput):
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    sender_email = SentForm
    receiver_email = TrgetEmail
    TheTime =  date.today()#pulls in the date
    #set up the msg to send
    msg = MIMEText(f'Palces to Rent report for {TheTime}')
    msg['Subject'] = f"""Rents in Cork for {TheTime}
    Here is the data:\n {DataOutput}
    """
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)
        server.sendmail(
            sender_email, receiver_email,msg.as_string())

r = requests.get('https://www.daft.ie/property-for-rent/ireland/houses?location=cork-commuter-towns-cork&location=cork-city').text
soup = BeautifulSoup(r, 'html.parser')
data = soup.find_all("div", class_="Card__Body-x1sjdn-3 dhiEPC")

MyList = []
for datas in data:
    price = datas.find("div", class_="TitleBlock__Price-sc-1avkvav-3 pJtsY").text# get the raw price in text
    address = datas.find("p", class_="TitleBlock__Address-sc-1avkvav-7 knPImU").text#get the adresss text
    both = address + "\n" + price
    MyList.append(both)


separator = ", "# useed for the join() method in python
DataOutput = separator.join(MyList)#Takes the list and makes it look nicer, will use this as a payloud in the email.
SendMail(DataOutput)
print("Done", DataOutput)
