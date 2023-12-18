import os
import string
import math

def list_of_files(directory, extension): 
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./speeches"
files_names = list_of_files(directory, "txt") #Get a list of files in a directory with a specific extension

c = 2
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


c = 3
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


c = 4
def lower_case(files):
    for file in files:
        with open ("./speeches/"+ file, "r") as f1:
            lines = f1.readlines()
            cleaned_line = ""
            for line in lines:
                for char in line:
                    if ord(char)<=ord("Z") and ord(char)>=ord("A"):
                        cleaned_line += chr(ord(char) + 32)
                    else:
                        cleaned_line += char
        with open ("./cleaned/"+ file, "w") as f2:
            f2.write(cleaned_line) 


lower_case(files_names)

c = 5
def cleaned_file(files):
    for file in files:
        with open("./cleaned/"+file,'r') as f:
            content = f.read()
        ponctuation = string.punctuation
        cleaning = ''.join(char for char in content if char not in ponctuation)
        with open("./cleaned/"+file,'w') as f2:
            f2.write(cleaning)

cleaned_file(files_names)



c = 6 
def term_frequency(text,word_cpt):
    list_of_words = text.split()
    for word in list_of_words:
        if word in word_cpt:
            word_cpt[word] += 1
        else:
            word_cpt[word] = 1
    return word_cpt

c = 7 
def inverse_document_frequency(directory,final_dictionary_word_cpt):
    number_of_files = len([file for file in os.listdir(directory)])
    idf_score = {}
    for word in final_dictionary_word_cpt.keys():
        cpt_of_file_who_contain_word = 0
        for file in os.listdir(directory):
            opened_file = os.path.join(directory,file)
            file_reading = open(opened_file,'r')
            content = str(file_reading)
            if word in content:
                cpt_of_file_who_contain_word += 1
        idf_score[word] = math.log(number_of_files/cpt_of_file_who_contain_word)
    return idf_score

c = 8 
def tf_idf_matrix(directory,final_dictionary_word_cpt):
    matrix = []
    names_files = os.listdir(directory)
    columns = [None]
    for file in names_files:
        columns.append(file)
    matrix.append(columns)
    for word,occurence in final_dictionary_word_cpt.items():
        if occurence == 1:
            row = [word]
            for file in os.listdir(directory):
                opened_file = os.path.join(directory, file)
                file_reading = open(opened_file, 'r')
                content = str(file_reading)
                if word in file:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
    return matrix
