#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint- prints all the elements of a double list.
 *@h: Receive the list to print
 * Return: The elements of the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	unsigned int data = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		data++;
	}
	return (data);
}
