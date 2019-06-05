/*
 ============================================================================
 Name        : test2.c
 Author      : Anjan
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */
//#include <add.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int result;
	printf("!!!Hello World!!!"); /* prints !!!Hello World!!! */
	result = add ( 7,6);
	printf("I added numbers Yey! it is: %d", result); /* prints !!!Hello World!!! */
	return EXIT_SUCCESS;
}

int add (int a, int b)
{
	int sum  = a + b;
	return sum;
}
