#ifndef HASH_TABLES_H
#define HASH_TABLES_H

#include <stdlib.h>

/* Data structure for a hash node */
typedef struct hash_node_s
{
    char *key;                  /* Key for the node */
    char *value;                /* Value stored in the node */
    struct hash_node_s *next;   /* Pointer to the next node in case of collision */
} hash_node_t;

/* Data structure for a hash table */
typedef struct hash_table_s
{
    size_t size;                /* Size of the hash table array */
    hash_node_t **array;        /* Array of hash nodes */
} hash_table_t;

/* Function prototypes */
hash_table_t *hash_table_create(unsigned long int size);

#endif /* HASH_TABLES_H */
