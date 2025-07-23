import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

from src.dataset import load_data
from src.features import preprocess
from src.config import MODEL_PATH

def train_model():
    df = preprocess(load_data())
    X = df.drop("Result", axis=1)
    y = df["Result"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X_train, y_train)
    #Luu mo hinh da tren
    joblib.dump(model, MODEL_PATH)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.2%}")

if __name__ == "__main__":
    train_model()
