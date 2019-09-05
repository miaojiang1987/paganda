import pickle as pk
import os
import torch
import numpy as np
import torch.utils.data as utils
import torch.utils as tutils
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
#my_x=np.array(result)
#tensor_x = torch.stack([torch.Tensor(i) for i in my_x])
#my_dataset = utils.TensorDataset(tensor_x)
#my_dataloader = utils.DataLoader(my_dataset)
#  print(result[0])

def generate_random():
    array=np.random.rand(512,3,20,10)
    additional_array=np.random.rand(512,3,64,64)
    additional_array.fill(0.0)
    for i in range(512):
        for m in range(3):
            for j in range(20):
                for k in range(10):
                    additional_array[i][m][j][k]=array[i][m][j][k]
    tensor= torch.stack([torch.Tensor(i) for i in additional_array])
    result=[]
    for i in range(len(tensor)):
        result.append((tensor[i],0))
#    my_dataset = utils.TensorDataset(tensor)
    print("Successful Generate the dataset")
    return result

def read_from_seed_data(filename):
    array=np.random.rand(32,3,20,10)
    additional_array=np.random.rand(32,3,64,64)
    additional_array.fill(0.0)
    file_open=open(filename,'r')
    feature_lines=[]
    defenders_lines=[]
    attackers_lines=[]
    for i in range(32):
        feature_lines.append(file_open.readline())
    for i in range(32):
        defenders_lines.append(file_open.readline())
    for i in range(32):
        attackers_lines.append(file_open.readline())
    for i in range(32):
        line=feature_lines[i]
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(160):
                array[i][dim][j//8][j%8]=(float)(data[j])
    for i in range(32):
        line=defenders_lines[i]
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(20):
                array[i][dim][j][8]=(float)(data[j])
    for i in range(32):
        line=attackers_lines[i]
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(20):
                array[i][dim][j][9]=(float)(data[j])
    for i in range(32):
        for m in range(3):
            for j in range(20):
                for k in range(10):
                    additional_array[i][m][j][k]=array[i][m][j][k]
    tensor=torch.stack([torch.Tensor(i) for i in additional_array])
    result=[]
    for i in range(len(tensor)):
        result.append((tensor[i],0))
    print("Successful Generate the dataset")
    file_write=open('transformed_array.out','w')
    for image in range(32):
        #for dim in range(3):
        for i in range(20):
            for j in range(10):
                file_write.write((str)(additional_array[image][0][i][j])+' ')
        file_write.write('\n')
    file_write.close()
    return result

def gather_trained_data(read_path,existing_file,size,add_size):
    total_size=size+add_size
    additional_array=np.random.rand(total_size,3,64,64)
    additional_array.fill(0.0)
    file_read=open(existing_file,'r')
    lines=[]
    for i in range(size):
        line=file_read.readline()
        lines.append(line)
    for i in range(size):
        line=lines[i]
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(200):
                if j<160:
                    additional_array[i][dim][j//8][j%8]=(float)(data[j])
                if j>=160 and j<180:
                    additional_array[i][dim][j-160][8]=(float)(data[j])
                if j>=180 and j<200:
                    additional_array[i][dim][j-180][9]=(float)(data[j])
    file_read.close()
    files=os.listdir(read_path)
    file_number=0
    for filename in files:
        file_read=open(read_path+'/'+filename,'r')
        line=file_read.readline()
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for i in range(200):
                if i<160:
                    additional_array[file_number+size][dim][i//8][i%8]=(float)(data[i])
                if i>=160 and i<180:
                    additional_array[file_number+size][dim][i-160][8]=(float)(data[i])
                if i>=180:
                    additional_array[file_number+size][dim][i-180][9]=(float)(data[i])
        file_number+=1
    tensor=torch.stack([torch.Tensor(i) for i in additional_array])
    result=[]
    for i in range(len(tensor)):
        result.append((tensor[i],0))
    print("Successful Generate the dataset")
    file_write=open('transformed_array.out','w')
    for image in range(size+add_size):
        for i in range(20):
            for j in range(10):
                file_write.write((str)(additional_array[image][0][i][j])+' ')
        file_write.write('\n')
    file_write.close()
    return result

def read_from_data_for_k_folder(filename,folder):
    array=np.random.rand(32,3,20,10)
    additional_array=np.random.rand(32,3,64,64)
    additional_array.fill(0.0)
    array_result=[]
    file_open=open(filename,'r')
    '''
    feature_lines=[]
    defenders_lines=[]
    attackers_lines=[]
    for i in range(32):
        feature_lines.append(file_open.readline())
    for i in range(32):
        defenders_lines.append(file_open.readline())
    for i in range(32):
        attackers_lines.append(file_open.readline())
    for i in range(32):
        line=feature_lines[i]
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(160):
                array[i][dim][j//8][j%8]=(float)(data[j])
    for i in range(32):
        line=defenders_lines[i]
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(20):
                array[i][dim][j][8]=(float)(data[j])
    for i in range(32):
        line=attackers_lines[i]
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(20):
                array[i][dim][j][9]=(float)(data[j])
    for i in range(32):
        for m in range(3):
            for j in range(20):
                for k in range(10):
                    additional_array[i][m][j][k]=array[i][m][j][k]
    '''
    for i in range(32):
        line=file_open.readline()
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(200):
                if j<160:
                    array[i][dim][j//8][j%8]=(float)(data[j])
                    
                elif j>=160 and j<180:
                    array[i][dim][j-160][8]=(float)(data[j])
                else:
                    array[i][dim][j-180][9]=(float)(data[j])
    for i in range(32):
        for m in range(3):
            for j in range(20):
                for k in range(10):
                    additional_array[i][m][j][k]=array[i][m][j][k]
    file_open.close()
   
    file_open=open('collection_0.out','w')
    for i in range(32):
        line=''
        for j in range(20):
            for k in range(10):
                line+=(str)(additional_array[i][0][j][k])+' '
        file_open.write(line+'\n')
    file_open.close()

    if folder==1:
        for i in range(24):
            array_result.append(additional_array[i])
        write_folder(array_result,24,1)
    elif folder==2:
        for i in range(8):
            array_result.append(additional_array[i])
        for i in range(16,32):
            array_result.append(additional_array[i])
        write_folder(array_result,24,2)
    elif folder==3:
        for i in range(16):
            array_result.append(additional_array[i])
        for i in range(24,32):
            array_result.append(additional_array[i])
        write_folder(array_result,24,3)
    else:
        for i in range(8,32):
            array_result.append(additional_array[i])
        write_folder(array_result,24,4)
    tensor=torch.stack([torch.Tensor(i) for i in array_result])
   
    result=[]
    for i in range(len(tensor)):
        result.append((tensor[i],0))

    print("Successful Generate the dataset")
    #file_write=open('transformed_array.out','w')
    #for image in range(32):
        #for dim in range(3):
    #    for i in range(20):
    #     for j in range(10):
    #            file_write.write((str)(additional_array[image][0][i][j])+' ')
    #    file_write.write('\n')
    #file_write.close()
    
    return result

def read_from_data_for_k_folder_add_size(path,folder,size,add_size,time):
    array=np.random.rand(size,3,20,10)
    additional_array=np.random.rand(size+add_size,3,64,64)
    additional_array.fill(0.0)
    array_result=[]
    file_open=open('collection_'+(str)(time-1)+'.out','r')
    for i in range(size):
        line=file_open.readline()
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for j in range(200):
                if j<160:
                    array[i][dim][j//8][j%8]=(float)(data[j])
                    
                elif j>=160 and j<180:
                    array[i][dim][j-160][8]=(float)(data[j])
                else:
                    array[i][dim][j-180][9]=(float)(data[j])
    for i in range(size):
        for m in range(3):
            for j in range(20):
                for k in range(10):
                    additional_array[i][m][j][k]=array[i][m][j][k]
    file_open.close()
    files=os.listdir(path)
    file_number=0
    for filename in files:
        file_read=open(path+'/'+filename,'r')
        line=file_read.readline()
        data=line.split('\n')[0].split(' ')
        for dim in range(3):
            for i in range(200):
                if i<160:
                    additional_array[file_number+size][dim][i//8][i%8]=(float)(data[i])
                if i>=160 and i<180:
                    additional_array[file_number+size][dim][i-160][8]=(float)(data[i])
                if i>=180:
                    additional_array[file_number+size][dim][i-180][9]=(float)(data[i])
        file_number+=1
    total_size=size+add_size
    file_write=open('collection_'+(str)(time)+'.out','w')
    for i in range(total_size):
        line=''
        for j in range(20):
            for k in range(10):
                line+=(str)(additional_array[i][0][k][j])+' '
        file_write.write(line+'\n')

    file_write.close()
    if folder==1:
        for i in range(total_size*3//4):
            array_result.append(additional_array[i])
    elif folder==2:
        for i in range(total_size//4):
            array_result.append(additional_array[i])
        for i in range(total_size//2,total_size):
            array_result.append(additional_array[i])
    elif folder==3:
        for i in range(total_size//2):
            array_result.append(additional_array[i])
        for i in range(total_size*3//4,total_size):
            array_result.append(additional_array[i])
    else:
        for i in range(total_size//4,total_size):
            array_result.append(additional_array[i])
    tensor=torch.stack([torch.Tensor(i) for i in array_result])
   
    result=[]
    for i in range(len(tensor)):
        result.append((tensor[i],0))

    print("Successful Generate the dataset")
    #file_write=open('transformed_array.out','w')
    #for image in range(32):
        #for dim in range(3):
    #    for i in range(20):
    #     for j in range(10):
    #            file_write.write((str)(additional_array[image][0][i][j])+' ')
    #    file_write.write('\n')
    #file_write.close()
    
    return result

    _
def write_folder(array,size,folder):
    file_open=open('folder_'+(str)(folder)+'.out','w')
    for i in range(size):
        line=''
        for j in range(20):
            for k in range(10):
                line+=(str)(array[i][0][j][k])+' '
        file_open.write('\n')
    file_open.close()



    

#result=read_from_data_for_k_folder('training.out',1)
#print(len(result))
#print(result[0][0].size())
