# converting the code to python3


def main():
	# Taking the number of processes
	n = int(input("Enter number of process: "))
	# Matrix for storing Process Id, Burst Time, Average Waiting Time & Average Turn Around Time.
	A = [[0 for j in range(4)] for i in range(100)]
	total, avg_wt, avg_tat = 0, 0, 0
	print("Enter Burst Time:")
	for i in range(n): # User Input Burst Time and alloting Process Id.
		A[i][1] = int(input(f"P{i+1}: "))
		A[i][0] = i + 1
	for i in range(n): # Sorting process according to their Burst Time.
		index = i
		for j in range(i + 1, n):
			if A[j][1] < A[index][1]:
				index = j
		temp = A[i][1]
		A[i][1] = A[index][1]
		A[index][1] = temp
		temp = A[i][0]
		A[i][0] = A[index][0]
		A[index][0] = temp
	A[0][2] = 0 # Calculation of Waiting Times
	for i in range(1, n):
		A[i][2] = 0
		for j in range(i):
			A[i][2] += A[j][1]
		total += A[i][2]
	avg_wt = total / n
	total = 0
	# Calculation of Turn Around Time and printing the data.
	print("P	 BT	 WT	 TAT")
	for i in range(n):
		A[i][3] = A[i][1] + A[i][2]
		total += A[i][3]
		print(f"P{A[i][0]}	 {A[i][1]}	 {A[i][2]}	 {A[i][3]}")
	avg_tat = total / n
	print(f"Average Waiting Time= {avg_wt}")
	print(f"Average Turnaround Time= {avg_tat}")


if __name__ == "__main__":
	main()
