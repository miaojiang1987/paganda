import pickle as pk
import os

#data = pk.load(open( "samples_211.pickle", "rb" ))

#print(type(data))
#print((data[0]))

def load_data(data_path,data):
    data_files=os.listdir(data_path)
    for i in range(len(data_files)):
        data_temp=pk.load(open(data_path+'/'+data_files[i],'rb'))
        for temp in data_temp:
            data.append(temp)

data=[]
load_data('data',data)
print(len(data))