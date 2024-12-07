

import os
def mkdir():
	dir = input ("[*]Enter the name of the directory you want to create:")
	os.mkdir(dir)
	print ("[*]Creating a directory")

def rmd():
	dir = input ("[*]Enter the name of the directory you want to delete:")
	os.rmdir(dir)
	print("[*] Deleting the directory")


def main():
	input_num = input("[*]Enter the thing you want to: ")
	if input_num == "1":
		mkdir()
	elif input_num == "2":
		rmd()
if __name__ == "__main__":
	main()
