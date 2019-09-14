#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

void free_dlistint(dlistint_t *head)
{
g	dlistint_t *p;

	if (head == NULL)
		return;
	while (head != NULL)
	{
		p = head;
		head = head->next;
		free(p);
	}
}