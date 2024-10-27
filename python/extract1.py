# extract_file_from_image.py

from PIL import Image

def extract_data_from_image(image_path):
    """Extract hidden data from an image."""
    try:
        # Open the image
        image = Image.open(image_path)
        image = image.convert("RGB")

        # Get the pixels
        pixels = list(image.getdata())

        # Extract the least significant bits to retrieve the hidden data
        binary_data = ""
        for pixel in pixels:
            r, g, b = pixel
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

        # Look for the delimiter to separate the extension and the data
        delimiter = '1111111111111110'
        delimiter_index = binary_data.find(delimiter)

        if delimiter_index == -1:
            raise ValueError("No hidden data found in the image.")

        # Extract the extension
        extension_binary = binary_data[:delimiter_index]
        extension = ''.join(chr(int(extension_binary[i:i+8], 2)) for i in range(0, len(extension_binary), 8))

        # Remove any embedded null byte from the extension
        extension = extension.replace('\0', '')

        # Extract the actual data
        binary_data = binary_data[delimiter_index + len(delimiter):]
        delimiter_index = binary_data.find(delimiter)
        if delimiter_index == -1:
            raise ValueError("No end delimiter found. The data might be corrupted.")
        
        binary_data = binary_data[:delimiter_index]

        # Convert the binary data to bytes
        byte_data = bytearray(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))

        return byte_data, extension

    except FileNotFoundError:
        print("Image file not found. Please provide a valid image path.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def save_extracted_file(data, extension, output_file_path):
    """Save the extracted data to a file."""
    try:
        # Ensure the output path is constructed without null bytes
        safe_extension = extension.replace('\0', '')
        complete_path = f"{output_file_path}{safe_extension}"

        with open(complete_path, 'wb') as file:
            file.write(data)
        print(f"Extracted data saved to {complete_path}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

if __name__ == '__main__':
    image_path = input("Enter the path of the image with hidden data: ")
    output_file_path = input("Enter the base path for the output file (without extension): ")

    # Extract the hidden data from the image
    hidden_data, file_extension = extract_data_from_image(image_path)

    if hidden_data and file_extension:
        # Save the extracted data to a file
        save_extracted_file(hidden_data, file_extension, output_file_path)
