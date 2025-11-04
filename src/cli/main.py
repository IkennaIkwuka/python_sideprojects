from pathlib import Path


class ToDoListApp:
    def __init__(self, menu: str, menu_length: int):
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

        self.menu = menu
        self.menu_length = menu_length

    def display_menu(self):
        menu_range = self.menu_length
        print(self.menu)
        while True:
            prompt = "What do you want to do? ('Q' to Quit)...\n: "
            user_input = input(prompt).strip().upper()

            if user_input != "Q" and not user_input.isdigit():
                print(
                    f"'{user_input}' is invalid. Please give a valid option or 'Q' to Quit\n"
                )
                continue

            if user_input == "Q":
                print("Closing Todo List App, goodbye!...")
                return

            index = int(user_input)

            if index not in range(menu_range + 1):
                print(
                    f"'{index}' is invalid. Please choose a valid option (1 ~ {menu_range}) ('Q' to quit)...\n"
                )
                continue

            if index == 1:
                self.view_tasks()
                print(self.menu)

            elif index == 2:
                self.add_tasks()
                print(self.menu)

            elif index == 3:
                self.remove_tasks()
                print(self.menu)

            elif index == 4:
                self.edit_tasks()
                print(self.menu)

    def view_tasks(self):
        if len(self.tasks_list) == 0:
            print("You have no tasks.\n")
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
                print("Closing 'Add Tasks' returning to menu...\n")
                return

            if user_input in self.tasks_list:
                print(f"Task: '{user_input}' already exists.\n")
                continue

            with open(self.tasks_file, "a") as f:
                f.write(user_input + "\n")
                self.tasks_list.append(user_input)
                prompt = "Add another? ('Q' to quit)\n: "
                print(f"'{user_input}' has been added to task list\n")

    def remove_tasks(self):
        list_length = len(self.tasks_list)

        if list_length == 0:
            print("Cannot remove task as there are no tasks.\n")
            return

        prompt = "Give the index of the task you would like to remove ('0' to remove all tasks, 'Q' to quit)\n: "

        while True:
            user_input = input(prompt).strip()

            if user_input == "Q" or user_input == "q":
                print("Closing 'Remove Tasks' returning to menu...\n")
                return

            if (user_input != "Q" or user_input != "q") and not user_input.isdigit():
                print(
                    f"'{user_input}' is invalid. Please give a valid index ('0' to remove all tasks, 'Q' to quit)\n"
                )
                continue

            index = int(user_input)

            if index == 0:
                self.tasks_list.clear()
                print("Clearing all tasks...\n")
                print("All tasks have been cleared. Returning to menu...\n")
                return

            if index - 1 not in range(list_length):
                print(
                    f"{index} is invalid. Please give a valid index 1 ~ {list_length} ('0' to remove all tasks, 'Q' to quit)\n"
                )
                continue

            print(f"Task: '{index}. {self.tasks_list[index - 1]}' has been removed\n")

            self.tasks_list.pop(index - 1)

            prompt = "Remove more? ('0' to remove all tasks, 'Q' to quit)\n: "

            with open(self.tasks_file, "w") as f:
                for i in self.tasks_list:
                    f.write(f"{i}\n")

    def edit_tasks(self):
        list_length = len(self.tasks_list)

        if list_length == 0:
            print("There are no tasks to edit.\n")
            return

        prompt = (
            "Provide the index of the task you would like to edit ('Q' to quit)\n: "
        )

        while True:
            user_input = input(prompt).strip()

            if user_input == "Q" or user_input == "q":
                print("Closing 'Edit Tasks' returning to menu...\n")
                return

            if (user_input != "Q" or user_input != "q") and not user_input.isdigit():
                print(
                    f"'{user_input}' is invalid. Please give a valid input ('Q' to quit)\n"
                )
                continue

            index = int(user_input)

            if index - 1 not in range(list_length):
                print(
                    f"'{index}' is invalid. Please give a valid index 1 ~ {list_length} ('Q' to quit)\n"
                )
                continue

            updated_task = input(
                f"You are now editing Task: '{index}. {self.tasks_list[index - 1]}' to ...\n: "
            )
            print(
                f"Task: '{index}. {self.tasks_list[index - 1]}' has been updated to '{updated_task}'\n"
            )

            self.tasks_list.pop(index - 1)

            self.tasks_list.insert(index - 1, updated_task)

            prompt = "Edit another task? ('Q' to Quit)...\n: "

            with open(self.tasks_file, "w") as f:
                for i in self.tasks_list:
                    f.write(f"{i}\n")


# main method to run program
def main():
    menu = """
        \rToDoList App
        1. View Tasks
        2. Add Tasks
        3. Remove Tasks
        4. Edit Tasks\n"""

    menu_length = 4

    app = ToDoListApp(menu=menu, menu_length=menu_length)
    app.display_menu()


if __name__ == "__main__":
    main()
