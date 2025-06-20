import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define pairs of patterns and responses
pairs = [
    [
        r"(.*) your name ?",
        ["My name is Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what (.*) want ?",
        ["I want to help you.",]
    ],
    [
        r"(.*) created ?",
        ["I was created by a Python enthusiast.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a digital entity, everywhere and nowhere at the same time.",]
    ],
    [
        r"how (.*) weather ?",
        ["Weather is just a concept for me!",]
    ],
    [
        r"(.) help (.)",
        ["Sure, I'd be happy to help!"]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I love watching all kinds of sports!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that.",]
    ]
]

# Create Chatbot class
class Chatbot:
    def _init_(self):
        self.chat = Chat(pairs, reflections)

    def get_response(self, text):
        return self.chat.respond(text)
