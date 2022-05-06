#First connect to the Server via SSH, 
#run sudo apt update upgrade, 
#run sudo apt install git
#cd /home
#then clone the repo with sudo git clone https://github.com/HochschulChaostruppe/KubeVerSys
#last: cd KubeVerSys
#run the script with sudo ./ spinup.sh
#if it won't run try: sudo chmod 700 spinup.sh
echo "Configuring Firewall..."
sudo apt install ufw -y
sudo ufw allow 22   #ssh
sudo ufw allow 80   #http-port reverse-proxy
sudo ufw allow 443  #https-port reverse-proxy
sudo ufw enable
echo "Installing Kubernetes components..."
sudo apt install snapd -y
sudo snap install microk8s --classic -y
sudo snap install kubectl --classic -y  #Optional for setup, but practical for maintaining the cluster
echo "Setting up Kubernetes..."
sudo micro-k8s enable dns dashboard helm3
echo "Installing Cluster components..."
cd /home/KubeVerSys/helmCharts/mariaDBChart/mariadb-galera
sudo microk8s helm3 install -f masterValues.yaml galera-master ./
sudo microk8s helm3 install -f node1Values.yaml galera-node1 ./
sudo microk8s helm3 install -f node2Values.yaml galera-node2 ./
sudo microk8s helm3 install -f node3Values.yaml galera-node3 ./
cd /home/KubeVerSys/helmCharts/restAPIChart/python-api-mariadb
sudo microk8s helm3 install -f values.yaml python-rest ./
cd /home/KubeVerSys/helmCharts/externalProxyChart/reverse-proxy
sudo microk8s helm3 install -f values.yaml reverse-proxy ./

