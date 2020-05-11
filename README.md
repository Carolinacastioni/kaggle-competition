# kaggle-competition


### Introduction

The goal of this competition is the prediction of the price of diamonds based on their characteristics (weight, color, quality of cut, etc.), putting into practice all the machine learning techniques that we learned on this week.

### Prepare Data

Clean and prepare the data in order to get the best prediction:
- Check the correlation between the columns.
- Drop correlated columns and maintain just one.
- Check and remove outliers.
- Make all columns numerical. 
- Apply all the steps in both datasets: diamonds_train and diamonds_test.

### H2O - Get top models

Use the H2O library to train the dataset and find out the more accure model to do the price prediction. 

Ps. I couldn't run the function in Jupyter due to the limitation of my computer, so I did it in a cloud programm: Colab.

Result:

- GradientBoosting

### Test Model

- Train choosen model in the dataset and apply on the dataset d_test.  
- Evalute the accuracy in order to get the best parameters.
- Convert the result into CSV and submit in the webpage: https://www.kaggle.com/c/diamonds-datamad0320