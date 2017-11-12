from flask import Flask,render_template
import urllib
import re

app = Flask(__name__)


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

