import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess the data."""
    df = df.copy()
    
    # Example preprocessing: fill missing values and encode categorical variables
    df = df.fillna(method='ffill')
    df = pd.get_dummies(df, drop_first=True)
    df = df[["Avg Monthly Long Distance Charges", "Avg Monthly GB Download",
             "Population", "Churn Score"]]
    return df

def split_data(df, target_column, test_size=0.2, random_state=42):
    """Split the data into training and testing sets."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)