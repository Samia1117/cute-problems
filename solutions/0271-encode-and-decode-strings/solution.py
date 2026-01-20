class Codec:
    # approach 1: using non-ASCII character as delimiter
    delimiter = "å"

    # approach 2: escaping
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        return Codec.delimiter.join(strs)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        str_list = s.split(Codec.delimiter)
        return str_list
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
