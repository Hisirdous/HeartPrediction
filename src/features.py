def preprocess(df):
    df["Result"] = df["Result"].map({"positive": 1, "negative": 0})
    df["Blood sugar"] = df["Blood sugar"].apply(lambda x: 1 if x > 120 else 0)
    return df
