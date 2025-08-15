# Read in one character from STDIN.
# If the character is 'Y' or 'y', print 'YES'.
# If the character is 'N' or 'n', print 'NO'.

read -n 1 char

if [ $char == 'Y' ] || [ $char == 'y' ]; then
    echo 'YES'
elif [ $char == 'N' ] || [ $char == 'n' ]; then
    echo 'NO'
fi