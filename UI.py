from tkinter import *
from quiz import Quiz

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: Quiz):  # TODO in order to make a connection between Quiz and QuizInterface,
        # we insert Quiz as a property of QuizInterface, so we can tap into ots method
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler App")
        self.window.config(bg=THEME_COLOR, padx=30, pady=20)

        self.score = self.quiz.score

        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, font=('kefa', 10, ""), fg="white")
        self.score_label.grid(column=2, row=0, padx=20, pady=20)
        self.canvas_text = ''

        self.my_canvas = Canvas(width=300, height=250, bg='white')
        self.my_canvas.grid(column=1, columnspan=2, row=1)
        self.my_canvas.create_image(150, 125)
        self.canvas_text = self.my_canvas.create_text(150,
                                                      125,
                                                      width=280,
                                                      text='Hello',
                                                      font=('kefa', 24, ""))

        self.false_image = PhotoImage(file="images/false.png")
        self.true_image = PhotoImage(file="images/true.png")

        self.red_button = Button(width=100, image=self.false_image, command=self.false_answer)
        self.red_button.grid(column=1, row=2, padx=20, pady=20)
        self.green_button = Button(width=100, image=self.true_image, command=self.true_answer)
        self.green_button.grid(column=2, row=2, padx=20, pady=20)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_got_question():
            q_text = self.quiz.draw_question()
            self.my_canvas.itemconfig(self.canvas_text, text=q_text, font=('kefa', 14, ""))
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.my_canvas.itemconfig(self.canvas_text, text="END", font=('kefa', 24, ""))
            self.green_button.config(state='disabled')
            self.red_button.config(state='disabled')

    def true_answer(self):
        if self.quiz.check_answer("True"):
            self.score += 1
            self.my_canvas.config(bg='green')
            self.window.after(100, self.feedback)
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.my_canvas.config(bg='red')
            self.window.after(100, self.feedback)
        self.next_question()

    def false_answer(self):
        if self.quiz.check_answer("False"):
            self.score += 1
            self.my_canvas.config(bg='green')
            self.window.after(100, self.feedback)
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.my_canvas.config(bg='red')
            self.window.after(100, self.feedback)
        self.next_question()

    def feedback(self):
        self.my_canvas.config(bg='white')
