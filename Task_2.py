'''Write a Python program that generates the Fibonacci sequence up to a specified number of
terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the
sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the
user to enter the number of terms (n) they want in the sequence and then display the
Fibonacci sequence up to that number of terms. '''

            

num = int(input("Enter a number : "))
n1,n2=0,1

if num==1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range(2, num):
        a = n1+n2
        n1=n2
        n2=a
        print(a)
