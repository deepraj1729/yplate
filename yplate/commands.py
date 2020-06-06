import cv2
import numpy as np
import os
from yplate.ops import load_model,display_input,display_top,display_output,display_error
import json

### Detect Command ###
def detect(img_name,cfg,weights,classes,save_img=True,hide_img=False,hide_out=False):
    try:
        img = cv2.imread(img_name)
        #Load Model
        net = cv2.dnn.readNet(weights,cfg)
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        """ Resize image (optional) """
        # stretch_near = cv2.resize(img, (780, 540), interpolation = cv2.INTER_NEAREST)
        # img = cv2.resize(img, (1000, 640), interpolation = cv2.INTER_NEAREST)
        # img = cv2.resize(img,None,fx=2,fy=2)

        # image dimensions 
        height, width, channels = img.shape

        # Dynamic Detected plate Font Text 
        if(width>height):
            text_font_size = int((width/1000)*5)
        else:
            text_font_size = int((height/1000)*5)
        colors = (0, 255, 34)

        # Create the pipeline
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        cropped_plate = []
        crop_rect = []
        class_ids = []
        confidences = []
        boxes = []

        # Loop to predict plates
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        #Detected plates put inside the image
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h),(0,255,0), 2)
                #Detected rectangle
                crop_rect.append([x,y,w,h])
                #Cropped detected rectangle
                crop = img[y:y+h, x:x+w]
                cropped_plate.append(crop)
                cv2.putText(img, label, (x, y-20), font, text_font_size, (255, 255, 80), 2)
        
        no_of_detected_plates = len(crop_rect)
        confidences = confidences[-no_of_detected_plates:]

        #Show image (default show image)
        if(hide_img == False):
            cv2.imshow("Output Image",img)
            key = cv2.waitKey(2000) & 0xFF
            if key == ord('q'):
                cv2.destroyAllWindows()

        display_top()

        # Display output (prediction)
        file_path = img_name.split("/")
        file_name = file_path[-1]

        #Silence output or not

        if(not hide_out):
            display_input(img_name)
            display_output()
            if(no_of_detected_plates > 0):
                data = {
                            "output": {
                                "model":"YOLO v3",
                                "confidence" : "{}".format(confidences),
                                "cropped_rectangles":"{}".format(crop_rect),
                                "plates_found":"{}".format(no_of_detected_plates),
                                "class_ids":"{}".format(class_ids)
                            }
                        }
                print(json.dumps(data,indent=2))
                print("\nPlate detected successfully :)")
                print("\n##################################################\n")
            else:
                print("No plates detected in the image ")
                print("\n##################################################\n")

        
        #Write detected image to disc
        if(save_img):
            if(save_img == True):  #Save image to output by default
                if('output' in os.listdir('./')):
                    try:
                        cv2.imwrite('output/'+file_name,img)
                        print("Detected image saved in 'output' directory as '"+ file_name +"'")
                        print("\n##################################################\n")
                        
                    except Exception as e:
                        display_error()
                        print("Oops an unknown error occured")
                        print("\n##################################################\n")
                else:
                    os.mkdir('output')
                    try:
                        cv2.imwrite('output/'+file_name,img)
                        print("Detected image saved in 'output' directory as '"+ file_name +"'")
                        print("\n##################################################\n")

                    except Exception as e:
                        display_error()
                        print("Oops an unknown error occured")
                        print("\n##################################################\n")

            elif(save_img.lower() == 'none'): #Don't save image
                pass
            elif(save_img != True):  #Custom name save image (if error then original name)
                if('output' in os.listdir('./')):
                    try:
                        cv2.imwrite('output/'+save_img,img)
                        print("Detected image saved in 'output' directory as "+ "'"+save_img+ "'")
                        print("\n##################################################\n")

                    except Exception as e:
                        display_error()
                        cv2.imwrite('output/'+file_name,img)
                        print("Detected image saved in 'output' directory as '"+ file_name +"' due to error in given output filename")
                        print("\n##################################################\n")
                else:
                    os.mkdir('output')
                    try:
                        cv2.imwrite('output/'+save_img,img)
                        print("Detected image saved in 'output' directory as "+ "'"+save_img+ "'")
                        print("\n##################################################\n")

                    except Exception as e:
                        display_error()
                        cv2.imwrite('output/'+file_name,img)
                        print("Detected image saved in 'output' directory as '"+ file_name +"' due to error in given output filename")
                        print("\n##################################################\n")

        return confidences,crop_rect,class_ids
    except AttributeError as error:
        display_top()
        display_error()
        print("File not found in the given path '{}' ".format(img_name))
        print("\n##################################################\n")
        
    except Exception as e:
        display_top()
        display_error()
        print("Oops!Couldn't detect plate due to some errors. Check command line inputs")
        print("\n##################################################\n")


### Crop command ###
def crop(img_name,cfg,weights,classes,save_img=True,hide_img=False,hide_out=False):
    try:
        img = cv2.imread(img_name)
        #Load Model
        net = cv2.dnn.readNet(weights,cfg)
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        """ Resize image (optional) """
        # stretch_near = cv2.resize(img, (780, 540), interpolation = cv2.INTER_NEAREST)
        # img = cv2.resize(img, (1000, 640), interpolation = cv2.INTER_NEAREST)
        # img = cv2.resize(img,None,fx=2,fy=2)

        # image dimensions 
        height, width, channels = img.shape

        # Create the pipeline
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        crop_img = []
        cropped_plate = []
        crop_rez = []
        crop_rect = []
        class_ids = []
        confidences = []
        boxes = []

        # Loop to predict plates
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        #Detected plates put inside the image
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                crop_rect.append([x,y,w,h])
                crop = img[y:y+h, x:x+w]
                crop_img.append(crop)
                cropped_plate.append(crop)
        
        no_of_detected_plates = len(crop_rect)
        confidences = confidences[-no_of_detected_plates:]

        for i in range(len(crop_img)):
            rez = cv2.resize(crop_img[i],None,fx=2,fy=2)
            crop_rez.append(rez)

        if(no_of_detected_plates > 0):
            #Show image (default show image)
            if(hide_img):
                pass
            else:
                for i in range(len(crop_img)):
                    cv2.imshow("Output Image (Cropped plate)",crop_rez[i])
                    key = cv2.waitKey(2000) & 0xFF
                    if key == ord('q'):
                        cv2.destroyAllWindows()

            # Display input 
            inp_path = img_name.split("/")
            inpFile = inp_path[-1]
            file_ = inpFile.split(".")
            inp_file_name = file_[0]  #filename provided
            inp_file_ext = file_[1] #file extension

            display_top()

            #hide output or not
            if(not hide_out):
                display_input(img_name)
                display_output()
                data = {
                            "output": {
                                "cropped_rectangles":"{}".format(crop_rect),
                                "plates_found":"{}".format(no_of_detected_plates),
                            }
                        }
                print(json.dumps(data,indent=2))
                print("\n##################################################\n")

            
            #Write detected image to disc
            if(save_img):
                if(save_img == True):  #Save image to output by default
                    if('plates' in os.listdir('./')):
                        try:
                            for i in range(len(crop_img)):
                                cv2.imwrite("plates/"+inp_file_name+"_plate_{}".format(i)+"."+inp_file_ext,crop_rez[i])
                            print("Detected plates saved in 'plates' directory")
                            print("\n##################################################\n")
                            
                        except Exception as e:
                            display_error()
                            print("Oops an unknown error occured")
                            print("\n##################################################\n")
                    else:
                        os.mkdir('plates')
                        try:
                            for i in range(len(crop_img)):
                                cv2.imwrite("plates/"+inp_file_name+"_plate_{}".format(i)+"."+inp_file_ext,crop_rez[i])
                            print("Detected plates saved in 'plates' directory")
                            print("\n##################################################\n")

                        except Exception as e:
                            display_error()
                            print("Oops an unknown error occured")
                            print("\n##################################################\n")

                elif(save_img.lower() == 'none'): #Don't save image
                    pass
                elif(save_img != True):  #Custom name save image (if error then original name)
                    #Display output image (predicted)
                    file_save = save_img.split(".")
                    file_sname = file_save[0]  #filename provided
                    file_save_ext  = file_save[1]  #file extension
                    if('plates' in os.listdir('./')):
                        try:
                            for i in range(len(crop_img)):
                                cv2.imwrite("plates/"+file_sname+"_plate_{}".format(i)+"."+file_save_ext,crop_rez[i])
                            print("Detected plates saved in 'plates' directory")
                            print("\n##################################################\n")

                        except Exception as e:
                            display_error()
                            for i in range(len(crop_img)):
                                cv2.imwrite("plates/"+inp_file_name+"_plate_{}".format(i)+"."+inp_file_ext,crop_rez[i])

                            print("Detected plates saved in 'plates' directory as original filename due to error in given output filename")
                            print("\n##################################################\n")
                    else:
                        os.mkdir('plates')
                        try:
                            for i in range(len(crop_img)):
                                cv2.imwrite("plates/"+file_sname+"_plate_{}".format(i)+"."+file_save_ext,crop_rez[i])
                            print("Detected plates saved in 'plates' directory")
                            print("\n##################################################\n")

                        except Exception as e:
                            display_error()
                            for i in range(len(crop_img)):
                                cv2.imwrite("plates/"+inp_file_name+"_plate_{}".format(i)+"."+inp_file_ext,crop_rez[i])
                            print("Detected plates saved in 'plates' directory as original filename due to error in given output filename")
                            print("\n##################################################\n")
        else:
            print("No plates detected in the given image ")
            print("\n##################################################\n")
        return crop_rect
    except AttributeError as error:
        display_top()
        display_error()
        print("File not found in the given path '{}' ".format(img_name))
        print("\n##################################################\n")
        
    except Exception as e:
        display_top()
        display_error()
        print("Oops!Couldn't detect plate due to some errors. Check command line inputs")
        print("\n##################################################\n")