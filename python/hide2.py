# hide_file_in_image.py

from PIL import Image

def hide_file_in_image(image_path, file_path, output_image_path):
    """Hide a file inside an image."""
    try:
        # Read the file data
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Open the image
        image = Image.open(image_path)
        image = image.convert("RGB")

        # Convert the file data into a byte array
        file_data = bytearray(file_data)

        # Add the length of the file data at the beginning (to know the size later)
        file_length = len(file_data).to_bytes(4, byteorder='big')
        file_data = file_length + file_data

        # Get the pixels of the image
        pixels = list(image.getdata())

        # Check if the image has enough space to hide the file data
        if len(file_data) * 8 > len(pixels) * 3:
            raise ValueError("The image is too small to hold the file data.")

        # Embed the file data into the image
        data_index = 0
        new_pixels = []
        for pixel in pixels:
            if data_index < len(file_data) * 8:
                r, g, b = pixel
                byte_index = data_index // 8
                bit_index = data_index % 8
                byte_value = file_data[byte_index]
                bit_value = (byte_value >> (7 - bit_index)) & 1

                # Modify the pixel's red component to hide the bit
                r = (r & ~1) | bit_value
                data_index += 1

                # If more data remains, modify the green component
                if data_index < len(file_data) * 8:
                    bit_index = data_index % 8
                    bit_value = (file_data[byte_index] >> (7 - bit_index)) & 1
                    g = (g & ~1) | bit_value
                    data_index += 1

                # If more data remains, modify the blue component
                if data_index < len(file_data) * 8:
                    bit_index = data_index % 8
                    bit_value = (file_data[byte_index] >> (7 - bit_index)) & 1
                    b = (b & ~1) | bit_value
                    data_index += 1

                new_pixels.append((r, g, b))
            else:
                new_pixels.append(pixel)

        # Create a new image with modified pixels
        encoded_image = Image.new(image.mode, image.size)
        encoded_image.putdata(new_pixels)

        # Save the output image
        encoded_image.save(output_image_path)
        print(f"File successfully hidden in {output_image_path}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    image_path = input("Enter the path of the image: ")
    file_path = input("Enter the path of the file to hide: ")
    output_image_path = input("Enter the output image path: ")

    hide_file_in_image(image_path, file_path, output_image_path)
