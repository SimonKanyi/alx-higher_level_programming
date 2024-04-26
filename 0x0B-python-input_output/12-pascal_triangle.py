def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to row n.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[i - 1]
            new_row = [1]  # First element of each row is always 1
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])  # Calculate element based on previous row
            new_row.append(1)  # Last element of each row is always 1
            triangle.append(new_row)

    return triangle

# Testing the function
if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print(row)
