# Recognition and Object Counting on Building Materials
## Building Dataset

Your directory sturcture should be as the following:

```
project_directory
│   README.md 
│
├─ pretrainedgooglenet.ipynb
│
├─ create_dataset.py
│
├─ dataset.csv
│
└─ dataset
    ├─ 1 (directory of type 1)
    │   ├─ big
    │   │
    │   ├─ medium
    │   │
    │   └─ small
    │
    ├─ 2 (directory of type 2)
    │   ├─ big
    │   │
    │   ├─ medium
    │   │
    │   └─ small
    │
    ├─ 3 (directory of type 3)
    │   ├─ big
    │   │
    │   ├─ medium
    │   │
    │   └─ small
    │
    ├─ 4 (directory of type 4)
    │   ├─ big
    │   │
    │   ├─ medium
    │   │
    │   └─ small
    │
    ├─ 5 (directory of type 5)
    │   ├─ big
    │   │
    │   ├─ medium
    │   │
    │   └─ small
    │
    ├─ 6 (directory of type 6)
    │   ├─ big
    │   │
    │   ├─ medium
    │   │
    │   └─ small
    │
    └─ 7 (directory of type 7)
        ├─ big
        │
        ├─ medium
        │
        └─ small

```

With distributing images to the right directory, and simply run the python script "create_dataset.py", four csv files for each dataset will be created.

## Building Material Recognition

This [link](https://colab.research.google.com/drive/1k99HyoaI9Ifc7Od1jKTSyP47GJwYynAa?usp=sharing) links to our transform learning model on google colab.

If you have enough data (at least thousands of images of each types is recommended), you can build your on model refer to this paper: 

> Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S.E., Anguelov, D., Erhan, D., Vanhoucke, V., & Rabinovich, A. (2015). Going deeper with convolutions. 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 1-9.

## Object detecting and counting

This [link](https://colab.research.google.com/drive/1AVC0aZoM0d9h8IC3X0H8Y_yHfQqdjqrj?usp=sharing) links to our yolo object detecting model on google colab. 

And all the following instructions is cited from and can be found at [AlexeyAB’s Github](https://github.com/AlexeyAB/darknet/).

* **YOLO Dataset labeling**

    There are lots of free tools or application for labeling yolo datset. such as [label studio](https://labelstud.io/), [OpenLabeling](https://github.com/Cartucho/OpenLabelin), etc. Choose one for your own usage and then download it.

    Remeber to create and upload the labeled custom dataset “obj.zip” file to the “yolov4” folder on your drive. This dataset should includes every image with its responding label txt file. The image and its label txt file should share the same name.

* **Custom Config Files for YOLO Training**

    * config file

        Download the custom config file from [AlexeyAB’s Github](https://github.com/AlexeyAB/darknet/).

        * change line batch to batch=64
        * change line subdivisions to subdivisions=16
        * change line max_batches to (classes*2000, but not less than number of training images and not less than 6000), f.e. max_batches=6000 if you train for 3 classes
        * change line steps to 80% and 90% of max_batches, f.e. steps=4800,5400
        * set network size width=416 height=416 or any value multiple of 32
        * change line classes=80 to your number of objects in each of 3 [yolo]-layers

            So if classes=1 then it should be filters=18. If classes=2 then write filters=21.
            
        * change [filters=255] to filters=(classes + 5)x3 in the 3 [convolutional] before each [yolo] layer, keep in mind that it only has to be the last [convolutional] before each of the [yolo] layers.

* **Create "obj.data" and "obj.names"**

    * obj.names

        Includes every object names, one in each line.

    * obj.data

        Includes following content:

        * The number of classes.
        * The path to train.txt and test.txt files created bu process.py.
        * The path to obj.names file which contains the names of the classes.
        * The path to the training folder where the training weights will be saved.

The directory structure for yolo traning should look similar as the following:

```
project_directory
│
├─ darknet
│ 
├─ training
│ 
├─ obj.data
│ 
├─ obj.names
│ 
├─ obj.zip
│ 
├─ process.py
│ 
└─ yolov4-custom.cfg

```

## **Contributers**
* YI-TE(Alex), Lyu 呂以德. Research Center for Information Technology Innovation, Academia Sinica
* Chieh-Ming(Jimmy), Chang 張傑名. Research Center for Information Technology Innovation, Academia Sinica