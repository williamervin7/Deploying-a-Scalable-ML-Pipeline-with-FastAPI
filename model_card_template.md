# Model Card

## Model Details
It is a Random Forest Classifier designed to perform binary classification on census data. The primary objective of this model is to predict whether a person's annual income exceeds $50,000 based on various demographic and professional attributes provided in the 1994 Census database. This project was built to demonstrate the integration of a machine learning pipeline within a DevOps framework, utilizing FastAPI for deployment and GitHub Actions for continuous integration.

## Intended Use
The primary intended use of this model is for educational and demonstrative purposes within the Udacity ML DevOps Nanodegree program. It serves as a functional example of how to automate model training, evaluation, and API deployment. The intended users are machine learning practitioners and reviewers evaluating the pipeline's infrastructure. This model is not intended for real-world applications such as automated hiring, credit scoring, or financial forecasting, as the training data is several decades old and contains historical biases.

## Training Data
The model was trained using the Census Income Dataset, commonly referred to as the Adult Dataset, sourced from the UCI Machine Learning Repository. The dataset contains approximately 32,561 records. For this implementation, a random 80% split of the data was utilized for the training phase. Pre-processing involved cleaning the data and applying a One Hot Encoder to categorical features, while the target label ("salary") was processed using a Label Binarizer to convert it into a machine-readable format.

## Evaluation Data
Evaluation was performed on a hold-out test set consisting of the remaining 20% of the original census data. To maintain the integrity of the evaluation, the test features were transformed using the same encoder and label binarizer objects that were fitted on the training set, ensuring that no data leakage occurred during the evaluation process.

## Metrics
The model's performance was evaluated using three primary metrics: Precision, Recall, and the F1-Score. Precision measures the accuracy of the positive predictions, while Recall measures the ability of the model to identify all actual positive cases. The F1-Score provides a harmonic mean of these two values. 

Based on the final test run, the model achieved the following performance:
* **Precision:** 0.7353 
* **Recall:** 0.6378 
* **F1-Score:** 0.6831

## Ethical Considerations
Given that the dataset contains sensitive demographic information including race, gender, and national origin, ethical implications were a primary focus during development. To address potential bias, the pipeline includes a model slicing analysis. This analysis evaluates model performance across specific categorical groups to ensure that the model does not disproportionately misclassify specific segments of the population. Users should be aware that historical data often reflects societal biases present at the time of collection.

## Caveats and Recommendations
The most significant caveat is that the data was collected in 1994, meaning it does not reflect modern inflation, the current job market, or contemporary social dynamics. Consequently, the model should be considered a "proof of concept" rather than a reliable predictive tool for current salaries. For future improvements, it is recommended to implement hyperparameter tuning and explore more modern datasets to improve the model's relevance and predictive power.