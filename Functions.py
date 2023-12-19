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
        Extract only the president's name from the nomination file name.

        Parameters:
        name_file (str): The file name of the nomination.

        Returns:
        str: The president's name.
        """
    president_name = name_file[11:]     #remove "Nomination_"
    if "1" in president_name or "2" in president_name:
        president_name = president_name[:-5]    #remove "[number].txt"
    else:
        president_name = president_name[:-4]    #remove ".txt"
    return president_name



def first_name_associate_name(president_name):
    """
    Map the president's last name to the first name.

    Parameters:
    president_name (str): The last name of the president.

    Returns:
    tuple: A tuple containing the last name and first name of the president.
    """
    # Mapping last names to first names
    if president_name == "Chirac":
        return ("Chirac", "Jacques")
    elif president_name == "Hollande":
        return ("Hollande", "François")
    elif president_name == "Mitterrand":
        return ("Mitterrand", "François")
    elif president_name == "Sarkozy":
        return ("Sarkozy", "Nicolas")
    elif president_name == "Giscard dEstaing":
        return ("Giscard dEstaing", "Valéry")
    elif president_name == "Macron":
        return ("Macron", "Emmanuel")




def lower_case(files):
    """
    Convert the content of files to lowercase and write to new files.

    Parameters:
    files (list): List of file names.

    Returns:
    None
    """
    for file in files:
        # Read content from the original file
        with open("./speeches/" + file, "r", encoding="utf-8") as f1:
            lines = f1.readlines()
            cleaned_line = ""
            # Process each line in the original file
            for line in lines:
                # Process each character in the line
                for char in line:
                    # Convert uppercase characters to lowercase
                    if ord(char) <= ord("Z") and ord(char) >= ord("A"):
                        cleaned_line += chr(ord(char) + 32)
                    else:
                        cleaned_line += char
            # Write the cleaned content to a new file
            with open("./cleaned/" + file, "w", encoding="utf-8") as f2:
                f2.write(cleaned_line)


lower_case(files_names)


def cleaned_file(files):
    """
    Clean the content of files by removing punctuation and special characters.

    Parameters:
    files (list): List of file names.

    Returns:
    None
    """
    for file in files:
        # Define sets of characters to be removed or replaced
        ponctuation = "!#$%&()*+,./:;<=>?@[\\]^`{|}~"
        special_case = "_-'"
        special_chr = {"é": "e", "è": "e", "ê": "e", "ë": "e", "à": "a", "â": "a", "ä": "a", "î": "i", "ï": "i",
                       "ù": "u", "û": "u", "ô": "o", "ö": "o", "ç": "c", "œ": "oe",
                       "À": "a", "É": "e", "È": "e", "Ê": "e", "Ë": "e", "Î": "i", "Ï": "i", "Ô": "o", "Œ": "oe",
                       "Ù": "u", "Û": "u", "Ü": "u", "Ç": "c"}

        with open("./cleaned/" + file, 'r', encoding="utf-8") as f:
            content = f.read()

        cleaning = ''
        # Process each character in the content
        for char in content:
            # Remove or replace characters based on predefined sets
            if char in ponctuation:
                cleaning += ''
            elif char in special_chr:
                cleaning += special_chr[char]
            elif char in special_case or char == '\n':
                cleaning += ' '
            else:
                cleaning += char

        # Write the cleaned content to a new file
        with open("./cleaned/" + file, 'w', encoding="utf-8") as f2:
            f2.write(cleaning)

cleaned_file(files_names)




def total_word(files):
    """
    Count the total number of unique words in the corpus.

    Parameters:
    files (list): List of file names.

    Returns:
    dict: A dictionary with unique words as keys and counts as values.
    """
    all_word = {}
    for file in files:
        # Read content from the cleaned file
        with open("./cleaned/" + file, "r", encoding="utf-8") as f:
            content = f.read()
            list_of_words = content.split()
            # Count occurrences of each unique word
            for word in list_of_words:
                if word not in all_word:
                    all_word[word] = 0
    return all_word

corpus = total_word(files_names)


def term_frequency(files, corpus):
    """
    Calculate the term frequency (TF) for each word in the corpus.

    Parameters:
    files (list): List of file names.
    corpus (dict): A dictionary with unique words as keys and counts as values.

    Returns:
    list: A list of dictionaries, each containing the term frequency for words in a file.
    """
    list_of_dico = []
    for file in files:
        dico_of_word = {}
        # Initialize the dictionary with all words from the corpus
        for elt in corpus:
            dico_of_word[elt] = 0
        with open("./cleaned/" + file, "r", encoding="utf-8") as f:
            content = f.read()
            list_of_words = content.split()
            # Count occurrences of each word in the file
            for word in list_of_words:
                dico_of_word[word] += 1
        list_of_dico.append(dico_of_word)
    return list_of_dico


tf_dico = term_frequency(files_names,corpus)



def inverse_document_frequency(list_of_dico, list_of_word):
    """
    Calculate the inverse document frequency (IDF) for each word in the corpus.

    Parameters:
    list_of_dico (list): List of dictionaries, each containing the term frequency for words in a file.
    list_of_word (list): List of all words in the corpus.

    Returns:
    dict: A dictionary with words as keys and their IDF scores as values.
    """
    number_of_files = len(list_of_dico)
    idf_score = {}
    for word in list_of_word:
        cpt_of_file_who_contain_word = 0
        # Count the number of files containing the word
        for dico in list_of_dico:
            if dico[word] > 0:
                cpt_of_file_who_contain_word += 1
        # Calculate IDF score for the word
        idf_score[word] = math.log10(number_of_files / (cpt_of_file_who_contain_word + 1))
    return idf_score

idf_dico = inverse_document_frequency(tf_dico,corpus)


def tf_idf(dico_tf, dico_idf):
    """
    Calculate the TF-IDF matrix for the corpus.

    Parameters:
    dico_tf (list): List of dictionaries, each containing the term frequency for words in a file.
    dico_idf (dict): Dictionary with words as keys and their IDF scores as values.

    Returns:
    list: TF-IDF matrix, where each row represents a word, and each column represents a file.
    """
    matrix = []

    # Iterate over words in the IDF dictionary
    for word in dico_idf:
        row = [word]

        # Calculate TF-IDF score for each file
        for i in range(len(dico_tf)):
            row.append(dico_tf[i][word] * dico_idf[word])

        # Append the row to the matrix
        matrix.append(row)

    return matrix

tf_idf_matrix = tf_idf(tf_dico,idf_dico)

def lower_question(char):
    """
    Convert uppercase character to lowercase if applicable.

    Parameters:
    char (str): Input character.

    Returns:
    str: Lowercase character if input is uppercase; otherwise, returns the input character.
    """
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return chr(ord(char) + 32)
    else:
        return char


def clean_text(text):
    """
    Clean the input text by removing punctuation, handling special cases, and converting to lowercase.

    Parameters:
    text (str): Input text.

    Returns:
    list: List of cleaned words extracted from the input text.
    """
    ponctuation = "!#$%&()*+,./:;<=>?@[\]^_`{|}~"
    special_case = "-'"
    special_chr = {"é": "e", "è": "e", "ê": "e", "ë": "e", "à": "a", "â": "a", "ä": "a", "î": "i", "ï": "i", "ù": "u",
                   "û": "u", "ô": "o", "ö": "o", "ç": "c", "œ": "oe",
                   "À": "a", "É": "e", "È": "e", "Ê": "e", "Ë": "e", "Î": "i", "Ï": "i", "Ô": "o", "Œ": "oe", "Ù": "u",
                   "Û": "u", "Ü": "u", "Ç": "c"}

    cleaning = ''

    # Process each character in the input text
    for char in text:
        # Remove punctuation
        if char in ponctuation:
            cleaning += ''
        # Handle special cases
        elif char in special_case:
            cleaning += ' '
        # Replace special characters
        elif char in special_chr:
            cleaning += special_chr[char]
        else:
            # Convert characters to lowercase using the specified function
            cleaning += lower_question(char)

    # Split the cleaned text into a list of words
    question_word = cleaning.split()

    return question_word

def present_terms_in_corpus(corpus, cleaned_question):
    """
    Filter and return the words from the cleaned question that are present in the corpus.

    Parameters:
    corpus (dict): A dictionary with unique words as keys.
    cleaned_question (list): List of cleaned words from the question.

    Returns:
    list: List of words from the cleaned question that are present in the corpus.
    """
    # Use list comprehension to filter words present in both cleaned_question and corpus
    return [word for word in cleaned_question if word in corpus]


def tf_question(cleaned_question):
    """
    Calculate the term frequency (TF) for each word in the cleaned question.

    Parameters:
    cleaned_question (list): List of cleaned words from the question.

    Returns:
    dict: A dictionary with words as keys and their normalized TF scores as values.
    """
    dico_question = {}

    # Count occurrences of each word in the cleaned question
    for word in cleaned_question:
        if word in dico_question:
            dico_question[word] += 1
        else:
            dico_question[word] = 1

    # Normalize TF scores by dividing by the total number of words in the cleaned question
    for elt in dico_question:
        dico_question[elt] = dico_question[elt] / len(cleaned_question)

    return dico_question


def tf_idf_question(tf_dico_question, dico_idf):
    """
    Calculate the TF-IDF vector for the cleaned question.

    Parameters:
    tf_dico_question (dict): Dictionary with words as keys and their normalized TF scores.
    dico_idf (dict): Dictionary with words as keys and their IDF scores.

    Returns:
    list: TF-IDF vector for the cleaned question.
    """
    vector = []

    # Iterate over words in the IDF dictionary
    for word in dico_idf:
        # Calculate TF-IDF score for each word in the cleaned question
        if word in tf_dico_question:
            vector.append(tf_dico_question[word] * dico_idf[word])
        else:
            vector.append(0)

    return vector


def scalar_product(vector_A, vector_B):
    """
    Calculate the scalar product of two vectors.

    Parameters:
    vector_A (list): First vector.
    vector_B (list): Second vector.

    Returns:
    float: Scalar product of the two input vectors.
    """
    tot = 0

    # Iterate over the elements of the vectors and calculate the sum of products
    for i in range(1, len(vector_A)):
        tot += vector_A[i] * vector_B[i]

    return tot


def norm_of_vector(vector):
    """
    Calculate the Euclidean norm of a vector.

    Parameters:
    vector (list): Input vector.

    Returns:
    float: Euclidean norm of the input vector.
    """
    tot = 0

    # Iterate over the elements of the vector and calculate the sum of squares
    for i in range(1, len(vector)):
        tot += (vector[i]) ** 2

    # Take the square root of the sum of squares to get the Euclidean norm
    tot = math.sqrt(tot)

    return tot

def similarity(vector_A, vector_B):
    """
    Calculate the cosine similarity between two vectors.

    Parameters:
    vector_A (list): First vector.
    vector_B (list): Second vector.

    Returns:
    float: Cosine similarity between the two input vectors.
    """
    # Calculate the cosine similarity using the scalar product and vector norms
    return scalar_product(vector_A, vector_B) / (norm_of_vector(vector_A) * norm_of_vector(vector_B))


def transpose_matrix(matrix):
    """
    Transpose the input matrix.

    Parameters:
    matrix (list of lists): Input matrix.

    Returns:
    list of lists: Transposed matrix.
    """
    nb_row = len(matrix)
    nb_col = len(matrix[0])

    # Use list comprehension to create the transposed matrix
    transposed_matrix = [[matrix[i][j] for i in range(nb_row)] for j in range(nb_col)]

    return transposed_matrix

transposes_tf_idf_matrix = transpose_matrix(tf_idf_matrix)


def relevant_document(vector_question, transposed_matrix_tf_idf, list_of_files):
    """
    Find the most relevant document based on the cosine similarity between the question vector
    and each document vector in the transposed TF-IDF matrix.

    Parameters:
    vector_question (list): TF-IDF vector of the cleaned question.
    transposed_matrix_tf_idf (list of lists): Transposed TF-IDF matrix of the corpus.
    list_of_files (list): List of file names in the corpus.

    Returns:
    str: The most relevant document name from the provided list of files.
    """
    best_score = 0
    index = None

    # Iterate over document vectors in the transposed matrix
    for i in range(1, len(transposed_matrix_tf_idf)):
        current_score = similarity(vector_question, transposed_matrix_tf_idf[i])

        # Update best score and index if a higher similarity is found
        if current_score > best_score:
            best_score = current_score
            index = i

    # Return the corresponding document name from the list of files
    return list_of_files[(index - 1) % 8]


def most_tf_idf_score(vector_question, transposed_matrix):
    """
    Find the term with the highest TF-IDF score in the question vector.

    Parameters:
    vector_question (list): TF-IDF vector of the cleaned question.
    transposed_matrix (list of lists): Transposed matrix used for obtaining terms.

    Returns:
    str: The term with the highest TF-IDF score.
    """
    best = 0
    index = None

    # Iterate over elements of the question vector
    for i in range(len(vector_question)):
        # Update best score and index if a higher TF-IDF score is found
        if vector_question[i] > best:
            best = vector_question[i]
            index = i

    # Return the term with the highest TF-IDF score
    return transposed_matrix[0][index]


def find_the_sentence_in_speeches(relevant_file, relevant_word):
    """
    Find the sentence containing the relevant word in a specific document.

    Parameters:
    relevant_file (str): Name of the relevant document file.
    relevant_word (str): Relevant word to search for in the document.

    Returns:
    str: The sentence containing the relevant word in the specified document.
    """
    with open("./speeches/" + relevant_file, "r", encoding="utf-8") as f:
        content = f.read()
        list_of_words = content.split()
        index = 0
        found = False
        word_uncleaned = ''

        # Iterate over words in the document content
        while not (found) and index < len(list_of_words):
            cleaned_word = clean_text(list_of_words[index])

            # Handle cases with multiple words separated by spaces
            if " " in cleaned_word:
                mini_list = cleaned_word.split()
                for elt in mini_list:
                    if elt == relevant_word:
                        found = True
                        word_uncleaned = elt
            elif cleaned_word == []:
                pass
            elif cleaned_word[0] == relevant_word:
                found = True
                word_uncleaned = cleaned_word[0]
            index += 1

        # Split content into sentences and find the one containing the relevant word
        text_splited_in_sentence = content.replace("M.", "Mr").split(".")
        for sentence in text_splited_in_sentence:
            if word_uncleaned in sentence:
                return sentence + '.'


def print_answer(question, answer, nomination):
    """
    Print the formatted answer based on the question, answer, and president's nomination.

    Parameters:
    question (str): The original question.
    answer (str): The relevant answer.
    nomination (str): President's nomination related to the question.

    Returns:
    None: Prints the formatted answer to the console.
    """
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!"
    }
    family_name, name = first_name_associate_name(president_name_exact(nomination))
    start_answer = ''
    list_of_word = question.split()

    # Find the appropriate starter based on the question words
    for word in list_of_word:
        if word in question_starters:
            start_answer += question_starters[word]
            break

    # Print the formatted answer
    print(f'{start_answer} Le président {name} {family_name} a dit : "{answer}" durant une de ses nominations.')

