#to do list app
tasks = []
length = 0

def create():
    global length
    task = input('Enter the task: ')
    tasks.append(task)
    length += 1

def display():
    for i in range(length):
        print(f"{i+1}.{tasks[i]}")

def add_new():
    global length
    task = input('Enter the task: ')
    tasks.append(task)
    length += 1

def delete():
    global length
    display()
    tnum = int(input('Enter the task number to be deleted: '))
    if 1 <= tnum <=length:
        tasks.pop(tnum-1)
        length -= 1
        print(f'Task {tnum} has been deleted')
    else:
        print('Invalid task number!')



def todo_list(choice):
    switch_dict ={
        1: create,
        2: display,
        3: add_new
    }
    return switch_dict.get(choice)

print('Welcome to-do list app!')

while True:
    choice = int(input('Choose an option (1-4, 0 to exit): '))
    if choice == 0:
        break
    if choice == 4:
        delete()
    else:
        result = todo_list(choice)
        result()



