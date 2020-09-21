def quick_sort(unsroted_list , left , right):
    if left < right :
        position = partition(unsroted_list , left , right)
        quick_sort(unsroted_list , left , position - 1)
        quick_sort(unsroted_list , position + 1 , right)

def partition(unsroted_list , left , right ):
    pivot = unsroted_list[right]
    low = left - 1
    for i in range( left , right ) :
        if unsroted_list[i] < pivot:
            low += 1
            swap (unsroted_list , i , low)

    swap( unsroted_list , right , low + 1)
    return low + 1

def swap (unsroted_list , i , low):
    temp = 0
    temp = unsroted_list[i]
    unsroted_list[i] = unsroted_list[low]
    unsroted_list[low] = temp   

def print_list(arr):
    print(arr)
    return arr   

if __name__ == "__main__":
    arr=[8,4,23,42,16,15]
    n = len(arr) 
    print("unsorted arr:",arr)
    quick_sort(arr,0,n-1)
    print("sorted arr using Quick_Sort",arr)
    print("*"*50)

    arr=[20,18,12,8,5,-2]
    n = len(arr) 
    print("unsorted arr:",arr)
    quick_sort(arr,0,n-1)
    print("sorted arr using Quick_Sort",arr)
    print("*"*50)

    arr=[5,12,7,5,5,7]
    n = len(arr) 
    print("unsorted arr:",arr)
    quick_sort(arr,0,n-1)
    print("sorted arr using Quick_Sort",arr)
    print("*"*50)

    arr=[2,3,5,7,13,11]
    n = len(arr) 
    print("unsorted arr:",arr)
    quick_sort(arr,0,n-1)
    print("sorted arr using Quick_Sort",arr)
    print("*"*50)


