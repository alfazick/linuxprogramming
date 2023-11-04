class CowList:
    def __init__(self, original_list):
        self.original_list = original_list
        self.modified_indices = {}

    def __getitem__(self, index):
        # If index has been modified, return the modified value, otherwise return the value from the original list
        if index in self.modified_indices:
            return self.modified_indices[index]
        return self.original_list[index]

    def __setitem__(self, index, value):
        # The "write" happens here; we record the modification in the dictionary, creating an actual copy of that element
        self.modified_indices[index] = value

    def __str__(self):
        final_list = []

        # Construct the final list using an explicit loop, checking each index for modifications
        for i in range(len(self.original_list)):
            if i in self.modified_indices:
                final_list.append(self.modified_indices[i])
            else:
                final_list.append(self.original_list[i])

        return str(final_list)


# Creating an original list
original_list = [1, 2, 3, 4, 5]

# Creating a COW list based on the original list
cow_list = CowList(original_list)

# Displaying the COW list (it should match the original list)
print("COW List before modification: ", cow_list)

# Modifying an element in the COW list (this will trigger an actual copy of the modified element)
cow_list[2] = 99

# Displaying the COW list and the original list to demonstrate that the original list remains unchanged
print("COW List after modification:  ", cow_list)
print("Original list:                ", original_list)
