import pickle as pk
import os

#data = pk.load(open( "samples_211.pickle", "rb" ))

#print(type(data))
#print((data[0]))


def load_data(data_path):
    data_files=os.listdir(data_path)
    features=[]
    defender=[]
    attacker=[]
    for i in range(len(data_files)):
        data_temp=pk.load(open(data_path+'/'+data_files[i],'rb'))
        for temp in data_temp:
            features.append(temp[0])
            defender.append(temp[1])
            attacker.append(temp[2])
	
    return features,defender,attacker

#features,defender, attacker=load_data('data')
#print(features[0])
#print(defender[0])
#print(attacker[0])

'''
def unbox(data):
    data_detail=[]
    for i in range(len(data)):
        for k in range(len(data[i])):
            data_detail.append(data[i][k])
    return data_detail

data_detail=unbox(data)
#for i in range(20):
print((data_detail[0]))
'''