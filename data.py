import pickle as pk
import os

#data = pk.load(open( "samples_211.pickle", "rb" ))

#print(type(data))
#print((data[0]))


def load_data(data_path):
    data_files=os.listdir(data_path)
    features=[]
    defenders=[]
    attackers=[]
    for i in range(len(data_files)):
        data_temp=pk.load(open(data_path+'/'+data_files[i],'rb'))
        for temp in data_temp:
            features.append(temp[0])
            defenders.append(temp[1])
            attackers.append(temp[2])
	
    return features,defenders,attackers

	
def merge(features,defenders,attackers):
    result=[]
    for i in range(len(features)):
        feature=features[i]
        defender=defenders[i]
        attacker=attackers[i]
        for j in range(len(defender)):
            feature[j].append(defender[j])
            feature[j].append(attacker[j])
        result.append(feature)
    return result
	
#features,defenders, attackers=load_data('data')
#result=merge(features,defenders,attackers)
#  print(result[0])

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