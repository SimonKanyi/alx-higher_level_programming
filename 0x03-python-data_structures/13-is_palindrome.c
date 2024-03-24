#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *mid_node = NULL;
    listint_t *second_half = NULL;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL) /* odd number of nodes, move slow one step forward */
    {
        mid_node = slow;
        slow = slow->next;
    }

    second_half = reverse_list(&slow);

    palindrome = compare_lists(*head, second_half);

    if (mid_node != NULL) /* restore original list if it was modified */
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow->next = reverse_list(&second_half);
    }

    return palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the linked list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *next = NULL;
    listint_t *current = *head;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}

/**
 * compare_lists - compares two linked lists for equality
 * @list1: pointer to the head of the first linked list
 * @list2: pointer to the head of the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;
        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}
