# Name: Muhammad Hassan Noorsumar
# Day: Tuesday
# Date: 18/07/2023
# Sub: Python
# Topic: Assignment-12
# Assignment-12: Q3
# Q3: It should be a menu driven program

from Q3.Module1 import function1 as m1_function1
from Q3.Module2 import function2 as m2_function2
from Q3.Module3 import function1 as m3_function1
from Q3.Module4 import function2 as m4_function2
from Q3.Module5 import function1 as m5_function1

while True:
    print("Menu: ")
    print("1. This is Function 1 in Module 1")
    print("2. This is Function 2 in Module 2")
    print("3. This is Function 1 in Module 3")
    print("4. This is Function 2 in Module 4")
    print("5. This is Function 1 in Module 5")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice=="1":
        m1_function1()
    elif choice=="2":
        m2_function2()
    elif choice=="3":
        m3_function1()
    elif choice=="4":
        m4_function2()
    elif choice=="5":
        m5_function1()
    elif choice=="6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

"""
Output of entire code:
Menu:
1. This is Function 1 in Module 1
2. This is Function 2 in Module 2
3. This is Function 1 in Module 3
4. This is Function 2 in Module 4
5. This is Function 1 in Module 5
6. Exit
Enter your choice (1-6): 1
This is Function 1 in Module 1
Menu: 
1. This is Function 1 in Module 1
2. This is Function 2 in Module 2
3. This is Function 1 in Module 3
4. This is Function 2 in Module 4
5. This is Function 1 in Module 5
6. Exit
Enter your choice (1-6): 2
This is Function 2 in Module 2
Menu: 
1. This is Function 1 in Module 1
2. This is Function 2 in Module 2
3. This is Function 1 in Module 3
4. This is Function 2 in Module 4
5. This is Function 1 in Module 5
6. Exit
Enter your choice (1-6): 3
This is Function 1 in Module 3
Menu: 
1. This is Function 1 in Module 1
2. This is Function 2 in Module 2
3. This is Function 1 in Module 3
4. This is Function 2 in Module 4
5. This is Function 1 in Module 5
6. Exit
Enter your choice (1-6): 4
This is Function 2 in Module 4
Menu:
1. This is Function 1 in Module 1
2. This is Function 2 in Module 2
3. This is Function 1 in Module 3
4. This is Function 2 in Module 4
5. This is Function 1 in Module 5
6. Exit
Enter your choice (1-6): 5
This is Function 1 in Module 5
Menu:
1. This is Function 1 in Module 1
2. This is Function 2 in Module 2
3. This is Function 1 in Module 3
4. This is Function 2 in Module 4
5. This is Function 1 in Module 5
6. Exit
Enter your choice (1-6): 6
Exiting the program...
"""