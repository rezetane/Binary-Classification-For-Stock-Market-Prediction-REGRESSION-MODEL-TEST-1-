
import numpy as np 
import pandas as pd 

def importing(filename):
    # IMPORTING DATASET 
   dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
   df = pd.read_csv(filename, parse_dates=['Date'], date_parser=dateparse)
   #Use All features, even those with almost same information 
   #x = df[['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39','p40']]
   #cut those who are opposite to some features
   x = df[['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p14','p16','p18','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39','p40']]

   x=x[5:len(x)-1]
   y=df[['CLASS']]
   y=y[5:len(y)-1]
   y=np.ravel(y)

   return x,y

def windowing(x,y,window_size):
   x=np.asarray(x)
   data_X, data_Y = [], []
   for i in range(len(x)-window_size-1):
		  a = x[i:(i+window_size),:]
		  data_X.append(a)
		  data_Y.append(y[i + window_size])
   return np.array(data_X), np.array(data_Y) 

def split_x_y(x,y,split_ratio):
      #Split Training and Testing
   train_size = int(len(x) * split_ratio)
   test_size = len(x) - train_size
   train_x , train_y  = x[0:train_size] ,y[:train_size] 
   test_x , test_y  = x[train_size:len(x)] ,y[train_size:len(y)]
   
   return train_x,train_y,test_x ,test_y   