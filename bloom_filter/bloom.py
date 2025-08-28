import hashlib
 
def sha256_int(s: bytes) -> int:
    return int.from_bytes(hashlib.sha256(s).digest(), "big")

def blake2b_int(s: bytes) -> int:
    return int.from_bytes(hashlib.blake2b(s, digest_size=32).digest(), "big")


class SimpleBloom:
    def __init__(self, size=100):
        self.size = size               
        self.hash_functions = [sha256_int, blake2b_int]
        self.bit_array = [0] * size

    def _hashes(self, item: bytes):
        for function in self.hash_functions:
            yield function(item) % self.size

    def add(self, item: bytes):
        for pos in self._hashes(item):
            self.bit_array[pos] = 1

    def __contains__(self, item):
        return all(self.bit_array[pos] for pos in self._hashes(item))

# Demo
if __name__ == "__main__":
    bloom = SimpleBloom(size=10)
    mylist = []

    def add_to_list(x):
        x = x.encode('utf-8')
        
        if x in bloom:
            print(f"'{x}' is probably already present (skip adding).")
        else:
            print(f"'{x}' not seen before → adding.")
            bloom.add(x)
            mylist.append(x)

    add_to_list("apple")
    add_to_list("banana")
    add_to_list("apple") 
    add_to_list("cherry")
    add_to_list("cherrys")
    add_to_list("cherryq")
    add_to_list("cherryqq")
    add_to_list("cherryqqq")
    add_to_list("cherryqqqq")
    add_to_list("cherryqww")
    add_to_list("cherryqw")
    

    print("Final list:", mylist)
