def diagonalsum(arr):
    prisum=0
    secsum=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                prisum+=arr[i][j]
            if i+j==len(arr)-1:
                secsum+=arr[i][j]
    print("Primary diagonal sum =",prisum)
    print("Secondary diagonal sum =",secsum)
mat=[]
n=int(input("Enter the no. of rows"))
print("Enter the matrix")
for _ in range(n):
    mat.append(list(map(int,input().split())))
diagonalsum(mat)
    
