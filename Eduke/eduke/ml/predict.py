# Reload models
import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'final_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')

model = None
scaler = None

def load_models():
    global model, scaler
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        print("Models successfully loaded!")
    except Exception as e:
        print(f"Error loading models: {e}")

# Try to load them initially
load_models()

def predict_performance(attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time):
    global model, scaler
    if model is None or scaler is None:
        load_models() # Try loading again just in case
        
    if model is None or scaler is None:
        print("Models are still None! Cannot predict.")
        return "Prediction Disabled"
        
    try:
        input_data = np.array([[attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time]])
        input_data_scaled = scaler.transform(input_data)
        predicted_marks = model.predict(input_data_scaled)[0]
        predicted_marks = max(0, min(100, predicted_marks))  
        return round(predicted_marks, 2)
    except Exception as e:
        print(f"Prediction error: {e}")
        return "Prediction Disabled"

# Example usage
if __name__ == "__main__":
    result = predict_performance(54, 20, 82, 50, 66.7, 50)
    print(f"Predicted Final Marks: {result}")
