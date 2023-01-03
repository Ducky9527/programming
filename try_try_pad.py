#Remove all the duplicates from a list

#Tools permitted to use
#if, else, and basic booleans
#for and while loop
#list.append()
#list.remove()
#list.pop()
#list.index()
#create an empty list, e.g. data = []

#This is an unsuccessful attempt with "for loop"

numb = [1, 2, 1, 3, 2, 1]

item_order = 1
count = 1

x = 1
for i in numb: # problem! When this for loop began, the list contains 6 elements. SO! this for loop will execute 6 times, with i = 1, i = 2, i = 1, i = 3, i = 2, i = 1. It will not change even if in the middle of the execution some of the elements have been removed. Tricky! Tricky!
    #1, 2, 3, 1, 2, 1
    turn = len(numb) - item_order # I thought i could avoid the beyond the boarder issue by using "item_order". I was so wrong.
    print(turn)
    print(i) 

    for com in range(turn): ##
        #0, 1, 2
        if i == numb[item_order]:
            print(f'{count}: {i} and {numb[item_order]} are duplicate!')
            numb.remove(numb[item_order])
            print(f'New List: {numb}')
            print(item_order)
            print(" ")

            count += 1

        else:
            print(f'{count}: {i} and {numb[item_order]} are not duplicate!')
            print(f'Same List: {numb}')
            item_order += 1
            print(item_order)
            print(" ")

            count += 1
 


#This is a successful attemp with 'while loop'


numb = [1, 2, 3, 2, 1, 9, 3]

#pop() 是指定看要remove哪個index的

x = 0 #indexing the first compared number; this one will remain unchange untill the programme goes through the rest of the list  
y = 0 #indexing the second compared number; this one will keep changing so that the programme can do the compaing between the first and the second number
c = 1 #indexing - enhance readability of the output
while x < len(numb) - 1:
    while y < len(numb) - 1:
        y += 1
        print(f'screening {c}:  x: {x}, y: {y}  ({numb[x]}, {numb[y]})')
        c +=1

        if numb[x] == numb[y]:
            print(f'Find duplicate! {numb[x]}')
            numb.pop(y)
            print(f'New List: {numb}')
            print('')
            y -= 1 # remember that after numb.pop(numb[x]), the length of the list will be changed. the numb[x] in the new list is the numb [x+1] in the original list. As a result, we need to use minus 1 to ask the programme check the new numb[x] again before it move forward. 

        else:
            print(f'Same List: {numb}')
            print('')
    
    x += 1 #finished the comparision with the rest of the list, move to the second number in the list. Let the Programme do the comparision again.
    y = x #reset the value of y, otherwise the condition of the second while (the while about the value y) will not be satisfied. Remember, always remain one place behind the 'unmoved' number. So, don't reset the value of y as 0, but as x. It will be incremented at the beginning of next while loop.

    