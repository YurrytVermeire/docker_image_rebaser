
def parse_image_input(image_string):
    parsed_string = list()
    if ":" in image_string:
        parsed_string = image_string.split(":")
    else:
        parsed_string.append(image_string)
    return parsed_string
