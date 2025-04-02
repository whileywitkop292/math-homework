def calculate_area(radius):
    """
    Calculate the area of a circle with given radius.
    
    Parameters:
    - radius: float or int, the radius of the circle
    
    Returns:
    - area: float, the area of the circle
    """
    area = 3.14159 * (radius ** 2)
    return area

# Example usage:
radius = 7
area = calculate_area(radius)
print("The area is:", area)
