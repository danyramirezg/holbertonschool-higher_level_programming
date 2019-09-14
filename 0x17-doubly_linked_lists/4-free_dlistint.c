#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * free_dlistint - Function that free a double linked list.
 * @head: Pointer that point to the list
 *
 * Return: void
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *p;

	if (head == NULL)
		return;
	while (head != NULL)
	{
		p = head;
		head = head->next;
		free(p);
	}
}
