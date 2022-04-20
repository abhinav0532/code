def tower_of_hanoi(disks, initial, aux, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(initial, target))  
        return

    tower_of_hanoi(disks - 1, initial, target, aux)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, initial, target))  
    tower_of_hanoi(disks - 1, aux, initial, target)  
  
disks = int(input('Enter the number of disks: '))

tower_of_hanoi(disks, 'A', 'B', 'C')