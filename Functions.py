import os
import string
import math

def n_function (c):
    print("Choose 1 for the display_president_name function ; 2 for the first_name_associate_name ; 3 for the lower_case ; 4 for the cleaned_file ; 5 for the term_frequency ; 6 inverse_document_frequency ; 7 for the tf_idf_matrix")
    c = int(input("Wich functions do you want call ?")) #Let the user choose the function he needs

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

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
    elif president_name == "Mitterand":
        return("Mitterans","François")
    elif president_name == "Sarkozy":
        return("Sarkozy","Nicolas")
    elif president_name == "Giscar dEstaing":
        return("Giscar dEstaing","Valéry")

c = 4
def display_president_name(list_president):
    for name in list_president:
        print(name[1],name[0])

c = 5
def lower_case(file):
    old_file = open(file,'r')
    cleaned_text = ""
    for char in old_file:
        if ord(char)<=ord("Z") and ord(char)>=ord("A"):
            cleaned_text += chr(ord(char) + 32)
        else:
            cleaned_text += char
    file_name = os.path.basename(file)
    new_file = os.path.join('/cleaned_speeches',file_name)
    with open(new_file,'w') as file2:
        file2.write(cleaned_text)

c = 5
def cleaned_file(file_path):
    with open(file_path,'r') as file:
        content = file.read()
    ponctuation = string.punctuation
    cleaning = ''.join(char for char in content if char not in ponctuation)
    with open(file_path,'w') as file2:
        file2.write(cleaning)

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

