#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 14:04:33 2018

@author: wenyijones
"""

import sys
import numpy as np

matrix = np.zeros((41,21), dtype=int)
ghosts = np.zeros((41,21), dtype=int)

def CLCSFast(A,B):
        m = len(A)
        n = len(B)
        matrix.fill(0)
        ghosts.fill(0)
        p = np.zeros(m, dtype=int)
        p[0] = LCS(A,B,m,n,0)
        p[m-1] = p[0]
        for i in range(1,m+1):
                for j in range(0,n+1):
                        if ghosts[i][j] != 0:
                                ghosts[i+m][j] = 1
        ghosts[m][0] = 1
        FINDSHORTESTPATHS(A,B,p,m-1,0)
        min = np.inf
        print "damn"
        for i in range(0,m):
                if p[i] < min and p[i] != 0:
                        min = p[i]
        return min

def FINDSHORTESTPATHS(A,B,p,l,u):
        if l - u <= 1:
                return
        mid = (l + u)/2
        print "there"
        p[mid] = SINGLESHORTESTPATH(A,B,len(A),len(B),u,l,mid)
        print "where"
        FINDSHORTESTPATHS(A,B,p,l,mid)
        print "uh"
        FINDSHORTESTPATHS(A,B,p,mid,u)

def LCS(A,B,m,n,index):
        for i in range(index+1,index+m+1):
                for j in range(1,n+1):
                        if A[i-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        ghostFill(A,B,m,n,index)
        return matrix[m][n]
    
#    def LCS(A,B):
#	m = len(A)
#	n = len(B)
#
#	for i in range(1,m+1):
#		for j in range(1,n+1):
#			if A[i-1] == B[j-1]:
#				arr[i][j] = arr[i-1][j-1]+1
#			else:
#				arr[i][j] = max(arr[i-1][j], arr[i][j-1])
#
#	return arr[m][n]

def SINGLESHORTESTPATH(A,B,m,n,u,l,mid):
        matrix.fill(0)
        print u
        print l
        print mid
        for k in range(mid,l+1):
                if ghosts[k][0] != 0:
                        k += 1
                        print "0"
        for i in range(k,l):
                j = 1
                print "first loop"
                while j <= n and (ghosts[i][j] == 0):
                        if A[i-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                                print "1"
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                                print "2"
                        j += 1
                while j <= n and (ghosts[i][j] != 0):
                        ghosts[i][j] = np.abs(ghosts[i][j])
                        if A[i-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                                print "3"
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                                print "4"
                        j += 1


        for i in range(l+1,mid+m+1):
                j = 0
                if ghosts[i][j] != 0:
                        ghosts[i][j] = -1 * np.abs(ghosts[i][j])
                j += 1
                print "second loop"
                while j <= n and ghosts[i][j] != 0:
                        ghosts[i][j] = -1 * np.abs(ghosts[i][j])
                        print ghosts
                        print matrix
                        if A[((i-1)%m+1)-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                                print "5"
                        else:
                            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1]) 
                            print "6"
                        j += 1
                while j <= n and ghosts[i][j] == 0:
                        if A[((i-1)%m+1)-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                                print "7"
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                                print "8"
                        j += 1
                while j <= n and ghosts[i][j] == 1:
                        if A[((i-1)%m+1)-1] == B[j-1]:
                                matrix[i][j] = matrix[i-1][j-1]+1
                                print "9"
                        else:
                                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])                                
                                print "10"
                        j += 1
        ghostFill(A,B,m,n,mid)
        return matrix[i][j]

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