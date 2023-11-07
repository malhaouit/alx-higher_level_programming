#include "lists.h"
#include <stdlib.h>

/**
 * initialize_array - Initialize array by numbers in nodes
 * @numbers: The dynamic array
 * @current: A pointer to iterate over the list of nodes
 *
 * Return: The number of nodes
 */
int initialize_array(int *numbers, listint_t *current)
{
	int n = 0;

	while (current != NULL)
	{
		numbers[n] = current->n;
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * is_palindrome - Checks if the linked list is palindrome or not
 * @head: A pointer to pointer to the first node of the linked list
 *
 * Return: 1 if the likendlist is palindrome, or 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *numbers;
	int n;
	int i = 0, j;

	if (head == NULL || *head == NULL)
		return (1);

	numbers = malloc(sizeof(int) * 1024);
	current = *head;

	n = initialize_array(numbers, current);
	
	j = n - 1;

	while (i < n / 2)
	{
		if (numbers[i++] != numbers[j--])
		{
			free(numbers);
			return (0);
		}
	}
	
	free(numbers);
	return (1);
}
