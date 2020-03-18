from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo

from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_COLL = os.getenv("MONGO_COLL")
MONGO_DB = os.getenv("MONGO_DB")

conn =  pymongo.MongoClient(MONGO_URI)

app = Flask(__name__)

@app.route("/")
def index():

    data = conn[MONGO_COLL][MONGO_DB]
    age = request.args.get('type')
    # reminder that arg will return string. so your comparison must be in string as well.
    if  age == "1":
        search = data.find()
        
    elif age == "2":
        search = data.find( { "cost": { "$gt":"100", "$lt": "200" } } )
        
    elif age == "3":
        search = data.find( { "cost": { "$gt":"200", "$lt": "300" } } )
        
    else:
        search = data.find()
    
    return render_template("index.html", search=search)

#"magic code" - - boilerplate
if __name__ == "__main__":
   app.run(host="localhost",
      port=int(8080),
      debug=True)