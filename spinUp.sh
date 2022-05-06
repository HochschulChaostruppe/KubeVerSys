GITHUB_URI = https://github.com/HochschulChaostruppe/KubeVerSys
#SERVER_IP = 
#echo "Please log in to the server:"
#ssh rn@$SERVER_IP
echo "Installing Kubernetes components..."
sudo apt install git
sudo snap install microk8s --classic
sudo snap install kubectl --classic
sudo micro-k8s enable dns helm3
sudo mkdir /home/KubeFiles
cd /home/KubeFiles
echo "Setting up Kubernetes..."
sudo mkdir  ~/.kube
cd ~/.kube
sudo microk8s config > config
sudo kubectl proxy --kubeconfig ~/.kube/config --port 8080
echo "Cloning Files from Github..."
sudo mkdir Repo
cd Repo
git clone $GITHUB_URI
echo "Installing Cluster components..."
cd helmCharts/mariaDBChart
sudo microk8s helm3 install -f masterValues.yaml GaleraMaster
sudo microk8s helm3 install -f nodeValues.yaml GaleraNode1
sudo microk8s helm3 install -f nodeValues.yaml GaleraNode2
sudo microk8s helm3 install -f nodeValues.yaml GaleraNode3
cd helmCharts/pythonRESTChart
sudo microk8s helm3 install -f values.yaml pythonREST


#SERVER_IP = 23.88.44.242
#If we also do the cluster on the second server, the script will be here:
#echo "Logging in on second server..."
#ssh rn@$SERVER_IP
