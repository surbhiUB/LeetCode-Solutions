def longestVowelString(s):

    vowels = set('aeiou')
    length = len(s)
    start = 0
    end = length-1

    while start<end and s[start] in vowels:
        start+=1
    while end>=0 and s[end] in vowels:
        end-=1

    if start>=length:
        return length

    res = start-end +length-1
    longest = 0
    summ = 0

    for i in range(start+1,end+1):
        if s[i] in vowels:
            summ+=1
        else:
            summ=0
        longest = max(longest,summ)
    return longest+res

print(longestVowelString('aexaeuixaeiou'))