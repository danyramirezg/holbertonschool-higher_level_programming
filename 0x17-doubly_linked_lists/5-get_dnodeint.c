#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * get_dnodeint_at_index - Returns the node of a dlistint_t linked list.
 * @head: Pointer that point to the list
 * @index: is the index of the node, starting from 0
 * Return: The node of a double linked list
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *p;

	unsigned int result = 0;

	if (head == NULL)
		return (NULL);
	while (head != NULL)
	{
		if (result == index)
		{
			p = head;
			return (p);
		}
		result++;
		head = head->next;
	}
	return (NULL);
}
