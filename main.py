# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class LinearHashing:
    def __init__(self, pageSize, policy=0, maxOverflow=0, sizeLimit=1.0):
        self.pageSize = pageSize # the maximum number of integers that can be stored in a bucket
        self.policy = policy # denoting when should a split occurs
        self.maxOverflow = maxOverflow # the limit of the number of overflow buckets for option 1 only
        self.sizeLimit = sizeLimit # the capacity of the hash table before splitting occurs for option 2 only

        self.pages = [] # initialize the pages

        self.level = 0 # the current level of hashing
        self.pointer = 0 # Points to the next bucket to be split

        if not self.parameters_are_valid(): raise ValueError("Parameters are invalid!")

    def parameters_are_valid(self):
        return self.pageSize > 0 and 0 <= self.policy <= 3 and self.maxOverflow >= 0 and self.sizeLimit >= 0

    def insert(self, x: int) -> bool: # insert x into the hash table
        # update the table based on the current level if needed
        self.update_table()
        # get the index to append to
        index = self.get_insert_index(x)
        # returns true if a split happens, false if not

    def update_table(self):
        if len(self.pages) < 2 ** self.level:
            # add buckets
            for i in range(len(self.pages), 2 ** self.level):
                self.pages.append([])

    def get_insert_index(self, x):
        # convert to binary and get the last (level) digits
        binary = "{0:b}".format(x)
        binary = binary[-self.level-1:]
        # convert the binary back to decimal to get the index
        index = int(str(binary))
        return index

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lh = LinearHashing(3)
    lh.insert(10)
    print(lh.pages)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
