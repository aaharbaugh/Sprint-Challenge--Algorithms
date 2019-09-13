'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    # find the first occurance of "th", 
    x = word.find('th')
    if x != -1:
        count += 1
        count += count_th(word[x+2:])
    
    return count