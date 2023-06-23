import subprocess
import os

directory = os.getcwd() # get current directory of the repository
charts_directory = os.path.join(directory, "k8s/charts") # create a path to tricity folder where where the chart scraper is to be created
os.chdir(charts_directory) # change directory to folder where the chart scraper is to be created
scraper_chart_name = "scraper"
release_name = "scraper"
namespace_name = "scraper"

p = subprocess.Popen(f"helm upgrade {release_name} {scraper_chart_name} -n {namespace_name} --install --create-namespace -f ./{scraper_chart_name}/values.yaml -f ./{scraper_chart_name}/values/common-values.yaml", shell=True)
print(p.communicate())

