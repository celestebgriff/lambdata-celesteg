# Single function to take a list, turn it into a series and add it to a dataframe as a new column
def list_to_column(list,df):
    import pandas as pd
    df["new column"] = pd.Series(list)
    return

# Train/validate/test split function for a dataframe
# train = 60%, test = 20%, val = 20%
def train_val_test(df):
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    train, val = train_test_split(train, test_size=0.25, random_state=42)
    return train.shape, test.shape, val.shape