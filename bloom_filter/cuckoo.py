import hashlib
import random

class CuckooFilter:
    """
    A simple implementation of a Cuckoo Filter.
    """

    def __init__(self, capacity=1000, bucket_size=4, max_kick_attempts=500):
        self.capacity = capacity
        self.num_buckets = int(capacity / bucket_size) + 10  
        self.bucket_size = bucket_size
        self.max_kick_attempts = max_kick_attempts
        
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self, item):
        h1 = int(hashlib.sha1(item.encode()).hexdigest(), 16)
        h2 = int(hashlib.sha1((item + "salt").encode()).hexdigest(), 16)
        idx1 = h1 % self.num_buckets
        idx2 = (h1 ^ h2) % self.num_buckets # A common trick to get a second, independent hash
        fingerprint = h1 % (2**16) # A 16-bit fingerprint for this example.
        return idx1, idx2, fingerprint

    def add(self, item):
        idx1, idx2, fingerprint = self._hash(item)

        # 1. Try to add the fingerprint to the first possible bucket.
        if len(self.buckets[idx1]) < self.bucket_size:
            self.buckets[idx1].append(fingerprint)
            return True

        # 2. If the first bucket is full, try the second one.
        if len(self.buckets[idx2]) < self.bucket_size:
            self.buckets[idx2].append(fingerprint)
            return True

        # 3. Both buckets are full. Time to "cuckoo"!
        # We start a loop to find a spot by kicking out other items.
        # We have a limited number of attempts to avoid infinite loops.
        for _ in range(self.max_kick_attempts):
            # Randomly choose one of the two buckets to perform the kick.
            # This helps to avoid getting stuck in a cycle.
            if random.random() < 0.5:
                current_idx = idx1
            else:
                current_idx = idx2

            # Pick a random fingerprint to kick out of the chosen bucket.
            kick_out_fingerprint = self.buckets[current_idx].pop(random.randint(0, self.bucket_size - 1))
            
            # The new item (our original fingerprint) now takes its place.
            self.buckets[current_idx].append(fingerprint)
            
            # The kicked-out fingerprint now becomes the one we need to find a home for.
            fingerprint = kick_out_fingerprint

            # Calculate the kicked-out fingerprint's alternate bucket index.
            # This is a key step: we use the fingerprint to find its other possible location.
            # This is why we use (h1 ^ h2) in the _hash function, as it allows us to reverse the calculation.
            alternate_idx = (current_idx ^ (fingerprint % self.num_buckets)) % self.num_buckets
            
            # Now, we try to place the kicked-out fingerprint in its alternate bucket.
            if len(self.buckets[alternate_idx]) < self.bucket_size:
                self.buckets[alternate_idx].append(fingerprint)
                return True
            else:
                # The alternate bucket is also full. We continue the loop with the new alternate index.
                # In the next iteration, the kicked-out item becomes the new "item to add".
                idx1, idx2 = current_idx, alternate_idx

        # If we reach this point, it means we failed to find a spot after
        # max_kick_attempts. The filter is considered "full" and needs to be resized.
        print("Cuckoo filter is full. A rebuild or resizing is required.")
        return False

    def contains(self, item):
        """
        Checks if an item is possibly in the filter.
        """
        idx1, idx2, fingerprint = self._hash(item)

        # Check if the fingerprint exists in either of the two possible buckets.
        if fingerprint in self.buckets[idx1] or fingerprint in self.buckets[idx2]:
            return True
        
        return False

    def remove(self, item):
        """
        Removes an item from the filter. This is a key advantage of Cuckoo Filters.
        """
        idx1, idx2, fingerprint = self._hash(item)

        # Check the first bucket.
        if fingerprint in self.buckets[idx1]:
            self.buckets[idx1].remove(fingerprint)
            return True

        # Check the second bucket.
        if fingerprint in self.buckets[idx2]:
            self.buckets[idx2].remove(fingerprint)
            return True

        return False # Item not found

if __name__ == "__main__":
    cf = CuckooFilter(capacity=100) # A small filter for demonstration

    items_to_add = ["apple", "banana", "orange", "grape", "kiwi", "melon", "cherry", "pear", "mango", "peach"]
    
    print("Adding items...")
    for item in items_to_add:
        if cf.add(item):
            print(f"'{item}' added successfully.")
        else:
            print(f"Failed to add '{item}'. Filter is full.")

    print("\n--- Checking for items ---")

    print(f"Is 'apple' in the filter? {cf.contains('apple')}")

    print(f"Is 'watermelon' in the filter? {cf.contains('watermelon')}")

    print(f"Is 'kiwi' in the filter? {cf.contains('kiwi')}")

    print("\n--- Removing 'grape' ---")
    if cf.remove("grape"):
        print("'grape' removed successfully.")
    print(f"Is 'grape' in the filter? {cf.contains('grape')}")
    
    # Adding a new item that might trigger cuckooing
    print("\n--- Adding more items to trigger cuckooing ---")
    new_items = ["blueberry", "strawberry", "raspberry", "blackberry", "lemon", "lime"]
    for item in new_items:
        if cf.add(item):
            print(f"'{item}' added.")
        else:
            print(f"Failed to add '{item}'.")
