import pandas as pd

def build_features(df):
    # 1. Time Features    
    df["hour"] = df["datetime"].dt.hour
    df["day_of_week"] = df["datetime"].dt.dayofweek
    df["month"] = df["datetime"].dt.month

    # 2. Sort for lag features
    df = df.sort_values(by=["station", "datetime"])

        # 3. Lag Features (previous pollution values)
    df["PM2.5_lag1"] = df.groupby("station")["PM2.5"].shift(1)
    df["PM10_lag1"] = df.groupby("station")["PM10"].shift(1)
    df["NO2_lag1"] = df.groupby("station")["NO2"].shift(1)


    # Fill missing lag values
    df = df.fillna(method="bfill")

    return df