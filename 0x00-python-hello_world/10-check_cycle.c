#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle
 * @list: the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list->next;

	if (!list)
		return (0);

	while (fast && slow && fast->next)
	{
		if (fast == slow)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
