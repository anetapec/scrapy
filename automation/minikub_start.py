
import subprocess
import fs 

'''
export CHANGE_MINIKUBE_NONE_USER=true
sudo sysctl fs.protected_regular=0
sudo -E minikube start --driver=none 
'''
name = 'CHANGE_MINIKUBE_NONE_USER'
p = subprocess.Popen(f"export {name}", shell=True)
print(p.communicate())

n = subprocess.Popen(f"sudo sysctl fs.protected_regular=0")
print(n.communicate())

l = subprocess.Popen(f"sudo -E minikube start --driver=none ")
print(l.communicate())

