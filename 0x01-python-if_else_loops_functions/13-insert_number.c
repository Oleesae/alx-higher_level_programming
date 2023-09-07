#include "lists.h"

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: head of linked list
 * @number: data for node
 * Return: address to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *new_node;

	/** create and populate new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/** Check for empty linked list */
	if (temp == NULL || temp->next->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
