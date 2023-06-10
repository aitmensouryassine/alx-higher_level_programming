#include "lists.h"

/**
 * dup_rev_list - duplicate and reverse a singly list
 * @head: the head of the list
 * Return: the head of the new list
 */
listint_t *dup_rev_list(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *newhead = NULL, *new;

	while (tmp)
	{
		new = malloc(sizeof(listint_t));

		new->n = tmp->n;
		new->next = newhead;
		newhead = new;

		tmp = tmp->next;
	}

	return (newhead);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *dup = dup_rev_list(head);
	listint_t *tmp = *head, *tmp1 = dup;

	if (!tmp || tmp->next == NULL)
		return (0);

	while (tmp)
	{
		if (tmp->n != tmp1->n)
			return (0);

		tmp = tmp->next;
		tmp1 = tmp1->next;
	}
	free_listint(dup);

	return (1);
}
