def merge_the_tools(string, k):
    # your code goes here
    i = 0
    p = k
    t = []
    while i < len(string):
        t.append(string[i:k])
        i = k
        k = k + p
    temp = ""
    
    for j in t:
        for x in j:
            if x in temp:
                continue
            else:
                temp = temp + x
        print(temp)
        temp = ""
             

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k) 