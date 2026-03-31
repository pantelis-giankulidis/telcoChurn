# Telco churn
A simple implementation of a linear regressor predicting the probability that a certain user will leave a telecommunication company.
The dataset that is used for training, validation and testing come from the popular telcoChurn dataset in kaggle https://www.kaggle.com/datasets/blastchar/telco-customer-churn.


### Run in docker
You can run the project with its predfined pickle file, in a docker container, by building an image with the docker file in the root directory and run the image in docker. \
For example:
`docker build -t telco-churn` and 
`docker run -p 8080:8080 telco-churn`

### Run with poetry
With poetry installed in your machine, navigate to the root directory and run \
`poetry install` in order to install, in a poetry virtual environment, the project dependencies. Keep in mind that there are certain requirements that you machine must meet, for different dependencies, otherwise your build will fail. \
 After installation, you must first train the model with
`poetry run python src/train.py` \
This will generate a .pkl file inside /models folder. This is the 'brain' for the fast API endpoints. Note that there is an existing pickle in the project. Feel free to train the model with your hyperparameters. \
Finally, run `poetry run python src.app.py` so that a fast API server runs locally.

### Use cases
There are two endpoints that you can call with the project running: a GET `/health` request and a POST `/predict` request. 

The first endpoint is just a heartbeat check that the application runs correctly.  

The second API endpoint, takes in the body request, a python dictionary representing the features of a customer that we want to predict if it will churn. It returns a JSON with the probability of churn and the final prediction for the specific user. Note that the key names in the JSON object in the body of the request, must much the data where the model has been trained (see inside data folder). For example, a valid body is 
``` 
{ 
    "Age": 33,
    "Monthly GB Download": 9.88,
    "Avg Monthly Long Distance Charges": 47.72,
    "City": "Chicago"
} 
```
If the keys in the JSON are not headers in the .cdv files , that had been used for training, or the data type is not correct (string instead of int) the program will throw an exception.
