#! /usr/bin/env python3
#os find the interpreterpath 
# coding: utf-8
#for accents , unnecessary for python3

import analysis.csv as c_an
import analysis.xml as x_an


def main():
	
	c_an.launch_analysis('current_mps.csv')
	x_an.launch_analysis('SyceronBrut.xml')


if __name__ == "__main__":
	main()
	