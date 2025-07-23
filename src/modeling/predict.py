import joblib
import pandas as pd
from src.config import MODEL_PATH

def predict_new(data_dict):
    model = joblib.load(MODEL_PATH)
    input_df = pd.DataFrame([data_dict])
    prediction = model.predict(input_df)
    return prediction[0]
