from flask import Flask, render_template, request  # Flask for web app  
import numpy as np  # NumPy for math  
import onnxruntime as rt  # ONNX Runtime for models  
import pickle  # Pickle to load objects  
import logging  # Logging for error tracking  

# Initialize Flask app  
app = Flask(__name__)  

logging.basicConfig(level=logging.INFO)  

# Load the ONNX model  
session = rt.InferenceSession("model/model.onnx")  

# Load the scaler  
with open('model/scaler.pkl', 'rb') as f:  
    scaler = pickle.load(f)  

@app.route('/')  
def home():  
    return render_template('index.html')  

@app.route('/prediction')  
def prediction():  
    return render_template('prediction_app.html')  

@app.route('/predict', methods=['POST'])  
def predict():  
    try:  
        # Collect input data from the form  
        input_features = [  
            float(request.form.get('current_address_months_count')),  
            float(request.form.get('credit_risk_score')),  
            float(request.form.get('device_os_windows')),  
            float(request.form.get('name_email_similarity')),  
            float(request.form.get('intended_balcon_amount')),  
            float(request.form.get('income')),  
            float(request.form.get('days_since_request')),  
            float(request.form.get('session_length_in_minutes')),  
            float(request.form.get('velocity_24h')),  
            float(request.form.get('velocity_6h')),  
            float(request.form.get('device_fraud_count')),  
            float(request.form.get('bank_branch_count_8w')),  
            float(request.form.get('bank_months_count')),  
            int(request.form.get('customer_age')),  
            int(request.form.get('has_other_cards'))  
        ]  

        # Scale input features using the scaler  
        input_data = np.array([input_features])  
        scaled_input = scaler.transform(input_data)  

        # Make prediction using the ONNX model  
        input_name = session.get_inputs()[0].name  
        prediction = session.run(None, {input_name: scaled_input.astype(np.float32)})  

        # Process the prediction to get the output class  
        predicted_class = np.argmax(prediction[0])  
        class_label = "Fraud" if predicted_class == 1 else "Not Fraud"  

        return render_template('result.html', prediction_text=f'The predicted class is: {class_label}')  
    except Exception as e:  
        logging.exception("An error occurred during prediction.")  
        return render_template('result.html', prediction_text=f'Error: {str(e)}')  

if __name__ == "__main__":  
    app.run(debug=True)