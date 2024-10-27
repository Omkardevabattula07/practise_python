

import os
dir = input ("[*]Enter the name of the directory")
def mkdir():
	os.mkdir(dir)
	print ("[*]Creating a directory")

def rmd():
	os.rmdir(dir)
	print("[*] Deleting the directory")


def main():
    
	mkdir()
	rmd()
if __name__ == "__main__":
	main()
