
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        categorie = {}

        for element in strs:

            count = {}

            # Count each letter
            for letter in element:
                count[letter] = count.get(letter, 0) + 1

            # Convert dictionary to something hashable
            key = tuple(sorted(count.items()))

            # Create category if it doesn't exist
            if key not in categorie:
                categorie[key] = []

            # Add word to its category
            categorie[key].append(element)

        return list(categorie.values())

