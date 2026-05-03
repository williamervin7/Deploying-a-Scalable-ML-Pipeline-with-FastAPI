import pytest
import pandas as pd
import os
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

# Fixture to load data for testing
@pytest.fixture
def data():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    return pd.read_csv(data_path)

# 1. Test Data Processing (Check types and shapes)
def test_process_data(data):
    """
    Check if process_data returns the expected types and non-empty arrays
    """
    cat_features = ["workclass", "education", "marital-status", "occupation", 
                    "relationship", "race", "sex", "native-country"]
    
    X, y, encoder, lb = process_data(
        data, 
        categorical_features=cat_features, 
        label="salary", 
        training=True
    )
    
    assert X.shape[0] > 0
    assert X.shape[1] > 0
    assert len(y) == X.shape[0]
    # Check that it returned the expected objects
    assert encoder is not None
    assert lb is not None

# 2. Test Model Training (Check algorithm type)
def test_train_model(data):
    """
    Verify that the train_model function returns the expected model type
    """
    cat_features = ["workclass", "education", "marital-status", "occupation", 
                    "relationship", "race", "sex", "native-country"]
    
    # Take a small slice for speed
    X, y, _, _ = process_data(
        data.iloc[:100], 
        categorical_features=cat_features, 
        label="salary", 
        training=True
    )
    
    model = train_model(X, y)
    
    # Check if the model has a 'predict' method (standard for sklearn models)
    assert hasattr(model, "predict")

# 3. Test Metrics (Check value ranges)
def test_compute_model_metrics():
    """
    Check if the metrics function returns values within valid ranges (0 to 1)
    """
    import numpy as np
    y_true = np.array([0, 1, 0, 1])
    y_preds = np.array([0, 1, 1, 1])
    
    precision, recall, fbeta = compute_model_metrics(y_true, y_preds)
    
    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
    assert 0.0 <= fbeta <= 1.0