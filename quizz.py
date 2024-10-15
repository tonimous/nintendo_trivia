import tkinter as tk
import sqlite3
import random

# Create a database connection with error handling
try:
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    exit(1)

# Create the tables with error handling

try:
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT UNIQUE NOT NULL, 
        score INTEGER DEFAULT 0)''')
except sqlite3.Error as e:
    print(f"Error creating users table: {e}")
    conn.close()
    exit(1)
try:
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        question TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        question_id INTEGER, 
        answer_text TEXT, 
        correct BOOLEAN, 
        FOREIGN KEY(question_id) REFERENCES questions(id))''')
except sqlite3.Error as e:
    print(f"Error creating tables: {e}")
    conn.close()
    exit(1)

# Insert questions and answers into database
questions_data = [
    {
        "question": "When was Nintendo founded?",
        "answers": [
            {"text": "23 September 1889", "correct": True},
            {"text": "15 October 1899", "correct": False},
            {"text": "01 May 1901", "correct": False}
        ]
    },
    {
    "question": "In which \"Pokémon\" game was the Johto region introduced?",
    "answers": [
      {"text": "Pokémon Gold/Silver", "correct": True},
      {"text": "Pokémon Ruby/Sapphire", "correct": False},
      {"text": "Pokémon Diamond/Pearl", "correct": False}
    ]
    },
    {
    "question": "Which Nintendo game features a character named Kirby?",
    "answers": [
      {"text": "Kirby's Dream Land", "correct": True},
      {"text": "Super Mario Bros.", "correct": False},
      {"text": "The Legend of Zelda", "correct": False}
    ]
    },
    {
        "question": "Where was Nintendo founded?",
        "answers": [
            {"text": "Kyoto", "correct": False},
            {"text": "Saporo", "correct": False},
            {"text": "Shimogyō-Ku", "correct": True}
        ]
    },
    {
        "question": "Who founded Nintendo?",
        "answers": [
            {"text": "Fusajiro Yamauchi", "correct": True},
            {"text": "Hidetaka Miyazaki", "correct": False},
            {"text": "Shigeru Miyamoto", "correct": False}
        ]
    },
    {
        "question": "Which console was the successor of WiiU?",
        "answers": [
            {"text": "Nintendo Switch", "correct": True},
            {"text": "Nintendo Wii", "correct": False},
            {"text": "Nintendo GameCube", "correct": False}
        ]
    },
    {
        "question": "\"Yoshi's Crafted World\" is exclusive to which Nintendo console?",
        "answers": [
            {"text": "Nintendo GameBoy", "correct": False},
            {"text": "Nintendo Switch", "correct": True},
            {"text": "Nintendo 64", "correct": False}
        ]
    },
    {
        "question": "Which year did Nintendo win an Emmy for their original control pad?",
        "answers": [
            {"text": "2006", "correct": False},
            {"text": "2007", "correct": True},
            {"text": "2008", "correct": False}
        ]
    },
    {
        "question": "Which is the best-selling Nintendo exclusive game of all time?",
        "answers": [
            {"text": "Wii Sports", "correct": True},
            {"text": "Super Mario Bros", "correct": False},
            {"text": "Pokemon Red/Green/Blue/Yellow", "correct": False}
        ]
    },
    {
        "question": "Luigi is what relation to Super Mario?",
        "answers": [
            {"text": "His Uncle", "correct": False},
            {"text": "His Brother", "correct": True},
            {"text": "His Friend", "correct": False}
        ]
    },
    {
        "question": "Which year did Mario go three dimensional?",
        "answers": [
            {"text": "1994", "correct": False},
            {"text": "1995", "correct": False},
            {"text": "1996", "correct": True}
        ]
    },
    {
        "question": "Which \"Legend Of Zelda\" game celebrated its 20th anniversary at the end of April 2020?",
        "answers": [
            {"text": "The Legend Of Zelda: Majora's Mask.", "correct": True},
            {"text": "The Legend of Zelda: Breath of the Wild", "correct": False},
            {"text": "The Legend of Zelda: Ocarina of Time", "correct": False}
        ]
    },
        {
        "question": "What was the first handheld console released by Nintendo?",
        "answers": [
            {"text": "Game Boy", "correct": True},
            {"text": "Nintendo DS", "correct": False},
            {"text": "Game & Watch", "correct": False}
        ]
    },
    {
        "question": "Which game series features a character named Samus Aran?",
        "answers": [
            {"text": "Metroid", "correct": True},
            {"text": "Kirby", "correct": False},
            {"text": "Donkey Kong", "correct": False}
        ]
    },
    {
        "question": "What is the name of Nintendo’s famous fighting game franchise?",
        "answers": [
            {"text": "Super Smash Bros", "correct": True},
            {"text": "Fire Emblem", "correct": False},
            {"text": "Arms", "correct": False}
        ]
    },
    {
        "question": "Which character is known as the hero of Hyrule in \"The Legend of Zelda\" series?",
        "answers": [
            {"text": "Link", "correct": True},
            {"text": "Zelda", "correct": False},
            {"text": "Ganon", "correct": False}
        ]
    },
    {
        "question": "What was Nintendo’s first home console?",
        "answers": [
            {"text": "Nintendo Entertainment System (NES)", "correct": True},
            {"text": "Super Nintendo Entertainment System (SNES)", "correct": False},
            {"text": "Nintendo 64", "correct": False}
        ]
    },
      {
    "question": "Which Nintendo console was the first to be released in a portable form factor?",
    "answers": [
      {"text": "Game Boy", "correct": True},
      {"text": "Nintendo DS", "correct": False},
      {"text": "Nintendo Switch", "correct": False}
    ]
  },
  {
    "question": "In which year was the Nintendo Switch released?",
    "answers": [
      {"text": "2017", "correct": True},
      {"text": "2016", "correct": False},
      {"text": "2018", "correct": False}
    ]
  },
  {
    "question": "What is the name of the princess that Link must rescue in \"The Legend of Zelda\" games?",
    "answers": [
      {"text": "Zelda", "correct": True},
      {"text": "Princess Peach", "correct": False},
      {"text": "Princess Daisy", "correct": False}
    ]
  }
]



# Insert the questions and answers into the database
try:
    for q in questions_data:
        c.execute("INSERT INTO questions (question) VALUES (?)", (q['question'],))
        question_id = c.lastrowid  # Get the last inserted question id

        for a in q['answers']:
            c.execute("INSERT INTO answers (question_id, answer_text, correct) VALUES (?, ?, ?)",
                      (question_id, a['text'], a['correct']))
    conn.commit()
except sqlite3.Error as e:
    print(f"Error inserting data: {e}")
    conn.rollback()
    conn.close()
    exit(1)

# GUI setup
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x480")

score = 0
question_count = 0
max_questions = 3  # Set the max number of questions to 3
used_questions = []  # List to store used question IDs
timer_seconds = 15  # Set the timer to 15 seconds

# Styling options
font_style = ("Helvetica", 14)
button_style = {"font": ("Helvetica", 12), "bg": "#E60012", "fg": "white", "activebackground": "#FFCCD5"}
label_style = {"font": font_style, "wraplength": 350}


# Question and answer labels
question_label = tk.Label(root, text="", **label_style)
question_label.pack(padx=20, pady=20)

answers_frame = tk.Frame(root)
answers_frame.pack(pady=10)

score_label = tk.Label(root, text=f"Score: {score}", font=font_style)
score_label.pack(pady=10)

feedback_label = tk.Label(root, text="", font=font_style)
feedback_label.pack(pady=10)

timer_label = tk.Label(root, text="", font=font_style)
timer_label.pack(pady=10)

# Load a random question from the database with error handling
def load_question():
    global question_count

    if question_count >= max_questions:
        end_game() 
        return

    score_label.config(text="")
    for widget in answers_frame.winfo_children():
        widget.destroy()

    try:
        while True:
            c.execute("SELECT id, question FROM questions ORDER BY RANDOM() LIMIT 1")
            question = c.fetchone()
            if question[0] not in used_questions:
                used_questions.append(question[0])
                break

        question_label.config(text=question[1])

        c.execute("SELECT id, answer_text, correct FROM answers WHERE question_id = ?", (question[0],))
        answers = c.fetchall()
    except sqlite3.Error as e:
        print(f"Error loading question: {e}")
        question_label.config(text="Error loading question. Please try again.")
        return

    def check_answer(is_correct):
        global score
        if is_correct:
            score_label.config(text="Correct!", fg="green")
            score += 1
        else:
            score_label.config(text="Incorrect!", fg="red")
        score_label.config(text=f"Score: {score}")
        disable_answers()
        next_button.config(state='normal')  # Enable the next button after an answer is selected
        root.after_cancel(timer_id)  # Cancel the timer


    for ans in answers:
        btn = tk.Button(answers_frame, text=ans[1], command=lambda is_correct=ans[2]: check_answer(is_correct), **button_style)
        btn.pack(anchor='w', pady=5)

    question_count += 1
    next_button.config(state='disabled')  # Disable the next button initially
    timer_seconds = 15
    update_timer()

 # Start the timer
def update_timer():
    global timer_seconds, timer_id
    if timer_seconds > 0:
        timer_seconds -= 1
        timer_label.config(text=f"Time left: {timer_seconds} seconds")
        timer_id = root.after(1000, update_timer)
    else:
        disable_answers()
        next_button.config(state='disabled')
        feedback_label.config(text="Time's up!", fg="red")
        timer_label.pack_forget()
        end_game()


def disable_answers():
    for widget in answers_frame.winfo_children():
        widget.config(state='disabled')

# Function to end the game
def end_game():
    question_label.config(text="Quiz finished!")

    for widget in answers_frame.winfo_children():
        widget.destroy()
    next_button.pack_forget()  # Hide the next button
    score_label.config(text=f"Your Final Score is: {score} out of {max_questions}", fg="blue")
    play_again_button.pack(pady=10)

def reset_quiz():
    global score, question_count, used_questions, timer_seconds
    score = 0
    question_count = 0
    used_questions = []
    timer_seconds = 15
    play_again_button.pack_forget()  # Hide the play again button
    timer_label.pack(pady=10) # Show the timer
    next_button.pack(pady=10)  # Show the next button
    feedback_label.pack_forget()  # Hide the feedback label
    load_question()


# Button to the next question
next_button = tk.Button(root, text="Next Question", command=load_question, **button_style)
next_button.pack(pady=10)

# Button to play the quiz again
play_again_button = tk.Button(root, text="Play Again", command=reset_quiz, **button_style)
play_again_button.pack_forget()  # Ensure the play again button is hidden initially

# Start the question
load_question()

# Start the Tkinter main loop
root.mainloop()

# Close database connection with error handling
try:
    conn.close()
except sqlite3.Error as e:
    print(f"Error closing the database connection: {e}")