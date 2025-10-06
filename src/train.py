import joblib
from sklearn import datasets, ensemble
from sklearn.metrics import accuracy_score
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.utils.fixes import parse_version
from data import load_data, preprocess_data, split_data

def train():
    # Load and preprocess the data
    df = load_data('data/train.csv')
    df = preprocess_data(df)
    
    # Split the data
    X_train, X_test, y_train, y_test = split_data(df, target_column='Churn Score')
    
    # Initialize and train the model
    params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
    }
    
    model = ensemble.GradientBoostingRegressor(**params)
    model.fit(X_train, y_train)

    mse = mean_squared_error(y_test, model.predict(X_test))
    print("The mean squared error (MSE) on test set: {:.4f}".format(mse))

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = mean_squared_error(y_test, y_pred)
    print(f'Accuracy: {accuracy:.4f}')
    
    # Save the trained model
    joblib.dump(model, 'models/model.pkl')

if __name__ == '__main__':
    train()
    