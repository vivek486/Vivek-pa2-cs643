# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR C:\Users\mptec\Downloads\vockey\vr33@njit.edu

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 80 available to the world outside this container
#EXPOSE 80

# Install Java (OpenJDK)
#RUN apt-get update && apt-get install -y openjdk-11-jdk &&  apt-get clean;

# Set JAVA_HOME environment variable
ENV JAVA_HOME C:\Program Files\Java\jdk1.8.0_321\bin

#Install pyspark
RUN	pip install pyspark


RUN pip install numpy


# Install distutils
RUN apt-get update && apt-get install -y python3-distutils

# Run app.py when the container launches
CMD ["python3", "train.py"]

