import subprocess
import os

directory = os.getcwd() # get current directory of the repository
charts_directory = os.path.join(directory, "k8s/charts") # create a path to tricity folder where Dockerfile is
os.chdir(charts_directory) # change directory to folder where Dockerfile is
helm_chart_name = "scrapy_dash"
release_name = "scrapy_dash"
namespace_name = "scrapy_dash"

p = subprocess.Popen(f"helm upgrade {release_name} {helm_chart_name} -n {namespace_name} --install --create-namespace -f ./{helm_chart_name}/values.yaml -f ./{helm_chart_name}/values/common-values.yaml", shell=True)
print(p.communicate())

