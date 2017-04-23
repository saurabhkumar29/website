def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

def bubblesort(arr):
    i = 0
    while(i<len(arr)):
        j = i + 1
        while(j<(len(arr)-1)):
            if(arr[j]>arr[j+1]):
                swap(arr,j,j+1)
            j = j + 1
        i = i + 1

def binary(arr,find):
    first = 0
    last = len(arr)-1
    while first<=last:
        mid = (first + last) // 2
        if arr[mid] == find:
            print("Number found at index "+str(mid))
            return
        elif find < arr[mid]:
            last = mid-1
        elif find > arr[mid]:
            first = mid+1
    print("Number not Found")

if __name__ == '__main__':
    n = input("How many numbers you want to enter")
    i = 0
    a = []
    while i<n:
        a.append(input())
        i = i + 1
    bubblesort(a)
    find = input("Enter the number to find")
    binary(a,find)
