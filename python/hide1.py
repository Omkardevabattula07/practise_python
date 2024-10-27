# hide_file_in_image.py

from PIL import Image
import os

def file_to_binary(file_path):
    """Convert a file to a binary format."""
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    return binary_string

def hide_data_in_image(image_path, file_path, output_image_path):
    """Hide file data in an image."""
    try:
        # Convert the file to binary
        binary_data = file_to_binary(file_path)

        # Get the file extension and add it to the binary data as metadata
        file_extension = os.path.splitext(file_path)[1]
        extension_binary = ''.join(format(ord(char), '08b') for char in file_extension)
        delimiter = '1111111111111110'  # Custom delimiter to indicate end of extension
        binary_data = extension_binary + delimiter + binary_data + delimiter

        # Open the image
        image = Image.open(image_path)
        image = image.convert("RGB")  # Ensure the image is in RGB format

        # Convert the image into a list of pixels
        pixels = list(image.getdata())

        # Check if the image can hold the data
        max_data_length = len(pixels) * 3  # Each RGB component can hold one bit
        if len(binary_data) > max_data_length:
            raise ValueError("The provided image is too small to hold the data.")

        # Embed the data in the pixels
        data_index = 0
        new_pixels = []
        for pixel in pixels:
            r, g, b = pixel

            if data_index < len(binary_data):
                r = (r & ~1) | int(binary_data[data_index])
                data_index += 1
            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index])
                data_index += 1
            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index])
                data_index += 1

            new_pixels.append((r, g, b))

        # Create a new image with modified pixels
        encoded_image = Image.new(image.mode, image.size)
        encoded_image.putdata(new_pixels)

        # Save the output image
        encoded_image.save(output_image_path)
        print(f"Data successfully hidden in {output_image_path}.")

    except FileNotFoundError:
        print("File or image not found. Please provide valid paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    image_path = input("Enter the path of the image to hide data in: ")
    file_path = input("Enter the path of the file to hide: ")
    output_image_path = input("Enter the path for the output image: ")

    hide_data_in_image(image_path, file_path, output_image_path)
