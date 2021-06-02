#INITIAL SET UP CODE 
# Python code to illustrate Sending mail from  
import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587)  # creates SMTP session 
s.starttls()  # start TLS for security 
username = "EducationRUsPython@gmail.com" #CHANGE THIS WITH YOUR OWN EMAIL
password = "sophiabecky"  #CHANGE THIS WITH YOUR OWN PASSWORD
s.login(username, password)  # Authentication 

#Task 1: Prompt the user for an email address to send an incoming email to. Save the value into a variable.
#Task 2: Determine the index of where "@" is located in the String.
#Hint: use .find()
#Task 3: Save the part of the string before the @ into a variable
#Task 4: Save the part of the string after the @ into a variable
#Task 5 : Determine the number of characters of the string, save the value into a variable.
#Task 6 : Calculate the index of where "@" is divided by the number of total characters in the email address String.
#Task 7 : Calculate the remainder of the number of total characters by the index of @
#Task 8 : Replace the List-typed variable 
#LIST_OF_EMAIL_ADDRESSS_TO_SEND_TO 
#with the value of the email address
LIST_OF_EMAIL_ADDRESSS_TO_SEND_TO = [None]
#Task 9 : Replace the List-typed variable 
#Task 10 : Demonstrate you succesfully did Task 1-9 by displaying information relevant to each task
#Hint : Create one string for each Task 1-9 and use .join()
#You are expected to change the String-typed variable below
message_to_send = ""

#SENDING THE EMAIL
SOURCE_EMAIL = "EducationRUsPython@gmail.com"
s.sendmail(SOURCE_EMAIL, LIST_OF_EMAIL_ADDRESSS_TO_SEND_TO, message_to_send) 
s.quit() # terminating the session 