from flask import Flask, render_template, request, session
import requests
import json

app = Flask(__name__)

def zipcode():
    headers = {"apikey": "b643b970-7f47-11ed-9ea3-5b00d8d122d4"}

    params = (
        ("codes", request.args.get("zip")),
        ("country", "US"),
    )

    zip_response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params)
    zipjson = zip_response.json()
    zip_list = zipjson['results']
    if not zip_list:
        return 1
    return zip_list[request.args.get('zip')][0]

@app.route("/")
def index():


    #setting our id from petfinder api
    client_id = "QLq2QnPENYRVHijAhEnApTuEkpbdZaWvQtKjxWq7wSiorkJ4gx"

    #set secret from petfinder api
    client_pass = "tsHhqdQRWLW90dSwlkJqS5CAQSlWZddXvzgfQLQE"
    header = {"grant_type":"client_credentials"}
    api_url = "https://api.petfinder.com/v2/oauth2/token"

    # returns token from post request of petfinder api
    token = requests.post(api_url,data=header,auth=(client_id,client_pass))
        
    # converting our token to json to access key:values
    tjson = token.json()

    # holds the type of token
    t_type = tjson['token_type']

    # holds the access token
    t_access = tjson['access_token']
    animal_type_req = requests.get('https://api.petfinder.com/v2/types', headers={"Authorization": t_type + " " + t_access})
    animal_type = animal_type_req.json()
    animal_type_name = animal_type['types']
    return render_template("index.html", animal_types=animal_type_name)

@app.route("/results")
def results():
    if request.method == "GET":

        zip_result = zipcode()
        if zip_result == 1:
            error = "Incorrect zip code"
            return render_template("failure.html", error=error)
        print(zip_result)

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
            error = "no animal selected"
            return render_template("failure.html", error=error)
        
        zip_code = request.args.get("zip")

        # get ages available from api
        animal_age = request.args.getlist("animal_age")

        child = request.args.get("children")
        print(child)
        dogs = request.args.get("dogs")
        print(dogs)
        cats = request.args.get("cats")
        print(cats)
        #declaring variable to use as a string to pass multiple parameters to api
        animal_param_age = ""
        for age in animal_age:
            if animal_param_age == "":
                animal_param_age = age
            else:            
                animal_param_age += "," + age

        # parameters to pass in our url get request
        params = {'type': animal_type, 'location': zip_code, 'distance':'50', 'age': animal_param_age, 'good_with_children': child, 'good_with_dogs': dogs, 'good_with_cats' : cats}

        animal_req = requests.get(api_request_url, params=params, headers={"Authorization": t_type + " " + t_access})
        #requests.get(url, params=None, headers=None, cookies=None, auth=None, timeout=None)
        
        # assigning json returned from api request
        animalsjson = animal_req.json()
        animalsdict = animalsjson['animals']

        # variable to hold image for those animals without photos
        noimg = [{"medium":"static/unavailable-image.jpg"}]

        # parsing through images to see if any are missing and assigning our missing image photo
        for x in range(len(animalsdict)):
            if not animalsdict[x]['photos']:
                animalsdict[x]['photos'] = noimg
        print(animalsdict)
        # rendering and passing results from the api request 
        return render_template("results.html", animalsdict=animalsdict)