



""""
The program is trying to determine the best option(payment).
The first option is ....
the second option is...
find a solutiion to see which option is best or if they are the same. 

function1 will output 100 * 10 

function2 will loop 10 times, with each time, doubling the amount and add the amount to the total.

if the amount is equal, we output to the user" Option 1 and Option 2 are the same"
if the option1 is better, we output to the user "option 1 is better"
if the option2 is better, we output to the user "option 1 is better"
"""
"""

#  Option1 
    return 100 * 10 

#  Option2 
    amount = 1
    list1 = []
    loop 10 times 
        add amount to list1 
        amount *= 2
    sum = sum of all items in the loop 
    return sum
#  main
    var1 = option1
    var2 = option1

    if var1 = var2
        "option 1 and option2 are the same"
     if var1 < var2
        "option 2 is better"
    if var2 < var1
        "option 1 is better"

    main 
    """

def option1():
    return 100 * 10

def option2(): 
    amount = 1 
    list1 = []
    for i in range (0, 10):
        list1.append(amount)
        amount *= 2
    print("list1", list1)
    total = sum(list1) 
    return total

def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    print("from main: var1", var1, 'var2', var2)
    if var1 == var2:
        answer = "option 1 and option2 are the same"
    if var1 < var2:
        answer = "option 2 is better"
    if var2 < var1:
        answer = "option 1 is better"
    print(answer)


main()
