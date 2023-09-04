#include "lists.h"

/**
 * check_cycle - check if there's a cycle in the singly linked list
 * @list: head of the singly linked list
 *
 * Return: int
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	if (slow == NULL || fast == NULL)
	{
		free(slow);
		free(fast);
		return (NULL);
	}

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
	

