FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
#RUN pip install Flask
RUN pip install webapp2 webob Werkzeug
 

# Bundle app source
COPY ./main.py /src/main.py

CMD ["python", "/src/main.py"]
