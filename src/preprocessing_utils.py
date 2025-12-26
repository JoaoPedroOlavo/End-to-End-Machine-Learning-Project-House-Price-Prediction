def cast_to_string(X):
    """
    Ensure input data is cast to string type.
    This is required for robust ordinal encoding.
    """
    return X.astype(str)
