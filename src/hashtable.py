# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None


class HashTable:
	"""
	A hash table that with `capacity` buckets
	that accepts string keys
	"""

	
	def __init__(self, capacity):
		self.capacity = capacity  # Number of buckets in the hash table
		self.storage = [None] * capacity

	def _hash(self, key):
		"""
		Hash an arbitrary key and return an integer.

		You may replace the Python hash with DJB2 as a stretch goal.
		"""
		return hash(key)

	def _hash_djb2(self, key):
		"""
		Hash an arbitrary key using DJB2 hash

		OPTIONAL STRETCH: Research and implement DJB2
		"""
		pass

	def _hash_mod(self, key):
		"""
		Take an arbitrary key and return a valid integer index
		within the storage capacity of the hash table.
		"""
		return self._hash(key) % self.capacity

	def insert(self, key, value):
		#region
		"""
		Store the value with the given key.

		# Part 1: Hash collisions should be handled with an error warning. (Think about and
		# investigate the impact this will have on the tests)

		# Part 2: Change this so that hash collisions are handled with Linked List Chaining.

		Fill this in.
		"""
		#endregion

		getloc = self._hash_mod(key)

		#if this location is empty
		if self.storage[getloc] == None:
			#put a new LP here
			self.storage[getloc] = LinkedPair(key,value)
			#BOUNCE
			return
		
		##### from this point forward, we know the location was not empty
		lp = self.storage[getloc]
		#run all existing linked pairs
			#if THIS key matches the insertion key
				#drop the value
			#else if a NEXT exists
				# go to next linked pair
			#else (there's no next)
				# put current keyValue into the next

		

	def remove(self, key):
		#region
		"""
		Remove the value stored with the given key.

		Print a warning if the key is not found.

		Fill this in.
		"""

		#endregion

		# gethash = self._hash(key)
		getloc = self._hash_mod(key)

		if self.storage[getloc] == None:
			print("nothing to remove")
			return "nothing to remove"
		
		self.storage[getloc] = None

	def retrieve(self, key):
		#region
		"""
		Retrieve the value stored with the given key.

		Returns None if the key is not found.

		Fill this in.
		"""
		#endregion

		# gethash = self._hash(key)
		getloc = self._hash_mod(key)

		if self.storage[getloc] == None:
			print("empty location")
			return None
		
		return self.storage[getloc]

	def resize(self):
		#region
		"""
		Doubles the capacity of the hash table and
		rehash all key/value pairs.

		Fill this in.
		"""
		#endregion

		self.capacity *= 2
		oldstore = self.storage
		self.storage = [None] * self.capacity

		for item in oldstore:
			if item == None:
				continue

			oldkey = item[0]
			oldval = item[1]
			
			self.insert(oldkey, oldval)




if __name__ == "__main__":
	ht = HashTable(2)

	ht.insert("line_1", "Tiny hash table")
	ht.insert("line_2", "Filled beyond capacity")
	ht.insert("line_3", "Linked list saves the day!")

	print("")

	# Test storing beyond capacity
	print(ht.retrieve("line_1"))
	print(ht.retrieve("line_2"))
	print(ht.retrieve("line_3"))

	# Test resizing
	old_capacity = len(ht.storage)
	ht.resize()
	new_capacity = len(ht.storage)

	print(f"\nResized from {old_capacity} to {new_capacity}.\n")

	# Test if data intact after resizing
	print(ht.retrieve("line_1"))
	print(ht.retrieve("line_2"))
	print(ht.retrieve("line_3"))

	print("")
