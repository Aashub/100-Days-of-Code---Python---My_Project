# Day 32 - Automated Birthday Wisher Project 

## Project Overview

This Project is an Automated Birthday Email Sender project where I automated the process of sending personalized birthday wishes using Python. The idea is simple we store birthday details in a CSV file, check if today's date and month matches someone’s birthday date and month and if it does than it generate a personalized birthday message from a letter template, and automatically send the email using SMTP.
To build this project, I revised about how to work with CSV files and store their specific details in variables, learned about Smtplib and datetime module and how to use them. All these concepts together helped me to build this project.

---

## What I Have Learned

* **SMTP module**: I learned how to use the smtplib module to send emails. By creating a secure SMTP connection using starttls(), logging in with email credentials, and using sendmail(), I was able to send automated birthday wishes directly to the receiver’s inbox.

* **datetime module**: Using the datetime module, I learned how to get the current day and month and also learned about other things of datetime module. This helped me compare today’s date and month with the birthday date and month stored in the CSV file to decide when the email should be sent.


## How It Works 

* **Reading birthday details**: The program first reads the birthdays.csv file using pandas. From this file, it filters out the required birthday person’s details such as name, birth day, birth month, and email address and stores them in separate variables.

* **Checking birthday date**: Using the datetime module, the program gets the current day and month. It then compares these values with the birthday date and time variables which we have got from CSV file to check whether today is the person’s birthday.

* **Creating a personalized birthday letter**: If the birthday matches today’s date, a random letter template is selected from the letter_templates folder. The program reads the template file and replaces the [NAME] placeholder with the actual birthday person’s name using the replace() function.

* **`send_mail()`**: The send_mail() function creates a secure SMTP connection with Gmail’s server. After logging in, it sends the personalized birthday message to the receiver’s email address with a subject line “Happy Birthday!”. Once the email is sent, the connection is closed automatically using the with statement.

