import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from tqdm import tqdm      # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
import pandas as pd

'''
This create_train_data function create and save two numpy array.

imagelabels : An image lable is a array of length 120 with 119 '0' and one '1' at the index of the breed label. This imagelabels
              numpy array contains such arrays for each training image.

dogbreedimages : All the training images are converted in to numpy arrays

As these images are with different sizes,here all are resized into 50*50

'''


IMAGE_DIR= 'D:/SEM3 TRONIC ACA/Machine learning/Dog/train'


def create_train_data():
    training_data=[]
    fields=['id','breed','breedlabel']
    df= pd.read_csv('D:/SEM3 TRONIC ACA/Machine learning/Dog/labels.csv', skipinitialspace=True, usecols= fields )
    labels= df.breedlabel
    imageids= df.id

    #print (labels)
    labelarray=[]
    for i in labels:
        a= [0]*120
        a[int(i)]=1
        labelarray.append(a)
    labelarray = np.array(labelarray)
    np.save('imagelabels', labelarray)
    #print (labelarray)


    #cv2.namedWindow('Display Window')
    for i in imageids:
        k=i+'.jpg'
        path = os.path.join(IMAGE_DIR,k)
        #path= path+'.jpg'
        img = cv2.imread(path)
        img = cv2.resize(img, (50,50))
        #cv2.imshow('Display Window', img)
        #cv2.waitKey(0)
        training_data.append([np.array(img)])
    np.save('dogbreedimages.npy', training_data)

create_train_data()