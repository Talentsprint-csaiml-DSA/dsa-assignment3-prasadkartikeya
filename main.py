import heapq
from collections import defaultdict

class Node:
    def _init_(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def _lt_(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap) from the frequencies
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman Tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new internal node with combined frequency
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the internal node back into the priority queue
        heapq.heappush(priority_queue, merged)

    # Return the root of the Huffman tree
    return priority_queue[0]

def generate_huffman_codes(root, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if root is not None:
        if root.char is not None:  # Leaf node
            codebook[root.char] = prefix
        generate_huffman_codes(root.left, prefix + "0", codebook)
        generate_huffman_codes(root.right, prefix + "1", codebook)

    return codebook

def huffman_coding(input_string):
    # Step 1: Count frequency of each character in the input string
    frequencies = defaultdict(int)
    for char in input_string:
        frequencies[char] += 1

    # Step 2: Build the Huffman Tree
    root = build_huffman_tree(frequencies)

    # Step 3: Generate Huffman codes for each character
    huffman_codes = generate_huffman_codes(root)

    # Step 4: Encode the input string by replacing each character with its Huffman code
    encoded_string = ''.join(huffman_codes[char] for char in input_string)

    return encoded_string

# Test case: huffman_coding('hello')
print(huffman_coding('hello'))  # Expected output: '1111100010'