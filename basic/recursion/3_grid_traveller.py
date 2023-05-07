def grid_traveller(m,n):
    if m == 0 or n == 0 : return 0
    elif m==1 and n ==1 : return 1

    return grid_traveller(m-1,n)+grid_traveller(m,n-1)


print(grid_traveller(1,1))
print(grid_traveller(2,3))
print(grid_traveller(18,18))