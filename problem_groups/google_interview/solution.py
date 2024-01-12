from itertools import accumulate
from collections import defaultdict

# def find_donating_accounts(accounts):
  
#   # Calculate prefix sum array.
#   prefix_sum = [0] + list(accumulate(accounts))
#   print(accounts)
#   print(prefix_sum)

#   # List to store potential matching indices.
#   potential_matches = []

#   # Iterate through each account.
#   for i in range(len(accounts)):
#     # Calculate total sum excluding the potential donated account.
    
#     total_sum = prefix_sum[-1] - accounts[i]
#     print(prefix_sum[-1] , accounts[i] , 'difference: ', total_sum)

#     # Check for even distribution possibility.
#     if total_sum % (len(accounts) - 1) == 0:
#       potential_matches.append(i)

#   return potential_matches


from collections import defaultdict

def find_donating_accounts(accounts):
    # Group accounts with equal balances.
    groups = defaultdict(list)
    for i, balance in enumerate(accounts):
        groups[balance].append(i)

    # Check for combinations of groups that allow for equal sums.
    potential_solutions = []
    for balance1, indices1 in groups.items():
        for balance2, indices2 in groups.items():
            if balance1 != balance2:
                for num_donated in range(1, len(indices1) + 1):  # Consider donating different numbers of accounts.
                    total_sum_excluding_donated = sum(accounts) - num_donated * balance1 - balance2
                    if total_sum_excluding_donated % 2 == 0:
                        potential_solution = indices1[:num_donated]  # Include indices of accounts to donate.
                        potential_solutions.append(potential_solution)

    return potential_solutions




# Example usage
accounts = [5, 1, 2, 6, 3]
print(find_donating_accounts(accounts))

accounts = [2,1,1,1,1,1,1,3]
print(find_donating_accounts(accounts))

# # Example usage
accounts = [7, 1, 2, 8, 3]
print(find_donating_accounts(accounts))

