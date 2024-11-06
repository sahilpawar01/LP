# Python3 program for next fit
# memory management algorithm

# Function to allocate memory to
# blocks as per Next fit algorithm
def NextFit(blockSize, m, processSize, n):
		
	# Stores block id of the block
	# allocated to a process

	# Initially no block is assigned
	# to any process
	allocation = [-1] * n
	j = 0
	t = m-1
	# pick each process and find suitable blocks
	# according to its size ad assign to it
	for i in range(n):

		# Do not start from beginning
		while j < m:
			if blockSize[j] >= processSize[i]:
				
				# allocate block j to p[i] process
				allocation[i] = j
				
				# Reduce available memory in this block.
				blockSize[j] -= processSize[i]
				
				# sets a new end point
				t = (j - 1) % m
				break
			if t == j:
				# sets a new end point
				t = (j - 1) % m
				# breaks the loop after going through all memory block
				break
			
			# mod m will help in traversing the
			# blocks from starting block after
			# we reach the end.
			j = (j + 1) % m
			
	print("Process No. Process Size Block no.")
	
	for i in range(n):
		print("\t", i + 1, "\t\t\t", processSize[i],end = "\t\t\t")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")

# Driver Code
if __name__ == '__main__':
	blockSize = [5, 10, 20]
	processSize = [10, 20, 5]
	m = len(blockSize)
	n = len(processSize)

	NextFit(blockSize, m, processSize, n)
