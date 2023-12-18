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



def first_name_associate_name(president_name):
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



def lower_case(files):
    for file in files:
        with open ("./speeches/"+ file, "r",encoding="utf-8") as f1:
            lines = f1.readlines()
            cleaned_line = ""
            for line in lines:
                for char in line:
                    if ord(char)<=ord("Z") and ord(char)>=ord("A"):
                        cleaned_line += chr(ord(char) + 32)
                    else:
                        cleaned_line += char
        with open ("./cleaned/"+ file, "w",encoding="utf-8") as f2:
            f2.write(cleaned_line)


lower_case(files_names)


def cleaned_file(files):
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




def total_word(files):
    all_word = {}
    for file in files:
        with open("./cleaned/" + file, "r",encoding="utf-8") as f:
            content = f.read()
            list_of_words = content.split()
            for word in list_of_words:
                if word not in all_word:
                    all_word[word] = 0
    return all_word

corpus = total_word(files_names)


def term_frequency(files,corpus):
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



def inverse_document_frequency(list_of_dico,list_of_word):
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



def tf_idf(dico_tf,dico_idf):
    matrix = []
    for word in dico_idf:
        row = [word]
        for i in range(len(dico_tf)):
            row.append(dico_tf[i][word]*dico_idf[word])
        matrix.append(row)
    return matrix

tf_idf_matrix = tf_idf(tf_dico,idf_dico)
