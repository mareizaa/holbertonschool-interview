#include <stdlib.h>
#include <stdio.h>

#include "palindrome.h"

/**
 * is_palindrome - checks whether or not a given integer is a palindrome
 * @n: Number to be checked
 * Return: integer 1 or 0
 */
int is_palindrome(unsigned long n)
{
	unsigned long num, i = 0;

	num = n;

	while (num != 0)
	{
		i = i * 10;
		i = i + num % 10;
		num = num / 10;
	}
	if (n == i)
		return (1);
	else
		return (0);
}
