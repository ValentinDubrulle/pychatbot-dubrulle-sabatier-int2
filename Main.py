from Functions import *
import os

choices = {1: "Nomination_Chirac1.txt", 2: "Nomination_Chirac2.txt", 3: "Nomination_Giscard dEstaing.txt", 4: "Nomination_Hollande.txt", 5: "Nomination_Macron.txt",
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

speeche_choice = int(input("Enter the number here :"))


while speeche_choice < 1 or speeche_choice > 8:
    print("Choose the speeche you wish to analyze\n\
        1・Nomination Chirac 1 \n\
        2・Nomination Chirac 2 \n\
        3・Nomination Giscard dEstaing \n\
        4・Nomination Hollande \n\
        5・Nomination Macron \n\
        6・Nomination Mitterand 1 \n\
        7・Nomination Mitterand 2 \n\
        8・Nomination Sarkozy ")

    speeche_choice = int(input("Enter the number here :"))

file_name = choices[speeche_choice]

print("Choose the function you want to use on the speech\n\
    1・president_name_exact \n\
    2・first_name_associate_name \n\
    3・lower_case \n\
    4・cleaned_file \n\
    5・term_frequency \n\
    6・inverse_document_frequency \n\
    7・tf_idf_matrix")
function_choice = int(input("Enter the number here :"))

while function_choice < 1 or function_choice > 8:
    print("Choose the function you want to use on the speech\n\
        1・president_name_exact \n\
        2・first_name_associate_name \n\
        3・lower_case \n\
        4・cleaned_file \n\
        5・term_frequency \n\
        6・inverse_document_frequency \n\
        7・tf_idf_matrix")
    function_choice = int(input("Enter the nuber here : "))

if function_choice == 1 :
    print(president_name_exact(file_name))
elif function_choice == 2 :
    print(first_name_associate_name(president_name_exact(file_name)))
elif function_choice == 3:
    filepath = os.path.join('cleaned', file_name)
    f = open(filepath, 'r')
    print(f.read)
elif function_choice == 4:
    cleaned_file()
elif function_choice == 5:
    term_frequency
elif function_choice == 6:
    tf_idf_matrix()
