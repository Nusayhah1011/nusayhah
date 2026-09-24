# task_manager_v1.py
# Version 1: Start with default tasks, add one more, display before and after.
tasks = ["Learn Python", "Build a Task Manager"]
print("=== Task Manager ===")
print("Current tasks:")
print(tasks)
new_task = input("\nEnter a new task: ")
tasks.append(new_task)
print("\nUpdated task list:")
print(tasks)