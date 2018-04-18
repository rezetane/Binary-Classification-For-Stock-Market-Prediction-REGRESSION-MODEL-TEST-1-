import numpy as np 


# FUNCTION TO CREATE 1D DATA INTO TIME SERIES DATASET
def new_dataset(dataset, step_size):
	data_X, data_Y = [], []
	for i in range(len(dataset)-step_size-1):
		a = dataset[i:(i+step_size), 0]
		data_X.append(a)
		data_Y.append(dataset[i + step_size, 0])
	return np.array(data_X), np.array(data_Y)
# THIS FUNCTION CAN BE USED TO CREATE A TIME SERIES DATASET FROM ANY 1D ARRAY

def classify(close_val,open_val):
    classes=[]
    for i in range(len(close_val)-1):
         value = 100*(close_val[i+1] - open_val[i+1])/open_val[i+1] 
         if value > 0.3 :
              classes.append(1)
         else :
              classes.append(0)
                                                                        
    return np.array(classes)                	

def accuracy(True_classes,Predicted_classes):
    acc_val=[]
    for i in range(len(Predicted_classes)-1):
        if Predicted_classes[i] == True_classes[i]:
            acc_val.append(1)
        else :    
            acc_val.append(0)
    acc_percent = 100 * (np.sum(acc_val))/len(acc_val)
    return acc_percent        
        
