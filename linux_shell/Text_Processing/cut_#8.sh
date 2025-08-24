# Given a sentence, identify and display its first three words.
# Assume that the space (' ') is the only delimiter between words.

while read line;
do
  echo $line | cut -d' ' -f1-3
done