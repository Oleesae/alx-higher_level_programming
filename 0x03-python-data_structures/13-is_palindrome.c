#include "lists.h"

/**
 * reverse_list - reverses a list
 * @head: pointer to the head of the list
 * Return: void
 */

void reverse_list(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *temp = *head;

	while (temp != NULL)
	{
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if the singly linked list is a palindrome
 * @head: the head of the singly linked list
 *
 * Return: int
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *split_list = NULL, *temp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (fast == NULL)
		{
			split_list = slow->next;
			break;
		}
		if (fast->next == NULL)
		{
			split_list =  slow->next->next;
			break;
		}
		slow = slow->next;
	}
	slow->next = NULL;

	reverse_list(&split_list);

	while (split_list && temp)
	{
		if (temp->n == split_list->n)
		{
			split_list = split_list->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!split_list)
		return (1);

	return (0);
}
