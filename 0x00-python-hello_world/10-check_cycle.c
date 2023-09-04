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

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
	

