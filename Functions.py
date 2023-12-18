import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./speeches"
files_names = list_of_files(directory, "txt") #Get a list of files in a directory with a specific extension


def president_name_exact(name_file):
    """
    :param name_file: str
    :return: Only the president's name of the nomination
    """
    president_name = name_file[11:]     #remove "Nomination_"
    if "1" in president_name or "2" in president_name:
        president_name = president_name[:-5]    #remove "[number].txt"
    else:
        president_name = president_name[:-4]    #remove ".txt"
    return president_name



def first_name_associate_name(president_name): #Asociates the last name of the president with his first name
    if president_name == "Chirac":
        return ("Chirac","Jacques")
    elif president_name == "Hollande":
        return("Hollande","François")
    elif president_name == "Mitterrand":
        return("Mitterrand","François")
    elif president_name == "Sarkozy":
        return("Sarkozy","Nicolas")
    elif president_name == "Giscard dEstaing":
        return("Giscard dEstaing","Valéry")
    elif president_name == "Macron":
        return ("Macron", "Emmanuel")



def lower_case(files):  #Turns all uppercase letters into lowercase letters
    for file in files:
        with open ("./speeches/"+ file, "r",encoding="utf-8") as f1:  #Open files in speeches. (UTF-8 for decoding special characters)
            lines = f1.readlines()
            cleaned_line = ""
            for line in lines:
                for char in line:
                    if ord(char)<=ord("Z") and ord(char)>=ord("A"):  
                        cleaned_line += chr(ord(char) + 32)
                    else:
                        cleaned_line += char
        with open ("./cleaned/"+ file, "w",encoding="utf-8") as f2:    #Adds modified speeches to a new folder (cleaned)
            f2.write(cleaned_line)


lower_case(files_names)


def cleaned_file(files):  #Deletes or transforms special characters
    for file in files:
        ponctuation = "!#$%&()*+,./:;<=>?@[\]^_`{|}~"
        special_case = "-'"
        special_chr = {"é": "e", "è": "e", "ê": "e", "ë": "e", "à": "a", "â": "a", "ä": "a","î": "i", "ï": "i", "ù": "u", "û": "u", "ô": "o", "ö": "o", "ç": "c", "œ": "oe"}
        with open("./cleaned/"+file,'r',encoding="utf-8") as f:
            content = f.read()
        cleaning = ''
        for char in content:
            if char in ponctuation:
                cleaning += ''
            elif char in special_chr:
                cleaning += special_chr[char]
            elif char in special_case or char == '\n':
                cleaning += ' '
            else:
                cleaning += char
        with open("./cleaned/"+file,'w',encoding="utf-8") as f2:
            f2.write(cleaning)

cleaned_file(files_names)




def total_word(files):  #Counts the iterations of a word in the file
    all_word = {} 
    for file in files:
        with open("./cleaned/" + file, "r",encoding="utf-8") as f:
            content = f.read()
            list_of_words = content.split()
            for word in list_of_words:
                if word not in all_word:
                    all_word[word] = 0  #Use a dictionary to list all the words in the text 
    return all_word

corpus = total_word(files_names)


def term_frequency(files,corpus):  '''Counts the occurrence of each word in the file'''
    liste_of_dico = []
    for file in files:
        dico_of_word = {}
        for elt in corpus:
            dico_of_word[elt] = 0
        with open("./cleaned/" + file, "r",encoding="utf-8") as f:
            content = f.read()
            list_of_words = content.split()
            for word in list_of_words:
               dico_of_word[word] += 1
        liste_of_dico.append(dico_of_word)
    return liste_of_dico


tf_dico = term_frequency(files_names,corpus)



def inverse_document_frequency(list_of_dico,list_of_word):  #Create an IDF score 
    number_of_files = len(list_of_dico)
    idf_score = {}
    for word in list_of_word:
        cpt_of_file_who_contain_word = 0
        for dico in list_of_dico:
            if dico[word] > 0:
                cpt_of_file_who_contain_word += 1
        idf_score[word] = math.log10(number_of_files/cpt_of_file_who_contain_word)
    return idf_score

idf_dico = inverse_document_frequency(tf_dico,corpus)

def tf_idf(dico_tf,dico_idf):  #calculates the TF-IDF score for each word in each document and stores the result in a matrix
    matrix = []
    for word in dico_idf:
        row = [word]
        for i in range(len(dico_tf)):
            row.append(dico_tf[i][word]*dico_idf[word])
        matrix.append(row)
    return matrix

tf_idf_matrix = tf_idf(tf_dico,idf_dico)

def lower_question(char):  #Turns all uppercase letters into lowercase letters
    if ord(char)>=ord('A') and ord(char)<=ord('Z'):
        return chr(ord(char) + 32)
    else:
        return char

def clean_question(text):  #Deletes or transforms special characters
    ponctuation = "!#$%&()*+,./:;<=>?@[\]^_`{|}~"
    special_case = "-'"
    special_chr = {"é": "e", "è": "e", "ê": "e", "ë": "e", "à": "a", "â": "a", "ä": "a", "î": "i", "ï": "i", "ù": "u", "û": "u", "ô": "o", "ö": "o", "ç": "c", "œ": "oe"}
    cleaning = ''
    for char in text:
        if char in ponctuation:
            cleaning += ''
        elif char in special_case:
            cleaning += ' '
        elif char in special_chr:
            cleaning += special_chr[char]
        else:
            cleaning += lower_question(char)
    question_word = cleaning.split()
    return question_word

def present_terms_in_corpus(corpus,cleaned_question):  #Check whether each of the words in the question is present in the corpus
    return [word for word in cleaned_question if word in corpus]

def tf_question(cleaned_question):  #Calculate the tf (term freqency) of each word in the question
    dico_question = {}
    for word in cleaned_question:
        if word in dico_question:
            dico_question[word] += 1
        else:
            dico_question[word] = 1
    for elt in dico_question:
        dico_question[elt] = dico_question[elt]/len(cleaned_question)
    print(dico_question)
    return dico_question

def tf_idf_question(tf_dico_question,dico_idf):
    vector = []
    for word in dico_idf:
        if word in tf_dico_question:
            vector.append(tf_dico_question[word]*dico_idf[word])
        else:
            vector.append(0)
    return vector

def scalar_product(vector_A,vector_B): #calculates the scalar product between two vectors by multiplying the corresponding elements and adding these products together
    tot = 0
    for i in range(1,len(vector_A)):
        tot += vector_A[i] * vector_B[i]
    return tot

def norm_of_vector(vector):
    tot = 0
    for i in range(1,len(vector)):
        tot += (vector[i])*2
    tot = math.sqrt(tot)
    return tot

def similarity(vector_A,vector_B):
     return scalar_product(vector_A,vector_B)/(norm_of_vector(vector_A)*norm_of_vector(vector_B))

def transpose_matrix(matrix):
    nb_row = len(matrix)
    nb_col = len(matrix[0])
    transposed_matrix = [[matrix[i][j] for i in range(nb_row)] for j in range(nb_col)]
    return transposed_matrix

def revenant_document(vector_question,transposed_matrix_tf_idf,list_of_files):
    best_score = 0
    index = None
    for i in range(len(transposed_matrix_tf_idf)):
        current_score = similarity(vector_question,transposed_matrix_tf_idf[i])
        if current_score > best_score:
            index = i
    return list_of_files[index]
