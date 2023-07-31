from tkinter import Tk, Label, Button, Entry, END
from tkinter.messagebox import showinfo
import pandas as pd

root = Tk()
root.title('Student Grading system')


def lettered(total):
  if total >= 97:
    return 'A+'
  elif total >= 94:
    return 'A'
  elif total >= 90:
    return 'A-'
  elif total >= 87:
    return 'B+'
  elif total >= 84:
    return 'B'
  elif total >= 80:
    return 'B-'
  elif total >= 77:
    return 'C+'
  elif total >= 74:
    return 'C'
  elif total >= 70:
    return 'C-'
  else:
    return 'F'

def clicked():
    try:
        test_s = float(entryt.get())
        quiz_s = float(entryq.get())
        hw_s = float(entryh.get())
        final_s = float(entryf.get())
        extra_s = float(entrye.get())
        test_w = float(entrytW.get())
        quiz_w = float(entryqW.get())
        hw_w = float(entryhW.get())
        final_w = float(entryfW.get())
        extra_w = float(entryeW.get())

        if any(n < 0 for n in [test_s, quiz_s, hw_s, final_s, extra_s, test_w, quiz_w, hw_w, final_w, extra_w]):
            showinfo("Error", "Please enter positive values for scores and weights.")
            return

        test = test_s * (test_w / 100)
        quiz = quiz_s * (quiz_w / 100)
        hw = hw_s * (hw_w / 100)
        final = final_s * (final_w / 100)
        extra = extra_s * (extra_w / 100)

        total = test + quiz + hw + final + extra
        total = round(total, 2)
        gpa = round((total / 100) * 4, 2)
        letter = lettered(total)

        showinfo(
            message=f'Your Grade Average is: {total}\nYour GPA is: {gpa}\nYour letter grade is: {letter}'
        )

    except ValueError:
        showinfo("Error", "Please enter only numerical values.")

def delete():
  entryt.delete(0, END)
  entryq.delete(0, END)
  entryh.delete(0, END)
  entryf.delete(0, END)
  entrye.delete(0, END)
  entrytW.delete(0, END)
  entryqW.delete(0, END)
  entryhW.delete(0, END)
  entryfW.delete(0, END)
  entryeW.delete(0, END)


def save():
  test_s = entryt.get()
  quiz_s = entryq.get()
  hw_s = entryh.get()
  final_s = entryf.get()
  extra_s = entrye.get()
  test_w = entrytW.get()
  quiz_w = entryqW.get()
  hw_w = entryhW.get()
  final_w = entryfW.get()
  extra_w = entryeW.get()
  test = float(test_s) * (float(test_w) / 100)
  quiz = float(quiz_s) * (float(quiz_w) / 100)
  hw = float(hw_s) * (float(hw_w) / 100)
  final = float(final_s) * (float(final_w) / 100)
  extra = float(extra_s) * (float(extra_w) / 100)

  total = test + quiz + hw + final + extra
  total = round(total, 2)
  gpa = (total / 100) * 4
  letter = lettered(total)
  entries = {
    'scores': [test_s, quiz_s, hw_s, final_s, extra_s],
    'Weight': [test_w, quiz_w, hw_w, final_w, extra_w],
    'Grade Average': [total, '', '', '', ''],
    'GPA': [gpa, '', '', '', ''],
    'Letter Grade': [letter, '', '', '', ''],
  }
  df = pd.DataFrame(entries)
  df.to_csv('eTranscript.csv', index=False)
  showinfo(message=f'Check Your Folder for Transcript..')


labelt = Label(master=root, text='Test Average :')
labelt.grid(row=1, column=0)
labelq = Label(master=root, text='Quiz Average :')
labelq.grid(row=2, column=0)
labelh = Label(master=root, text='Homework Average :')
labelh.grid(row=3, column=0)
labelf = Label(master=root, text='Final Average :')
labelf.grid(row=4, column=0)
labele = Label(master=root, text='Extra Credit(if any) :')
labele.grid(row=5, column=0)
label1 = Label(master=root, text='Scores')
label1.grid(row=0, column=1)
label2 = Label(master=root, text='Weight')
label2.grid(row=0, column=2)
labelSpace = Label(master=root)
labelSpace.grid(row=6)

entryt = Entry(root)
entryt.grid(row=1, column=1)
entryq = Entry(root)
entryq.grid(row=2, column=1)
entryh = Entry(root)
entryh.grid(row=3, column=1)
entryf = Entry(root)
entryf.grid(row=4, column=1)
entrye = Entry(root)
entrye.grid(row=5, column=1)

entrytW = Entry(root)
entrytW.grid(row=1, column=2)
entryqW = Entry(root)
entryqW.grid(row=2, column=2)
entryhW = Entry(root)
entryhW.grid(row=3, column=2)
entryfW = Entry(root)
entryfW.grid(row=4, column=2)
entryeW = Entry(root)
entryeW.grid(row=5, column=2)

button = Button(root, text='Compute Grade AVG', command=clicked)
button.grid(row=7, column=1)

button = Button(root, text='Clear', command=delete)
button.grid(row=7, column=0, sticky='nesw')

button = Button(root, text='Save', command=save)
button.grid(row=7, column=2, sticky='nesw')

root.mainloop()
