import pymongo
import time
import logging
from sqlalchemy import create_engine,text
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#import psychopg2-binary

s  = SentimentIntensityAnalyzer()
# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017,directConnection=True, serverSelectionTimeoutMS=60000)

time.sleep(90)  # seconds

# Select the database you want to use withing the MongoDB server
db = client.reddit
docs=db.posts.find()

pg_client = create_engine('postgresql://docker_user:12345@postgresdb:5432/reddit', echo=True)
pg_client_connect = pg_client.connect()
create_table= text('''
    CREATE TABLE IF NOT EXISTS posts(
    text VARCHAR(500),
    sentiment NUMERIC
);
''')
pg_client_connect.execute(create_table)
pg_client_connect.commit()

#docs = list(db.post.find(limit=5))
#print(docs)
#logging.warning(f'found {len(docs)} reddit posts') 
            

for doc in docs:
    #logging.warning(doc)
    title=doc['text'].replace("'"," ")
    scorex=s.polarity_scores(title)
    score=scorex['compound']
    insert=text(f"INSERT INTO posts VALUES('{title}','{score}');")
    pg_client_connect.execute(insert)
    pg_client_connect.commit()

pg_client_connect.close()


# import pymongo
# import time
# from sqlalchemy import create_engine

# # Establish a connection to the MongoDB server
# client = pymongo.MongoClient(host='mongodb', port=27017)

# time.sleep(10)  # seconds

# # Select the database you want to use withing the MongoDB server
# db = client.reddit

# pg = create_engine('postgresql://docker_user:12345@postgresdb:5432/reddit', echo=True)
# pg.execute('''
#     CREATE TABLE IF NOT EXISTS posts (
#     text VARCHAR(500),
#     sentiment NUMERIC
# );
# ''')

# docs = db.posts.find()
# for doc in docs:
#     print(doc)
#     text = doc['text']
#     score = 1.0  # placeholder value
#     query = "INSERT INTO posts VALUES (%s, %s);"
#     pg.execute(query, (text, score))