# KubeVerSys

### Project Description
Simple To-Do-List Application using Kubernetes.
Just a backend consisting of a REST-API written in Python and MariaDB as Database software.
Also using galera as a load balancer to redirect requests to different instances.

### How to install (on Ubuntu)
First connect to the Server via SSH, then run sudo apt update upgrade.
Run sudo apt install git then clone the repo with 
sudo git clone https://github.com/HochschulChaostruppe/KubeVerSys
Change directory into the repo: cd KubeVerSys
Last step run the spin up script with sudo ./ spinup.sh
If it won't run try: sudo chmod 700 spinup.sh