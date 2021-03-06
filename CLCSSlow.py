import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

#cut partitions A at character i and re-appends the two.
def cut(A,i):
	A = A[i:] +  A[:i]
	return A

#CLCS iterates from 1 to m, cutting A and then calling LCS on the re-formed string, updating the value of longest each time LCS returns a higher value.
def CLCS(A,B):
	longest = 0
	m = len(A)
	for i in range(0,m):
            temp = cut(A,i)
            interim = LCS(temp,B)
            print(interim)
            if interim > longest:
			longest = interim
	
	return longest

def LCS(A,B):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return arr[m][n]

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		print CLCS(A,B)
	return

if __name__ == '__main__':
	main()
