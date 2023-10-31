#include "lists.h"

/**
 * check_cycle - Checks a singly linked lists if contains any cycle
 * @list: A pointer to the first node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	int counter = 0;

	if (!list)
		return (0);

	current = list;

	while (current != NULL)
	{
		current = current->next;

		if (current == list)
		{
			counter++;
			break;
		}
	}

	if (counter)
		return (1);

	return (0);
}
