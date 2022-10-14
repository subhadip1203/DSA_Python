def grid_traveller(m,n,memo={}):
    key = str(m)+'-'+str(n)
    if memo.get(key,None) != None : return memo[key]
    if m == 0 or n == 0 : return 0
    elif m==1 and n ==1 : return 1
    memo[key] = grid_traveller(m-1,n,memo)+grid_traveller(m,n-1,memo)
    return memo[key]



print(grid_traveller(1,1))
print(grid_traveller(2,3))
print(grid_traveller(18,18))