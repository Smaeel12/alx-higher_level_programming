#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function in C that checks
 * if a singly linked list is a palindrome.
 * @head: singly linked list node structure
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, lenght, size = 1024;
	int *array;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	array = malloc(size * sizeof(int));
	if (array == NULL)
		return (-1);
	for (i = 0; current != NULL; i++)
	{
		array[i] = current->n;
		if (i == 1024)
		{
			size = size + 1024;
			array = realloc(array, size * sizeof(int));
			if (array == NULL)
			{
				free(array);
				return (-1);
			}
		}
		current = current->next;
	}
	lenght = i - 1;
	for (i = 0; i <= lenght; i++, lenght--)
	{
		if (array[i] != array[lenght])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
