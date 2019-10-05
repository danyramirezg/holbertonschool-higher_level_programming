#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_dnodeint_at_index - Inserts a new node at a given position.
 * @h: Pointer that point to the double list
 * @idx: Index of the list where the new node should be added.
 * Index starts at 0
 * @n: Value of the index
 * Return: The node of a double linked list
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *p, *new = malloc(sizeof(dlistint_t));
	unsigned int result = 0;

	if (new == NULL)
		return (NULL);
	new->n = n;
	new->prev = NULL;
	new->next = NULL;
	if (*h == NULL)
	{
		*h = new;
		return (new);
	}
	p = *h;
	if (idx == 0)
	{
		new->next = p;
		p->prev = new;
		*h = new;
		return (new);
	}
	while (result != (idx - 1))
	{
		p = p->next;
		result++;
		if (p == NULL)
		{
			free(new);
			return (NULL);
		}
	}
	new->next = p->next;
	new->prev = p;
	if (p->next == NULL)
		p->next = new;
	else
	{
		p->next->prev = new;
		p->next = new;
	}
	return (new);
}
