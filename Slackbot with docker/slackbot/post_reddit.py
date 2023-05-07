import os
import requests
from sqlalchemy import create_engine, text
import time

time.sleep(90)

webhook_url=os.getenv("WEBHOOK")
query=text('''
SELECT text
FROM posts
WHERE sentiment = 0.0 LIMIT 1;
''')

pg_client = create_engine('postgresql://docker_user:12345@postgresdb:5432/reddit',echo=True)
pg_client_connect=pg_client.connect()
with pg_client_connect as conn:
    text_sql=conn.execute(query).fetchall()
    #post=text_sql.fetchall()
    # print(post)
    data={'text': str(text_sql)}
    print(data)
    requests.post(url=webhook_url, json=data)

pg_client_connect.close()