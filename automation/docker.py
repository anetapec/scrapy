import subprocess
import os

directory = os.getcwd() # get current directory of the repository
scrapy_directory = os.path.join(directory, "tricity") # create a path to tricity folder where Dockerfile is
os.chdir(scrapy_directory) # change directory to folder where Dockerfile is
docker_image_name = "tricity:0.0.0"
p = subprocess.Popen(f"docker build -t {docker_image_name} .", shell=True)

print(p.communicate())

