
    
            


class ToDo():
    def __init__(self):
        self.current_id = 1
        self.priority = ""
        self.id_content = {}

    #prioritises a task
    def ToDoPriority(self, task_id):
        if task_id not in self.id_content:
            print("Task not found")
        else: 
            self.priority = self.id_content[task_id]
            print(f"Prioritised Task is: {self.priority}")
    
    
    
    #displays the whole list
    def ToDoView(self):
        if not self.id_content:
            print("Nothing to see")

        else:
            for task_id, content in self.id_content.items():
                print(f"{task_id}: {content}")
                if self.priority != "":
                    print(f"Prioritised Task is {self.priority}")


    #You can add a task into the ToDoList
    def ToDoAdd(self, content):
        task_id = self.current_id
        self.id_content[task_id] = content
        self.current_id += 1
        print(f"{content} has been added") 
    
    
    
    #You can delete a task of the ToDolist
    def ToDoDelete(self, task_id):
        if task_id in self.id_content:
            print(f"ID number:{task_id} has been deleted")
            del self.id_content[task_id]
        else:
            print("Id missing")

    
    #You can edit the ToDoList
    def ToDoEdit(self, task_id):
        
        print(f"The Task write now is {self.id_content[task_id]}")
        content_change = input("What do you want to change the task to: ")
        self.id_content[task_id] = content_change
        print(f"Task ID {task_id} has been changed to {content_change}: ")

    #Makes sure the input matches the appropiate options 
    @staticmethod
    def ModeChecker(mode):
        if mode not in ["view","add","delete","view","edit","priority"]:
            print(f"{mode} is not a valid input")
            
        
    
    #Gets the input for a function then sends it to the function
    def ModeSender(self, mode):
        if mode == "view":
            ToDo.ToDoView()

        elif mode == "add":
            content = input("What do you want to add? ")
            ToDo.ToDoAdd(content)

        elif mode == "delete":
            task_id = int(input("What ID do you want to delete "))
            ToDo.ToDoDelete(task_id)

        elif mode == "edit":
            id = int(input("Give the ID for the task you want to edit "))
            ToDo.ToDoEdit(id)

        elif mode == "quit":
            print("Bye")
            quit()

        elif mode == "priority":
            task_id = int(input("What task id do you want to prioritise? "))
            ToDo.ToDoPriority(task_id)
                    


    

    
def main():
    ToDoList = ToDo()
 
    while True:
        mode = input("Options are:  View, Add, Edit, Priority or Delete (or quit) \n Choose one ").lower()
        
        ToDoList.ModeChecker(mode)
        ToDoList.ModeSender(mode)
    
if __name__ == "__main__":
    main()