#include <stdio.h>
#include <stddef.h>
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
	int i, j;
	int a[100];

	if (*head == NULL)
		return (1);

	current = *head;
	for (i = 0; current != NULL; i++)
	{
		a[i] = current->n;
		current = current->next;
	}
	i--;
	for (j = 0; j <= i + 1 / 2; j++, i--)
	{
		if (a[i] != a[j])
			return (0);
	}
	return (1);
}
