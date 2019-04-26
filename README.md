# dog-breed
---

### Intro

This is an attempt to create a dog breed identification mobile application using neural networks. The famous Kaggle dog breed classification dataset is used here to train and test the model. Basically, there are two significant steps in this project.
1.  Training and testing neural network
2.  Mobile application development

The main focus here is to create a neural network to classify the dog in to there breeds. The mobile app development is just for experimenting. 

---

### Description

- breedlabels.py

There are exactly 120 dog breeds to classify. So, all these dog breeds are given a unique number between 0 to 119. To generate these breed labels from the given labels csv file in the dataset, a python script is used (included I this repo as breedlabels.py). This will generate a separate csv file called breedlabels.csv (also included in this repo). To make the things easy in future steps, the content in this csv file have to copied into the labels.csv given in the dataset (or can modify the given python script to do that).

- create_train_data.py

There are separate train and test images in the dataset. Labels for all the train images are also given. Before going into the neural network, it’s better to convert those images in to numpy arrays. Also, it’s better to convert the image labels in to another numpy array, so that we have all the required data as two numpy arrays. To do both these tasks there is a python script included in this repo (create_train_data.py). 

---
