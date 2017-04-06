def load_data():
    df = pd.read_csv("hn_stories.csv")
    df.columns = ["submission_time", "upvotes", "url", "headline"]
    return df

import pandas as pd

if __name__ == "__main__":
    data = load_data()
    domains = data["url"].value_counts()
    print(domains)
    
    for name, row in domains.items():
        print("{0}: {1}".format(name, row))
