
def parse_image_input(image_string):
    """
    It takes a string as input and returns a list with the image name and tag split
    
    :param image_string: The string that contains the image name and tag
    :return: A list with the image name and tag split.
    """
    parsed_string = list()
    if ":" in image_string:
        parsed_string = image_string.split(":")
    else:
        parsed_string.append(image_string)
    return parsed_string
