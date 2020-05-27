#ISIC-2019

This repo deals with the ISIC 2019 dataset for multiclass classification of skin lesions.

###Installations

The required installed packages for this repo are:

numpy==1.18.4
tensorflow==2.2.0
cv2==4.2.0
pandas==1.0.3
Werkzeug==1.0.1
Flask==1.1.2
Pillow==7.0.0

Directory Setup
```bash
├── Callbacks
├── static
│   ├── models
│   └── uploads
├── ISIC_2019_Test_Input
├── ISIC_2019_Training_Input
└── datasets
    └── medium_size
        ├── test
        │   └── Images
        └── train
            ├── Images
            └── gt
```
###Data

Raw data can be directly downloaded from the ISIC website (https://challenge2019.isic-archive.com/data.html)
Model weights can be download from the following drive link (https://drive.google.com/open?id=1087rbiEJwO9EJMNsLjSPg-7xqCsoXOMW)
Processed Vectors can be downloaded from the following drive link (https://drive.google.com/open?id=144n6Q0VZIkMnEzgqSjAuANPEre7NjmFk)
Training

The model was trained in two steps

A learning rate of 0.0001 for 25 epochs
A learning rate of 0.00001 for 10 epochs
Usage

###ISIC_preprocessing.py

ISIC_preprocessing.py can be used as a command line program. There are 3 required arguments needed for usage:

--training_folder --> The folder where the training data is located
--test_folder --> The folder where the test data is located
--train_gt --> .csv file where ground truths are located
Additionally there are optional arguments:

--img_size --> The new dimension (square) of the new image, default = 224
--train_img_img --> Folder to save .npy arrays of processed training images
--train_img_gt --> Folder to save .npy of gt
--test_img_img --> Folder to save .npy arrays of processed test images
```bash
python ISIC_preprocessing.py --training_folder ISIC_2019_Training_Input/ --test_folder ISIC_2019_Test_Input/ --train_gt ISIC_2019_Training_GroundTruth.csv
```

###ISIC.ipynb

ISIC.ipynb can be used as a jupyter or colab notebook. For best results, load the notebook into colab and ensure that GPU support is enabled. The notebook can be run as is, with the files placed in the correct directories on drive.

Drive file locations are as follows under '/content/drive/My Drive/':
```bash
ISIC
├── callbacks
└── datasets
    └── medium_size
        ├── test
        │   └── Images
        └── train
            ├── Images
            └── gt
```
###app.py

app.py is the Flask webapp that can be run to make inferences on images. When launched, the file make take some time to load, this is due to the ML model being loaded in the background. Once running, upload an image of a skin lesion of file type (.png, .jpg, .tiff) and click the submit button. The web app will then make a prediction on the type of skin lesion as well as provide resources to learn more about that specific skin lesion
