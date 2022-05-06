# KubeVerSys

### Project Description
Simple To-Do-List Application using Kubernetes.
Just a backend consisting of a REST-API written in Python and MariaDB as Database software.
Cluster only runs on one server for now.
Also using galera to maintain data on multiple db instances.

### How to install (on Ubuntu)
First connect to the Server via SSH, then run sudo apt update && apt upgrade.
Run sudo apt install git then clone the repo with 
sudo git clone https://github.com/HochschulChaostruppe/KubeVerSys
Change directory into the repo: cd KubeVerSys
Last step run the spin up script with sudo ./ spinup.sh
If it won't run try: sudo chmod 700 spinup.sh

### Usage
Connect to the server ip you've installed the cluster on, on either port 80 or port 443 (TLS doesn't work because of missing certificate). You can send the requests specified in the REST-README.md file to the adress on port 80.