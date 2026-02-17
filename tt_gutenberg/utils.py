import pandas as pd
def count():

    df = pd.read_csv("gutenberg_authors.csv")

    df = df[df['alias'].notna() & (df['alias'] != "")]

    # Logic: Count occurrences of each alias (representing translation count)
    # and sort them in descending order
    sorted_series = df['alias'].value_counts(ascending=False)


    # Return just the list of names (the index of the series)
    return sorted_series.index.tolist()
    