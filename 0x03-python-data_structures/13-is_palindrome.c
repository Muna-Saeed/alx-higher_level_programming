#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *node = *head, *next, *prev = NULL;

    while (node)
    {
        next = node->next;
        node->next = prev;
        prev = node;
        node = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half;
    int is_palindrome = 1;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    second_half = reverse_listint(&slow);
    listint_t *temp1 = *head;
    listint_t *temp2 = second_half;

    while (temp2 != NULL)
    {
        if (temp1->n != temp2->n)
        {
            is_palindrome = 0;
            break;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    reverse_listint(&second_half);
    prev_slow->next = second_half;

    return is_palindrome;
}
