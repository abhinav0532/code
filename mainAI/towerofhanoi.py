# TowerOfHanoi
 
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')

#output
#Move disk 1 from rod A to rod B
#Move disk 2 from rod A to rod C
#Move disk 1 from rod B to rod C
#Move disk 3 from rod A to rod B
#Move disk 1 from rod C to rod A
#Move disk 2 from rod C to rod B
#Move disk 1 from rod A to rod B
#Move disk 4 from rod A to rod C
#Move disk 1 from rod B to rod C
#Move disk 2 from rod B to rod A
#Move disk 1 from rod C to rod A
#Move disk 3 from rod B to rod C
#Move disk 1 from rod A to rod B
#Move disk 2 from rod A to rod C
#Move disk 1 from rod B to rod C