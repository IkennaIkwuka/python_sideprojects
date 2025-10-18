import os

os.makedirs("docs", exist_ok=True)
# Steps


# class of todolistapp
class ToDoListApp:
    def __init__(self, file_name, max_file_length: int) -> None:
        self.max = max_file_length
        self.file_name = file_name
        self.tasks_list = []
        self.load_tasks()

    # method to read file for tasks
    # append to list or set?
    def load_tasks(self):
        non_duplicates = set(str())
        try:
            with open(self.file_name, "r") as file:
                file_list = file.readlines()
                for item in file_list:
                    non_duplicates.add(item.strip())
        except FileNotFoundError:
            ...
        self.tasks_list.extend(list(non_duplicates))

    # method to save tasks
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            for _ in self.tasks_list:
                file.write(_ + "\n")

    def display_tasks(self):
        if not self.tasks_list:
            print("No tasks available.")
        else:
            print("\nTask List:")
            for idx, task in enumerate(self.tasks_list, 1):
                print(f"Id: {idx} Task: {task}")
            print("")

    # method to add tasks to tasks list
    # add till a certain limit
    # validate for no duplicates (use sets)
    def add_tasks(self):
        if len(self.tasks_list) > self.max:
            print("Task list is full.")
            return

        prompt = "Provide a task you would like to add (q to quit): "
        task = input(prompt).strip()
        if task.lower() == "q":
            return

        if task in self.tasks_list:
            print(f"Task: {task} already exists.")
        else:
            self.tasks_list.append(task)
            self.save_tasks()
            print(f"'{task}' has been created successfully")

    # method to remove tasks from list/file
    # employ use of indexes
    def remove_task(self):
        if not self.tasks_list:
            print("Cannot remove task as there are no tasks.")
            return

        prompt = "Give the 'id' of the task you would like to remove('0' to quit)"
        while True:
            try:
                idx = int(input(prompt).strip()) - 1
                if idx == -1:
                    return

                if idx in range(len(self.tasks_list)):
                    print(
                        f"\n'{self.tasks_list[idx]}' has been removed at index {idx + 1}."
                    )
                    self.tasks_list.pop(idx)
                    self.save_tasks()
                    return
                else:
                    print(f"Id must be between 1 ~ {len(self.tasks_list)} ")
            except ValueError:
                print("Please input a number")

    # method to update tasks in file
    # employ use of indexes
    def update_tasks(self):
        if not self.tasks_list:
            print("Cannot update task as there are no tasks.")
            return

        id_prompt = "Give the 'id' of the task you would like to update('0' to quit): "
        task_prompt = "Provide the updated task(q to quit): "
        while True:
            try:
                idx = int(input(id_prompt).strip()) - 1
                if idx == -1:
                    return

                if idx in range(len(self.tasks_list)):
                    task = input(task_prompt).strip()
                    self.tasks_list.insert(idx, task)
                    print(
                        f"\n'{self.tasks_list[idx]}' has been updated at index {idx + 1}."
                    )
                    self.tasks_list.pop(idx + 1)
                    self.save_tasks()
                    return
                else:
                    print(f"Id must be between 1 ~ {len(self.tasks_list)} ")
            except ValueError:
                print("Please input a number")


# main method to run program
# display index, tasks .. in tasks list
def main():
    print("\nToDoList App")
    print("1. Add Tasks")
    print("2. Remove Tasks")
    print("3. Edit Tasks")
    print("4. Quit")

    file_name = "docs/Tasks.txt" 
    app = ToDoListApp(file_name, 10)

    while True:
        app.display_tasks()

        user_input = input("What do you want to do? (add, remove, update, quit): ")
        print("")
        if user_input == "add":
            app.add_tasks()
        elif user_input == "remove":
            app.remove_task()
        elif user_input == "update":
            app.update_tasks()
        elif user_input == "quit":
            print("Closing program, goodbye!")
            break
        else:
            print(f"'{user_input}' is an invalid input")


if __name__ == "__main__":
    main()
