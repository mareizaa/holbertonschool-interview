#include "search_algos.h"

/**
 * print_array - Entry point
 *
 * @array: Array
 * @first: Size of array
 * @last: Value to find
 * Return: Always EXIT_SUCCESS
 */
void print_array(int *array, int first, int last)
{
	int i;

	printf("Searching in array: ");
	for (i = first; i < last; i++)
		printf("%d, ", array[i]);
	printf("%d", array[i]);
	printf("\n");
}

/**
 * advanced_binary - Entry point
 *
 * @array: Array
 * @size: Size of array
 * @value: Value to find
 * Return: Always EXIT_SUCCESS
 */
int advanced_binary(int *array, size_t size, int value)
{
	size_t f;
	size_t l;

	if (!array)
		return (-1);

	f = 0;
	l = size - 1;
	return (recursive_search(array, f, l, value));

}


/**
 * recursive_search - Recursive advanced binary search
 * @array: Array
 * @f: First element of array
 * @l: Last element of array
 * @value: Value to find
 * Return: Always EXIT_SUCCESS
 */
int recursive_search(int *array, size_t f, size_t l, int value)
{
	size_t half;

	if (f < l)
	{
		half = f + (l - f) / 2;
		print_array(array, (int)f, (int)l);
		if (array[half] >= value)
			return (recursive_search(array, f, half, value));
		else
			return (recursive_search(array, half + 1, l, value));
		return ((int)(half));
	}
	if (array[f] == value)
		return (f);
	print_array(array, (int)f, (int)l);
	return (-1);
}
