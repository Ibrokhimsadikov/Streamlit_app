import seaborn as sns
from matplotlib.colors import rgb2hex

def generate_color_palette(strings):
    """
    Generate a dictionary mapping each string in the list to a unique HEX color.
    
    Args:
        strings (list of str): List of strings for which to generate colors.
    
    Returns:
        dict: A dictionary where keys are strings and values are HEX color codes.
    """
    # Generate a scalable color palette using Seaborn
    palette = sns.color_palette("husl", len(strings))
    
    # Convert RGB values to HEX and create a dictionary
    color_dict = {item: rgb2hex(palette[i]) for i, item in enumerate(strings)}
    
    return color_dict

# Example usage
str_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
color_mapping = generate_color_palette(str_list)

# Print the resulting dictionary
print(color_mapping)
