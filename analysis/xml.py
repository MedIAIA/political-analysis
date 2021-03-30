import os


def launch_analysis(data_file):
	# print("file_value",__file__)
	# print(" dir",os.path.dirname(__file__))
	directory = os.path.dirname(os.path.dirname(__file__))  # return the root dirctory
	path_to_file = os.path.join(directory, "data", data_file)  ## Build of the complet path
	
	with open(path_to_file, 'r') as file:
		preview = file.readline()
	
	print(" Yeah! We manged to read the file. here is a preview {}".format(preview))


def main():
	print("Main is Run")
	launch_analysis('SyceronBrut.xml')


if __name__ == "__main__":
	main()