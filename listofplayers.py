from pyscript import display
from js import document

def show_players(e): # does the code after the button is clicked
    document.getElementById('output1').innerHTML = ''

    players = (
        "Ebtisam A Al Hazmi",
        "Yaniszsol Aeiou Alvarez",
        "Ethan Drei S Belsa",
        "Giana Zoe Bernas",
        "Julianna Calaycay",
        "Jamie Alyanna Castelo",
        "Francesca Meyer Cruz",
        "Ely Defensor",
        "Dannielle Luna Dimasuhid",
        "Althea Mauri Francisco",
        "Cristina Wen Hsu",
        "Denise Juatchon",
        "Judah Judge",
        "Francis Lilagan",
        "Sam Luna",
        "Enzo Josh Macaranas",
        "Pain Adler Mateo",
        "Ashley Mondragon",
        "Lance Naldoza",
        "Gabriel Emilio Natividad",
        "Sofia Ng",
        "Hendrich Mathis Ong",
        "Trisha Paz",
        "Miguel Ramos",
        "Queeny Haraj Ramos",
        "Samantha Ramos",
        "Ashlei Reodica",
        "Vaughn Repolona"
    ) # list of players

    number = 1
    for i in players: # using loops we can display the list players
        display("Player " + str(number) + ": " + i, target="output1")
        number += 1 