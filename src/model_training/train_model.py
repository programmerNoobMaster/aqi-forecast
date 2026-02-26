from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import mlflow
import mlflow.sklearn
import os

# IMPORTANT: Use RELATIVE tracking path (portable for Docker)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
mlflow.set_tracking_uri(f"file:{BASE_DIR}/mlruns")
mlflow.set_experiment("AQI_Experiment")


def train_model(df, model_type="linear", params=None):

    df = df.drop(columns=["datetime", "station", "wd"])

    y = df["PM2.5"]
    X = df.drop(columns=["PM2.5"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    with mlflow.start_run():

        if model_type == "linear":
            model = LinearRegression()

        elif model_type == "random_forest":

            if params is None:
                params = {
                    "n_estimators": 200,
                    "max_depth": 15,
                    "min_samples_split": 2
                }

            model = RandomForestRegressor(
                n_estimators=params["n_estimators"],
                max_depth=params["max_depth"],
                min_samples_split=params["min_samples_split"],
                random_state=42
            )

            mlflow.log_params(params)

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))

        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(model, "model")

    return model, rmse