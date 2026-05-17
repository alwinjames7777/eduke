# Reload models
import joblib
import numpy as np
import os
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'final_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')
LOG_PATH = os.path.join(BASE_DIR, '..', 'predict_error.log')

def log_error(msg):
    try:
        print(msg)
        with open(LOG_PATH, 'a', encoding='utf-8') as f:
            f.write(msg + '\n')
    except:
        pass

model = None
scaler = None

def load_models():
    global model, scaler
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        log_error("Models successfully loaded!")
    except Exception as e:
        log_error(f"Error loading models: {traceback.format_exc()}")

load_models()

def predict_performance(attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time):
    global model, scaler
    if model is None or scaler is None:
        load_models()
        
    if model is None or scaler is None:
        log_error("Models are still None! Cannot predict.")
        return "Prediction Disabled"
        
    try:
        log_error(f"Predicting for: {attendance}, {internal_marks}, {class_participation}, {academic_activities}, {sleep_time}, {study_time}")
        input_data = np.array([[attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time]])
        input_data_scaled = scaler.transform(input_data)
        predicted_marks = model.predict(input_data_scaled)[0]
        predicted_marks = max(0, min(100, predicted_marks))  
        log_error(f"Success! Score: {predicted_marks}")
        return round(predicted_marks, 2)
    except Exception as e:
        log_error(f"Prediction error: {traceback.format_exc()}")
        return "Prediction Disabled"

# Example usage
if __name__ == "__main__":
    result = predict_performance(54, 20, 82, 50, 66.7, 50)
    print(f"Predicted Final Marks: {result}")
