from PIL import Image


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65  
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")  

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]  
    return ascii_str

def main(image_path, new_width=100):

    image = Image.open(image_path)

    image = grayify(image)

    image = resize_image(image, new_width)

    ascii_str = pixels_to_ascii(image)
    
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:index + new_width] for index in range(0, ascii_str_len, new_width)])

    print(ascii_img)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

image_path = "monalisa.jpeg"
main(image_path, new_width=100)
