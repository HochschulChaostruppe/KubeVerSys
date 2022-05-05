GITHUB_URI = https://github.com/HochschulChaostruppe/KubeVerSys
#SERVER_IP = 
#echo "Please log in to the server:"
#ssh rn@$SERVER_IP
echo "Installing Kubernetes components..."
sudo snap install micro-k8s
sudo micro-k8s enable dns
sudo mkdir /home/KubeFiles
cd /home/KubeFiles
sudo curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
sudo chmod 700 get_helm.sh
sudo ./get_helm.sh
echo "Cloning Files from Github..."
sudo mkdir Repo
cd Repo
git clone $GITHUB_URI
echo "Installing Cluster components..."
cd helmCharts/mariaDBChart
sudo helm install -f values.yaml mariaDB
cd helmCharts/pythonRESTChart
sudo helm install -f values.yaml pythonREST


#SERVER_IP = 23.88.44.242
#If we also do the cluster on the second server, the script will be here:
#echo "Logging in on second server..."
#ssh rn@$SERVER_IP
