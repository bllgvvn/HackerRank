# Display the 2nd and 7th characters from each line of text.

while read line;
do 
    echo "${line}" | cut -c 2,7
done