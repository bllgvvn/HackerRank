# Print the character from thirteenth position to the end.

while read line;
do
    echo "${line}" | cut -c 13-
done