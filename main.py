import requests
import smtplib
import secrets
myemail = ("YOUR EMAIL")
password = ("EXTERNAL APP TWO FACTOR AUTHENTICATION PASSWORD")
to = ("WHOS BEING SENT EMAIL")
count = 0
while count < 5 :
 with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
     
     smtp.ehlo()
     smtp.starttls()
     smtp.ehlo()
 
     smtp.login(myemail, password)
 
     subject = ''
     body = '(r.text)'
     r = requests.get('https://icanhazdadjoke.com', headers={"Accept":"text/plain"})
     Joke = r.text
     msg = f'subject: {Joke}\n\n{subject}'
 
     smtp.sendmail(myemail, to, msg)
     print ("Email sent successfully!")
     print(Joke)
     smtp.quit
 

