# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class LinearHashing:
    def __init__(self, pageSize, policy=0, maxOverflow=0, sizeLimit=1.0):
        self.pageSize = pageSize # the maximum number of integers that can be stored in a bucket
        self.policy = policy # denoting when should a split occurs
        self.maxOverflow = maxOverflow # the limit of the number of overflow buckets for option 1 only
        self.sizeLimit = sizeLimit # the capacity of the hash table before splitting occurs for option 2 only

        if not self.parameters_are_valid(): raise ValueError("Parameters are invalid!")

    def parameters_are_valid(self):
        return self.pageSize > 0 and 0 <= self.policy <= 3 and self.maxOverflow >= 0 and self.sizeLimit >= 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lh = LinearHashing(3, -3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
