import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash=None, previous_block=None):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.previous_block = previous_block
      self.hash = self.calc_hash()

    def set_previous(self, previous_block):
        self.previous_hash = previous_block.get_hash()
        self.previous_block = previous_block

    def get_previous(self):
        return self.previous_block

    def get_data(self):
        return self.data

    def get_hash(self):
        return self.hash

    def check_integrity(self):
        if self.previous_hash == self.previous_block.get_hash():
            return True
        else:
            return False

    def calc_hash(self):
        sha = hashlib.sha256()

        data = str(self.timestamp) + str(self.data)

        hash_str = data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class LinkedList:
    def __init__(self, tail=None):
        self.tail = tail

    def append(self, timestamp, data):
        if self.tail is None:
            self.tail = Block(timestamp, data)
            return

        # Move to the tail (the last node)
        node = self.tail
        while node.previous_block:
            node = node.previous_block

        node.previous_block = Block(timestamp, data)
        node.previous_hash = node.previous_block.get_hash()
        return


# Example 1
blockchain_tail = Block(time.time(),'djlsdjfldkj')
blockchain_list = LinkedList(blockchain_tail)
blockchain_list.append(time.time(), 'this is data')
print(blockchain_tail.get_previous().get_data())

#Check if data has been tampered with
print(blockchain_tail.check_integrity()) #returns True - hash data is correct

#Example 2
blockchain_tail_2 = Block(time.time(),'dogs are cute')
blockchain_list_2 = LinkedList(blockchain_tail_2)
blockchain_list_2.append(time.time(), 'cats are also cute')
#tamper with the data
blockchain_list_2.tail.get_previous().hash = 'sdfjdsljflk'

#Check if data has been tampered with
print(blockchain_tail_2.check_integrity()) #returns False - hash data has been changed

#Example 3
blockchain_tail_3 = Block(time.time(),'horses are cute')
blockchain_list_3 = LinkedList(blockchain_tail_3)
blockchain_list_3.append(time.time(), 'donkeys are also cute')
blockchain_list_3.append(time.time(), 'mules are also cute')
print(blockchain_tail_3.get_previous().get_previous().get_data())
print(blockchain_tail_3.get_previous().get_data())

#edge cases
blockchain_tail_4 = Block(time.time(), 8989898) #converts value to string
blockchain_list_4 = LinkedList(blockchain_tail_4)
blockchain_list_4.append(time.time(), False)
print(blockchain_tail_4.get_data()) #returns 8989898
print(blockchain_tail_4.get_previous().get_data()) #returns False