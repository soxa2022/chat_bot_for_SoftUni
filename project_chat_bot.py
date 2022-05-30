from nltk.chat.util import Chat, reflections
import textwrap
import ast


def text(question):
    # you have to use the file from a folder. Download it from Github.
    with open(r'information.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    my_dict = ast.literal_eval(data)
    if question in my_dict:
        line = my_dict[question]
        return textwrap.fill(line, 145)


pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?\n(start with I am ...)", ]
    ],
    [
        r"hi|hey|hello|hola|holla",
        ["Hello", "Hey there", "Hi"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Anton Ivanov.You can call me SpecialOne!", ]
    ],
    [r"I am fine|good|ok|perfect|super",
     ["Great to hear that, How can I help you?", ]
     ],
    [
        r"Can you give me info for SoftUni`s program?",
        [text("Can you give me info for SoftUni`s program?"), ]
    ],
    [
        r"Do you have information for the curriculum?",
        [text("Do you have information for the curriculum?"), ]
    ],
    [
        r"How to apply?",
        [text("How to apply?"), ]
    ],
    [
        r"How will my training go?",
        [text("How will my training go?"), ]
    ],
    [
        r"When will I start work?",
        [text("When will I start work?"), ]
    ],
    [
        r"When will I graduate?",
        [text("When will I graduate?"), ]
    ],
    [
        r"Can you inform me about C# Web developer?",
        [text("Can you inform me about C# Web developer?"), ]
    ],
    [
        r"Can you inform me about Java Web developer?",
        [text("Can you inform me about Java Web developer?"), ]
    ],
    [
        r"Can you inform me about Python Web developer?",
        [text("Can you inform me about Python Web developer?"), ]
    ],
    [
        r"Can you inform me about JavaScript developer?",
        [text("Can you inform me about JavaScript developer?"), ]
    ],
    [
        r"What do you know about C# Full-Stack?",
        [text("What do you know about C# Full-Stack?"), ]
    ],
    [
        r"What do you know about Java Full-Stack?",
        [text("What do you know about Java Full-Stack?"), ]
    ],
    [
        r"What do you know about Python Full-Stack?",
        [text("What do you know about Python Full-Stack?"), ]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['I can not find any information about that! Please,ask me another question.']
    ]
]

print("")
# default message at the start of chat
print("""The list with possible questions: Can you give me info for SoftUni`s program?, Do you have information for the curriculum?,
How to apply?, How will my training go?, When will I start work?, When will I graduate?,Can you inform me about C# Web developer?,
Can you inform me about Java Web developer?, Can you inform me about Python Web developer?, Can you inform me about JavaScript developer?,
What do you know about C# Full-Stack?, What do you know about Java Full-Stack?, What do you know about Python Full-Stack?\n""")

print("Please type English language to start a conversation. ""Type 'quit' if you get enough information.\n\n"
      "Hi! I am a chat bot created by Anton Ivanov for the website of SoftUni.\n"
      "I am here to answer you questions about SoftUni`s Curriculum.\n\nWhat is your name?(please start with 'my name is ...')")
if __name__ == "__main__":

    chat = Chat(pairs, reflections)
    # Start conversation
    chat.converse()
