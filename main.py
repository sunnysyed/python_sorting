def readfile(fname):
    content =[]
    with open(fname) as f:
        for line in f:
            content.append(int(line))
    return content

def insertionSort(a):
    insertComparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while (j >= 0):
            insertComparisons += 1
            if(a[j] > key):
                a[j+1] = a[j]
                j = j - 1
            else:
                break;
        a[j+1] = key
    print a
    return insertComparisons

def merge(left,right):
    global mergeComparisons
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if (left[i] <= right[j]):
            mergeComparisons+=1
            result.append(left[i])
            i+=1
        else:
            mergeComparisons+=1
            result.append(right[j])
            j+=1
    while (i<len(left)):
        mergeComparisons+=1
        result.append(left[i])
        i+=1
    while (j<len(right)):
        mergeComparisons+=1
        result.append(right[j])
        j+=1
    return result

def mergeSort(a):
    if len(a) <= 1:
        return a
    middle = len(a) / 2
    left = mergeSort(a[:middle])
    right = mergeSort(a[middle:])
    return merge(left, right)

def quickSort(a):
    global quickComparison
    left = []
    middle = []
    right = []
    
    if len(a) > 1:
        pivot = a[0]
        for i in a:
            if i < pivot:
                quickComparison +=1
                left.append(i)
            if i == pivot:
                middle.append(i)
            if i > pivot:
                quickComparison +=1
                right.append(i)
        return quickSort(left)+ middle + quickSort(right)
    else:
        return a


def main():
    global insertComparisons, mergeComparisons, quickComparison
    random_10 = readfile("10_Random.txt")
    reverse_10 = readfile("10_Reverse.txt")
    sorted_10 = readfile("10_Sorted.txt")
    random_100 = readfile("100_Random.txt")
    reverse_100 = readfile("100_Reverse.txt")
    sorted_100 = readfile("100_Sorted.txt")
    random_1000 = readfile("1000_Random.txt")
    reverse_1000 = readfile("1000_Reverse.txt")
    sorted_1000 = readfile("1000_Sorted.txt")
    

    print "------====Random 10====------"
    insertComparisons = 0
    insertComparisons = insertionSort(list(random_10))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    mergeComparisons = 0
    print mergeSort(list(random_10))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    quickComparison = 0
    print quickSort(list(random_10))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"


    print "------====Reverse 10====------"
    insertComparisons = 0
    insertComparisons = insertionSort(list(reverse_10))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    mergeComparisons = 0
    print mergeSort(list(reverse_10))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    quickComparison = 0
    print quickSort(list(reverse_10))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"


    print "------====Sorted 10====------"
    insertComparisons = 0
    insertComparisons = insertionSort(list(sorted_10))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    mergeComparisons = 0
    print mergeSort(list(sorted_10))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    quickComparison = 0
    print quickSort(list(sorted_10))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"


    print "------====Random 100====------"
    insertComparisons = 0
    insertComparisons = insertionSort(list(random_100))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    mergeComparisons = 0
    print mergeSort(list(random_100))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    quickComparison = 0
    print quickSort(list(random_100))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"
    
    
    print "------====Reverse 100====------"
    insertComparisons = 0
    insertComparisons = insertionSort(list(reverse_100))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    mergeComparisons = 0
    print mergeSort(list(reverse_100))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    quickComparison = 0
    print quickSort(list(reverse_100))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"
    
    
    print "------====Sorted 100====------"
    print sorted_100
    insertComparisons = 0
    insertComparisons = insertionSort(list(sorted_100))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    print sorted_100
    mergeComparisons = 0
    print mergeSort(list(sorted_100))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    print sorted_100
    quickComparison = 0
    print quickSort(list(sorted_100))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"



    print "------====Random 1000====------"
    insertComparisons = 0
    insertComparisons = insertionSort(list(random_1000))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    mergeComparisons = 0
    print mergeSort(list(random_1000))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    quickComparison = 0
    print quickSort(list(random_1000))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"
    
    
    print "------====Reverse 1000====------"
    insertComparisons = 0
    insertComparisons = insertionSort(list(reverse_1000))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    mergeComparisons = 0
    print mergeSort(list(reverse_1000))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    quickComparison = 0
    print quickSort(list(reverse_1000))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"
    
    
    print "------====Sorted 1000====------"
    print sorted_1000
    insertComparisons = 0
    insertComparisons = insertionSort(list(sorted_1000))
    print "Insertion Sort Total Comparisons Performed: ", insertComparisons
    print sorted_1000
    mergeComparisons = 0
    print mergeSort(list(sorted_1000))
    print "Merge Sort Total Comparisons Performed: ", mergeComparisons
    print sorted_1000
    quickComparison = 0
    print quickSort(list(sorted_1000))
    print "Quick Sort Total Comparisons Performed: ", quickComparison
    print "------=================------"




if __name__ == "__main__": main()
