# Given a tab delimited file with several columns print the first three fields.

while read line;
do
    echo "${line}" | cut -d$'\t' -f 1-3
done