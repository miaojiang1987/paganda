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
#for i in range(20):
#    print((data[i]))

def unbox(data):
    data_detail=[]
    for i in range(len(data)):
        for k in range(len(data[i])):
            data_detail.append(data[i][k])
    return data_detail

data_detail=unbox(data)
#for i in range(20):
print((data_detail[0]))