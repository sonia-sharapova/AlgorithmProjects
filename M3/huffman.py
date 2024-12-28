from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering

from bitstring import Bits

import functools



class HuffmanCodec:
    """Codec (encoder/decoder) for a specific Huffman code.

    Examples
    --------
    ASCII requires 424 bits to encode this test string.
    >>> test_string = "David Huffman invented Huffman coding at MIT in 1952."
    >>> ascii_encoding = test_string.encode(encoding="ascii")
    >>> len(Bits(ascii_encoding))
    424

    Our HuffmanCodec should produce a more efficient encoding than ASCII.
    We should be able to encode, decode, and get the same string back.
    >>> from collections import Counter
    >>> frequency_map = Counter(test_string)
    >>> codec = HuffmanCodec(frequency_map)
    >>> huffman_encoding = codec.encode(test_string)
    >>> len(huffman_encoding)
    226
    >>> codec.decode(huffman_encoding)
    'David Huffman invented Huffman coding at MIT in 1952.'

    The HuffmanCodec should throw an error if we ask it to encode unfamiliar symbols:
    >>> codec.encode("y = 19x + 52 + c")
    Traceback (most recent call last):
      ...
    ValueError: Unsupported symbol: 'y'

    It should also throw an error if we ask it to decode some data which it did not encode:
    >>> garbage_bits = Bits(bin="0b1")
    >>> codec.decode(huffman_encoding + garbage_bits)
    Traceback (most recent call last):
      ...
    ValueError: Could not decode.
    """

    def __init__(self, frequency_map: dict[str, float]):
        """Constructs a HuffmanCodec for the given distribution of source symbols.

        Parameters
        ----------
        frequency_map : dict[str, float]
            Distribution of source symbols
        """
        self.root = HuffmanCodec._build_tree(frequency_map=frequency_map)
        self.code = self._get_code()

    def encode(self, source_data: str) -> Bits:
        """Encodes the given source data.

        Parameters
        ----------
        source_data : str
            String over source alphabet.

        Returns
        -------
        encoded_bits : Bits
            Encoded source data.

        Raises
        ------
        ValueError
            If source_data contains symbols which are unsupported by the codec.
        """
        try:
            return Bits().join(self.code[symbol] for symbol in source_data)
        except KeyError as err:
            raise ValueError(f"Unsupported symbol: {err.args[0]!r}")

    def decode(self, encoded_data: Bits) -> str:
        """Decodes the given string.

        Parameters
        ----------
        encoded_data : Bits
            Bitstring containing some encoded data.

        Returns
        -------
        source_data : str
            Original source data.

        Raises
        ______
        ValueError
            If encoded_data contains bits which could not be decoded.
        """
        # TODO

        result, node = [], self.root
        for bit in encoded_data:
            node = node.left if bit == 0 else node.right
            if node.is_leaf:
                result.append(node.symbol)
                node = self.root
        return ''.join(result)

    @staticmethod
    def _build_tree(frequency_map: dict[str, float]) -> TreeNode:
        """Builds the Huffman tree and returns the root TreeNode.

        Parameters
        ----------
        frequency_map : dict[str, float]
            Distribution of source symbols.

        Returns
        -------
        TreeNode
            Root node of resulting tree.
        """
        # TODO

        def compare_nodes(node1: TreeNode, node2: TreeNode):
            if node1.weight != node2.weight:
                return -1 if node1.weight < node2.weight else 1
    
            return 0  # Order doesnt matter when weughts are equal. 

        # get nodes from the tree
        nodes = [TreeNode(symbol, weight) for symbol, weight in frequency_map.items()]

        while len(nodes) > 1:
            nodes.sort(key=functools.cmp_to_key(compare_nodes))
            left = nodes.pop(0)
            right = nodes.pop(0)
            # merge the nodes
            merged = TreeNode(None, left.weight + right.weight, left, right)
            nodes.append(merged)
        return nodes[0]


    def _get_code(self) -> dict[str, Bits]:
        """Returns the Huffman code represented by this tree.

        Returns
        -------
        code : dict[str, Bits]
            Dictionary mapping source symbols to code words.
        """
        # TODO

        def build_code(node: TreeNode, prefix: Bits):
            if node.is_leaf:
                return {node.symbol: prefix}
            code = {}
            if node.left:
                # 0b0: This is a string that represents the binary digit 0. 
                # Moving to a left child corresponds to adding a '0' to the current code. 
                code.update(build_code(node.left, prefix + '0b0'))
            if node.right:
                # 0b1: String that represents the binary digit 1. 
                # Moving to a right child corresponds to adding a '1' to the current code.
                code.update(build_code(node.right, prefix + '0b1'))
            return code
        # recursion
        return build_code(self.root, Bits())


@total_ordering
@dataclass(eq=False)
class TreeNode:
    symbol: str
    weight: float
    left: TreeNode | None = None
    right: TreeNode | None = None

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __lt__(self, other: TreeNode) -> bool:
        return (self.weight, self.symbol) < (other.weight, other.symbol)

    def __eq__(self, other: TreeNode) -> bool:
        return (self.weight, self.symbol) == (other.weight, other.symbol)


if __name__ == "__main__":
    import doctest
    doctest.testmod()