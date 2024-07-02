tasks=[]
def addtask():
    task=input("please enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}.{task}")
def deleteTask():
    listTasks()
    try:
        taskToDelete=input("Enter the # to delete:")
        if taskToDelete>=0 and taskToDelete<len(tasks):
            tasks.pop(taskToDelete)
            print(f"{taskToDelete} has been removed.")
        else:
            print(f"{taskToDelete} has not removed.")
    except:
        print("Invalid input.")
if __name__=="__main__":
    print("welcome to list app:")
    while True:
        print("\n")
        print("please select one of the following option")
        print("___________________________________")
        print("1.add a new task")
        print("2.delete a task")
        print("3.list task")
        print("4.quit")
        choice=input("Enter your choice:")
        if (choice=="1"):
            addtask()
        elif (choice=="2"):
            deleteTask()
        elif (choice=="3"):
            listTasks()
        elif (choice=="4"):
            break
        else:
            print("Invalid input please try again.")