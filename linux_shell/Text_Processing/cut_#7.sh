# Given a sentence, identify and display its fourth word.
# Assume that the space (' ') is the only delimiter between words.

while read line;
do
  echo $line | cut -d' ' -f4
done