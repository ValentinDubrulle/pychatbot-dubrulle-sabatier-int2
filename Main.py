from Functions import *
choices = {1: "Nomination_Chirac1.txt", 2: "Nomination_Chirac_2.txt", 3: "Nomination_Giscard dEstaing.txt", 4: "Nomination_Hollande.txt", 5: "Nomination_Macron.txt",\
           6: "Nomination_Mitterrand1.txt", 7: "Nomination_Mitterrand2.txt", 8: "Nomination_Sarkozy.txt"}

print("Choose the speeche you wish to analyze\n\
        1・Nomination Chirac 1 \n\
        2・Nomination Chirac 2 \n\
        3・Nomination Giscard dEstaing \n\
        4・Nomination Hollande \n\
        5・Nomination Macron \n\
        6・Nomination Mitterand 1 \n\
        7・Nomination Mitterand 2 \n\
        8・Nomination Sarkozy ")

 
# c = int(input("Choose 1 for the display_president_name function ; 2 for the first_name_associate_name ; \
            #   3 for the lower_case ; 4 for the cleaned_file ; 5 for the term_frequency ; 6 inverse_document_frequency ; 7 for the tf_idf_matrix")) #Let the user choose the function he needs

#display_president_name('Chirac')

'''list_tuple_president_name = []
for names in files_names:
    cleaned_name = president_name_exact(names)
    tuple_name = first_name_associate_name(cleaned_name)
    if tuple_name not in list_tuple_president_name:
        list_tuple_president_name.append(tuple_name)

print(n_function(c))

display_president_name(list_tuple_president_name)

list_files = os.listdir(directory)
for files in list_files:
    lower_case(files)

cleaned_directory = "./cleaned_speeches"
cleaned_list = list_of_files(cleaned_directory,"txt")
final_dictionary_word_cpt = {}

for file in cleaned_list:
    cleaned_file(file)
    content = str(open(file))
    term_frequency(content,final_dictionary_word_cpt)

dico_IDF = inverse_document_frequency(cleaned_directory,final_dictionary_word_cpt)
dico_TF_IDF = final_dictionary_word_cpt
for word in dico_TF_IDF.keys():
    dico_TF_IDF = final_dictionary_word_cpt[word] * dico_TF_IDF[word]

TF_IDF_matrix = tf_idf_matrix(cleaned_directory,final_dictionary_word_cpt)

#1
list_of_important_word = []
for word,score in dico_TF_IDF.items():
    if score == 0:
        list_of_important_word.append(word)

#2
highest = 0
for score in dico_TF_IDF.values():
    if score > highest:
        highest = score

for word,score in dico_TF_IDF.items():
    if score == highest:
        print(word)

#3
dico_chirac = {}
list_chirac_nomination = list_of_files(cleaned_directory,"txt")
for name in list_chirac_nomination:
    if cleaned_file(list_chirac_nomination) != "Chirac":
        list_chirac_nomination.pop(name)

for file in list_chirac_nomination:
    content = str(open(file))
    term_frequency(content,dico_chirac)

most_used_word_occurence = 0
most_used_word = ""
for word,occurence in dico_chirac.items():
    if occurence > most_used_word_occurence:
        most_used_word_occurence = occurence
        most_used_word = word

print("The most used word by Chirac is: ",most_used_word)

#4
list_of_index_nomination = []
list_of_president_nation = []
most_president_nation_index = 0

for word in TF_IDF_matrix:
    if word[0] == "nation":
        list_of_index_nomination.append(word)

for i in range(1,len(TF_IDF_matrix[0])):
    if list_of_index_nomination[i] >= 1:
        list_of_president_nation.append(TF_IDF_matrix[i])
        if list_of_index_nomination[i] > most_president_nation_index:
            most_president_nation_index = list_of_index_nomination[i]

for name in list_of_president_nation:
    name = president_name_exact(name)

most_president_nation = president_name_exact(TF_IDF_matrix[0][most_president_nation_index])
list_of_president_nation = set(list_of_president_nation)
print("Presidents who spoke of the 'Nation' are",list_of_president_nation)
print("The president who repeated it the most of times is:",most_president_nation)

#5
ecolo_climate_president = ""
for word in TF_IDF_matrix:
    if word[0] == "écologie" or word[0] == "climat":
        for i in range(1,len(word)):
            if word[i] >= 1:
                ecolo_climate_president =  TF_IDF_matrix[0][i]
            break
    if len(ecolo_climate_president)==0:
        break
ecolo_climate_president = president_name_exact(ecolo_climate_president)

print("The first president who talk about climate or ecology is:",ecolo_climate_president)

#6
total = len(TF_IDF_matrix[0])
word_used_by_all_president = []
for i in range(1,len(TF_IDF_matrix)):
    for j in range(1,len(TF_IDF_matrix[0])):
        for occcurence in TF_IDF_matrix[i][j]:
            total_occurence = 0
            total_occurence += occcurence
        if total == total_occurence:
            word_used_by_all_president.append(TF_IDF_matrix[i][0])

print("Words used by all the presidents are:",word_used_by_all_president)'''
