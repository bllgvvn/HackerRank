# Read in one character from STDIN.
# If the character is 'Y' or 'y' display "YES"
# If the character is 'N' or 'n' display "NO".

read -n 1 char
if [[ $char == 'Y' || $char == 'y' ]]; then
    echo "YES"
elif [[ $char == 'N' || $char == 'n' ]]; then
    echo "NO"
fi