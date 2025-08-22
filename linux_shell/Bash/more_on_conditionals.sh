# Given three integers (X, Y, Z), representing the three sides of a triangle,
# identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.

read X
read Y
read Z

if [ $X -eq $Y ] && [ $Y -eq $Z ]; then
    echo "Equilateral"
elif [ $X -eq $Y ] || [ $Y -eq $Z ] || [ $X -eq $Z ]; then
    echo "Isosceles"
else
    echo "Scalene"
fi