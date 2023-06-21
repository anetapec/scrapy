
import subprocess
import fs 
import os

'''
export CHANGE_MINIKUBE_NONE_USER=true
sudo sysctl fs.protected_regular=0
sudo -E minikube start --driver=none --extra-config=kubelet.resolv-conf=/run/systemd/resolve/resolv.conf
'''


name = 'CHANGE_MINIKUBE_NONE_USER'
p = subprocess.Popen(f"export {name}", shell=True)
print(p.communicate())

p = subprocess.Popen(f'["sudo", "sysctl", "fs.protected_regular=0"]')
print(p.communicate())

path = "/run/systemd/resolve/resolv.conf"
os
# p = subprocess.Popen('sudo -E minikube start --driver=none --ext.ra-config=kubelet.resolv-conf=/run/systemd/resolve/resolv.conf')

#print(p.communicate())

# name_n = 'protected_regular=0'
# n = subprocess.Popen(f"sudo sysctl fs.{name_n}")
# print(n.communicate())

l = subprocess.Popen(f'["sudo", "-E minikube start",  "--driver=none", "--extra-config=kubelet.resolv-conf=/run/systemd/resolve/resolv.conf"]')
print(l.communicate())





'''
name = 'CHANGE_MINIKUBE_NONE_USER'
p = subprocess.Popen(f"export {name}", shell=True)
print(p.communicate())

n = subprocess.Popen(f"sudo sysctl fs.protected_regular=0")
print(n.communicate())

l = subprocess.Popen(f"sudo -E minikube start --driver=none ")
print(l.communicate())

'''