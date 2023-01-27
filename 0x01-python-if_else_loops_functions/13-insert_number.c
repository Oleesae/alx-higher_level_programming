#include "lists.h"
listint_t *get_nodeint_at_index(listint_t **head, int index);
/**
 * insert_node - inserts a node in a sorted linked list
 * @head: head of linked list
 * @number: data for node
 * Return: address to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;
	listint_t *prev;
	int i = 0;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	temp = *head;
	while (temp->next != NULL)
	{
		if (temp->n > new_node->n)
			break;
		temp = temp->next;
		i++;
	}
	prev = *head;
	prev = get_nodeint_at_index(&prev, i - 1);
	prev->next = new_node;
	new_node->next = temp;

	return (new_node);
}

/**
 * get_nodeint_at_index - returns the nth node of a listint_t linked list
 * @head: pointer to the struct list_t
 * @index: index to be returned
 * Return: listint_t
 */

listint_t *get_nodeint_at_index(listint_t **head, int index)
{
	int i;

	for (i = 0; *head != NULL && i < index; i++)
	{
		*head = (*head)->next;
	}

	return (*head);
}
