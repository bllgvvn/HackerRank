# You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates (i, j, k) on a 3D grid where the sum of i, j, and k is not equal to n.
# Here, 0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z.

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))

print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])