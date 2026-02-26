def save_feature_data(df, path):
    df.to_csv(path, index=False)