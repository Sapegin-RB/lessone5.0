# Создаём класс Task для управления задачами
class Task:
    # Инициализация задачи с описанием, сроком выполнения и статусом
    def __init__(self, description: str, deadline: str):
        # Описание задачи
        self.description = description
        # Срок выполнения задачи
        self.deadline = deadline
        # По умолчанию задача считается не выполненной
        self.completed = False

    # Метод для отметки задачи как выполненной
    def mark_completed(self):
        self.completed = True

    # Метод для вывода информации о задаче
    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"


# Создаём класс TaskManager для управления списком задач
class TaskManager:
    # Инициализация списка задач
    def __init__(self):
        # Пустой список для хранения задач
        self.tasks = []

    # Метод для добавления новой задачи
    def add_task(self, description: str, deadline: str):
        # Создаём новую задачу и добавляем её в список
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    # Метод для отметки задачи как выполненной
    def complete_task(self, task_index: int):
        # Проверяем, что индекс задачи корректен
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Неверный индекс задачи.")

    # Метод для вывода списка всех невыполненных задач
    def show_pending_tasks(self):
        # Выводим только невыполненные задачи
        pending_tasks = [task for task in self.tasks if not task.completed]
        if pending_tasks:
            for task in pending_tasks:
                print(task)
        else:
            print("Все задачи выполнены!")


# Пример использования TaskManager в консоли:

# Создаем объект менеджера задач
task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task("Написать отчёт", "2024-09-20")
task_manager.add_task("Позвонить клиенту", "2024-09-18")
task_manager.add_task("Сходить в магазин", "2024-09-17")

# Выводим список текущих (не выполненных) задач
task_manager.show_pending_tasks()

# Отмечаем первую задачу как выполненную
task_manager.complete_task(0)

# Повторно выводим список текущих задач
task_manager.show_pending_tasks()
