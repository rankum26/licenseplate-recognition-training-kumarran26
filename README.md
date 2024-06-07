#License Plate Recognition Training Repository
------------------
This repository is an addition to the [main License Plate Recognition Project](https://github.com/rankum26/licenseplate-recognition-kumarran26). This repo is dedicated to training the model.

#Data Collection
------------------
As mentioned in the main repository, I used my [own dataset](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/tree/main/data_new/images/train) consisting of car pictures taken with my smartphone that clearly show license plates. 

#Annotation
------------------
For the annotation process, I used CVAT (Computer Vision Annotation Tool). I uploaded all 249 images to CVAT and manually annotated them, marking the license plates. The annotations were then exported in YOLOv1.1 format, resulting in a set of label files (.txt) corresponding to each image. These label files are crucial for training the model. The annotated files are stored in the data_new folder, which contains these .txt files.

#Training
------------------
#Attention
To run a training session, go to config.yaml. Update the paths to match the full path to the data_new folder. The relative paths for train and val should work as they are.

#Running the Training
------------------
In main.py, you can configure the number of epochs and other parameters. After setting your desired configuration, run the training script:

python main.py

After the run, all results will be saved in the runs/detect folder. For example, train4 contains interesting analysis from the training process, such as the confusion matrix, F1 curve, labels, precision and recall curves, training batches, and validated batches with predictions.

Confusion Matrix
![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/runs/detect/train4/confusion_matrix.png)

F1 Curve
![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/runs/detect/train4/F1_curve.png)

P Curve
![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/runs/detect/train4/P_curve.png)

R Curve
![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/runs/detect/train4/R_curve.png)

Results

![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/runs/detect/train4/results.png)

Batch labels
![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/runs/detect/train4/val_batch0_labels.jpg)

Batch Preditions
![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/runs/detect/train4/val_batch2_pred.jpg)


#Using trained Model
------------------
You don't need to train your own model. You can test the trained model (train4), which was trained for 8.5 hours with 100 epochs.

#Testing
------------------
To test the trained model, use testing.py. Attention: Before running the script, update the path of the trained model in testing.py to match your environment.

I have provided two pictures for testing in the testing_pictures folder. You can also upload your own pictures to test. After running the script, a plot will pop up with the prediction, and the plot will be saved in the testing_runs folder.

#Running the Tests
------------------
python testing.py

This script will perform predictions on the test images and visualize the results.

![alt text](https://github.com/rankum26/licenseplate-recognition-training-kumarran26/blob/main/testing_runs/tested_IMG_0498.JPG) 

#Help or Questions
------------------
If you need help don't hesitate to contact me over Teams: kumarran@students.zhaw.ch 
Otherwise you can [ask my bestfriend](https://chatgpt.com/) :D 