from tkinter  import *
from datetime import datetime

temp = 0
after_id = ''
split_data = []
def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    formated_time = datetime.fromtimestamp(temp).strftime("%M:%S")
    time_label.configure(text=str(formated_time))
    temp += 1

def start_watch():
    '''STARTING'''
    start_button.grid_forget()

    stop_button.grid(row=1, columnspan=2, sticky='ew')
    #split_button.grid(row=2, columnspan=2, sticky='ew')
    tick()
def stop_watch():
    stop_button.grid_forget()
    #split_button.grid_forget()

    continue_button.grid(row=1, column=0, sticky='ew')
    reset_button.grid(row=1, column=1, sticky='ew')
    root.after_cancel(after_id)


# def split_watch():
#     global split_data
#     formated_time = datetime.fromtimestamp(temp).strftime("%M:%S")
#     split_data.append(str(formated_time))
#     i = 0
#     n_row = 3
#     for data in split_data:
#         split_label = Label(root, width=8, font=('Arial', 30), text='')
#         split_label.grid(row=n_row, columnspan=2)
#         split_label.configure(text=data)
#         i += 1
#         n_row += 1
#
#     print(split_data)

def split_watch():
    global split_data
    formated_time = datetime.fromtimestamp(temp).strftime("%M:%S")
    split_data.append(str(formated_time))
    split_label.grid(row=3, columnspan=2)
    split_label.configure(text=formated_time)


    print(split_data)

def continue_watch():
    continue_button.grid_forget()
    reset_button.grid_forget()

    stop_button.grid(row=1, columnspan=2, sticky='ew')
    #split_button.grid(row=2, columnspan=2, sticky='ew')
    tick()


def reset_watch():
    global temp, split_data, split_label
    temp = 0

    time_label.configure(text='00:00')
    continue_button.grid_forget()
    reset_button.grid_forget()
    #split_button.grid_forget()
    #split_label.grid_forget()

    start_button.grid(row=1, columnspan=2, sticky='ew')

root = Tk()
root.title('Cекундомір')


time_label = Label(root, width=8, font=('Arial', 70), text='00:00')
time_label.grid(row=0, columnspan=2)
#split_label= Label(root, width=8, font=('Arial', 30), text='')


start_button = Button(root, bg="green", font=('Arial',30), text="START", command=start_watch)
stop_button = Button(root, bg="red", font=('Arial',30), text="STOP", command=stop_watch)
continue_button = Button(root, bg="green",font=('Arial',30), text="CONTINUE", command=continue_watch)
reset_button = Button(root, bg="blue", font=('Arial',30), text="RESET", command=reset_watch)
#split_button = Button(root, bg="blue", font=('Arial',30), text="SPLIT", command=split_watch)
start_button.grid(row=1, columnspan=2, sticky= 'ew')



root.mainloop()