#include "hash_tables.h"

/**
 * hash_table_create - Creates a hash table
 * @size: Size of the array
 * Return: Pointer to the newly created hash table, or NULL if failed
 */
hash_table_t *hash_table_create(unsigned long int size)
{
    hash_table_t *hash_table = NULL;
    size_t i;

    /* Allocate memory for the hash table structure */
    hash_table = malloc(sizeof(hash_table_t));
    if (hash_table == NULL)
        return NULL;

    /* Allocate memory for the array of hash nodes */
    hash_table->array = malloc(sizeof(hash_node_t *) * size);
    if (hash_table->array == NULL)
    {
        free(hash_table); /* Free hash_table if malloc fails */
        return NULL;
    }

    /* Initialize each element of the array to NULL */
    for (i = 0; i < size; i++)
        hash_table->array[i] = NULL;

    hash_table->size = size;

    return hash_table;
}

