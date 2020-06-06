[![yplate](https://img.shields.io/badge/yplate-v0.0.1-blue)](https://github.com/deepraj1729/yplate/releases/tag/0.0.1)  [![license](https://img.shields.io/badge/License-MIT-yellow)](https://github.com/deepraj1729/yplate/blob/master/LICENSE) [![dependencies](https://img.shields.io/badge/dependencies-packages-orange)](https://github.com/deepraj1729/yplate/blob/master/requirements.txt)
![python](https://img.shields.io/badge/python-3.5%3E-red)
# Yplate

## Detect Vehicle Number plates with YOLOv3 powered by OpenCV 3.x

### Usage:

    pip install yplate
    
## Command-line Arguments:-

1. `detect`

2. `crop`


## `detect` (Detect  Plates) :-

### (1.a)  Detect plates manually (detected image will be saved to output directory always with original starting file name) 

    yplate detect img.jpg
    
### (1.b)  Detect plates and custom save it with a valid new filename (detected image will be saved to output directory with custom file name) 
    
    yplate detect img.jpg --save out.jpg
    
### (1.c)  Hide output detected image

    yplate detect img.jpg --hide_img
    
### (1.d)  Hide output in command-line

    yplate detect img.jpg --hide_out

### (1.e)  Don't save output image 

    yplate detect img.jpg --save none


## `crop` (Crop Plates) :-

### (2.a)  Crop plates automatically ( Cropped plates will be saved to 'plates/' directory always with original starting file name)

    yplate crop img.jpg
    
### (2.b)  Detect plates and custom save it with a valid new filename (Cropped image will be saved to output directory with starting custom file name)
    
    yplate crop img.jpg --save plate1.jpg
    
### (2.c)  Hide cropped image in command-line

    yplate crop img.jpg --hide_img
    
### (2.d)  Hide output in command-line

    yplate crop img.jpg --hide_out

### (2.e)  Don't save output image

    yplate crop img.jpg --save none


### Check `yplate` version:

    yplate -v

### Model Configuration:

    yplate --config
