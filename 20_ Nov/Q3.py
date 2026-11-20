# Insert 0 after every element 
def insertZeroAfterEveryElement(arr: List[int] ) -> List[int]:
    # Write your solution here
    n = len(arr)

    for i in range(n-1,-1,-1):
        if i*2 < n:
            arr[i*2] = arr[i]

        if i*2+1<n:
            arr[i*2+1] = 0 
    return arr 