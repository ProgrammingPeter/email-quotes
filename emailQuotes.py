# Import unirest to make HTTP requests
import unirest
# Import smtplib for the actual sending function
import smtplib

response = unirest.get("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1")

#If response code is OK, proceed
if response.code == 200:
	try:
		sender = ''
		receivers = [''] #Each receipient

		quote = response.body[0]['content'] #Take quote from response
		quote = quote[3:len(quote)-5] + " - " + response.body[0]['title'] #Shave off HTML paragraph tags and ending new line and reassign it to quote

		message = "\r\n".join(["From: " sender, "To: " receivers, "Subject: Add your subject here!s", "", quote])

		# Credentials (if needed)
		username = ''
		password = ''

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(sender, receivers, message)
		server.quit()
		print "Successfully sent email"
	except Exception, e:
		print "Email was not sent"
		pass