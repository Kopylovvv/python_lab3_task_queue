from src.task import Task
from src.exceptions import InvalidTaskStateError

# 1. Создание задачи
print("1. СОЗДАНИЕ ЗАДАЧИ")
task = Task(
    id="demo_001",
    payload={"user": "admin",
             "action": "test",
             "description": "Моя первая задача",
             "priority": "высокий", }
)
print(task)

print()

# 2. Свойства
print("2. СВОЙСТВА ЗАДАЧИ")
print(task.get_info())

print()

# 3. Редактирование
print("3. РЕДАКТИРОВАНИЕ")
task.edit(description="Обновленное описание", priority="обычный")
print(f"Новое описание: {task.description}")
print(f"Новый приоритет: {task.priority}")

print()

# 4. Запуск
print("4. ЗАПУСК")
task.start()
print(f"Статус после запуска: {task.status}")

print()

# 5. Попытка редактировать (должно быть запрещено)
print("5. ПОПЫТКА РЕДАКТИРОВАНИЯ ПОСЛЕ ЗАПУСКА")
try:
    task.edit(description="Попытка изменить")
except InvalidTaskStateError as e:
    print(f"Ошибка: {e}")

print()

# 6. Завершаем
print("6. ЗАВЕРШЕНИЕ")
task.complete()
print(f"Статус после завершения: {task.status}")
print(f"Завершена: {task.is_finished}")
print(f"Активна: {task.is_active}")
