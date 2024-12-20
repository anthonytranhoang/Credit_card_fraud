# Project Description ( Group 4 )

# Fraud Detection in Financial Transactions Using Machine Learning
![images](https://github.com/user-attachments/assets/896def5a-0056-4ada-9592-87c54612d7a2)


The main aim of the project is to develop a machine learning model for detecting fraudulent transactions in financial datasets. This model will enhance security, improve detection accuracy, and enable real-time assessments to protect against fraud. Ultimately, the project seeks to build trust in financial systems by ensuring robust fraud detection measures.


# Objectives:

Finance Fraud Detection
This project aims to develop a machine learning model to detect fraudulent financial transactions using algorithms like XGBoost and RandomForest. It deals with class imbalance through techniques such as SMOTE and undersampling, and is deployed as a web application using Flask for real-time predictions.

# Project Overview

The main goal is to create a robust machine learning model and web-based interface to securely and accurately identify fraudulent transactions in real time. This tool, integrated into a bank’s decision-making system, plays a pivotal role in fraud risk assessment, thereby enhancing customer trust in financial systems.

# Project Structure
Finance_Fraud_Detection.ipynb: Jupyter Notebook for data analysis, preprocessing, model training, and evaluation.

model.onnx: ONNX format of the trained RandomForestClassifier model for deployment.

scaler.pkl: Saved StandardScaler object for feature standardization.

app.py: Flask application file for serving the model predictions via a web interface.

templates/: Contains HTML files (index.html, prediction_app.html, and result.html) for the web interface.

static/: Static files needed for the web interface (e.g., images, CSS).

requirements.txt: Specifies all the dependencies and packages required for the project.


# Database

The project's data is stored in a PostgreSQL database hosted on AWS. The connection details are as follows:

Host: database-1.cxu0eg8y6y4k.ap-southeast-2.rds.amazonaws.com

Database: Finance_db

User: postgres

Password: Radin5286

Port: 5432

Installation and Usage

# Requirements

Python 3.7 or higher

Libraries: pandas, numpy, matplotlib, seaborn, psycopg2, scikit-learn, xgboost, imblearn, joblib, skl2onnx, onnx, onnxruntime, pickle, Flask

# Installation

Clone the repository:
git clone <repository_url>  
Install necessary libraries:
pip install -r requirements.txt  
Running the Jupyter Notebook
Connect to the AWS Database:
Ensure you have internet access and update the connection string in Finance_Fraud_Detection.ipynb to connect to the AWS-hosted PostgreSQL database using the provided credentials.

# Execute the Notebook:

Open Finance_Fraud_Detection.ipynb in Jupyter Notebook or JupyterLab and execute cells sequentially to perform:

Data loading from the AWS database.
Data preprocessing and feature engineering.
Model training using machine learning algorithms.
Hyperparameter tuning and model evaluation.
Export the trained model to ONNX format and save the scaler.

# Output Files:

After running the notebook, the trained model (model.onnx) and scaler (scaler.pkl) will be produced for later use in the Flask application.

# Setting Up the Flask Application

We've saved a machine learning model in ONNX format as model.onnx and a fitted scaler as scaler.pkl using Python. The sklearn-onnx library was used to convert the model to ONNX format, ensuring compatibility with various platforms, while pickle was used to serialize the scaler for consistent data preprocessing. Error handling is included to manage any issues during the conversion and saving processes. Adjust the input dimensions as needed and execute the script to effectively preserve your model and scaler for future use.

# Run the Flask App:
Navigate to the repository's main directory containing app.py and execute:

python app.py  
This starts the Flask server, usually accessible at http://127.0.0.1:5000/.

Access the Web Interface:
To use the prediction form, open a web browser and go to http://127.0.0.1:5000/.

Submit Predictions:
Fill in the transaction details in the form and receive fraud predictions instantly.
![ui1_720](https://github.com/user-attachments/assets/6bb37bc4-6cda-4b27-a7f2-425af986c776)
![ui2_720](https://github.com/user-attachments/assets/8fc94e70-98b0-4c8d-9593-7b28615f219f)
![UI3](https://github.com/user-attachments/assets/565e0250-6faa-49a2-a43c-5a34a706f288)




# Features

Home Page: Introduction to the fraud detection tool.
Prediction Form: Fields for inputting transaction attributes and submission for prediction.
Prediction Result: Displays whether the transaction is "Fraud" or "Not Fraud".
Key Steps
Data Preprocessing: Address missing values, outliers, and standardize data for model input.
Feature Engineering: Analyze feature importance, create new features, and apply dimensionality reduction.
Model Building: Train and optimize models using algorithms like Logistic Regression, Decision Trees, Random Forest, and XGBoost.
Deployment: Deploy via Flask for immediate fraud prediction capability.
Evaluation
Evaluates models with metrics such as accuracy, precision, recall, and F1-score. Ensure robustness with cross-validation.

# Technologies Used

Frontend: HTML, CSS
Backend: Flask
Data Processing: Python (Pandas, NumPy)
Modeling: Scikit-Learn, XGBoost, ONNX Runtime


# Expected Deliverables:

A trained and evaluated machine learning model capable of detecting fraudulent transactions.
A Flask API that can host the model and process real-time fraud detection requests.
A detailed report documenting model performance and how it can be integrated into the bank’s decision-making process.
GitHub repository containing the code for the entire project, including data preprocessing, model training, and API development.

# License:

Our project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA) license. This allows others to share, copy, and redistribute the material in any medium or format. They are also free to remix, transform, and build upon the material, as long as they follow the license terms.
Under this license, appropriate credit must be given, with a link to the license, and any changes must be indicated. The material cannot be used for commercial purposes. Additionally, if others create derivative works, they must distribute them under the same license. No extra legal restrictions or technological measures that limit these permissions are allowed.
Read more about the license on the link below:
https://creativecommons.org/licenses/by-nc-sa/4.0/

# Models overview

In this project, we developed and optimized a machine learning model to detect fraud in financial transactions. Our approach consisted of two main phases:

#### Model Optimization (Trial Models)
In the initial phase, we explored different machine learning models to assess their suitability for the task. We experimented with both XGBoost and Random Forest classifiers to identify the model that best balanced accuracy and performance. During these trials, we focused on key steps such as data loading, preprocessing, training, and evaluating each model based on accuracy and classification reports. This phase served as a testing ground to fine-tune hyperparameters and optimize model configurations collaboratively.

#### Final Model
Why We Chose This Model ?

We selected the RandomForest model because it effectively handles complex datasets and is robust against overfitting. Additionally, it provides insights into feature importance, which is valuable for understanding the contributing factors of fraud. The model also supports balanced class weights, allowing us to address the class imbalance between fraud and non-fraud cases.

Steps We Took :

First, we checked the distribution of instances in each class (fraud and non-fraud) to understand the extent of the imbalance. To address this, we applied undersampling by randomly reducing the number of non-fraud cases (the majority class) to match the number of fraud cases (the minority class). Next, we performed feature engineering by using one-hot encoding for categorical variables and selecting the most relevant features for our analysis. We then applied StandardScaler to normalize the feature values, ensuring that they were on a consistent scale for better model training. Finally, we trained the RandomForest model with balanced class weights to further handle any remaining class imbalances.

# Conclusion

In this project, we built a machine learning model to detect fraudulent financial transactions. We tested different models, like RandomForest and XGBoost, and used techniques such as undersampling and SMOTE to handle the imbalance between fraud and non-fraud cases. After comparing results, we chose the RandomForest model because it performed well and provided helpful insights into important features.

The project also included a Flask web app that makes real-time predictions, making it easy to use and integrate into financial systems. Our solution helps banks quickly identify suspicious transactions, reducing risks and improving security. This work shows how machine learning can strengthen trust in financial systems and provide reliable tools for fraud detection.






