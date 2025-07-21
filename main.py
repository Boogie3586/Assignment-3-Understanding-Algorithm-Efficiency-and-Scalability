from quicksort.randomized_quicksort import randomized_quicksort
from quicksort.deterministic_quicksort import deterministic_quicksort
from hashtable.hash_table import HashTable

def test_quicksort():
    print("=== Part 1: Quicksort ===\n")
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", test_arr)
    print("Randomized Quicksort:", randomized_quicksort(test_arr.copy()))
    print("Deterministic Quicksort:", deterministic_quicksort(test_arr.copy()))

def test_hashtable():
    print("\n=== Part 2: Hash Table with Chaining ===\n")
    ht = HashTable(size=5)
    ht.insert("apple", 5)
    ht.insert("banana", 3)
    ht.insert("orange", 7)
    ht.insert("grape", 2)

    print("Hash Table contents:")
    print(ht)
    print("\nSearch for 'banana':", ht.search("banana"))
    print("Deleting 'banana'...")
    ht.delete("banana")
    print("After deletion:")
    print(ht)

if __name__ == "__main__":
    test_quicksort()
    test_hashtable()
