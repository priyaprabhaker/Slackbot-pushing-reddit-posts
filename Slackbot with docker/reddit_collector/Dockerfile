# take the python image
FROM python:3.10

# create a workfolder `app`
WORKDIR /app 

# doesn't matter if COPY or ADD (here!)
COPY requirements.txt /app
#ADD get_reddits.py /app
#ADD config.py /app

# install everything mentioned in the requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "get_reddits.py"]

