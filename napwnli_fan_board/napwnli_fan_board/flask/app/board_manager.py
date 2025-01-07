import os
from hashlib import md5
import random
import re

flag_regex = re.compile(r"[a-zA-Z0-9]{31}=")

def get_board_content(board_name):
    directory = os.path.join(os.getcwd(), 'uploads', board_name)
    if not os.path.exists(directory):
        return "Don't have content yet!"
    
    with open(directory, 'r') as f:
        return f.read()
    
def save_board_content(board_name, content):
    directory = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Check if the file contains the flag
    with open(os.path.join(directory, board_name), 'r') as f:
        if flag_regex.search(f.read()):
            return False


    with open(os.path.join(directory, board_name), 'w') as f:
        f.write(content)

    return True

def get_random_board_content():
    directory = os.path.join(os.getcwd(), 'uploads')
    data = None

    for _ in range(20):
        while data is None:
            file_list = os.listdir(directory)
            file_name = random.choice(file_list)
            
            with open(os.path.join(directory, file_name), 'r') as f:
                data = f.read()

            if "!hidden!" in data or len(data) == 0:
                data = None

    return data if (data is not None) else "Forza Napoli Sempre!"


def initialize_board():
    sentences = ["Tifo Napoli da quando ero bambino!", "Forza Napoli Sempre!", "Napoli è la mia vita!",
                 "Un giorno all'improvviso...", "Forza Juve!", "Kvaratskhelia è il migliore!", "Napoli è una città bellissima!",
                 "Forza Inter!", "Noi del Nord siamo meglio di voi del Sud!"]
    
    directory = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(len(sentences)):
        file_name = md5(str(i).encode()).hexdigest()
        with open(os.path.join(directory, file_name), 'w') as f:
            f.write(sentences[i % len(sentences)])

    