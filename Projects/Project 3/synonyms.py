'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math



def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):

    dot_1 = []

    for i in list(vec1.keys()):
        if i in list(vec2.keys()):
            dot_1.append(vec1[i]*vec2[i])

    dot_prod = 0

    # [2, 3]
    # [4, 5]

    for i in range(len(dot_1)):
        dot_prod += dot_1[i]

    mag_1 = 0
    for i in list(vec1.values()):
        mag_1 += i**2
    mag_2 = 0
    for i in list(vec2.values()):
        mag_2 += i**2

    sqrt = (mag_1 * mag_2)**0.5

    sim = dot_prod / sqrt

    return sim


def count_words(text):
    word_counts = {}
    for i in range(len(text)):
        if text[i] in list(word_counts.keys()):
            word_counts[text[i]] += 1
        else:
            word_counts[text[i]] = 1
    return word_counts


def build_semantic_descriptors(sentences):
    # given a list of sentences, build a semantic descriptor
      
    adam_dict = {}
    
    for sentence in sentences:
        lora_list = list(set(sentence)) # gets rid of repeated words in sentence as set is a datatype that cannot have repeated values
        if len(lora_list) > 1:
            for word in lora_list:
                if word != "":
                    word = word.lower()
                    if word not in adam_dict:
                        other_dic = {}
                        for word2 in lora_list:
                            if word2 != word:
                                if word2 in other_dic:
                                    other_dic[word2] += 1
                                else:
                                    other_dic[word2] = 1
                            adam_dict[word] = other_dic
                    else:
                        for word1 in lora_list:
                            if word1 != word:
                                if word1 in adam_dict[word]:
                                    adam_dict[word][word1] += 1
                                else:
                                    adam_dict[word][word1] = 1
    return adam_dict


def build_semantic_descriptors_from_files(filenames):
    singlemingle = ""
    loralist = [[]]


    for i in filenames:
        singlemingle += open(i, "r", encoding = "latin1").read()

    temp = ""
    punklist = [".", "!", "?", "\n"]
    punk2 = [",","-","--",":",";"]
    sencountlora = 0
    for i in range(len(singlemingle)):
        if singlemingle[i].isalpha():
            temp += singlemingle[i].lower()
            if singlemingle[i+1] == " ":
                loralist[sencountlora].append(temp)
                temp = ""
            if singlemingle[i+1] in punklist:
                loralist[sencountlora].append(temp)
                loralist.append([])
                sencountlora += 1
                temp = ""
            if singlemingle[i+1] in punk2:
                loralist[sencountlora].append(temp)
                temp = ""
    loralist.remove([])

    return build_semantic_descriptors(loralist)




def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    if word in semantic_descriptors.keys():
        wordword = semantic_descriptors[word]
        adamlist = []
        

        for i in choices:
            i = i.lower()
            if i not in semantic_descriptors.keys():
                adamlist.append(-1)
            else:
                choiceword = semantic_descriptors[i]
                adamlist.append(similarity_fn(wordword, choiceword))
        return choices[adamlist.index(max(adamlist))]
    return -1


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    tests = open(filename,"r",encoding="latin1").readlines()
    correct = 0
    total = len(tests)
    for line in tests:
        line = line.strip("\n")
        line = line.split(" ")
        word = line[0]
        answer = line[1]
        choices = line[2:]
        sim_answer = most_similar_word(word,choices,semantic_descriptors,similarity_fn)
        if sim_answer == answer:
            correct += 1

    return float(correct/total)*100

if __name__ == "__main__":
    file = "wandp.txt"
    file1 = "proust.txt"
    file2 = "pg1184.txt"
    test = "test.txt"
    text1 = open(file1, "r", encoding = "latin1").read()
    sem_desc = build_semantic_descriptors_from_files([file,file1,file2])
    res = run_similarity_test(test,sem_desc,cosine_similarity)
    print(res)