import hashlib

def sha256_int(s: bytes) -> int:
    return int.from_bytes(hashlib.sha256(s).digest(), "big")

def blake2b_int(s: bytes) -> int:
    return int.from_bytes(hashlib.blake2b(s, digest_size=32).digest(), "big")


class MultiArrayBloom:
    def __init__(self, size=100):
        self.size = size
        self.hash_functions = [sha256_int, blake2b_int]
        # one array per hash function, all same size
        self.bit_arrays = [[0] * size for _ in self.hash_functions]

    def _positions(self, item: bytes):
        for fn in self.hash_functions:
            yield fn(item) % self.size

    def add(self, item: bytes):
        for arr, pos in zip(self.bit_arrays, self._positions(item)):
            arr[pos] = 1

    def __contains__(self, item: bytes):
        return all(arr[pos] == 1 for arr, pos in zip(self.bit_arrays, self._positions(item)))


# Demo
if __name__ == "__main__":
    bloom = MultiArrayBloom(size=10)
    mylist = []

    def add_to_list(x: str):
        xb = x.encode("utf-8")
        if xb in bloom:
            print(f"'{x}' is probably already present (skip).")
        else:
            print(f"'{x}' not seen → adding.")
            bloom.add(xb)
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
