#include "lists.h"
/**
 * check_cycle - a function in C that checks if a singly
 * linked list has a cycle in it.
 * @list:  a list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *start;
	listint_t *cycle;

	if (list == NULL)
		return (0);

	start = list;
	cycle = list->next;
	while (cycle->next != NULL)
	{
		if (cycle->n == start->n && cycle->next == start->next)
			return (1);
		cycle = cycle->next;
	}
	return (0);
}
