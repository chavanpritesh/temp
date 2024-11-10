import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

def build_huffman_tree(chars, freq):
    nodes = []
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = 0
        right.huff = 1
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    return nodes[0]

def get_user_input():
    chars = input("Enter characters separated by spaces: ").split()
    freq = list(map(int, input("Enter frequencies corresponding to the characters, separated by spaces: ").split()))

    if len(chars) != len(freq):
        raise ValueError("The number of characters must match the number of frequencies.")

    return chars, freq

def main():
    try:
        chars, freq = get_user_input()
        root = build_huffman_tree(chars, freq)
        print("Huffman Codes:")
        print_nodes(root)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
