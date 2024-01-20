from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"

class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzes")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="Questions", font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        self.image = PhotoImage(file='images/true.png')
        self.button_true = Button(image=self.image, highlightthickness=0,command=self.check_true)
        self.button_true.grid(row=2, column=0)
        self.imagef = PhotoImage(file='images/false.png')
        self.button_false = Button(image=self.imagef, highlightthickness=0, command=self.check_false)
        self.button_false.grid(row=2, column=1)
        self.get_next()

        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="That is it! Thanks")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000,self.get_next)


