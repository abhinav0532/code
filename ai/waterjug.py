def pour(jug1, jug2):
    maxCapacityOfJug1 = 2
    maxCapactityOfjug2 = 5
    fill = 3

    print(str(jug1) + "\t" + str(jug2))

    if jug2 == fill:
        return
    elif jug2 == maxCapactityOfjug2:
        pour(0, jug1)
    elif jug2 == 0 and jug1 != 0:
        pour(0, jug1)
    elif jug1 == fill:
        pour(jug1, 0)
    elif jug1 < maxCapacityOfJug1:
        pour(maxCapacityOfJug1, jug2)
    elif jug1 < (maxCapactityOfjug2 - jug2):
        pour(0, (jug1 + jug2))
    else:
        pour(jug1 - (maxCapactityOfjug2 - jug2), (maxCapactityOfjug2 - jug2) + jug2)

print("Jug1\tJug2")
pour(0, 0)