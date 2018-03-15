import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)


#Step 1: create 2-d array (or matrix) 'p' for storing paths
	#need to figure out how to represent paths

#Step 2: compute p[0] using singleshortestpath (which should be a modified version of LCS) that stores the nodes along the path of p[0] in array p. Then copy the values of p[0] to p[m]. Also store the length of the path (arr[m][n]) as the current "longest"

#Step 3: call the below recursive method on (A,B, p, 0, m). Somwhere in here update "longest" if p[mid] is longer (as returned by singleshortestpath)
def FINDSHORTESTPATHS(A,B, p,l,u):
    if (u-l) <= 1:
        return 
	mid = (l+u)/2
	p[mid] = SINGLESHORTESTPATH(A,B,mid, p[l], p[u])
	FINDSHORTESTPATHS(A,B, p,l,mid)
	FINDSHORTESTPATHS(A,B, p,mid,u)

#this needs to be modified to create an array of values for the path it will return as it progresses (indices could represent columns, values rows). It also needs to be modified to only look at the indicies within the bounds of pl and pu.
def SINGLESHORTESTPATH(A,B,mid,pl,pu):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return arr[m][n]

#Step 4: Return 'longest' to the main method

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		m = len(A)
#create placeholder for the values of the paths		
		p = [] 
#		print LCS(A,B)
#call recursive method
		FINDSHORTESTPATHS(A,B,p,0,m)

	return

if __name__ == '__main__':
	main()
