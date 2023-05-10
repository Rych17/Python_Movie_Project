import csv
import pandas as pd

# Define columns for the results dataframe
columns = ['Title', 'Release Date', 'Budget', 'Rating', 'Budget-Rating Ratio']

# Create an empty dataframe with the defined columns
results_df = pd.DataFrame(columns=columns)

# Load data from CSV file
keep = [0, 1, 2, 3, 7, 10]
big_lst = []
with open("db.csv") as my_file:
    for dataset in csv.reader(my_file, delimiter=","):
        new = []
        i = 0
        for data in dataset:
            if i in keep:
                new.append(data)
            i += 1
        big_lst.append(new)

# Sort movies by rating
rate_dict = {}
for line in big_lst:
    if line[0] != "":
        rate_dict[line[0]] = line[3]
sorted_rating = sorted(rate_dict.items(), key=lambda x:x[1], reverse=True)

# Calculate budget-rating ratios and add to results dataframe
for movie in sorted_rating:
    data = big_lst[int(movie[0])]
    ratio = float(data[4])/float(data[3])
    results_df = results_df.append({'Title': data[0], 'Release Date': data[1], 'Budget': data[3], 
                                    'Rating': data[4], 'Budget-Rating Ratio': ratio}, ignore_index=True)

# Sort dataframe by budget-rating ratio
results_df = results_df.sort_values(by='Budget-Rating Ratio')

# Print dataframe
print(results_df)
results_df.to_csv('results.csv', index=False)
