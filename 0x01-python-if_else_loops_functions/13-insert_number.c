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
	listint_t *node, *tmp = *head, *prev;
	int i = 0;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	node->n = number;
	if (!(*head))
	{
		node->next = *head, *head = node;
	}
	else
	{
		while (*head)
		{
			if (number <= (*head)->n && i == 0)
			{
				node->next = (*head), *head = node;
				break;
			}
			if ((*head)->next != NULL)
			{
				if (number <= (*head)->n && i != 0)
				{
					node->next = *head;
					prev->next = node, *head = tmp;
					break;
				}
			}
			else
			{
				(*head)->next = node, node->next = NULL;
				*head = tmp;
				break;
			}
			prev = *head, *head = (*head)->next, i++;
		}
	}
	return (node);
}
