#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * add_dnodeint - Adds a new node at the beginning of a double linked list.
 * @head: Double pointer that point to the list
 * @n: Value to add to the list
 * Return: The elements of the list
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

	if(*head == NULL)
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
	return(new);
	
}
