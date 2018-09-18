import sys

txt_file = sys.argv[1]

def txt2csv(txt_file):
	csv_name = txt_file[0:-3] + 'csv'
	csv = open(csv_name, 'w')
	
	with open(txt_file) as f:
		line = f.readline()
		num = 0
		while line:
			if num%7 in [2,4]:
				csv.write(line.rstrip('\n') + ',')
			if num%7 == 6:
				csv.write(line.rstrip('m\n') + '\n')
			line = f.readline()
			num += 1

	csv.close()



def main():
	txt2csv(txt_file)

if __name__ == '__main__':
	main()