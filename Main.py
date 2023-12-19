from Functions import *
import os
from random import randint

print("Hi, I'm Raquita ! My wonderful editors create me to analyse texts while they are studying hardly to success their DE in algebra (spoil: they failed).\n\
      If you want to analyse texts enter: analyse,\n\
      If you want to ask me some questions about texts enter: chat\n\
      If you want to leave me enter: stop")
while True:
    choice = input("What do you want to do ? ")
    if choice == "stop":
        break
    elif choice == "analyse":
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

        speeche_choice = input("Enter the number here : ")


        while speeche_choice not in "12345678":
            print("Choose the speeche you wish to analyze\n\
                1・Nomination Chirac 1 \n\
                2・Nomination Chirac 2 \n\
                3・Nomination Giscard dEstaing \n\
                4・Nomination Hollande \n\
                5・Nomination Macron \n\
                6・Nomination Mitterand 1 \n\
                7・Nomination Mitterand 2 \n\
                8・Nomination Sarkozy ")

            speeche_choice = input("Enter the number here : ")
        speeche_choice = int(speeche_choice)
        file_name = choices[speeche_choice]

        print("Choose the function you want to use on the speech\n\
            1・president_name_exact \n\
            2・first_name_associate_name \n\
            3・cleaned_file \n\
            4・total_word \n\
            5・term_frequency \n\
            6・tf_idf")
        function_choice = input("Enter the number here :")

        while function_choice not in "12345678":
            print("Choose the function you want to use on the speech \n\
            1・president_name_exact \n\
            2・first_name_associate_name \n\
            3・cleaned_file \n\
            4・total_word \n\
            5・term_frequency \n\
            6・tf_idf")
            function_choice = input("Enter the nuber here : ")

        function_choice = int(function_choice)

        if function_choice == 1:
            print(president_name_exact(file_name))
        elif function_choice == 2:
            print(first_name_associate_name(president_name_exact(file_name)))
        elif function_choice == 3:
            filepath = os.path.join('cleaned', file_name)
            f = open(filepath, 'r')
            print(f.read())
        elif function_choice == 4:
            for word in corpus.keys():
                print(word)
        elif function_choice == 5:
            tf = tf_dico[speeche_choice]
            tf_cleaned = {}
            for word in tf:
                if tf[word] != 0:
                    tf_cleaned[word] = tf[word]
            for key,value in tf_cleaned.items():
                print(key,value)
        else:
            for row in tf_idf_matrix:
                print(*row)

    elif choice == "chat":
        sentences = ["How can I help you ? ", "What's your question ? ", "Ask your question ! ", "I'm ready to answer your question ! ",
                     "I got the answers so don't hesitate to ask me ! "]
        nb_question = randint(0,len(sentences)-1)
        question_user = input(sentences[nb_question])
        while question_user == "":
            question_user = input(sentences[nb_question])

        question = tf_idf_question(tf_question(present_terms_in_corpus(corpus,clean_text(question_user))),idf_dico)
        while sum(question) == 0:
            question_user = input("I don't understand your question. Please retry: ")
            while question_user == "":
                question_user = input("I don't understand your question. Please retry: ")
            question = tf_idf_question(tf_question(present_terms_in_corpus(corpus,clean_text(question_user))),idf_dico)


        best_document = relevant_document(question,transposes_tf_idf_matrix,files_names)
        relevant_word = most_tf_idf_score(question,transposes_tf_idf_matrix)
        answer = find_the_sentence_in_speeches(best_document,relevant_word)
        print_answer(question_user,answer,best_document)

    else:
        pass

print("Ok, bye ! See you a next time ^^")
