# You are given a file of text, which contains temperature information about American cities, in TSV format.
# The first column is the name of the city and the next four columns are the average temperature in the months of Jan, Feb, March and April.
# Rearrange the rows of table in descending order of the values for the average temperature in January.

sort -r -n -k 2 -t $'\t' 