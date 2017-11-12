from flask import Flask,render_template
import urllib
import re
# sudo pip install mysql-connector-python-rf
import mysql.connector as mariadb 
app = Flask(__name__)

mariadb_connection = mariadb.connect(user='root', database='Articles')
cursor = mariadb_connection.cursor()




sql = "insert into article VALUES(3,'dghffdhg')"
cursor.execute(sql)
mariadb_connection.commit()
mariadb_connection.close()
   
@app.route('/')
def index():         
 return render_template('home.html')  


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

