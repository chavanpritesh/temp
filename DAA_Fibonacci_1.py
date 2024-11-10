def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

def iterative_fibo(nterms):
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence up to", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

def main():
    while True:
        print("\nChoose the method to generate Fibonacci sequence:")
        print("1. Iterative")
        print("2. Recursive")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '3':
            print("Exiting the program.")
            break

        nterms = int(input("How many terms? "))

        if choice == '1':
            iterative_fibo(nterms)
        elif choice == '2':
            if nterms <= 0:
                print("Please enter a positive integer")
            else:
                print("Fibonacci sequence:")
                for i in range(nterms):
                    print(recur_fibo(i))
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
