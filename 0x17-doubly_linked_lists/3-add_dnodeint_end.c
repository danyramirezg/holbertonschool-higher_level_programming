#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * add_dnodeint_end - Adds a new node at the end of a double linked list.
 * @head: Double pointer that point to the list
 * @n: Value to add to the list
 * Return: The address of the new element, or NULL if it failed
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new, *p = *head;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->prev = NULL;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	while (p->next != NULL)
	{
		p = p->next;
	}
	new->prev = p;
	p->next = new;
	return (new);
}
