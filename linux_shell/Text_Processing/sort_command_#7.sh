# You are given a file of pipe-delimited weather data.
# There is no header column in this data file.
# The first five columns of this data are: 
#  (a) the name of the city
#  (b) the average monthly temperature in Jan (in Fahrenheit)
#  (c) the average monthly temperature in April
#  (d) the average monthly temperature in July
#  (e) the average monthly temperature in October
# You need to sort this file in descending order of the second column.

sort -n -r -k 2 -t '|'