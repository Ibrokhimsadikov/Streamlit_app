import random
from matplotlib.colors import rgb2hex

def generate_distinct_colors(strings):
    """
    Generate a dictionary mapping each string in the list to a unique, distinct HEX color.
    
    Args:
        strings (list of str): List of strings for which to generate colors.
    
    Returns:
        dict: A dictionary where keys are strings and values are distinct HEX color codes.
    """
    num_colors = len(strings)
    random.seed(42)  # For reproducibility
    colors = set()
    
    while len(colors) < num_colors:
        # Generate a random RGB color and convert it to HEX
        r, g, b = [random.randint(0, 255) for _ in range(3)]
        hex_color = rgb2hex((r/255, g/255, b/255))
        colors.add(hex_color)
    
    # Assign each unique color to a string
    color_dict = {string: color for string, color in zip(strings, colors)}
    return color_dict

# Example usage
str_list = [f"item_{i}" for i in range(1, 201)]  # List of 200 strings
color_mapping = generate_distinct_colors(str_list)

# Print a small sample of the result
for key, value in list(color_mapping.items())[:10]:  # Show only the first 10
    print(f"{key}: {value}")
