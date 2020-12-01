# pip install flask
from flask import Flask #to build website

# variable to hold flask object
app= Flask(__name__)
@app.route('/') # if you put'/about/' in browser you must do localhost:5000/about/ not just local host5000
def home():
    return "Website content goes here!"

if __name__=="__main__":
    app.run(debug=True)

# put localhost:5000 in browser
