FROM python:3.9

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /docker_test

# Set the working directory to /music_service
WORKDIR /docker_test

# Copy the current directory contents into the container at /music_service
ADD . /docker_test/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["bash", "entypoint.sh"]