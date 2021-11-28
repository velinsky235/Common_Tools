import argparse


def parseArguments():
	parser = argparse.ArgumentParser(description="Let's do some shit")
	parser.add_argument("-current_number", help='the current point you are at')
	parser.add_argument("-total_number", help='the total number of records')
	args = parser.parse_args()
	return args


def find_percent_finished(current_number, total_number):
	progress = float(current_number/total_number) * 100
	percent_done = str("{0:.2f}".format(progress))
	return percent_done


def main(current_number, total_number):
	percent_done = find_percent_finished(current_number / total_number)
	return percent_done


if __name__ == '__main__':
	args = parseArguments()
	current_number = args.current_number
	total_number = args.total_number
	main(current_number, total_number)

## what needs to be added to another script
# from tools import percent_finished
# percent_done = percent_finished.main(current, total)
# line_print = f"Processing {current}: {percent_done}%"
# print(line_print, end='\r')