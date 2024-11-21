def generate_triangle_pattern(num_rows):
    """
    Generates a triangle pattern of asterisks with increasing width.
    
    Parameters:
    num_rows (int): Number of rows to generate
    
    Returns:
    list[str]: List of strings representing the triangle pattern
    """
    pattern = []
    for i in range(1, num_rows + 1):
        row = (" " * (num_rows - i)) + ("*" * i)
        pattern.append(row)
    return pattern
print(generate_triangle_pattern(5))