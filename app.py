from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
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

    print(t_type, t_access)

    # parameters to pass in our url get request
    params = {'type': 'dog'}

    animal_req = requests.get(api_request_url, params=params, headers={"Authorization": t_type + " " + t_access})
    #requests.get(url, params=None, headers=None, cookies=None, auth=None, timeout=None)
    print(animal_req.json())
    return render_template("index.html")