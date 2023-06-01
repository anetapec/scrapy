import subprocess
import os


class Docker:

    def build_docker_image(name_folder, name_image):
        directory = os.getcwd()
        scrapy_directory = os.path.join(directory, name_folder)
        os.chdir(scrapy_directory)
        p = subprocess.Popen(f"docker build -t {name_image} .", shell=True)
        print(p.communicate())
        
    
# docker_tricity = Docker
# docker_tricity.build_docker_image("tricity", "tricity:0.0.3")

docker_dashboards = Docker
docker_dashboards.build_docker_image("dasboards", "scrapy_dash:0.0.0")
