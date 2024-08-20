# 2024 Fall CPSCI-307

This is the home page for Hamilton College CPSCI-307: Deep Learning. Be sure to ***READ THIS PAGE CAREFULLY!!!***

## Lecture Details

**Lecture time**: Monday and Wednesday 2:30 PM - 3:45 PM 

**Location**: Christian A. Johnson Hall (CJ) 305.

**Office Hours**: 

1. Monday 1:15 PM - 2:15 PM

2. Tuesday 10:00 AM - 11:00 AM 

3. Wednesday 1:15 PM - 2:!5 PM

4. Friday 11:00 AM - noon 

5. or by appointment via email. 

You can meet me at my office (SCCT 2016) or via Zoom if needed. 

**Email**: schen3@hamilton.edu

**Gradescope**: https://www.gradescope.com/courses, Entry Code: 8KXJGY

**Edsteam**: [Ed Discussion](https://edstem.org/us/courses/61325/discussion/)

## Course Description

This course discusses deep learning, covering foundational machine learning principles (loss functions, bias-variance trade-off, and optimization) and advanced models (Convolutional Neural Networks, Recurrent Neural Networks, Transformers) and their applications. The course is project-based, emphasizing the application of these techniques to real-world datasets using the deep learning framework PyTorch.

## Learning Objectives

In this class, we will learn:

1. Basic machine/deep learning concepts
2. Classic and state-of-the-art deep learning architectures
3. How to build, train, and test your own deep learning model on real-world data using PyTorch

After this class, you should be able to:

1. Convert a real-life or research question into a computer science problem
2. Build a deep learning pipeline to solve the problem
3. Correctly evaluate your deep learning model's performance


## Prerequisites

1. This class heavily relies on Python. You should be comfortable using Python for programming or be familiar with other programming languages and able to learn and use Python quickly.
2. Be familiar with the basic linear algebra (vector, matrix, matrix operations, ...) is required.

## Course Materials

### Textbook

**Required**: [Dive into Deep Learning](https://d2l.ai/) 

**Recommended**: [Deep Learning](https://www.deeplearningbook.org/)

### Environment Setup

We will use [PyTorch](https://pytorch.org/get-started/locally/) (version: Stable 2.3.1) for all assignments and projects. This class requires a GPU for deep learning model training. You need to prepare your own GPU for the class. Usually, an NVIDIA GPU is the default for training. However, you can also choose AMD or Apple M chips for training, although they may bring some unexpected errors that you will need to debug yourself.

If you do not have a GPU, some online platforms can be considered. Here are some GPU notebook options:

1. Google Colab (default for this class)
2. Amazon SageMaker
3. Kaggle GPU

You will need a GPU for assignment 2, assignment 3 and final project.

### Fee

Colab provides free GPU resources (with very limited GPU hours), but you also can pay for more resources. You can sign up for a paid account at [Google Colab](https://colab.research.google.com/signup). 

If you have any financial difficulties in purchasing GPU services, **TALK TO ME**.

### Laptops and Electronics

You should bring a laptop to lectures as we will live code in every class. If you are unable to do this, let me know. You should not use a phone or any similar device during lectures. If you take notes on a tablet, then you should not be typing on it during class, but only writing (e.g. with a stylus) unless you require accommodation for a disability. Tablets should be kept flat on the desk and should not be propped up unless you require accommodation for a disability. If you would like to discuss this restriction, you are always welcome to come talk to me about it.

During most lectures, we will have mini labs (live coding). **You can only use your laptop  for coding at mini lab time. You can't use the computer for anything unrelated to the course content. For example, I found twice that if you use the computer for something unrelated (E.g.: facebook, youtube, game,...) to the course, you will lose 5% of your final grade.** For example: If your final score is 90, because of using laptop for unrelated to the course content twice. Your score will drop to $90 \times 0.95 =85.5$.

## Academic Integrity & Collaboration

You should work on all assignments by yourself. You can discuss your assignments with me, your classmates, your friends, or other professors, but you are **NOT** allowed to use others' code or any code from the internet.

You can work on the final project on your own or team up with up to 3 students. If you choose to work in a team, your team must report each member's contribution in the final report. I encourage all team members to join the entire project pipeline as much as possible, instead of each team member only being in charge of one part of the project. Here is an [example](https://github.com/XiaoChen1992/CPSCI-307/blob/main/project_example/contrbution.md). You should include this file in your own project, otherwise, each team member will lose 5% of project score. For example, if you final project's score is 90, because of missing file, the score will drop to $90\times0.95=85.5$

### AI Policy

### Assignments

You are **NOT** allowed to use any generative AI tools (online or offline) for your assignments. Any code from generative AI tools (online or offline) will be considered cheating and you will receive 0 points for the assignments.

### Final Project

You are **ENCOURAGED** to use AI tools for your final project, but you **NEED** to provide your prompt history to me, **otherwise you will lose 5%** of your final project score. Here is a prompt history [example](https://github.com/XiaoChen1992/CPSCI-307/blob/main/project_example/prompt_history_example.pdf). For example, if you final project's score is 90, because of missing prompt history, the score will drop to $90\times0.95=85.5$

**THIS POLICY APPLIES ONLY TO THIS CLASS!!!** For other classes, follow the academic integrity policy of that class or ask your professor.

## Grading

Your final score will be comprised of the following weighted components:

1. **Assignments (30%)**: Three assignments, each assignment contributes 10% of your final score.  The assignments' goal is to let you building, training, and testing different types of neural network by PyTorch.

2. **Midterm (10%)**: One midterm exam (no notes) at Week 7. The exam's goal is to ensure you understand the basic concepts of machine/deep learning.  

3. **Final Project (60%)**: The final project covers:
   
   1. Proposal (10%): Create a plan of the final project, up to 2 pages ([IEEE - Manuscript Templates for Conference Proceedings](https://www.ieee.org/conferences/publishing/templates.html))  
   
   2. Data (10%): Report how you collected your own data for the final project. Include the following parts: a. Where is the data source? b. How did you collect the data? c. How did you preprocess the data? The report is up to 1 page (IEEE format). You also need to provide some data examples to me.
   
   3. Code (15%): Upload your project's code to the gradescope. Your code should be well-organized and easy to read. Check this [example](https://github.com/XiaoChen1992/CPSCI-307/tree/main/project_example) to organize your code. If you do not follow the example's style, you will lose 5% of your final project score. For example, if you final project's score is 90, because of missing prompt history, the score will drop to $90\times0.95=85.5$
   
   4. Performance (15%):
      
      1. I should be able to directly run your `inference.py` file in the terminal to use your model. For example:
         
         ```shell
         python inference.py --data /example/data1
         ```
      
      2. You need to report your learning curve through [Weights & Biases](https://wandb.ai/site). 
      
      3. Your model's performance should be evaluated by suitable metrics and achieve reasonable performance.
         
         1. The learning curve should show your model was learning, with no obvious overfitting or underfitting pattern.
         
         2. The model's test data does not have a leaking issue. 
   
   5. Poster (10%): We plan to have a department-wide poster presentation. The poster should cover the following parts:
      
      1. Introduction of the question
      2. Details of the deep learning model's design
      3. Results and analysis
      4. Conclusion and future work

4. **Participation**: If you have three unexcused absences. You will lose 5% of your final score. For example, your final score is 90, but you missed three class, then your final score is $90 \times 0.95 = 85.5$.  Check section **Attendance and Late Policy** for more details.

Your final score will be a weighted sum of all three parts. For example, Assignments: 89, exam: 80, and final project: 95, then the final score is $89 \times 0.3 + 80 \times 0.1 + 95 \times 0.6 = 91.7$.
Your final score will convert to a letter grade by following table:

| Score | Letter Grade |
| ----- | ------------ |
| >=93  | A            |
| 90~93 | A-           |
| 87~89 | B+           |
| 84~86 | B            |
| 80~83 | B-           |
| 77~79 | C+           |
| 74~76 | C            |
| 70~73 | C-           |
| 67~69 | D+           |
| 64~66 | D            |
| 60~63 | D-           |
| <60   | F            |

## Attendance and Late Work Policy

### Attendance

You are expected to attend every class. You may be excused only for college-sanctioned activities, and you must let me know about such absences as soon as you are notified. This includes missing class for religious, athletic, or academic conflicts. If you are sick or have an important appointment at the health or counseling center, please email me before the class and take care of yourself. If you will be absent for a significant period, please contact me to work out a way to catch up. If you must miss a class for a college-sanctioned activity, you must notify me prior to the class in question via email.

### Late Work

No late work will be accepted without prior permission. If you contact me at least one day before the due date (unless faced with an emergency) with appropriate requests for an extension and/or makeup assignments, you will be given additional time to make up late assignments equal to the time lost due to the unforeseen circumstance.

**Any unexcused late (within 24 hours) will result 10% of score deduction for the assignment. For example, your assignment's score is 89, because of the late, the score will drop to $ 89 \times 0.9 = 80.1$. If you submit your assignment late more than 24 hours, I will not accept it, the score will be 0.**

You cannot re-do assignments for a better score.

## Seeking Help

### Accommodations

If you believe you may need accommodation for a disability, contact me privately within the first two weeks (2024-10-09) of the semester to discuss your specific needs. If you have not already done so, please contact Allen Harrison, Assistant Dean of Students for International Students and Accessibility, at 315-859-4021, or via email at aharriso@hamilton.edu. He is responsible for determining reasonable and appropriate accommodations for students with disabilities on a case-by-case basis. 

### Mental Health and Wellness

If you are feeling isolated, depressed, sad, anxious, angry, or overwhelmed, you aren’t alone: we all struggle sometimes. Don’t stay silent! Talk to a trusted confidant: a friend, a family member, a professor you trust. The counseling center offers completely confidential and highly professional services and can be contacted at 315-859-4340. If this seems like a difficult step, contact me. We can talk and call or walk to the counseling center together.

## Learning topics

The course calendar is intended to be flexible enough to accommodate our class’s particular interests and needs while providing overall guidance and structure. The instructor may adjust topics/assignments as the course progresses. The instructor reserves the right to add or substitute additional readings if relevant materials become
available during the semester that illustrate key course concepts.

| Week                           | Learning topics                                                                                                                                 | Student activities                                                                                                                                                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2024-08-26 (Monday)<br>Week1   |                                                                                                                                                 |                                                                                                                                                                                                                                     |
| 2024-09-02 (Monday)<br>Week 2  | 1. Introduction<br>2. Linear algebra + calculus<br>3. Linear regression<br>4. Basic optimization                                                | Work on Assignment 0                                                                                                                                                                                                                |
| 2024-09-09 (Monday)<br>Week 3  | 1. Linear classification<br>2. loss function<br>3. softmax<br>4. MLP<br>5. activation function<br>6. Bais and variance trade-off, model fitting | Due: Assignment 0 (2024-09-09), bring assignment 0 to class                                                                                                                                                                         |
| 2024-09-16 (Monday)<br>Week 4  | 1. Weight decay<br>2. drop out<br>3. Stochastic Gradient Descent<br>4. Momentum, AdaGrad, Adam<br>5. Learning rate schedules                    | 1. Work on Assignment 1 (2024-09-16)<br>2. Start to work on final project's proposal                                                                                                                                                |
| 2024-09-23 (Monday)<br>Week 5  | 1. Initialization<br>2. Build our first model on House Prices data<br>3. Convolution layer/ Dilated Convolution layer                           | Due: Discuess final project proposal with me at any office hour this week.                                                                                                                                                          |
| 2024-09-30 (Monday)<br>Week 6  | 1. Polling layer <br>2. AlexNet<br>3. VGG<br>4. NiN<br>5. GoogleNet                                                                             | Due: Submit assignment 1 to gradescope before class (2:30 PM)<br>1. Start to work on data plan                                                                                                                                      |
| 2024-10-07 (Monday)<br>Week 7  | 1. Batch Normalization<br>2. More drop out<br>3. ResNet                                                                                         | Due: Submit final project proposal to gradescope before class (2:30 PM) <br>1. Discuses data plan with me at any office hour this week. <br>2. Work on Assignment 2 (2024-10-07)                                                    |
| 2024-10-14 (Monday)<br>Week 8  | 1. Build a CNN for image classification task<br>2. pytorch lightning<br>3. Weights & Biases                                                     | Midterm: 2024-10-16 (Wednesday),  7:00 PM - 8:30 PM                                                                                                                                                                                 |
| 2024-10-21 (Monday)<br>Week 9  | Guest Talk<br>1. Data augmentation<br>2. Fine tune                                                                                              | Due: Submit data collection report to gradescope before class (2:30 PM)<br>Due: Submit Assignment 2 to gradescope before 2024-10-23 2:30 PM<br>1. Start to work on model building and training<brbrork on Assignment 3 (2014-10-23) |
| 2024-10-28 (Monday)<br>Week 10 | Object Detection and Image Segmentation                                                                                                         |                                                                                                                                                                                                                                     |
| 2024-11-04 (Monday)<br>Week 11 | 1. Review probability<br>2. Word vector and embeddings<br>3. Sequential model                                                                   | Due: Discuss training details with me at any office hour this week.<br>Due: Submit Assignment 3 to gradescope before 2024-11-16 2:30 PM                                                                                             |
| 2024-11-11 (Monday)<br>Week 12 | 1. GRU<br>2. LSTM/bi-LSTM<br>3.Seq2seq                                                                                                          |                                                                                                                                                                                                                                     |
| 2024-11-18 (Monday)<br>Week 13 | 1. Word embedding<br>2. Attention, axial attention, channel attention                                                                           | Start to work on proposal                                                                                                                                                                                                           |
| Thanksgiving                   | No Class                                                                                                                                        |                                                                                                                                                                                                                                     |
| 2024-12-02 (Monday)<br>Week 15 | 1. self-attention<br>2. Transformer<br>3. ViT (vision transformer)<br>                                                                          | Due: Submit proposal to gradescope before  2024-12-04 2:30 PM                                                                                                                                                                       |
| 2024-12-09 (Monday)<br>Week 16 | Introduction to diffusion                                                                                                                       |                                                                                                                                                                                                                                     |
| 2024-12-13 (Friday)            |                                                                                                                                                 | Due: Submit project folder (includes all required codes, files, plots, etc.) to gradescope before 12:00 PM                                                                                                                          |
