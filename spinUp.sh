#First connect to the Server via SSH, 
#run sudo apt update upgrade, 
#run sudo apt install git
#cd /home
#then clone the repo with sudo git clone https://github.com/HochschulChaostruppe/KubeVerSys
#last: cd KubeVerSys
#run the script with sudo ./ spinup.sh
#if it won't run try: sudo chmod 700 spinup.sh

echo "Installing Kubernetes components..."
sudo apt install snapd
sudo snap install microk8s --classic
sudo snap install kubectl --classic
echo "Setting up Kubernetes..."
sudo micro-k8s enable dns dashboard helm3
#sudo mkdir  ~/.kube
#cd ~/.kube
#sudo microk8s config > config
#sudo kubectl proxy --kubeconfig ~/.kube/config --port 8080
echo "Installing Cluster components..."
cd /home/KubeVerSys/helmCharts/mariaDBChart/mariadb-galera
sudo microk8s helm3 install -f masterValues.yaml galera-master
sudo microk8s helm3 install -f node1Values.yaml galera-node1
sudo microk8s helm3 install -f node2Values.yaml galera-node2
sudo microk8s helm3 install -f node3Values.yaml galera-node3
cd /home/KubeVerSys/helmCharts/pythonRESTChart/python-api-mariadb
sudo microk8s helm3 install -f values.yaml python-rest
cd /home/KubeVerSys/helmCharts/externalProxyChart/reverse-proxy
sudo microk8s helm3 install -f values.yaml reverse-proxy

