# Exercise 1 for the second week of the internship
# here I variable will be accepting input for the given command of the list
# the following program will show a dropdown list in console menu

print("1. Press 1 for string palindrome\n2. Press for words sorting alphabetically\n"
      "3. Press 3 for largest among three numbers\n4. Press 4 to find 2nd &4th largest number \n"
      "5. Press 5 for largst number in the list\n6. Press 6 for prime number\n7. Press 7 to find prime number n given range\n"
      "8. Press 8 to print pyramid of number\n9. Press 9 to print pyramid of 0 and 1 ")

i = int(input("enter your choice : "))

if i == 1:
    a = input("Enter the string : ")
    b = a[::-1]
    print("The string you entered is : ", a, "\nReverse of the string you entered is ", b)
    if a == b:
        print("The entered string is palindrome")
    else:
         print("String is not palindrome")

elif i == 2:
    a = input("Enter a line : ")
    b = a.split()
    print(b)
    b.sort()
    for i in b:
        print(i)

elif i == 3:
    a, b, c = input("Enter three numbers : ").split()
    print(a, " ", b, " ", c, " ")
    if a > b and a > c:
        print(a, " is greatest")
    elif b > a and b > c:
        print(b, " is greatest")
    else:
        print(c, " is greatest")

elif i == 4:
    b = []
    a = input("Enter elements into the list seprated by the space ")
    b = a.split()
    print("sorted List elements are : ", sorted(b))
    c = sorted(b)
    print("2, 3, 4 ,5 largest numbers are : ", c[-2], c[-3], c[-4], c[-5])

elif i == 5:
    l = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        l.append(ele)
    print("Largest number in the list is : ", max(l))

elif i == 6:
    num = int(input("Enter a number : "))
    #if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print("not a prime number")
            break
    else:
        print(num," is a prime number")
    #else:
       # print(num," not a prime number")

elif i == 7:
    i=0
    m = int(input("Enter starting range : "))
    n = int(input("Enter ending range : "))
    for i in range (m, n):
        if i > 1:
            for num in range(2,i):
                if(i % num) == 0:
                    break
            else:
                print(i)

elif i == 8:
    n = 5
    for i in range(0, n):
        for j in range(0, i+1):
            print(j, end=" ")
        print("\n")

elif i == 9:
    n = 5
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1   # decrementing k after every line
        for j in range(0, i + 1):
            if j % 2 == 1:
                print("0", end=" ")
            else:
                print("1", end=" ")
        print("\n")

elif i == 10:
    x, y, z = input("Please enter three numbers : ").split()
    print("value of x is : {0} and value of y is : {1} and addition of : {0} and {1} is : {2}".format(x, y, z))
