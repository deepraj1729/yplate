[![yplate](https://img.shields.io/badge/yplate-v0.0.1-blue)](https://github.com/deepraj1729/yplate/releases/tag/0.0.1)  [![license](https://img.shields.io/badge/License-MIT-yellow)](https://github.com/deepraj1729/yplate/blob/master/LICENSE) [![dependencies](https://img.shields.io/badge/dependencies-packages-orange)](https://github.com/deepraj1729/yplate/blob/master/requirements.txt)
[![pull](https://img.shields.io/badge/pull--requests-requests-green)](https://github.com/deepraj1729/yplate/pulls) [![issues](https://img.shields.io/badge/issues-issues-red)](https://github.com/deepraj1729/yplate/issues) ![python](https://img.shields.io/badge/python-3.5%3E%3D-brightgreen)
# Yplate

## Detect Vehicle Number plates with YOLOv3 powered by OpenCV >= 3.x 

### Updates:
It will be updated to `pypi` and `conda` soon with stable releases

### Install:

#### a. With `wheel` 

    pip install https://github.com/deepraj1729/yplate/releases/download/0.0.1/yplate-0.0.1-py3-none-any.whl

#### b. With `tar.gz` 
    
    pip install https://github.com/deepraj1729/yplate/releases/download/0.0.1/yplate-0.0.1.tar.gz
    
    
# Usage:

### Command-line Arguments:-

1. `detect`

2. `crop`


## `detect`

### (1.a)  Detect plates automatically (detected image will be saved to output directory always with original starting file name) 

    yplate detect images/car2.jpg


![car2](output/car2.jpg)

<img src="https://github.com/deepraj1729/yplate/blob/master/out_txt/out.png" width = "400" height = "500">


### (1.b)  Detect plates and custom save it with a valid new filename (detected image will be saved to output directory with custom file name) 
    
    yplate detect images/car2.jpg --save out2.jpg
    
### (1.c)  Hide output detected image

    yplate detect images/car2.jpg --hide_img
    
### (1.d)  Hide output in command-line

    yplate detect images/car2.jpg --hide_out

### (1.e)  Don't save output image 

    yplate detect images/car2.jpg --save none


## `crop`

### (2.a)  Crop plates automatically ( Cropped plates will be saved to 'plates/' directory always with original starting file name)

    yplate crop images/car2.jpg

![car2](plates/car2_plate_0.jpg) 

<img src="https://github.com/deepraj1729/yplate/blob/master/out_txt/out_crop.png" width = "400" height = "500">

### (2.b)  Detect plates and custom save it with a valid new filename (Cropped image will be saved to output directory with starting custom file name)
    
    yplate crop images/car2.jpg --save plate2.jpg
    
### (2.c)  Hide cropped image in command-line

    yplate crop images/car2.jpg --hide_img
    
### (2.d)  Hide output in command-line

    yplate crop images/car2.jpg --hide_out

### (2.e)  Don't save output image

    yplate crop images/car2.jpg --save none


### Check `yplate` version:

    yplate -v

### Model Configuration:

    yplate --config

## Sample Outputs:

### Detected Plates:

<img src="https://github.com/deepraj1729/yplate/blob/master/output/car2.jpg" width = "230" height = "170"> <img src="https://github.com/deepraj1729/yplate/blob/master/output/car3.jpg" width = "230" height = "170"> <img src="https://github.com/deepraj1729/yplate/blob/master/output/car4.jpg" width = "230" height = "170"> <img src="https://github.com/deepraj1729/yplate/blob/master/output/car5.jpg" width = "230" height = "170"> <img src="https://github.com/deepraj1729/yplate/blob/master/output/car6.jpg" width = "230" height = "170"> <img src="https://github.com/deepraj1729/yplate/blob/master/output/car1.jpg" width = "230" height = "170">

### Corresponding plates:

<img src="https://github.com/deepraj1729/yplate/blob/master/plates/car2_plate_0.jpg" width = "120" height = "40">  <img src="https://github.com/deepraj1729/yplate/blob/master/plates/car3_plate_0.jpg" width = "120" height = "40">  <img src="https://github.com/deepraj1729/yplate/blob/master/plates/car4_plate_0.jpg" width = "120" height = "40">  <img src="https://github.com/deepraj1729/yplate/blob/master/plates/car4_plate_1.jpg" width = "120" height = "40">  <img src="https://github.com/deepraj1729/yplate/blob/master/plates/car5_plate_0.jpg" width = "120" height = "40">  <img src="https://github.com/deepraj1729/yplate/blob/master/plates/car6_plate_0.jpg" width = "120" height = "40">  <img src="https://github.com/deepraj1729/yplate/blob/master/plates/car1_plate_0.jpg" width = "100" height = "40">

