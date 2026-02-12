

# ==========================================
# To-Do List Manager
# Developed by Ahmed
# ==========================================

import json

FILE_NAME = "tasks.json"


# ---------------- File Handling ----------------

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ---------------- Core Functions ----------------

def add_task(tasks):
    title = input("ادخل اسم المهمة: ").strip()
    if title == "":
        print("❌ لا يمكن إضافة مهمة فارغة")
        return

    task = {"title": title, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ تم إضافة المهمة")


def view_tasks(tasks):
    if not tasks:
        print("📭 لا توجد مهام")
        return

    print("\n===== قائمة المهام =====")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. {task['title']} [{status}]")


def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("اختر رقم المهمة لإكمالها: "))
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("✅ تم تحديث المهمة")
    except (ValueError, IndexError):
        print("❌ اختيار غير صحيح")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("اختر رقم المهمة للحذف: "))
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑 تم حذف المهمة: {removed['title']}")
    except (ValueError, IndexError):
        print("❌ اختيار غير صحيح")


# ---------------- Menu ----------------

def menu():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1️⃣ إضافة مهمة")
        print("2️⃣ عرض المهام")
        print("3️⃣ إكمال مهمة")
        print("4️⃣ حذف مهمة")
        print("5️⃣ خروج")

        choice = input("اختر رقم: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 تم إغلاق البرنامج")
            break
        else:
            print("❌ اختيار غير صحيح")


# ---------------- Start ----------------

if __name__ == "__main__":
    menu()
