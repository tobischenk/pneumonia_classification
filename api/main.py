from fastapi import FastAPI, Body
from api.util import get_prediction

app = FastAPI()


@app.post("/predict")
def predict(img_data: str = Body(...)):
    try:
        return {"prediction": str(get_prediction(img_data))}
    except Exception as e:
        print(e)
        return {"error": "Internal Server Error"}
