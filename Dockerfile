# Use an official Python runtime as a parent image
FROM python:3.10

# Install necessary dependencies
RUN apt-get update \
    && apt install git ffmpeg python3 python3-pip -y

# Set the working directory in the container
WORKDIR /musicfa

# Copy the requirements file and install dependencies
COPY requirements.txt /musicfa/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /musicfa

# Expose the port the app runs on
EXPOSE 8080

# Specify the default command to run your application
CMD ["python3", "main.py"]
