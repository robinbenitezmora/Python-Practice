from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def mailstu(li, msg):
    from_id = 'cXXXXXXXX@gmail.com'
    pwd = 'XXXXXXXXXXXX'
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_id, pwd)

    for i in range(0, len(li)):
        to_id = li[i]
        message = MIMEMultipart()
        message.attach(MIMEText(msg, 'plain'))
        content = message.as_string()
        s.sendmail(from_id, to_id, content)
        s.quit
    print('Mail sent successfully')

    def mailstaff(mail_id, msg):
        from_id = 'cXXXXXXXXXXs@gmail.com'
        pwd = 'XXXXXXXX'
        to_id = mail_id
        message = MIMEMultipart()
        message['Subject'] = 'Lack of Attendance report'
        message.attach(MIMEText(msg, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(from_id, pwd)
        content = message.as_string()
        s.sendmail(from_id, to_id, content)
        s.quit
        print('Mail sent successfully')


def main():
    print('Welcome to the Attendance Tracker!')
    print('Please enter the details below: ')
    print('Enter the number of students: ')
    n = int(input())
    print('Enter the number of classes: ')
    m = int(input())
    print('Enter the minimum attendance percentage: ')
    min_att = int(input())
    print('Enter the email IDs of the students: ')
    li = []
    for i in range(0, n):
        li.append(input())
    print('Enter the number of classes attended by each student: ')
    att = []
    for i in range(0, n):
        att.append(int(input()))
    for i in range(0, n):
        if att[i] < (min_att / 100) * m:
            msg = 'Dear student, you have failed to meet the minimum attendance requirement of ' + str(
                min_att) + '%. Please make sure to attend the next class.'
            mailstu(li, msg)
            msg = 'Dear staff, the following student has failed to meet the minimum attendance requirement of ' + str(
                min_att) + '%. Please take necessary action.'
            mailstu('staff_email_id', msg)
        else:
            print('All students have met the minimum attendance requirement. No action required.')
    print('Thanks for using the Attendance Tracker!')
    return


if __name__ == '__main__':
    main() 
        