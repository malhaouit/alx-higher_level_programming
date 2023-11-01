#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to a pointer to the first node
 * @number: The number stored in the node
 *
 * Return: New node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;
		listint_t *previous = NULL;

		while (current != NULL && number > current->n)
		{
			previous = current;
			current = current->next;
		}

		previous->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
