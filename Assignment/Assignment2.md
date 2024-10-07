# Assignment 2: Image Classification of NIKE and Adidas Shoes

## Dataset Overview

You are provided with a dataset containing images of NIKE and Adidas shoes. The dataset is organized by brand, each with separate train and test folders:

Download data: https://drive.google.com/file/d/11u7tm95zylQ0UEdWFQaVrZgHqOOAVZzL/view?usp=sharing

* train: Contains images to be used exclusively for training and validation.
* test: Contains images reserved strictly for testing your model's performance.
  Important: You may only use the images in the train folders for training and validation purposes. Do not use the test images during the training or validation phases.

## Assignment Requirements

### 1. Data Processing

**Dataset Preparation**:

* Research and implement methods to build an image dataset suitable for training a classification model.
* Create appropriate labels for the images to distinguish between NIKE and Adidas shoes.

**Data Augmentation (Optional)**:
* Apply data augmentation techniques to enhance the diversity of your training dataset.

**Preprocessing:**
* Normalize image data as required (if needed).
* Resize or crop images to a uniform size compatible with your CNN model.

### 2. Model Development

**Build a Convolutional Neural Network (CNN)**:
* Design a CNN architecture capable of classifying images as either NIKE or Adidas.
* Justify your choice of architecture and layers.
**Implementation**:
* Use a deep learning framework of your choice (e.g., TensorFlow, Keras, PyTorch).

## 3. Model Training and Validation

**Training:**

* Train your CNN model using only the train dataset.
Implement a validation strategy (e.g., train-validation split) to monitor overfitting and underfitting.

**Learning Curve:**
* Plot the training and validation accuracy and loss over epochs to present a learning curve.
Ensure the learning curve demonstrates reasonable performance improvements over time.

## 4. Performance Optimization

**Techniques:**
* Employ any techniques you find appropriate to improve model performance on the test dataset.
This may include hyperparameter tuning, regularization, transfer learning with pre-trained models, etc.


**Evaluation:**
* After training, evaluate your model using the test dataset.
* Report the final performance metrics (e.g., accuracy, precision, recall).

## 5. Reporting

**Summary Report (Max 2 Pages):**
**Introduction:**
* Briefly describe the problem and your approach.

**Methodology:**
* Outline the data processing steps, model architecture, and training process.
* Results:
Present your learning curves and final evaluation metrics.

**Observations:**

* Discuss any challenges faced and how you addressed them.
Reflect on the effectiveness of the techniques used for performance improvement.

**Formatting:**
* The report should be clear, concise, and well-organized.
Include figures and tables as necessary, ensuring they are properly labeled and referenced.

## 6. Submission Instructions

**Code:**
Submit all source code used for data processing, model training, and evaluation.
Ensure your code is well-documented with comments and organized into logical sections or scripts.

**Pre-trained Model:**
Include the trained model file (e.g., saved weights or checkpoint).

**Report:**
Submit the summary report in PDF format.
Submission Platform:
Upload all required files to Gradescope under the appropriate assignment entry.

**Deadline:**
Ensure you submit all components before the specified deadline (2024-10-23 2:30 PM).