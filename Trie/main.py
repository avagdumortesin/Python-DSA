from trie import Trie


insertions = [ "CAT", "DOG", "BIRD", "FISH", "HAMSTER", "SNAKE" ]
searches = [
    "CAT", "BAT", "RAT", "HIPPOPOTAMUS", "HAMSTER", "FERRET", "OCTOPUS"
]

# Create a trie and insert some strings
trie = Trie()
for string_to_insert in insertions:
    print(f"Inserting \"{string_to_insert}\"")
    trie.insert(string_to_insert)

# Search for various strings, displaying the number of nodes visited during
# each search
for search_string in searches:
    contains_result = trie.contains_with_count(search_string)
    found = contains_result[ 0 ]
    num_nodes_visited = contains_result[ 1 ]

    print(f"Search for \"{search_string}\" returned ", end="")
    print("True" if found else "False", end="")
    print(f" and visited {num_nodes_visited} node", end="")
    if num_nodes_visited != 1:
        print("s", end="")
    print()
