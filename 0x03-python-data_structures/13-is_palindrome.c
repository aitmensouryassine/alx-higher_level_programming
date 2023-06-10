#include "lists.h"

/**
 * list_len - returns the length of a list
 * @head: the head of the list
 * Return: length of the list
 */
int list_len(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0;

	while (tmp)
	{
		tmp = tmp->next;
		i++;
	}

	return (i);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = list_len(head);
	int *arr, i;
	listint_t *tmp = *head;
	int palindrome = 1;

	if (len == 0)
		return (1);

	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);

	i = 0;
	while (tmp)
	{
		arr[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}

	i = 0;
	while (i < len)
	{
		if (arr[i] != arr[(len - 1) - i])
		{
			palindrome = 0;
			break;
		}
		i++;
	}

	free(arr);
	return (palindrome);
}
