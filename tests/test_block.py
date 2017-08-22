import unittest
import hashlib

class Block(object):
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calc_hash()

    def __str__(self):
        return str(self.index) + self.previous_hash + str(self.timestamp) + self.data

    def has_valid_index(self, prev_block):
         return self.index == prev_block.index + 1

    def has_valid_hash(self):
        return self.hash == self.calc_hash()

    def calc_hash(self):
        return hashlib.sha256(str(self).encode()).hexdigest()


class TestBlockTest(unittest.TestCase):

    def test_valid_index(self):
        prev_block = Block(0, '0', 1, 'first block')
        block = Block(1, '0', 1, 'second block')
        self.assertTrue(block.has_valid_index(prev_block))

    def test_invalid_index(self):
        prev_block = Block(0, '0', 1, 'first block')
        block = Block(2, '0', 1, 'second block')
        self.assertFalse(block.has_valid_index(prev_block))

    def test_has_valid_hash(self):
        block = Block(1, '0', '0', 'first block')
        self.assertTrue(block.has_valid_hash())

if __name__ == '__main__':
    unittest.main()