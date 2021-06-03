#INITIAL SET UP CODE 
# Python code to illustrate Sending mail from  
import smtplib 
s = smtplib.SMTP('smtp.gmail.com', 587)  # creates SMTP session 
s.starttls()  # start TLS for security 
username = "EducationRUsPython@gmail.com" #CHANGE THIS WITH YOUR OWN NEWLY-CREATED EMAIL
password = "sophiabecky"  #CHANGE THIS WITH YOUR OWN PASSWORD
s.login(username, password)  # Logins in to gmail 

#Task 1: Prompt the user for an email address to send an incoming email to. Save the value into a variable.


#Task 2: Prompt the user for the index of where "@" is located in the previous email address. 

#Task 3: Determine the index of where "@" is located in the String in Task 1.
#Hint: use .find()

#Task 4: Verify the two indexes in Task 2 and Task 3 are the same.

#Task 5: Save the part of the string from Task 1 before the @ into a variable

#Task 6: Save the part of the string from Task 1 after the @ into a variable

#Task 7 : Determine the number of characters of the string from Task 1 , save the value into a variable.

#Task 8 : Calculate the index of where "@" from Task 3 is divided by the number of total characters from Task 7.

#Task 9 : Calculate the remainder of the number of total characters divided by the index of @

#Task 10 : Replace the None within the List-typed variable 
#LIST_OF_EMAIL_ADDRESSS_TO_SEND_TO  
#with the value of the email address from Task 1 
LIST_OF_EMAIL_ADDRESSS_TO_SEND_TO = [None]
#do not create a new list!


#Task Final : Demonstrate you succesfully did previous tasks by displaying information relevant to each task. Place all of it in the variable below.
#Hint : Create one String-typed variable for each task and use .join()
#Hint #2: create a new list that stores all ten variables from before 
#You are expected to change the String-typed variable below
message_to_send = "HELLO THERE!"


#SENDING THE EMAIL
SOURCE_EMAIL = "EducationRUsPython@gmail.com"  
s.sendmail(SOURCE_EMAIL,LIST_OF_EMAIL_ADDRESSS_TO_SEND_TO, message_to_send) 
s.quit() # terminating the session 