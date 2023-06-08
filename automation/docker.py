import subprocess
import os
import argparse

parser = argparse.ArgumentParser(description='Building docker images.')
parser.add_argument('-f')

parser.add_argument('-folder', '--name_folder', type=str, help='Enter the name of the folder where the docker image is located')
parser.add_argument('-image', '--name_image', type=str, help='Enter the name of the resulting docker image')
args = parser.parse_args()



def build_docker_image(name_folder, name_image):
    directory = os.getcwd()
    scrapy_directory = os.path.join(directory, name_folder)
    os.chdir(scrapy_directory)
    p = subprocess.Popen(f"docker build -t {name_image} .", shell=True)
    print(p.communicate())

if __name__ == '__main__':
    build_docker_image(args.name_folder, args.name_image)
        
    
# docker_tricity = Docker
# docker_tricity.build_docker_image("tricity", "tricity:0.0.3")

# docker_dashboards = Docker
# docker_dashboards.build_docker_image("dashboards", "scrapy_dash:0.0.0")