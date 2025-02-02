from tkinter import *
score = 0

def results():      #Use this after question 10 please
    if score < 10:
        lbl.configure(text = "You are an introvert! You prefer to be alone or with a small group of friends.", wraplength = 200, justify = "center")
    elif score < 20:
        lbl.configure(text = "You are an ambivert! You enjoy socializing and being alone in equal measure.", wraplength = 200, justify = "center")
    else:
        lbl.configure(text = "You are an extrovert! You thrive in social situations and love being the center of attention.", wraplength = 200, justify = "center")
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    go.destroy()

window = Tk()
window.title("Test your Personality!")
window.geometry('400x400')
window.configure(bg = 'light blue')

def question10():
    lbl.configure(text = "10. How do you feel about initiating conversations?", wraplength = 200, justify = "center")
    a.configure(text = "a) I rarely start conversations and prefer to listen.", command = lambda: [afori(), results()])
    b.configure(text = "b) b) I’ll initiate a conversation if I have something specific to say.", command = lambda: [bfori(), results()])
    c.configure(text = "c) I’ll start conversations if the situation calls for it, and I don’t mind small talk.", command = lambda: [cfore(), results()])
    d.configure(text = "d) I love meeting new people and starting conversations wherever I go.", command = lambda: [dfore(), results()])

def question9():
    lbl.configure(text = "9. When working on a project, how do you prefer to do it?", wraplength = 200, justify = "center")
    a.configure(text = "a) I prefer working alone, in a quiet environment.", command = lambda: [afori(), question10()])
    b.configure(text = "b) I like some quiet, but I don’t mind occasional collaboration.", command = lambda: [bfori(), question10()])
    c.configure(text = "c) I like brainstorming and collaborating with others frequently.", command = lambda: [cfore(), question10()])
    d.configure(text = "d) I thrive when I can bounce ideas off others and work in a team.", command = lambda: [dfore(), question10()])

def question8():
    lbl.configure(text = "8. How do you feel when someone invites you to an event or party?", wraplength = 200, justify = "center")
    a.configure(text = "a) I feel a little anxious and would prefer to stay home.", command = lambda: [afori(), question9()])
    b.configure(text = "b) I’ll go if I know a few people, but I may leave early.", command = lambda: [bfori(), question9()])
    c.configure(text = "c) I’m excited to go, but I still might take a break during the event.", command = lambda: [cfore(), question9()])
    d.configure(text = "d) I look forward to it and can’t wait to socialize!", command = lambda: [dfore(), question9()])

def question7():
    lbl.configure(text = "7. How do you feel about long periods of solitude?", wraplength = 200, justify = "center")
    a.configure(text = "a) I enjoy and need it to feel balanced.", command = lambda: [afori(), question8()])
    b.configure(text = "b) I’m okay with solitude for a while, but I like some social interaction.", command = lambda: [bfori(), question8()])
    c.configure(text = "c) I don’t mind solitude, but I prefer to spend time with others when possible.", command = lambda: [cfore(), question8()])
    d.configure(text = "d) I find solitude draining and prefer being around people.", command = lambda: [dfore(), question8()])

def question6():
    lbl.configure(text = "6. When you’re feeling stressed or overwhelmed, what helps you most?", wraplength = 200, justify = "center")
    a.configure(text = "a) Spending time alone to clear my head.", command = lambda: [afori(), question7()])
    b.configure(text = "b) Talking it through with a close friend or family member.", command = lambda: [bfori(), question7()])
    c.configure(text = "c) Getting out of the house and engaging with others.", command = lambda: [cfore(), question7()])
    d.configure(text = "d) Going out and being in a lively environment to forget about it.", command = lambda: [dfore(), question7()])

def question5():
    lbl.configure(text = "5. How do you approach new experiences or activities?", wraplength = 200, justify = "center")
    a.configure(text = "a) I prefer to try things on my own, at my own pace.", command = lambda: [afori(), question6()])
    b.configure(text = "b) I’ll go if I have a close companion with me.", command = lambda: [bfori(), question6()])
    c.configure(text = "c) I’m open to new activities, as long as there are others to share it with.", command = lambda: [cfore(), question6()])
    d.configure(text = "d) I dive right into new experiences and love the excitement of trying new things with others.", command = lambda: [dfore(), question6()])

def question4():
    lbl.configure(text = "4. How do you in a converstion with a stranger?", wraplength = 200, justify = "center")
    a.configure(text = "a) I prefer to listen and let others do most of talking.", command = lambda: [afori(), question5()])
    b.configure(text = "b) I’ll speak if necessary but don’t mind the silence.", command = lambda: [bfori(), question5()])
    c.configure(text = "c) I can easily make small talk and enjoy chatting.", command = lambda: [cfore(), question5()])
    d.configure(text = "d) I love meeting new people and talking to anyone I can.", command = lambda: [dfore(), question5()])

def question3():
    lbl.configure(text = "3. When making plans for the weekend, what's your first instinct?", wraplength = 200, justify = "center")
    a.configure(text = "a) Spend the weekend at home doing something solitary or calm.", command = lambda: [afori(), question4()])
    b.configure(text = "b) Do something small with a couple of close friends.", command = lambda: [bfori(), question4()])
    c.configure(text = "c) Go out to a bar, concert or large event with lots of people.", command = lambda: [cfore(), question4()])
    d.configure(text = "d) Plan something with a big group or go somewhere new and lively.", command = lambda: [dfore(), question4()])

def question2():
    lbl.configure(text = "2. How do you recharge after a busy day?", wraplength = 200, justify = "center")
    a.configure(text = "a) I need alone time to relax and unwind.", command = lambda: [afori(), question3()])
    b.configure(text = "b) I like being around a close friend or family, but still need quiet.", command = lambda: [bfori(), question3()])
    c.configure(text = "c) I enjoy socializing with others to feel recharged.", command = lambda: [cfore(), question3()])
    d.configure(text = "d) I feel energized after being out with a group of friends.", command = lambda: [dfore(), question3()])

def question1():
    lbl.configure(text = "1. How do you feel about large social gatherings?", wraplength = 200, justify = "center")
    go.destroy()
    a.grid(row = 2, column=2, pady=5, padx=20, sticky=W)
    b.grid(row = 3, column=2, pady=5, padx=20, sticky=W)
    c.grid(row = 4, column=2, pady=5, padx=20, sticky=W)
    d.grid(row = 5, column=2, pady=5, padx=20, sticky=W)

def afori():        #i stands for introvert
    global score
    score += 1

def bfori():
    global score
    score += 2

def cfore():        #e stands for extrovert
    global score
    score += 3

def dfore():
    global score
    score += 4

lbl = Label(window, text = "Hello! Wanna test if you're an introvert or extrovert? You will be asked 10 questions, no right or wrong.", wraplength = 200, justify = "center")
lbl.grid(row = 1, column=2, pady=20, padx=20)
go = Button(window, text = "Go!", command=question1)
go.grid(row = 2, column=2, pady=10)

#answer buttons
a = Button(window, text = "a) I prefer to avoid them or stay for a short time.", command = lambda: [afori(), question2()])
b = Button(window, text = "b) I can enjoy them for a while, but need breaks.", command = lambda: [bfori])
c = Button(window, text = "c) I enjoy being around a lot of people for the most part.", command = lambda: [cfore])
d = Button(window, text = "d) I thrive in large crowds and love being the center of attention.", command = lambda: [dfore])

window.mainloop()
#props to GitHub copilot for helping me with the code! And also ChatGPT for the questions!
#If you see this, please don't judge me for my code, I'm still learning. Also, try Copilot, it's really helpful!
#Have a great day!