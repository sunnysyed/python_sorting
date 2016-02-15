def readfile(fname):
    content =[]
    with open(fname) as f:
        for line in f:
            content.append(int(line))
    return content
def insertionSort(a):
    comparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while (j >= 0):
            comparisons += 1
            if(a[j] > key):
                a[j+1] = a[j]
                j = j - 1
            else:
                break;
        a[j+1] = key
    print a
    return comparisons


def main():
    random_10 = readfile("10_Random.txt")
    reverse_10 = readfile("10_Reverse.txt")
    sorted_10 = readfile("10_Sorted.txt")
    random_100 = readfile("100_Random.txt")
    reverse_100 = readfile("100_Reverse.txt")
    sorted_100 = readfile("100_Sorted.txt")
    random_1000 = readfile("1000_Random.txt")
    reverse_1000 = readfile("1000_Reverse.txt")
    sorted_1000 = readfile("1000_Sorted.txt")

    #InsertionSort Sort
    print "------====Random 10====------"
    comparisons = insertionSort(list(random_10))
    print "Total Comparissons Performed: ", comparisons
    print "------=================------"
    print "------====Reverse 10====------"
    comparisons = insertionSort(list(reverse_10))
    print "Total Comparissons Performed: ", comparisons
    print "------=================------"
    print "------====Sorted 10====------"
    comparisons = insertionSort(list(sorted_10))
    print "Total Comparissons Performed: ", comparisons
    print "------=================------"

    print "------====Random 100====------"
    comparisons = insertionSort(list(random_100))
    print "Total Comparissons Performed: ", comparisons
    print "------==================------"
    print "------====Reverse 100====------"
    comparisons = insertionSort(list(reverse_100))
    print "Total Comparissons Performed: ", comparisons
    print "------==================------"
    print "------====Sorted 100====------"
    comparisons = insertionSort(list(sorted_100))
    print "Total Comparissons Performed: ", comparisons
    print "------==================------"

    print "------====Random 1000====------"
    comparisons = insertionSort(list(random_1000))
    print "Total Comparissons Performed: ", comparisons
    print "------===================------"
    print "------====Reverse 1000====------"
    comparisons = insertionSort(list(reverse_1000))
    print "Total Comparissons Performed: ", comparisons
    print "------===================------"
    print "------====Sorted 1000====------"
    comparisons = insertionSort(list(sorted_1000))
    print "Total Comparissons Performed: ", comparisons
    print "------===================------"





if __name__ == "__main__": main()
