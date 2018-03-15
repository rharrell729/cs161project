import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

#Iterates recursively through the DP, finding the shortest path and the LCS as each path by calling SINGLESHORTESTPATH at each index of A.
def FINDSHORTESTPATHS(A,B,p,l,u,longest):
    if (u-l) <= 1:
        return 
	mid = (l+u)/2
	p[mid], longest[mid] = SINGLESHORTESTPATH(A,B,mid, p[l], p[u])
	FINDSHORTESTPATHS(A,B, p,l,mid)
	FINDSHORTESTPATHS(A,B, p,mid,u)


#This method finds the shortest path between p[l] and p[u] starting at the index mid and stores it in p[mid]. It also returns the LCS of the path.
def SINGLESHORTESTPATH(A,B,mid,pl,pu):
#calculate the LCS
	m = len(A)
	n = len(B)
	#INCOMPLETE: cut off the loops when you hit a lower or upper bound 
	for i in range(mid+1,mid+m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])
#store the path by iterating backward through the DP 
	#return arr[m][n]
	#this stores the value of LCS
    	path = np.zeros((m+1,n+1))
	i = m+mid
    	j = n
    	while i >= mid and j >= 0:
 
        	#Store a 1 in the path at node (i,j)
		path[i][j] = 1	

		# If current character in A and B is the same, go up diagonally
        	if A[i-1] == B[j-1]:
            		i-=1
            		j-=1
 
        	# If not same, then find the larger of two and go in the direction of larger value
        	elif arr[i-1][j] > arr[i][j-1]:
			i-=1
        	else:
            		j-=1
	return path, arr[m][n]


def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		m = len(A)
		n = len(B)

#Step 1: create 2-d array (or matrix) 'p' for storing paths and array 'longest' for storing LCS values of paths
       # p[index][A-dimension][B-dimension]=1 if path falls on that node
	p = np.zeros((m+1,m+1,n+1))
	longest = np.zeros(m+1)

#Step 2: compute p[0] using singleshortestpath (which should be a modified version of LCS) that stores the nodes along the path of p[0] in array p. Then copy the values of p[0] to p[m]. Also store the length of the path (arr[m][n]) as the current "longest"
	p[0] = SINGLESHORTESTPATH(A,B,0,0,m)

#Step 3: call Findhsortestpaths(A,B, p, 0, m).
	FINDSHORTESTPATHS(A,B,p,0,m,longest)

#Step 4: iterate through longest[] to find the longest path. Print the longest path.
	temp = 0
	for i in 0 to m+1
		if longest[i] > temp
		temp = longest[i]
	Print(longest[i])

	return

if __name__ == '__main__':
	main()
