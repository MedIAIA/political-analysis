#! /usr/bin/env python3
#os find the interpreterpath 
# coding: utf-8
#for accents , unnecessary for python3

import csv_analysis as c_an
import xml_analysis as x_an


def main():
	c_an.launch_analysis('current_maps.csv')
	x_an.launch_analysis('SyceronBrut.xml')


if __name__ == "__main":
		main()
	