class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index.")