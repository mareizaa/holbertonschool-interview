#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: integer
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;

	tmp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (tmp == NULL || number < tmp->n)
	{
		new->next = tmp;
		*head = new;
		return (new);
	}
	while (tmp->next != NULL && tmp->next->n < number)
		tmp = tmp->next;

	new->next = tmp->next;
	tmp->next = new;

	return (new);
}
