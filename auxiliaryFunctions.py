# Import necessary libraries for data analysis
import pandas as pd

# Function to explore the DataFrame, providing a summary of its contents
def explore_data_frame(dataframe):
    """
    Display the first few rows of the DataFrame and print information about the DataFrame's structure.
    """
    print(dataframe.head())
    print(dataframe.info())

# Function that returns useful stats about the DataFrame
def stats(dataframe):
    # Break Illinois down by city if available, otherwise fall back to state
    group_col = 'city' if 'city' in dataframe.columns else 'state'

    counts = dataframe[group_col].value_counts()
    percs = dataframe[group_col].value_counts(normalize=True)
    group_stats = pd.concat([counts, percs * 100], axis=1, keys=['count', 'percentage'])

    with open('IllinoisHauntingStats.txt', 'w') as f:
        f.write(f"Total Illinois hauntings: {len(dataframe)}\n\n")
        f.write(f"Breakdown by {group_col}:\n")
        f.write(str(group_stats))

def success_message():
    # This message gets printed if the program was successful
    print("-----------------------------------------------------------------------------------")
    print("The program succeeded.")
    print("Please refer to the 'IllinoisHauntingsDistribution.html' and the 'IllinoisHauntingStats.txt' files.")
    print("Happy Haunting! 👻")
    print("-----------------------------------------------------------------------------------")
