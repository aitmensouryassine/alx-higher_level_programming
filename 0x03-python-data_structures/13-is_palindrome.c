#include "lists.h"

/**
 * rev_list - reverse a singly list
 * @head: the head of the list
 */
void rev_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *curr = *head;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;

		prev = curr;
		curr = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *q = *head, *p = *head, *middle, *tmp = *head;

	if (!(*head) || !(*head)->next)
		return (1);

	while (1)
	{
		p = p->next->next;

		if (!p->next || !p->next->next)
		{
			middle = q->next->next;
			break;
		}

		q = q->next;
	}

	rev_list(&middle);

	while (middle)
	{
		if (tmp->n != middle->n)
			return (0);

		middle = middle->next;
		tmp = tmp->next;
	}

	return (1);
}
