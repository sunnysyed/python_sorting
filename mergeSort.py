def readfile(fname):
    content =[]
    with open(fname) as f:
        for line in f:
            content.append(int(line))
    return content

def merge(left,right):
    global comparisons
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if (left[i] <= right[j]):
            comparisons+=1
            result.append(left[i])
            i+=1
        else:
            comparisons+=1
            result.append(right[j])
            j+=1
    while (i<len(left)):
        comparisons+=1
        result.append(left[i])
        i+=1
    while (j<len(right)):
        comparisons+=1
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

def main():
    global comparisons
    random_10 = readfile("10_Random.txt")
    reverse_10 = readfile("10_Reverse.txt")
    sorted_10 = readfile("10_Sorted.txt")
    random_100 = readfile("100_Random.txt")
    reverse_100 = readfile("100_Reverse.txt")
    sorted_100 = readfile("100_Sorted.txt")
    random_1000 = readfile("1000_Random.txt")
    reverse_1000 = readfile("1000_Reverse.txt")
    sorted_1000 = readfile("1000_Sorted.txt")



    #print mergeSort Sort
    print "------====Random 10====------"
    comparisons = 0
    print mergeSort(random_10)
    print "Total Comparissons Performed: ", comparisons
    print "------=================------"
    print "------====Reverse 10====------"
    comparisons = 0
    print mergeSort(reverse_10)
    print "Total Comparissons Performed: ", comparisons
    print "------=================------"
    print "------====Sorted 10====------"
    comparisons = 0
    print mergeSort(sorted_10)
    print "Total Comparissons Performed: ", comparisons
    print "------=================------"

    print "------====Random 100====------"
    comparisons = 0
    print mergeSort(random_100)
    print "Total Comparissons Performed: ", comparisons
    print "------==================------"
    print "------====Reverse 100====------"
    comparisons = 0
    print mergeSort(reverse_100)
    print "Total Comparissons Performed: ", comparisons
    print "------==================------"
    print "------====Sorted 100====------"
    comparisons = 0
    print mergeSort(sorted_100)
    print "Total Comparissons Performed: ", comparisons
    print "------==================------"

    print "------====Random 1000====------"
    comparisons = 0
    print mergeSort(random_1000)
    print "Total Comparissons Performed: ", comparisons
    print "------===================------"
    print "------====Reverse 1000====------"
    comparisons = 0
    print mergeSort(reverse_1000)
    print "Total Comparissons Performed: ", comparisons
    print "------===================------"
    print "------====Sorted 1000====------"
    comparisons = 0
    print mergeSort(sorted_1000)
    print "Total Comparissons Performed: ", comparisons
    print "------===================------"





if __name__ == "__main__": main()
