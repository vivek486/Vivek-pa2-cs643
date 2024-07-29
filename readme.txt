
EA2

Create and Select the instance type (e.g., t2.medium).

Install Java 

	sudo yum install -y wget
	wget https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.rpm

	sudo rpm -ivh amazon-corretto-11-x64-linux-jdk.rpm


Check Python3 Installed

python3  > check python installed


Install and Download Docker 

	sudo yum install -y yum-utils device-mapper-persistent-data lvm2

	sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

	sudo nano /etc/yum.repos.d/docker-ce.repo

Update the Docker file and Save it.

	[docker-ce-stable]
	name=Docker CE Stable - $basearch
	baseurl=https://download.docker.com/linux/centos/7/$basearch/stable
	enabled=1
	gpgcheck=1
	gpgkey=https://download.docker.com/linux/centos/gpg


Enter and Save file 


Install Docker container

	sudo yum install -y docker-ce docker-ce-cli containerd.io

	sudo systemctl start docker

Download and Install Apache Spark

	wget https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz


	tar xvf spark-3.1.2-bin-hadoop3.2.tgz

	sudo mv spark-3.1.2-bin-hadoop3.2 /opt/spark

	export SPARK_HOME=/opt/spark
	export PATH=$SPARK_HOME/bin:$PATH
	
	source ~/.bashrc

Install pip

	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python3 get-pip.py

	pip --version

Install pyspark

	pip install pyspark


Install Apache Spark:

	wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
	tar xvf spark-3.1.2-bin-hadoop3.2.tgz
	sudo mv spark-3.1.2-bin-hadoop3.2 /opt/spark

	echo "export SPARK_HOME=/opt/spark" >> ~/.bashrc
	echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.bashrc
	source ~/.bashrc


Set Java Home to Environment file.

export JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto
export PATH=$JAVA_HOME/bin:$PATH

/usr/lib/jvm/java-11-amazon-corretto/bin/java


pip install pyspark==3.1.2   > It should be same version as spark-submit --version


