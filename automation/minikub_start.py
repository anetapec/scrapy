
import subprocess

result1 = subprocess.Popen([f"export CHANGE_MINIKUBE_NONE_USER=true" ], shell=True)
print(result1.communicate())

result2 = subprocess.Popen([f"sudo sysctl fs.protected_regular=0" ], shell=True)
print(result2.communicate())

result2 = subprocess.Popen([f"sudo -E minikube start --driver=none --extra-config=kubelet.resolv-conf=/run/systemd/resolve/resolv.conf"], shell=True)
print(result2.communicate())

