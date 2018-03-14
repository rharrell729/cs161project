import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)


# p0 is from (0,0) to (m,n)
# pm is from (m, 0) to (2m, n) 

#need to initialize storage for p.
p=[None]*20

#recursive method
#p and l are int indices
def FINDSHORTESTPATHS(A,B, p,l,u):
    if (u-l) <= 1:
        return 
	mid = (l+u)/2
	p[mid] = SINGLESHORTESTPATH(A,B,mid, p[l], p[u])
#store mid for use as bounds (l and u) in next recursive step. How to store it?? 	
	FINDSHORTESTPATHS(A,B, p,l,mid)
	FINDSHORTESTPATHS(A,B, p,mid,u)


#LCS needs to be modified to only check the relevant paths: the nested for loops 
#should only check items within the bounds of the shortest paths explored prior 
#(stored in the singleshortestpath method). We might need to update the arguments 
#in 'range' each time we call singleshortest
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
