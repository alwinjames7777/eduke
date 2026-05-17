import joblib
import numpy as np
import os

# Define absolute paths to ensure the models load correctly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'final_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scaler.pkl')

# Load trained model and scaler safely
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    scaler = None

def predict_performance(attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time):
    if model is None or scaler is None:
        return "Prediction Disabled"
        
    try:
        # Convert input to numpy array
        input_data = np.array([[attendance, internal_marks, class_participation, academic_activities, sleep_time, study_time]])

        # Scale input using saved scaler
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        predicted_marks = model.predict(input_data_scaled)[0]

        # Ensure prediction is within 0-100
        predicted_marks = max(0, min(100, predicted_marks))  

        return round(predicted_marks, 2)
    except Exception as e:
        print(f"Prediction error: {e}")
        return "Prediction Disabled"

# Example usage
if __name__ == "__main__":
    result = predict_performance(54, 20, 82, 50, 66.7, 50)
    print(f"Predicted Final Marks: {result}")
