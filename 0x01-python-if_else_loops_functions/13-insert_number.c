#include "lists.h"

listint_t *get_nodeint_at_index(listint_t **head, int index);
int list_len(listint_t *head);

/**
 * insert_node - inserts a node in a sorted linked list
 * @head: head of linked list
 * @number: data for node
 * Return: address to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *bef;
	listint_t *aft;
	int len, i = 0;

	/** create and populate new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/** Check for empty linked list */
	if (*head == NULL || head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	/**
	 * use the bef to traverse the linked list to
	 * desired position
	 * use len variable to store the length of the
	 * linked list
	 * traverse through the list till index is reached
	 * and exit loop using break
	 */
	bef = *head;

	len = list_len(bef);
	while (bef->next != NULL)
	{
		if (bef->n >= number)
			break;
		bef = bef->next;
		i++;
	}

	if (i == 0)
	{
		new_node->next = *head;
		*head = new_node;
		printf("at beginning at %d\n", i);
	}


	return (*head);
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

	for (i = 1; *head != NULL && i < index; i++)
	{
		*head = (*head)->next;
	}

	return (*head);
}

/**
 * list_len - returns the number of elements in a listint_t list
 * @head: pointer to the head of the struct listint_t
 * Return: int the number of elements in the linked list
 */

int list_len(listint_t *head)
{
	int total = 0;

	while (head != NULL)
	{
		if (head->next != NULL)
			total++;
		head = head->next;
	}
	return (total);
}
