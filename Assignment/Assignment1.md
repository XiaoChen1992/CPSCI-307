# Assignment 1: House Prices Prediction using Deep MLP

**Due Date:** September 30, 2024, at 2:30 PM

For this assignment, you will build a deep Multi-Layer Perceptron (MLP) model to predict house prices. The assignment is based on the Kaggle dataset **"House Prices: Advanced Regression Techniques"**, which contains 79 explanatory variables describing various attributes of residential homes in Ames, Iowa. The target variable is the sale price of the house.

The assignment consists of two parts:

1. **First Stage Model:** Build your own deep MLP model using the PyTorch library without copying code from others or the internet. You can use google to debug and check PyTorch documentation.
2. **Second Stage Model:** Explore Kaggle kernels or other public code to see how others have built their deep MLP models for house price prediction. Incorporate at least two techniques from others to improve your own model. Note that some public solutions are machine learning-based, and some are deep learning-based; therefore, some techniques may not directly apply to your deep learning model.

---

## Data

You can download the dataset from Kaggle at: [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). To download the data, you need to sign up for a Kaggle account and join the competition.

After downloading and extracting the `.zip` file, you will find:

- **`train.csv`** - The training set.
- **`test.csv`** - The test set.
- **`data_description.txt`** - Full description of each column, originally prepared by Dean De Cock but lightly edited to match the column names used here.
- **`sample_submission.csv`** - A benchmark submission from a linear regression on year and month of sale, lot square footage, and number of bedrooms.

**Important:** You are only allowed to use `train.csv` to build your training and validation sets. Use `test.csv` solely to evaluate your model's performance on the test set.

An example code demonstrating how to build a custom dataset in PyTorch is provided here: [[create_dataset.py](https://github.com/XiaoChen1992/CPSCI-307/blob/main/notebooks/create_dataset.py)](https://github.com/XiaoChen1992/CPSCI-307/blob/main/notebooks/create_dateset.py). Use this code as a reference to build your dataset for house price prediction. If you have any questions, feel free to ask.

---

## First Stage Model

In this stage, you need to use the concepts learned in class to build a deep MLP model for house price prediction. After training your model, you should test it on the test set and report its performance.

### Requirements:

1. **Model Design:** Describe how you designed your model. Include details such as:
   - Types of layers used.
   - Number of layers.
   - Activation functions.
   - Any other relevant architectural choices.
2. **Learning Curve:** Provide a plot showing the training and validation loss over epochs. Use different colors to distinguish between training and validation loss.
3. **Performance Metrics:** Report the Mean Squared Error (MSE) and Mean Absolute Error (MAE) on the test set.

### Submission:

- **Report:** Compile your answers to requirements 1–3 into a PDF document named `yourname_stage_1.pdf`.
- **Code:** Organize your code following this example: [Project Example](https://github.com/XiaoChen1992/CPSCI-307/tree/main/project_example). You do not need to include `contribution.md` and `prompt_history_example.pdf`, as this is a personal project and you are not allowed to use any AI language models. Note that, I should directly run your infernce_stage_1.py as follows:


```shell
python inference_stage_1.py --test_path path/to/test.csv
```
---

## Second Stage Model

In this stage, you are encouraged to use techniques from others to improve your model. You can find other people's code at the [Kaggle competition code page](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/code). Select at least **two techniques** from these resources and attempt to incorporate them into your model. Actual improvement is not mandatory; the objective is to experiment with and report on these techniques.

### Requirements:

1. **Techniques Used:** Describe the techniques you selected and cite their sources.
2. **Improvement Analysis:** Discuss whether you achieved any improvement in your model's performance. If yes, quantify the improvement.
3. **Evaluation:** Explain why you think these techniques worked or did not work for house price prediction.
4. **Learning Curve:** Provide a plot showing the training and validation loss over epochs, similar to the first stage.
5. **Performance Metrics:** Report the MSE and MAE on the test set.

### Submission:

- **Report:** Compile your answers to requirements 1–5 into a PDF document named `yourname_stage_2.pdf`.
- **Code:** You do not need to create a new folder. Instead, provide code files with different names, such as `stage_1_train.py` and `stage_2_train.py`.

---

## Submission Details

- **Due Date:** September 30, 2024, at 2:30 PM.
- **Submission Platform:** Submit your code and reports via Gradescope.

---

**Note:** Ensure that your code is well-documented and follows good coding practices. Remember, plagiarism is strictly prohibited. Any form of code copying without proper citation will result in severe penalties.

If you have any questions or need clarification on the assignment, please feel free to reach out.

Good luck!
