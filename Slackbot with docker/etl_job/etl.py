import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(".env")
import pymongo
import time
import logging
from sqlalchemy import create_engine,text
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#s  = SentimentIntensityAnalyzer()


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
    classification VARCHAR(500)
);
''')
pg_client_connect.execute(create_table)
pg_client_connect.commit()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))            

for doc in docs:
    #logging.warning(doc)
    title=doc['text'].replace("'"," ")
    completion=client.chat.completions.create(model="gpt-3.5-turbo-0301",
        messages=[
            {"role":"system", "content": f"You can classify postive and negative sentences."},
            {"role":"user", "content": f"""Does this statement sound positive or negative:{title}.Say Negative or Positive. 
                                        Examples of good answer
                                            -"Positive"
                                            -"Negative"
                                                    """}],max_tokens=256)
    score=completion.choices[0].message.content
    # scorex=s.polarity_scores(title)
    # score=scorex['compound']
    insert=text(f"INSERT INTO posts VALUES('{title}','{score}');")
    pg_client_connect.execute(insert)
    pg_client_connect.commit()

pg_client_connect.close()

