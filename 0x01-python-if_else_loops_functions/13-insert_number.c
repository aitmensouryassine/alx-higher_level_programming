#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the head of the list
 * @number: the number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp = *head;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	node->n = number;

	if (!tmp)
	{
		node->next = tmp;
		tmp = node;
	}
	while (tmp)
	{
		if (number <= tmp->next->n)
		{
			node->next = tmp->next;
			tmp->next = node;
			break;
		}
		tmp = tmp->next;
	}

	return (node);
}
