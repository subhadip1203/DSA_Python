'''
geekforgeeks : https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1


Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.

'''

def check_Empty_Dict(my_dict):
    for x in my_dict:
        if my_dict[x] > 0 :
            return False
    return True

def search(pat, txt):
    answer = 0
    pat_dict = {}
    pat_length = 0
    for char in pat:
        pat_length = pat_length +1
        pat_dict[char] = pat_dict.get(char,0) + 1

    start = 0
    end = 0
    for i in range(pat_length):
        end = end+1
        item = txt[i]
        if item in pat_dict and pat_dict[item] > 0:
            pat_dict[item] = pat_dict[item] -1

    if check_Empty_Dict(pat_dict) :
        answer = answer+1



    

txt = "forxxorfxdofr"
pat = "for"
print(search(pat, txt))
