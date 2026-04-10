from sklearn.preprocessing import LabelEncoder

def feature_engineering(df):
    """
    Convert all categorical columns into numeric
    """
    le = LabelEncoder()

    for col in df.columns:
        try:
            df[col] = le.fit_transform(df[col])
        except:
            pass

    return df