import pickle as pk
import os
import torch
import numpy as np
import torch.utils.data as utils

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
	
features,defenders, attackers=load_data('data')
result=merge(features,defenders,attackers)
my_x=np.array(result)
tensor_x = torch.stack([torch.Tensor(i) for i in my_x])
my_dataset = utils.TensorDataset(tensor_x)
my_dataloader = utils.DataLoader(my_dataset)
#  print(result[0])

def generate_random():
    array=np.random.rand(5000,20,10)
    tensor= torch.stack([torch.Tensor(i) for i in array])
    my_dataset = utils.TensorDataset(tensor)
    print("Successful Generate the dataset")
    return my_dataset	

generate_random()
