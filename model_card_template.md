# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
* **Author:** William  Ervin 
* **Date:** May 2026
* **Model Version:** 1.0.0
* **Model Type:** Random Forest Classifier
* **Description:** This model predicts whether an individual's annual income exceeds $50,000 based on census data. It was developed as part of a machine learning pipeline project to demonstrate DevOps principles including CI/CD and automated testing.

## Intended Use
* **Primary Intended Uses:** This model is intended for educational purposes as part of the Udacity ML DevOps Nanodegree. It serves as a demonstration of deploying a machine learning API using FastAPI.
* **Primary Intended Users:** Students, reviewers, and machine learning engineers interested in ML infrastructure.
* **Out-of-scope Use Cases:** This model should not be used for actual financial auditing, hiring decisions, or credit scoring. The data is historical and does not reflect current economic conditions.

## Training Data
* **Dataset:** Census Income Dataset (Adult Dataset).
* **Source:** UCI Machine Learning Repository.
* **Size:** 80% of the original census.csv file was used for training.
* **Pre-processing:** Categorical features were encoded using a One Hot Encoder, and labels were binarized. The processing steps are automated via the `process_data` function in the pipeline.

## Evaluation Data
* **Dataset:** 20% hold-out set from the census.csv file.
* **Pre-processing:** Evaluation data was transformed using the encoder and label binarizer fitted during the training phase to ensure feature parity.

## Metrics
*Performance metrics based on the test split:*
* **Precision:** 0.7353 
* **Recall:** 0.6378 
* **F1-Score:** 0.6831

## Ethical Considerations
* **Bias Awareness:** The model trained on data containing sensitive attributes such as race, sex, and native country. 
* **Mitigation:** Performance was evaluated across categorical slices to identify potential performance disparities among different demographic groups. This transparency allows for a better understanding of how the model treats different segments of the population.

## Caveats and Recommendations
* **Temporal Bias:** The data was collected in 1994. Factors like inflation, changes in the labor market, and shifting social norms mean this model is not applicable to modern salary prediction.
* **Future Work:** Recommendations include hyperparameter optimization (e.g., GridSearch) and investigating data augmentation techniques to balance classes if specific slices show significant underperformance.