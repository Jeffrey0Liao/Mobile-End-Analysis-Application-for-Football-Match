This folder contains all resources for classification net.
---------------------------------------------------------

* dependencies
-PIL
-torch
-torchvision
-matplotlib

* Hierarchy
	/dataset/test_data/0
		             /1
		             /2
	                             /3
	             /train_data/0
		              /1
		              /2
		              /3
	/LeNet5.py (network architecture)
	/net.pkl (network model file)
	/train.py (training script)

* Dataset
	train_data(3200): noball(800, denoted as 0)
		            passing(800, denoted as 1)
		            shooting(800, denoted as 2)
		            dribbling(800, denoted as 3)
	test_data(800): noball(200, denoted as 0)
		        passing(200, denoted as 1)
		        shooting(200, denoted as 2)
		        dribbling(200, denoted as 3)

* Please run train.py to update net.pkl for a new network model.