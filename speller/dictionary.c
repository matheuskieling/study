// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
char word[LENGTH + 1];
struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
unsigned int word_count;
unsigned int hash_value;
// Returns true if word is in dictionary, else false
bool check(const char *word)
{
	hash_value = hash(word);
	node *cursor = table[hash_value];

	while (cursor != 0)
	{
		if (strcasecmp(word, cursor->word) == 0)
		{
			return true;
		}
		cursor = cursor->next;
	}
	return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
	// TODO: Improve this hash function
	unsigned long total = 0;
	for (int i = 0; i < strlen(word); i++)
	{
		total += tolower(word[i]);
	}
	return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
	// open dictionary file
	// use fopen
	FILE *dict_file = fopen(dictionary, "r");
	// check if return value is null
	if (dict_file == NULL)
	{
		printf("Unable to open %s\n", dictionary);
		return false;
	}
	// read strings from file one at a time
	// use loop for fscan f
	char word[LENGTH + 1];
	while (fscanf(dict_file, "%s", word) != EOF)
	{
		// allocate new node
		node *n = malloc(sizeof(node));
		// if n is NULL, return false
		if (n == NULL)
		{
			return false;
		}
		strcpy(n->word, word);
		hash_value = hash(word);
		n->next = table[hash_value];
		table[hash_value] = n;
		word_count++;
	}
	fclose(dict_file);
	return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
	// TODO
	if (word_count > 0)
	{
		return word_count;
	}
	return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
	for (int i = 0; i < N; i++)
	{
		node *cursor = table[i];
		while (cursor != NULL)
		{
			node *tmp = cursor;
			cursor = cursor->next;
			free(tmp);
		}
		if (cursor == NULL && i == N - 1)
		{
			return true;
		}
	}
	return false;
}
