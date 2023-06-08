# Slackbot-pushing-reddit-posts

This project is focused on building a data pipeline that collects reddits using Docker, and stores them in a database. It also analyzes the sentiment of reddits, and stores the annotated text in a second database. Finally, it uses the Reddit API to collect notes and store them in MongoDB. It then creates an ETL job to transport data from MongoDB to PostgreSQL. The project also includes sentiment analysis on the text, a Slack bot that publishes selected reddits, and NLP using psychopg2, vadersentimentanalyzer, pymongo, and sqlalchemy.

 
## Installation

To install this project, follow these steps:
1. Clone the repository to your local machine.
2. Install Docker and PostgreSQL.
3. Go to the cloned folder and run `docker-compose up -d` to start the Slack bot.
```     
    cd Slackbot-with-docker
    docker-compose up -d
```
  
 ## Usage

The steps of this project is to :
1. Collect reddits using the Docker container and store them in the database.
2. Analyze the sentiment of reddits and store the annotated text in the second database.
3. Use the Reddit API to collect notes and store them in MongoDB.
4. Run the ETL job to transport data from MongoDB to PostgreSQL.
5. Use sentiment analysis on the text to gain insights.
6. Use the Slack bot to publish selected reddits.

To use the Slack bot, you'll need to follow these steps:
1. Create a new bot in your Slack by creating a new app and activate the *Incoming webhook*.
2. Copy the Webhook URL and set environment variables in your .env file.
3. Additionally, .env files should be added with reddit API client-ID and secret along with reddit username and password. 
    
## Contributing

If you'd like to contribute to this project, please follow these steps:
- Fork the repository.
- Create a new branch with your changes.
- Submit a pull request.

## License

This project is licensed under the GNU License. See the LICENSE file for more information.
