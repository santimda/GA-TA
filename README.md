# GA-TA 

## Introduction
**GA-TA** is a bla bla bla

## Functionalities

The excecution command line: $python main.py [OPTIONS] SPREADSHEET . 

[OPTIONS]: The user can specify one, two or three letters, each one corresponds to the output tables: R (r), Arlequin (a) and/or Structure (s) respectivly. If the user do not specify any options, info of SPREADSHEET will be showed by terminal. 

SPREADSHEET: Can be with Excel extention and with open office '.ods'
Examples:	$ python main.py ra spreadsheet.xlsx
			it will return output files for R and Arlequin

			$ python main.py s spreadsheet.xlsx
			it will return output file for Structure
			
Output: dos archivos. Uno en .txt y otro en .xlsx por cada tipo de tabla solicitado..
Incorporado: conversion de txt a xlsx automaticamente (dentro de main)

Warning: The first line must not to be white, it should be the header of the input file, otherwise will show an ErrorMsg

Warning: All the columns with information must to have a NameColumn, otherwise, will not be read the colmn info

### Arlequin
ble ble ble

### R

R_structure is the module that generate the output table for R software. Done it.

### Structure
blo blo blo
