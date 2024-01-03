#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
 * insert_node - a function in C that inserts a number into
	* a sorted singly linked list.
 * @head: sorted singly linked list.
 * @number: a number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_node;
	listint_t *next_node;

	current_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
		*head = new_node;
	else
	{
		/* find the correct node */
		if (current_node->n > number)
		{
			new_node->next = current_node;
			*head = new_node;
		}
		else
		{
			while (current_node->next != NULL && current_node->next->n < number)
				current_node = current_node->next;
			next_node = current_node->next;
			current_node->next = new_node;
			new_node->next = next_node;
		}
	}
	return (new_node);
}
