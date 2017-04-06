def load_data():
    df = pd.read_csv("hn_stories.csv")
    print(df.head(5))
    df.columns = ["submission_time", "upvotes", "url", "headline"]
    print(df.head(5))
    return df

import pandas as pd

if __name__ == "__main__":
    data = load_data()
