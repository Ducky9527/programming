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