from typing import List, Tuple

def can_be_poly(s: str) -> bool:
    count_map = {}
    for char in s:
        if char in count_map:
            count_map[char] += 1
        else:
            count_map[char] = 1

    odd_count = sum(1 for count in count_map.values() if count % 2 != 0)
    return odd_count <= 1


print(can_be_poly('abcba')) # True
print(can_be_poly('abbbc')) # False