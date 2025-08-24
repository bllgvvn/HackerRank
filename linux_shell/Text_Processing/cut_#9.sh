# Given a tab delimited file with several columns print the fields from second fields to last field.

while read line;
do
    echo $line | cut -f2-
done