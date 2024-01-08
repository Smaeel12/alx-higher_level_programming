#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
/**
 * lenght_calculate - calculate the lenght of an array
 * @array: an pointer to an array
 * Return: the lenght of the array
 */
int lenght_calculate(int *array)
{
	int lenght = 0;

	while (array[lenght] != '\0')
		lenght += 1;
	return (lenght);
}
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
	int i, lenght;
	int array[1024];

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	for (i = 0; current != NULL; i++)
	{
		array[i] = current->n;
		current = current->next;
	}
	array[i] = '\0';
	lenght = lenght_calculate(array);
	if (lenght % 2 != 0)
		return (0);
	for (i = 0; i < lenght / 2; i++)
	{
		if (array[i] != array[lenght - i - 1])
			return (0);
	}
	return (1);
}
