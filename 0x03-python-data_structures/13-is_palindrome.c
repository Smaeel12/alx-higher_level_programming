#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked
 * list is a palindrome.
 * @head: linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int size = 0, i;
	int num_arr[128];
	listint_t *current = *head;

	if (current == NULL)
		return (1);
	while (current != NULL)
	{
		num_arr[size] = current->n;
		current = current->next;
		size++;
	}
	for (i = 0; i != size; i++, size--)
	{
		if (num_arr[i] != num_arr[size - 1])
		{
			free(current);
			return (0);
		}
	}
	free(current);
	return (1);
}
