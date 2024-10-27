
def req():
	import requests

	req = requests.get('https://www.sviet.edu.in/')


	with open("vasavi.txt","w") as file: 
		file.writelines(req.text[:2000])
def main():
	req()


if __name__ == "__main__":
	main()
