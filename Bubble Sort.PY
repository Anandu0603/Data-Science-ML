l1 = []
n = int(input("enter number of elements required: "))
for i in range(0, n):
    element = int(input())
    l1.append(element)
print("Original List:", l1)
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
print("Sorted List", l1)


***output***
enter number of elements required: 6
34
20
78
49
10
65
Original List: [34, 20, 78, 49, 10, 65]
Sorted List [10, 20, 34, 49, 65, 78]
