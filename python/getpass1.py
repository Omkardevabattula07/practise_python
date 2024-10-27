


#by using this we can hide the input of the user 

import getpass

def get1():
	password = getpass.getpass("{*}Enter the password: ")
	print ("your pass word is :",password)


def main():
	get1()

if __name__ == "__main__":
	main()
