# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /home/ec2-user

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "train.py"]