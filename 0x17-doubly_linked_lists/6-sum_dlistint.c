#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * sum_dlistint - Returns the sum of all data(n) of a double linked list.
 * @head: Pointer that points to the list
 * Return: The sum of all data. if the list is empty, return 0
 */
int sum_dlistint(dlistint_t *head)
{
	unsigned int data = 0;

	while (head != NULL)
	{
		data += head->n;
		head = head->next;
	}
	return (data);
}
