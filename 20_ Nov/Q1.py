# Delete at given index 

def deleteAtIndex(arr: List[int], P: int) -> List[int]:
    # Write your solution here
    n = len(arr)

    for i in range(P,n-1):
        arr[i] = arr[i+1]
    arr[n-1] = 0 
    
    return arr 