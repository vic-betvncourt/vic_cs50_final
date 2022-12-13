from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/results")
def results():
    if request.method == "GET":
        #setting our id from petfinder api
        client_id = "QLq2QnPENYRVHijAhEnApTuEkpbdZaWvQtKjxWq7wSiorkJ4gx"

        #set secret from petfinder api
        client_pass = "tsHhqdQRWLW90dSwlkJqS5CAQSlWZddXvzgfQLQE"
        header = {"grant_type":"client_credentials"}
        api_url = "https://api.petfinder.com/v2/oauth2/token"
        api_request_url = "https://api.petfinder.com/v2/animals"

        # returns token from post request of petfinder api
        token = requests.post(api_url,data=header,auth=(client_id,client_pass))
        
        # converting our token to json to access key:values
        tjson = token.json()

        # holds the type of token
        t_type = tjson['token_type']

        # holds the access token
        t_access = tjson['access_token']

        #print(t_type, t_access)

        animal_type = request.args.get("animal_type")
        if not animal_type:
            return render_template("failure.html")
        # parameters to pass in our url get request
        params = {'type': animal_type, 'location':'70065', 'distance':'50'}

        print("ANIMAL_TYPE_RRRRRRREEEEAAAADDD", animal_type)
        animal_req = requests.get(api_request_url, params=params, headers={"Authorization": t_type + " " + t_access})
        
        #requests.get(url, params=None, headers=None, cookies=None, auth=None, timeout=None)
        
        animalsjson = animal_req.json()

        print(animalsjson['animals'][0]['photos'])
        return render_template("results.html")
    return render_template("index.html")