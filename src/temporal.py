def add_temporal_features(df):
    df = df.copy()

    df["PropertyAge"] = df["YrSold"] - df["YearBuilt"]
    df["YearsSinceRemodel"] = df["YrSold"] - df["YearRemodAdd"]

    return df