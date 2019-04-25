import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from tqdm import tqdm      # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
import pandas as pd

''' 
This function will convert all the dog breeds in to a value between 0 to 119 ( an unique value for a breed )

breed : 120 dog breed list
breedlabels : dog breed as a value between 0 to 119

This will create a seperate csv file with breed labels
Also, this will create another csv file with 120 dogbreeds which will be useful in future reference

'''

def breed_label():
    label_dir = 'D:/SEM3 TRONIC ACA/Machine learning/Dog/labels.csv'
    breedlablels = []
    fields =['id','breed']
    df = pd.read_csv(label_dir, skipinitialspace=True, usecols= fields )
    dogbreed = df.breed
    imageids = df.id

    breed = list(dict.fromkeys(dogbreed))    
    breednp = np.array(breed)
    #np.save('breeds',breednp)
    np.savetxt("dogbreeds.csv", breednp, delimiter=",", fmt='%s', header="dogbreed")

    for i in dogbreed:
        breedlablels.append(breed.index(i))

    breedlablelsnp = np.array(breedlablels)
    #np.save('breedlabels',w)
    np.savetxt("breedlabels.csv", breedlablelsnp, delimiter=",", fmt='%s', header="breedlabel")

breed_label()
    
'''
After running this, copy the breedlabel colum of the created csv file and paste that as the third colum in the orginal csv file.
Also, remeber to name that colum as breedlabel

'''