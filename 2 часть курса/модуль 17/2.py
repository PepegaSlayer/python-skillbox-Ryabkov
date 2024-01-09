from typing import List, Tuple

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5]

def merge_lists(lst1: List[str], lst2: List[int]) -> List[Tuple[str, int]]:
    merged_list = []
    for i in range(min(len(lst1), len(lst2))):
        merged_list.append((lst1[i], lst2[i]))
    return merged_list

results = merge_lists(letters, numbers)

print(results) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]