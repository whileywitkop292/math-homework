def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

# Example usage
rectangle_length = 10.5
rectangle_width = 7.2
area = calculate_area(rectangle_length, rectangle_width)
print(f"The area is {area}")
