# extract_file_from_image.py

from PIL import Image

def extract_file_from_image(image_path, output_file_path):
    """Extract a hidden file from an image."""
    try:
        # Open the image
        image = Image.open(image_path)
        image = image.convert("RGB")

        # Get the pixels
        pixels = list(image.getdata())

        # Extract the hidden data
        binary_data = ""
        for pixel in pixels:
            r, g, b = pixel
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

        # Convert the binary data to bytes
        all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
        file_data = bytearray(int(byte, 2) for byte in all_bytes if len(byte) == 8)

        # Extract the file length from the first 4 bytes
        file_length = int.from_bytes(file_data[:4], byteorder='big')
        file_content = file_data[4:4 + file_length]

        # Save the extracted file
        with open(output_file_path, 'wb') as file:
            file.write(file_content)
        print(f"File successfully extracted to {output_file_path}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    image_path = input("Enter the path of the image with hidden data: ")
    output_file_path = input("Enter the output file path: ")

    extract_file_from_image(image_path, output_file_path)
