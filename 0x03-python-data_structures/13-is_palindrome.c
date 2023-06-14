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
	int size = 0, i = 0;
	int *num_arr;
	listint_t *tmp = *head;
	listint_t *current = *head;

	if (current == NULL)
		return (1);
	while (tmp != NULL)
	{
		tmp = tmp->next;
		size++;
	}
	free(tmp);
	num_arr = malloc(size * sizeof(int));
	if (num_arr == NULL)
		return (-1);
	for (i = 0; i != size; i++)
	{
		num_arr[i] = current->n;
		current = current->next;
	}
	do {
		i--;
		if (num_arr[i] != num_arr[size - i - 1])
		{
			free(num_arr);
			free(current);
			return (0);
		}
	} while (size - i - 1 <= i);
	free(num_arr);
	free(current);
	return (1);
}
