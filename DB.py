from flask import Flask,render_template
import urllib
import re
# sudo pip install mysql-connector-python-rf
import mysql.connector as mariadb 
app = Flask(__name__)

mariadb_connection = mariadb.connect(user='root', database='Articles')
cursor = mariadb_connection.cursor()
Bages = [("http://www.purplemath.com/modules/sqrcircle.htm"),("http://www.purplemath.com/modules/sqrellps.htm")]

sql = "insert into article(url) VALUES('http://www.purplemath.com/modules/sqrcircle.htm')"
cursor.execute(sql)

print(remaining_rows)
mariadb_connection.commit()
mariadb_connection.close()
   
@app.route('/')
def index():         
 return render_template('home.html')  

# article

# i=0
# while (i < len(Bages)):
#      htmlfile = urllib.urlopen("http://www.purplemath.com/modules/"+Bages[i]+".htm") 
#      htmltext = htmlfile.read()
#      print (htmltext)
#      i += 1





