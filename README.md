# MLintegrationAWS
Integration of Machine Learning Model with AWS, FLASK

**aws-ml.py**  
2 Variable - Value can be changed as per requirement.   
pkl_file = 'iris-trained-model.pkl'  
custom_port = "5000"  

Execute on Web server:python aws-pl.py  

**request.py**  
3 Variable - Value can be changed as per requirement.  
ip_address = "<IP Address of Web Server>"  
port = "5000"  
data = [[5.1, 3.5, 1.5, 0.3]]  
data should have same number of feature as the original dataset  
Execute from you server:python aws-pl.py

**AWS Security Group:**  
Open TCP Custom port 5000 for all IP like in Image.  

