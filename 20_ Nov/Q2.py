# Delete all occurences of x
def deleteAllOccurrences(arr: List[int], X: int) -> List[int]:
    # Write your solution here
    n = len(arr)
    j = 0 

    for i in range(n):
        if arr[i] !=X:
            arr[j]=arr[i]
            j+=1
    while j < n:
        arr[j] = 0
        j += 1
    return arr  