import os
import json
import joblib
import numpy as np

# load model
def init():
    global model
    
    model_path = os.path.join(
        os.getenv("AZUREML_MODEL_DIR"),
        "breastcancer_model.pkl"
    )
    
    model = joblib.load(model_path)
    print("Model loaded successfully")

# prediction function
def run(raw_data):
    data = json.loads(raw_data)
    data = np.array(data["data"])
    result = model.predict(data)
    return result.tolist()