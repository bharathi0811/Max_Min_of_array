max_=0
array=list(map(int,input("Enter the array:").split()))
def max_min(array):
    for i in array:
        if max_<i:
            max_=i
    min_ =array[0]       
    for j in array:
        if min_<j:
            continue
        else:
            min_=j
    return max_+min_
print(max_min(array))
