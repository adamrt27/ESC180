def count_words(text):
    word_counts = {}
    for i in range(len(text)):
        if text[i] in list(word_counts.keys()):
            word_counts[text[i]] += 1
        else:
            word_counts[text[i]] = 1
    return word_counts

def top10(L):
    l = []
    for iter in range(10):
        max = 0
        index = 0
        for num in range(len(L)):
            if L[num] > max:
                max = L[num]
                index = num
        del L[index]
        l.append(max)
    return l
    
def invert_dict(d):
    items = list(d.items())
    inv_d = {}
    for i in range(len(items)):
        if items[i][1] in list(inv_d.keys()):
            temp = inv_d.get(items[i][1])
            temp.append(items[i][0])
            inv_d[items[i][1]] = temp
        else:
            inv_d[items[i][1]] = [items[i][0]]
    return inv_d

def top10words(dict):
    res = []
    dict_inv = sorted(invert_dict(dict).items())
    for i in range(len(dict_inv)-1,-1,-1):
        for k in range(len(dict_inv[i][1])):
            res.append(dict_inv[i][1][k])
    
    return res[:10]
    




text = open("pride_and_prejudice.txt", encoding="latin-1").read().split()
text_dict = count_words(text)
# print(text_dict)
# val = list(text_dict.items())
# print(val)
# print(text_dict)
# print(sorted(invert_dict(text_dict).items()))
print(top10words(text_dict))