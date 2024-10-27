import base64
import os

def encode_file(file_path):
    """Encode the file at the given path using base64."""
    try:
        with open(file_path, "rb") as file:
            encoded_data = base64.b64encode(file.read())
        print("Encoded data:")
        print(encoded_data.decode("utf-8"))
        return encoded_data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def decode_file(encoded_data, output_file_path):
    """Decode the base64 data and save it to a file."""
    try:
        decoded_data = base64.b64decode(encoded_data)
        with open(output_file_path, "wb") as file:
            file.write(decoded_data)
        print(f"File decoded and saved as: {output_file_path}")
    except Exception as e:
        print(f"An error occurred while decoding the file: {e}")

def main():
    # Get the file path from the user
    file_path = input("Enter the path of the file you want to encode: ")
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("The specified file does not exist. Please provide a valid file path.")
        return
    
    # Encode the file
    encoded_data = encode_file(file_path)
    if encoded_data is None:
        return
    
    # Get the output file name for the decoded file
    output_file_path = input("Enter the name for the decoded output file (with extension): ")
    
    # Decode the file and save it
    decode_file(encoded_data, output_file_path)

if __name__ == "__main__":
    main()
