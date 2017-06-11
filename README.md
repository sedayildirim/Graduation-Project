# Graduation-Project

### Dependencies:
- Cuda
- Theano/Tensorflow

### Folders:
- nyu-script/ -> scripts to process the NYU-Depth V2 dataset
- neural-network/ -> the modified VGG-16 network

### Preprocessing:
Run nyu-script.py to process the NYU-Depth dataset. All scripts need to be in the same directory.
 ```bash
python nyu-depth.py <dataset-directory>
```
Script creates 3 folders: 
- **0** -> Images that have the closest object on the left
- **1** -> Images that have the closest object on the center
- **2** -> Images that have the closest object on the right

Script creates 4 txt files:
- **data.txt**        -> list of directories of PPM (RGB) images
- **jpgdata.txt**     -> list of directories of PGM (Depth) images corresponding to the PPM (RGB) images in *data.txt*
- **labels.txt**      -> list of JPG images that were converted from PPM images in *data.txt*
- **categories.txt**  -> list of categories of images

### Modified VGG-16
Batch size is set to 16. Can be changed from the variable *batch_size*.  
*train_set* and *test_set* values need to be changed according to the dataset size. 
- *train_set*: size of the training set
- *test_set*: size of the testing set
