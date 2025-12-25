from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline


def evaluate_models(models, preprocessor, X, y, cv=5):
    """
    Trains and evaluates multiple models using the same preprocessing pipeline.

    Parameters
    ----------
    models : dict
        Dictionary with model name as key and model object as value.
    preprocessor : ColumnTransformer
        Preprocessing pipeline.
    X : pd.DataFrame
        Feature matrix.
    y : pd.Series
        Target vector.
    cv : int
        Number of cross-validation folds.

    Returns
    -------
    results : dict
        Dictionary with RMSE mean and std for each model.
    """
    results = {}

    for model_name, model in models.items():
        pipeline = Pipeline(steps=[
            ("preprocessing", preprocessor),
            ("model", model)
        ])

        rmse_scores = -cross_val_score(
            pipeline,
            X,
            y,
            scoring="neg_root_mean_squared_error",
            cv=cv
        )

        results[model_name] = {
            "rmse_mean": rmse_scores.mean(),
            "rmse_std": rmse_scores.std()
        }

    return results
