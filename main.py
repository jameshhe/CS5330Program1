# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class LinearHashing:
    def __init__(self, pageSize, policy=0, maxOverflow=0, sizeLimit=1.0):
        self.pageSize = pageSize  # the maximum number of integers that can be stored in a bucket
        self.policy = policy  # denoting when should a split occurs
        self.maxOverflow = maxOverflow  # the limit of the number of overflow buckets for option 1 only
        self.sizeLimit = sizeLimit  # the capacity of the hash table before splitting occurs for option 2 only

        self.pages = [[]]  # initialize the pages
        self.isSplit = [False]  # keeps track of which bucket has been split

        self.level = 0  # the current level of hashing
        self.pointer = 0  # Points to the next bucket to be split

        if not self.parameters_are_valid(): raise ValueError("Parameters are invalid!")

    def parameters_are_valid(self):
        return self.pageSize > 0 and 0 <= self.policy <= 3 and self.maxOverflow >= 0 and self.sizeLimit >= 0

    def insert(self, x: int) -> bool:  # insert x into the hash table
        index = self.get_insert_index(x, self.level)

        # check if the current bucket size is less than the page size, if it is insert
        if len(self.pages[index]) < self.pageSize:
            self.pages[index].append(x)
            # get the index to append to
            return False
        else:  # otherwise, we need to split
            # a level finishes when all the buckets at the current level is split
            self.split()
            index = self.get_insert_index(x, self.level)
            self.pages[index].append(x)
            return True
        # returns true if a split happens, false if not

    def update_table(self):
        if len(self.pages) < 2 ** self.level:
            # add buckets
            for i in range(len(self.pages), 2 ** self.level):
                self.pages.append([])
                self.isSplit.append(False)

    def get_insert_index(self, x, lastNDigit) -> int:
        if self.level == 0:
            return 0
        # convert to binary and get the last (level) digits
        binary = "{0:b}".format(x)
        binary = binary[-lastNDigit:]
        # convert string binary number to int
        index = int(binary, 2)
        return index

    def split(self):
        # split the bucket that self.pointer is pointing to instead of the overflow bucket
        # add 0 and 1 to the current cell
        # add 0 would make no difference
        # add 1 would mean 2 ^ (curr.level) + self.pointer.
        # For example, adding a 1 in front of 11 would be 111 (binary) => 7 (decimal) => 2 ^ 2 + decimal(11)
        # go through every single entry in self.pointer and see what needs to be moved
        newCell = 2 ** self.level + self.pointer
        self.pages.append([])
        # turn isSplit to true because we're splitting the cell that the pointer is referring to
        self.isSplit[self.pointer] = True
        # if we're not done with the current level, increment the level by 1
        if False in self.isSplit[:newCell]:
            self.pointer += 1
        # otherwise, reset the pointer to 0 and allocate new space
        else:
            self.pointer = 0
            self.level += 1
            self.update_table()
        for num in self.pages[self.pointer]:
            # we're now looking at one more last digit than the current level
            # if the current level is 0, we need to get the last 2 digits for example
            insert_index = self.get_insert_index(num, self.level)
            # move the number to the new index
            if insert_index != self.pointer:
                self.pages[self.pointer].remove(num)
                self.pages[insert_index].append(num)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lh = LinearHashing(3)
    for number in [14, 7, 8, 15, 11, 1]:
        lh.insert(number)
        print(lh.pages)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
