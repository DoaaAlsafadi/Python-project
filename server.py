from flask import Flask,render_template,request
from wtforms import Form, StringField, BooleanField, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
import urllib
# from flask import Flask
import re
import mysql.connector as mariadb 
app = Flask(__name__)

mariadb_connection = mariadb.connect(user='root', database='Articles')
cursor = mariadb_connection.cursor()

class RegisterForm(Form):
	userName = StringField('userName')
	password = StringField('password')

@app.route('/',methods=['GET','POST','OPTIONS'])
def index():         
 return render_template('home.html')  


@app.route('/login', methods=['GET','POST','OPTIONS'])
def register(): 
	form = RegisterForm(request.form)
	userName = form.userName.data
	password = form.password.data

	cursor.execute("INSERT INTO user (userName,password) VALUES (%s, %s)",(userName, password))
	mariadb_connection.commit()
	mariadb_connection.close()
	return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


# Bages = ["sqrquad","vertx","sqrcircle","sqrellps","drofsign",
# "sqrvertx","drofsign","fcns2","absineq"]

# i=0
# while (i < len(Bages)):
#      htmlfile = urllib.urlopen("http://www.purplemath.com/modules/"+Bages[i]+".htm") 
#      htmltext = htmlfile.read()
#      print (htmltext)
#      i += 1

