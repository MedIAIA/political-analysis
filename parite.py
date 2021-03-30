#! /usr/bin/env python3
#os find the interpreterpath 
# coding: utf-8
#for accents , unnecessary for python3
import argparse
import analysis.csv as c_an
import analysis.xml as x_an
import logging as lg


def parse_arguments(): # Launch analysis with command line and the choose of file for analysis( CSV or XML in option of command )
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--extension", help= """Type of file to analyse. Is it a CSV or an XML?""") # doc terminal : python parite.py --help
	parser.add_argument("-d", "--datafile", help= """ CSV file or containing the data for analysis""")
	return  parser.parse_args()




def main():
	args = parse_arguments()
	
	try:
		datafile = args.datafile
		
		if datafile == None:
			raise lg.warning('You must indicate a datafile')
		else:
			try:
				if args.extension == 'csv':
					c_an.launch_analysis(datafile)
				elif args.extension == 'xml':
					x_an.launch_analysis(datafile)
			except FileNotFoundError as e:
				lg.critical(':( File not find {} \n'.format(e))  # we must to use format(e) if we want to see error message.
			finally:
				lg.debug('########################### Analysis is over    #################################')
	except Warning as e:
		lg.warning(e)
	
	#import pdb; pdb.set_trace() # pdb = python debuger , pdb.set_trace() for define a breakpoint if we need to check any things / after that we can remove this code line
	
	
	
  

if __name__ == "__main__":
	main()
	