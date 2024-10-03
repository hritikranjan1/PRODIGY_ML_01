# Sale Price Prediction using Linear Regression

## Author
**Hritik Ranjan**

## Project Overview
This project implements a Linear Regression model to predict house sale prices based on various features such as living area, number of bathrooms, and bedrooms. The model is built using the scikit-learn library in Python.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Dataset](#dataset)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Evaluation Metrics](#evaluation-metrics)
- [Results](#results)
- [License](#license)
- [Contact](#contact)

## Introduction
Predicting house prices is a common problem in data science and machine learning. This project uses a Linear Regression model to analyze the relationship between several features of a house and its sale price, allowing for accurate predictions.

## Features
- Linear Regression implementation for price prediction.
- Visualization of key statistics of the dataset.
- Evaluation of model performance using Mean Squared Error and R-squared metrics.

## Installation
To run this project, ensure you have Python installed on your system. Follow the steps below to install the required libraries:

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/hritikranjan1/sale-price-prediction.git
   cd sale-price-prediction
2.Install the necessary libraries using pip:

    pip install pandas scikit-learn

## Dataset

The dataset used for this project is ranjan.csv. It contains various features related to houses, including:

  GrLivArea: Above grade (ground) living area square feet
    BsmtFullBath: Full bathrooms in basement
    BsmtHalfBath: Half bathrooms in basement
    BedroomAbvGr: Bedrooms above grade
    FullBath: Full bathrooms above grade
    HalfBath: Half bathrooms above grade
    SalePrice: Sale price of the house (target variable)

Make sure to place the ranjan.csv file in the same directory as your script or update the path accordingly.

## Usage

Follow these steps to run the model:

  1.Update the file path in the script to point to your dataset:

    python

    dataFrame = pd.read_csv("/path/to/your/ranjan.csv")  # Change this to your actual file path

2Run the script:

bash

    python sale_price_prediction.py

View the results in the console. The Mean Squared Error and R-squared values will be printed.

 ##  Libraries:
    pandas: Used for data manipulation and analysis.
    scikit-learn: Used for building the Linear Regression model and evaluating its performance.

##  Functions:
         train_test_split(): Splits the dataset into training and testing sets.
        LinearRegression(): Initializes the Linear Regression model.
        mean_squared_error(): Calculates the mean squared error for model evaluation.
        r2_score(): Computes the coefficient of determination (R-squared) for model evaluation.

Evaluation Metrics

   Mean Squared Error (MSE): Measures the average squared difference between predicted and actual values. A lower value indicates a better fit.
    Coefficient of Determination (R-squared): Indicates the proportion of the variance in the dependent variable that is predictable from the independent variables. Values closer to 1 indicate a better fit.

Results

    After running the script, you will see the following outputs in the console:

    Summary statistics of the SalePrice column.
    Mean squared error and R-squared value of the model.
  Example Output:

    Mean squared error: 1234567.89
    Coefficient of determination (R-squared): 0.76
    Name: Hritik ranjan
    GitHub: https://github.com/hritikranjan1
    LinkedIn: https://www.linkedin.com/in/hritikranjan

Contact

    Name: Hritik ranjan
    GitHub: https://github.com/hritikranjan1
    LinkedIn: https://www.linkedin.com/in/hritikranjan
