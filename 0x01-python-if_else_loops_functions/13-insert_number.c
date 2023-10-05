#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode = createNode(number);

    if (newNode == NULL)
    {
        return NULL;
    }

    if (*head == NULL || number < (*head)->data)
    {
        newNode->next = *head;
        *head = newNode;
    }
    else
    {
        listint_t *current = *head;

        while (current->next != NULL && number > current->next->data)
        {
            current = current->next;
        }

        newNode->next = current->next;
        current->next = newNode;
    }

    return newNode;
}
