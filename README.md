# 2024 Fall CPSCI-307

This is the home page for Hamilton College CPSCI-307: Deep Learning. Be sure to ***READ THIS PAGE CAREFULLY!!!***

## Lecture Details

**Lecture time**: Monday and Wednesday 2:30 PM - 3:45 PM at Christian A. Johnson Hall (CJ) 305.

**Office Hours**: Monday and Wednesday 1:15 PM - 2:15 PM, Tuesday 10:00 AM - 11:00 AM, Thursday 10:00 AM - 12:00 PM or by appointment via email. You can meet me at my office (SCCT 2016) or via Zoom if needed. I encourage you to come to office hours if you have any questions or need help with your assignments, projects, or exam.

**Email**: schen3@hamilton.edu
I usually respond to emails within 24 hours. 

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

### Important Date and Schedules

| Date                   | Due                                                                                                                                                                                                                          | Note                                                                                                                                                                                 |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2024-09-02 (Monday)    |                                                                                                                                                                                                                              | Release Assignment 0                                                                                                                                                                 |
| 2024-09-09 (Monday)    | Assignment 0                                                                                                                                                                                                                 |                                                                                                                                                                                      |
| 2024-09-16 (Monday)    |                                                                                                                                                                                                                              | 1. Release Assignment 1<br/>2. Start to work on proposal                                                                                                                             |
| 2024-09-23 (Monday)    |                                                                                                                                                                                                                              | Email proposal to me before class (2:30 pm)                                                                                                                                          |
| 2024-09-27 (Friday)    | Discuss proposal with me at any office hour this week. If you don't share your proposal with me before Friday noon, points will be reduced. This week I have an extra office hour on Friday 11:00 AM - noon.                 |                                                                                                                                                                                      |
| 2024-09-30 (Monday)    | Assignment 1                                                                                                                                                                                                                 | 1. Push assignment 1 to git before class (2:30 pm) <br/>2. It's time to think about data plan                                                                                        |
| 2024-10-07 (Monday)    | Proposal due                                                                                                                                                                                                                 | Release Assignment 2                                                                                                                                                                 |
| 2024-10-11 (Friday)    | Discuss data plan with me at any office hour this week. If you don't share your data plan with me before Friday noon, points will be reduced. This week I have an extra office hour on Friday 11:00 AM - noon.               |                                                                                                                                                                                      |
| 2024-10-16 (Wednesday) | In-class exam (75 mins)                                                                                                                                                                                                      |                                                                                                                                                                                      |
| 2024-10-21 (Monday)    | Data collection report due                                                                                                                                                                                                   | 1. You do not need to have all data ready, but you should have a solid plan and some data at this time point. <br/>2. Email your data collection report to me before class (2:30 pm) |
| 2024-10-23 (Wednesday) | Assignment 2                                                                                                                                                                                                                 | 1. Push assignment 2 to git repo before class (2:30 pm) <br/>2. Release Assignment 3                                                                                                 |
| 2024-11-04 (Monday)    |                                                                                                                                                                                                                              | Discuss your model building details with me at office hour                                                                                                                           |
| 2024-11-06 (Wednesday) | Assignment 3                                                                                                                                                                                                                 | Push assignment 3 to git repo before class (2:30pm)                                                                                                                                  |
| 2024-11-22 (Friday)    | Discuss training details with me at any office hour this week. If you don't share your training details with me before Friday noon, points will be reduced. This week I have an extra office hour on Friday 11:00 AM - noon. |                                                                                                                                                                                      |
| 2024-12-04 (Wednesday) | Poster Due                                                                                                                                                                                                                   | I will provide you feedback. So you still have one week to refine it.                                                                                                                |
| TBD                    | Poster presentation                                                                                                                                                                                                          |                                                                                                                                                                                      |
| 2024-12-13             | Push project folder (includes all required codes, files, plots) to git repo before 12:00 PM                                                                                                                                  |                                                                                                                                                                                      |

Here is the detailed class [schedule](https://docs.google.com/spreadsheets/d/1zrNzYpYoMB3QBeflDs98WeM7FcPjadZg7CCuY6cjhQg/edit?usp=sharing) and plan. The table will keep updating.

## Prerequisites

1. This class heavily relies on Python. You should be comfortable using Python for programming or be familiar with other programming languages and able to learn and use Python quickly.
2. Basic linear algebra background (vector, matrix, matrix operations, etc.) is required.

## Course Materials

### Textbook

We will use [Dive into Deep Learning](https://d2l.ai/) as our textbook. Additionally, some classic machine/deep learning papers will be included in the reading list.

The following two books are also worth reading if you want to explore more about the math behind machine/deep learning, but they are not required for this class:

1. [Deep Learning](https://www.deeplearningbook.org/)
2. [The Elements of Statistical Learning (ESL)](https://hastie.su.domains/ElemStatLearn/)

### Environment Setup

We will use [PyTorch](https://pytorch.org/get-started/locally/) (version: Stable 2.3.1) for all assignments and projects. This class requires a GPU for deep learning model training. You need to prepare your own GPU for the class. Usually, an NVIDIA GPU is the default for training. However, you can also choose AMD or Apple M chips for training, although they may bring some unexpected errors that you will need to debug yourself.

If you do not have a GPU, some online platforms can be considered. Here are some GPU notebook options:

1. Google Colab
2. Amazon SageMaker
3. Kaggle GPU

All these products provide different plans to choose from based on how complex a model you want to work with. In this class, we will use **Google Colab** for demonstration. Feel free to choose other online products if you think they fit you better, but you need to figure out the settings and environments by yourself.

You will need a GPU starting at Assignment 2.

### Fee

Colab provides free GPU resources (with very limited GPU hours), but you also can pay for more resources. You can sign up for a paid account at [Google Colab](https://colab.research.google.com/signup). 

If you have any financial difficulties in purchasing GPU services, **TALK TO THE DEPARTMENT or ME**. We are ready to help!

### Laptops and Electronics

You should bring a laptop to lectures as we will live code in every class. If you are unable to do this, let me know. You should not use a phone or any similar device during lectures. If you take notes on a tablet, then you should not be typing on it during class, but only writing (e.g. with a stylus) unless you require accommodation for a disability. Tablets should be kept flat on the desk and should not be propped up unless you require accommodation for a disability. If you would like to discuss this restriction, you are always welcome to come talk to me about it.

During most lectures, we will have mini labs (live coding). **You can only use your laptop  for coding at mini lab time. You can't use the computer for anything unrelated to the course content. For example, I found twice that if you use the computer for something unrelated (facebook, youtube, game,...) to the course, you will lose 5% of your final grade.**

If your final score is 90, because of using laptop for unrelated to the course content twice. Your score will drop to $90 \times 0.95 =85.5$.

## Academic Integrity & Collaboration

You should work on all assignments by yourself. You can discuss your assignments with me, your classmates, your friends, or other professors, but you are **NOT** allowed to use others' code or any code from the internet.

You can work on the final project on your own or team up with up to 3 students. If you choose to work in a team, your team must report each member's contribution in the final report. I encourage all team members to join the entire project pipeline as much as possible, instead of each team member only being in charge of one part of the project. Here is an [example](https://github.com/XiaoChen1992/CPSCI-307/blob/main/project_example/contrbution.md). You should include this file in your own project, otherwise, each team member will lose 5% of project score. For example,

### AI Policy

### Assignments

You are **NOT** allowed to use any generative AI tools (online or offline) for your assignments. Any code from generative AI tools (online or offline) will be considered cheating.

### Final Project

You are **ENCOURAGED** to use AI tools for your final project, but you **NEED** to provide your prompt history to me, **otherwise you will lose 5%** of your final project score. Here is a prompt history [example](https://github.com/XiaoChen1992/CPSCI-307/blob/main/project_example/prompt_history_example.pdf).

**THIS POLICY APPLIES ONLY TO THIS CLASS!!!** For other classes, follow the academic integrity policy of that class or ask your professor.

## Grading

Your grade will be comprised of the following weighted components:

1. **Assignments (30%)**: We will have 3 assignments, with **two** weeks for each assignment. Each assignment contributes 10% of your final grade.

2. **Midterms (10%)**: We will only have one in-class exam (no notes) before Thanksgiving. The exam's goal is to ensure you understand the basic concepts of machine/deep learning.

3. **Project (60%)**: The final project covers:
   
   1. Proposal (10%): Explain your plan for the final project, up to 2 pages  
   
   2. Data (10%): You should report how you collected your own data for the final project. Include the following parts: a. Where is the data source? b. How did you collect the data? c. How did you preprocess the data? The report is up to 1 pages.
   
   3. Code (15%): You need to push your project's code to the class's GitHub repo. Your code should be well-organized and easy to read. Check this [example](https://github.com/XiaoChen1992/CPSCI-307/tree/main/project_example) to organize your code.
   
   4. Performance (15%):
      
      1. I should be able to directly run your `inference.py` file in the terminal to use your model. For example:
         
         ```shell
         python inference.py --data /example/data1
         ```
      
      2. You need to report your learning curve through [Weights & Biases](https://wandb.ai/site). We will learn how to use this tool in class.
      
      3. Your model's performance should be evaluated by suitable metrics and achieve reasonable performance.
         
         1. The learning curve should show your model was learning, with no obvious overfitting or underfitting pattern.
         
         2. The model's performnace is in a reasonable level.
         
         3. The model's test data does not have a leaking issue. 
   
   5. Poster (10%): We plan to have a department-wide poster session. The poster should cover the following parts:
      
      1. Introduction of the question
      2. Details of the deep learning model's design
      3. Results and analysis
      4. Conclusion and future work

4. **Participation**: If you have three unexcused absences. You will lose 5% of your final grade. For example, your final score is 90, but you missed three class, then your final score is $90 \times 0.95 = 85.5$.  Check section **Attendance and Late Policy** for more details.

Your final score will be a weighted sum of all three parts. For example, Assignments: 89, exam: 80, and project: 95, then the final score is $89 \times 0.3 + 80 \times 0.1 + 95 \times 0.6 = 91.7$.
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

## Attendance and Late Policy

You are expected to attend every class. You may be excused only for college-sanctioned activities, and you must let me know about such absences as soon as you are notified. This includes missing class for religious, athletic, or academic conflicts. If you are sick or have an important appointment at the health or counseling center, please email me before the class and take care of yourself. If you will be absent for a significant period, please contact me to work out a way to catch up. If you must miss a class for a college-sanctioned activity, you must notify me prior to the class in question via email.

No late work will be accepted without prior permission. If you contact me at least one day before the due date (unless faced with an emergency) with appropriate requests for an extension and/or makeup assignments, you will be given additional time to make up late assignments equal to the time lost due to the unforeseen circumstance.

**Any unexcused late (within 24 hours) will result 10% of score deduction for the assignment. For example, your raw assignment's score is 89, because of the late, the score will drop to $ 89 \times 0.9 = 80.1$. If you submit your assignment late more than 24 hours, I will not accept it, the score will be 0.**

## Seeking Help

### Accommodations

If you believe you may need accommodation for a disability, contact me privately within the first two weeks of the semester to discuss your specific needs. If you have not already done so, please contact Allen Harrison, Assistant Dean of Students for International Students and Accessibility, at 315-859-4021, or via email at aharriso@hamilton.edu. He is responsible for determining reasonable and appropriate accommodations for students with disabilities on a case-by-case basis. 

***Let me know if you need any kind of accommodations via email before 2024-09-06 (Friday).***

### Mental Health and Wellness

If you are feeling isolated, depressed, sad, anxious, angry, or overwhelmed, you aren’t alone: we all struggle sometimes. Don’t stay silent! Talk to a trusted confidant: a friend, a family member, a professor you trust. The counseling center offers completely confidential and highly professional services and can be contacted at 315-859-4340. If this seems like a difficult step, contact me. We can talk and call or walk to the counseling center together.
