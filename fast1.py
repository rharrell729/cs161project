import sys
import numpy as np
np.set_printoptions(threshold=np.nan)

matrix = np.zeros((4001,2001), dtype=int)
ghosts = np.zeros((4001,2001), dtype=int)

def CLCSFast(A,B):
        m = len(A)
        n = len(B)
        matrix.fill(0)
        ghosts.fill(0)
        p = np.zeros(m, dtype=int)
        p[0] = LCS(A,B,m,n)
        p[m-1] = p[0]
        for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                        if ghosts[i][j] != 0:
                                ghosts[i+m-1][j] = 1
        FINDSHORTESTPATHS(A,B,p,m-1,0)
        max = -1*np.inf
        for i in range(0,m):
                if p[i] > max:
                        max = p[i]
        return max

def FINDSHORTESTPATHS(A,B,p,l,u):
        if l - u <= 1:
                return
        mid = (l + u)/2
        p[mid] = SINGLESHORTESTPATH(A,B,len(A),len(B),u,l,mid)
        FINDSHORTESTPATHS(A,B,p,l,mid)
        FINDSHORTESTPATHS(A,B,p,mid,u)


def LCS(A,B,m,n):
        for i in range(1,m+1):
                for j in range(1,n+1):
                        if A[i-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        ghostFill(A,B,m,n,0)
        return matrix[m][n]

def SINGLESHORTESTPATH(A,B,m,n,u,l,mid):
        matrix.fill(0)
        outside = 1
        for k in range(mid,l):
                if ghosts[k][0] != 0:
                        k += 1
        for i in range(k,l):
                j = 1
                while j <= n and (ghosts[i][j] == 0):
                        if A[i-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                        j += 1
                while j <= n and (ghosts[i][j] != 0):
                        if A[i-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                        j += 1
        for i in range(l,mid+m+1):
                j = 0
                if ghosts[i][j] == 0:
                        while j <= n and ghosts[i][j] == 0:
                                j += 1
                else:
                        j = 1
                while j <= n and ghosts[i][j] != 0:
                        if A[((i-1)%m+1)-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                        j += 1
                if outside == 1:
                        for k in range (j,n+1):
                                if ghosts[i][k] != 0:
                                        outside = 0
                if outside == 1:
                        continue
                while j <= n and ghosts[i][j] == 0:
                        if A[((i-1)%m+1)-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                        j += 1
                while j <= n and ghosts[i][j] != 0:
                        if A[((i-1)%m+1)-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                        j += 1
        ghostFill(A,B,m,n,mid)
        return matrix[m+mid][n]

def ghostFill(A,B,m,n,mid):
        i = mid + m
        j = n
        while (i >= mid and j >= 0) and (i > mid or j > 0):
                ghosts[i][j] = 1
                if A[((i-1)%m+1)-1] == B[j-1] and matrix[i-1][j-1] != 0:
                        i -= 1
                        j -= 1
                elif i == mid:
                        j -= 1
                elif j == 0:
                        i -= 1
                elif matrix[i-1][j] == 0 and matrix[i][j-1] != 0:
                        j -= 1
                elif matrix[i][j-1] == 0 and matrix[i-1][j] != 0:
                        i -= 1
                elif matrix[i-1][j] != 0 and matrix[i][j-1] != 0:
                        if matrix[i-1][j] > matrix[i][j-1]:
                                i -= 1
                        else:
                                j -= 1
                elif matrix[i-1][j] == 0 and matrix [i][j-1] == 0:
                        if j != 0:
                                j -= 1
                        else:
                                i -= 1
        ghosts[i][j] = 1
        return

def main():
        if len(sys.argv) != 1:
                sys.exit('Usage: `python LCS.py < input`')

        for l in sys.stdin:
                A,B = l.split()
                print CLCSFast(A,B)
        return

if __name__ == '__main__':
        main()
