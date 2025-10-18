from pathlib import Path


# class of todolistapp
class ToDoListApp:
    def __init__(self, file_name, max_file_length: int):
        # Go two levels up from main.py → project root
        self.tasks_file = (
            Path(__file__).resolve().parents[2] / "docs" / "Tasks_file.txt"
        )

        # Ensure file and directory exist
        self.tasks_file.parent.mkdir(parents=True, exist_ok=True)
        self.tasks_file.touch(exist_ok=True)

        self.max_file_size = 10

        with open(self.tasks_file, "r") as f:
            self.tasks_list = []
            for line in f.readlines():
                self.tasks_list.append(line.strip())

        self.menu = """
        \rToDoList App
            1. View Tasks
            2. Add Tasks
            3. Remove Tasks
            4. Edit Tasks\n
        """
        self.number_of_options = 4

        self.max = max_file_length
        self.file_name = file_name

    def display_menu(self):
        menu_range = self.number_of_options
        print(self.menu)
        while True:
            prompt = "What do you want to do? 'Q' to Quit\n: "
            user_input = input(prompt).strip().upper()

            if user_input != "Q" and not user_input.isdigit():
                print(
                    f"{user_input} is invalid. Please give a valid option or 'Q' to quit"
                )
                continue

            if user_input == "Q":
                print("Closing Todo List App, goodbye!...")
                return

            user_input = int(user_input)

            if user_input not in range(menu_range + 1):
                print(
                    f"{user_input} is invalid. Please choose a valid option (1 ~ {menu_range}) or 'Q' to quit"
                )
                continue

            if user_input == 1:
                self.view_tasks()
                print(self.menu)

            elif user_input == 2:
                self.add_tasks()
                print(self.menu)

            elif user_input == 3:
                self.remove_tasks()
                print(self.menu)

            elif user_input == 4:
                self.edit_tasks()

    # add indexes // added
    # add time feature
    def view_tasks(self):
        if len(self.tasks_list) == 0:
            print("You have no tasks.")
            return

        with open(self.tasks_file, "r") as f:
            print("Viewing tasks list...\n")

            view = f.readlines()
            for n, i in enumerate(view, start=1):
                print(f"{n}. {i.strip()}\n")

            print("\nEnd of task list returning to menu...\n")

    def add_tasks(self):
        if len(self.tasks_list) > self.max_file_size:
            print("Tasks file is full.")
            return

        prompt = "Provide a task you would like to add ('Q' to quit)\n: "

        while True:
            user_input = input(prompt).strip()

            if user_input == "Q" or user_input == "q":
                print("Returning to menu...")
                return

            if user_input in self.tasks_list:
                print(f"Task: '{user_input}' already exists.")
                continue

            with open(self.tasks_file, "a") as f:
                f.write(user_input + "\n")
                self.tasks_list.append(user_input)
                prompt = "Add another? ('Q' to quit)\n: "
                print(f"'{user_input}' has been added to task list")
                continue

    # method to remove tasks from list/file // added
    # employ use of indexes // added
    # option to remove all tasks at once // added
    # add feature that saves the current edited task list to file // added
    # add time feature
    def remove_tasks(self):
        list_length = len(self.tasks_list)

        if list_length == 0:
            print("Cannot remove task as there are no tasks.")
            return

        prompt = "Give the index of the task you would like to remove ('0' to remove all tasks, 'Q' to quit)\n: "

        while True:
            user_input = input(prompt).strip()

            if user_input == "Q" or user_input == "q":
                print("Returning to menu...")
                return

            if (user_input != "Q" or user_input != "q") and not user_input.isdigit():
                print(
                    f"{user_input} is invalid. Please give a valid index ('0' to remove all tasks, 'Q' to quit)"
                )
                continue

            user_input = int(user_input)

            if user_input == 0:
                self.tasks_list.clear()
                print("Clearing all tasks...\n")
                print("All tasks have been cleared. Returning to menu...")
                return

            if user_input - 1 not in range(list_length):
                print(
                    f"{user_input} is invalid. Please give a valid index 1 ~ {list_length} ('0' to remove all tasks, 'Q' to quit)"
                )
                continue

            else:
                print(
                    f"{user_input}. {self.tasks_list[user_input - 1]} has been removed"
                )

                self.tasks_list.pop(user_input - 1)

                prompt = "Remove more? ('0' to remove all tasks, 'Q' to quit)\n: "

                with open(self.tasks_file, "w") as f:
                    for i in self.tasks_list:
                        f.write(f"{i}\n")
                continue

    # method to update tasks in file
    # employ use of indexes
    def edit_tasks(self):
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


# main method to run program
# display index, tasks .. in tasks list
def main():
    file_name = "docs/Tasks.txt"
    app = ToDoListApp(file_name, 10)

    app.display_menu()


if __name__ == "__main__":
    main()
