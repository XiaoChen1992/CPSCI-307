# CPSCI-307
This is home page for Hamilton College CPSCI-307 Topics in Computer Science II: Deep Learning. Be sure you ***READ THIS PAGE CAREFULLY!!!***

# Lecture logic
## Lecture time
Monday, Wendsday, and Firday 2:30 PM-3:45 PM at Taylor Science Center, 3024

## Office Hours
Monday, Wendsday and Friday 4:00 PM-4:50 PM or appointment by email. You can meet me at my office, Taylor Science Center 2016 or zoom if needed. 

## Email
schen3@hamilton.edu
Usually I will reply your email no later than 48 hours, if you do not receive any reply, email me again.

# Learning objectives

In this class, we will focus on applying deep learning technoigy on the real world data. After this class, you shoud be able to:

1. Covert a real-life or research question into computer science way

2. Build a deep learing pipeline to solve the question

3. Evaluate your deep learning model's performance correctly

# Prerequisites

1. This class havily relies on Python. You should be comfortable to use python for programming or you are familar with other programming languages and can learn and use python in a short time.

2. Some basic linear algebra backgroud (vector, matrix, matrix operation, etc) are required


# Cousrse Materials

## Textbook

We will use [Dive into Deep Learning](https://d2l.ai/) as our main text book [(PDF download](https://arxiv.org/pdf/2106.11342#page=25.12)). Also, some classic machine/deep learning papers will also be included in readling list.

The following two books are also worth to read if you want to discover more math behind machine learning and deep learning, but they are not required.

1. [Deep Learning ](https://www.deeplearningbook.org/)

2. [ESL](https://hastie.su.domains/ElemStatLearn/)


## Enviroment setting

We will use [PyTorch ](https://pytorch.org/get-started/locally/) (version: Stable 2.3.1) for all assignments and projects. This class requires GPU for deep learning model training. You need to prepare your own GPU for class. Usually, NVIDIA GPU is default for training. But you also can choose AMD or Apple M chip for traning. However, AMD and Apple GPU may bring some unexpeted warnings or errors which need you to debug by yourself. 

If you do not have a GPU, some online platforms can be considered. Here are some GPU notebook options. 

1. Google Colab

2. Amazon  SeageMake

3. Kaggle GPU 

All these products provid differnt plans. If you want to train more complcaited models, you always can choose build cloud machine for use, but this is not required for this class.

# Academic Integrity & Collaboration

You should work on your all your homeworks by yourself. You can discuss your homework with me, your classmates, or your firends, but you are **NOT** allowed to use other's code or any code from internet. 

You can work on the final project on your own or team up to 3 students. If you team work on the final project, report each member's contribution on final report.

## AI policy

You are **NOT** allowed to use any kind of generative AI tools (online or offline) for your homeworks. Any code from generative AI tools (online or offline) or internet will be consider as cheating. 

You are **ENCOURAGED** to use AI tools for your final project. But you **NEED** to provide your prompt history to me.

# Grading

Your grade will be comprised of the following weighted components:

1. **Assignments(30%):** We will have 3 assignments, you have **two** weeks for each assignment. Each assignment contributs 10% of your final grade.

2. **Midterms (10%):** We will only have one in-class exam before Thanksgiving. The exam's goal is make sure you understand the basic conpet of machine learing and deep learning.

3. **Project (60%):** The final project covers:
   
   1. Proposal (10%): Expalin your paln for the final project, maximum to 2 pages. Ths proposal should explain what is the question that interest you? What kind of data you want to collect. How to collect the data? What kind of model you want to use? How to evaluate your model's performance?
   
   2. Data (10%): You shoud report how you collect your own data for final project. The following part should be included. a. Where is the data resource? b. How you collect the data? c. How you pre-process data? The report is maximum up to 2 pages. 
   
   3. Code (15%):  You need to push your project's code to class's GitHub repo. Your code should be well-originized and easy to read. Check this [example](https://github.com/XiaoChen1992/CPSCI-307/tree/main/project_example) to orgnize your code.
   
   4. Performance (15%): 
      4.1. I should be able to directly run your inference.py file in termial to use your model. For example:
      `shell
      python inference.py --data_path /example/data
      `
      4.2. You need to report your learning curve though [Weights&Biases](https://wandb.ai/site). We will learn how to use this tool in class.
      4.3. You model's performance should be evaluated by suiable metrics and get a resonable performance. 
   4. Project report (10%): 
   
   Report shouid follow [IEEE format](https://www.ieee.org/conferences/publishing/templates.html), maxiumum 8 pages (includes reference). The report covers following parts:
      
      1. Abstract
      
      2. Introduction
      
      3. Method and materials
      
      4. Performance
      
      5. Conclusion.

# Tips for success

If want to learning this class well, here are some suggestions

1. Read high quality code and learning how they orgnized their code

2. Design your deep learing model pipeline carefully
