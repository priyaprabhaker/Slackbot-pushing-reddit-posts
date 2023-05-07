"""
This script gets reddits titles from the reddit api 
and serve in the first step of the dockerized pipeline.
TODO
- add Mongodb connection with pymongo and insert reddits into Mongodb 
"""
## I have forgot install mongodb and that solved the error after installing

import requests
from requests.auth import HTTPBasicAuth
import sys
import json
from  pprint import pprint

import time
from datetime import datetime
import logging
import random
import pymongo
from pymongo import MongoClient
import os
#from pymongo import MongoClient
print(os.getenv("CLIENT_ID"))
sys.stdout.reconfigure(encoding='utf-8') # Useful for windows user
#client=pymongo.MongoClient("mongodb://localhost:27017")
client=MongoClient(host="mongodb", port=27017, directConnection=True, serverSelectionTimeoutMS=60000)
db=client.reddit

## PREPARE AUTHENTIFICATION INFORMATION ##
## FOR REQUESTING A TEMPORARY ACCESS TOKEN ##

basic_auth = HTTPBasicAuth(
    username=os.getenv("CLIENT_ID"), # tokens.get("key")
    password=os.getenv("SECRET")
)



print(basic_auth)

GRANT_INFORMATION = dict(
    grant_type="password",
    username=os.getenv("USERNAME"), # REDDIT USERNAME
    password=os.getenv("PASSWORD") # REDDIT PASSWORD
)

headers = {
    'User-Agent': "Mozilla"
}

### POST REQUEST FOR ACCESS TOKEN

POST_URL = "https://www.reddit.com/api/v1/access_token"

access_post_response  = requests.post(
    url=POST_URL,
    headers=headers,
    data=GRANT_INFORMATION,
    auth=basic_auth
).json()

# Print the Bearer Token sent by the API
print(access_post_response)

# ### ADDING TO HEADERS THE Authorization KEY

headers['Authorization'] = access_post_response['token_type'] + ' ' + access_post_response['access_token']

#print(headers)

# ## Send a get request to download most popular (hot) Python subreddits title using the new headers.

topic = 'python'
URL = f"https://oauth.reddit.com/r/{topic}/hot"

response = requests.get(
    url=URL,
    headers=headers
).json()

# pprint(response)

print ('hi')
full_response = response['data']['children']
pprint(full_response)
# # Go through the full response and define a mongo_input dict
# # filled with reddit title and corresponding id

# for post in full_response:
#     _id = post['data']['id']
#     title = post['data']['title']
#     mongo_input = {"_id":_id, 'text': title}

# print(mongo_input)
 # hostname = servicename for docker-compose pipeline

# # Create/use a database



# # # Define the collection
collection = db.posts

# # # Go through the full response and define a mongo_input dict
# # # filled with reddit title and corresponding id
print ('hi')

for post in full_response:
    print ('hi')
    _id = post['data']['id']
    title = post['data']['title']
    mongo_input = {"_id":_id,'text':title}
    #if _id not in collection.distinct("_id"):
    collection.insert_one(mongo_input)

#print(db.posts.insert_one(dict(post)))


