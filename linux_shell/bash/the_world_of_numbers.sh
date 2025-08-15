# Given two integers, x and y, find their sum, difference, product, and quotient.

read x
read y

sum=$((x + y))
difference=$((x - y))
product=$((x * y))
quo=$((x / y))

echo $sum
echo $difference
echo $product
echo $quo