def display_menu():
    """显示菜单"""
    print("\n" + "="*40)
    print("学生成绩管理系统")
    print("="*40)
    print("1. 添加学生")
    print("2. 显示所有学生")
    print("3. 查询学生")
    print("4. 删除学生")
    print("5. 统计信息")
    print("6. 保存到文件")
    print("7. 从文件加载")
    print("0. 退出系统")
    print("="*40)

def add_student(students): # 添加学生
    name = input("请输入学生的姓名：")
    age = int(input("请输入学生的年龄："))
    score = float(input("请输入学生的成绩："))
    student = {
        "name" : name,
        "age" : age,
        "score" : score
    }
    students.append(student)
    print("{}的信息添加成功！".format(name))

def show_all_students(students): # 显示所有学生
    if len(students) == 0:
        print("没有学生信息！")
        return
    print("所有学生信息如下：")
    print(f"{'序号':<5}, {'姓名':<10}, {'年龄':<5}, {'成绩':<5}")
    print("-"*40)
    for i, student in enumerate(students):
        print(f"{i:<5},{student['name']:<10},{student['age']:<5},{student['score']:<5}")

def query_student(students): # 查询学生
    name = input("请输入要查询的学生姓名：")
    f = 1
    for student in students:
        if student['name'] == name:
            f = 0
            print(f"{name}的信息如下：")
            print(f"姓名：{student['name']:<10}\n 年龄：{student['age']:<5}\n 成绩：{student['score']:<5}")
            break
    if f == 1:
        print(f"没有找到{name}的信息")

def delete_student(students): # 删除学生
    name = input("请输入要删除的学生姓名：")
    f = 1
    for i, student in enumerate(students):
        if student['name'] == name:
            f = 0
            del students[i]
            print(f"{name}的信息已经被删除！")
            break
    if f == 1:
        print(f"'没有{name}的信息")

def count_info(students): # 统计信息
    if len(students) == 0:
        print("没有学生信息！")
        return
    print(f"'学生人数一共有：{len(students)}人'")
    print(f"'平均年龄为：{sum(student['age'] for student in students)/len(students)}")
    print(f"'平均成绩为：{sum(student['score'] for student in students)/len(students)}")

def save_to_file(students, filename = "students.txt"): # 保存到文件
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            """
            f.write("{'序号':<5},{'姓名':<10},{'年龄':<5},{'成绩':<5}\n")
            line = "--"*40 + "\n"
            f.write(line)
            """
            for student in students:
                line = f"{student['name']},{student['age']},{student['score']}\n"
                f.write(line)
        print(f"文件已经成功保存到{filename}中")
    except Exception as e:
        print(f"保存失败: {e}")

def load_from_file(filename = "students.txt"): # 从文件加载
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    name,age,score = line.strip().split(",")
                    student = {
                        "name" : name,
                        "age" : int(age),
                        "score" : float(score)
                    }
                    students.append(student)
        print(f"文件{filename}已经成功加载了{len(students)}条学生信息！")
        return students
    except FileNotFoundError:
        print("文件不存在！")
        return []
    except Exception as e:
        print(f"读取文件失败:{e}")
        return []


def exit_system(): # 退出系统
    print("欢迎下次使用！")

def main():
    print("欢迎进入学生管理系统")
    students = []  # 学生列表
    while True:
        display_menu()
        # print(students)
        choice = int(input("请输入您需要进行的操作："))
        if choice == 1:  # 添加学生
            add_student(students)
        elif choice == 2:  # 显示所有学生
            show_all_students(students)
        elif choice == 3:  # 查询学生
            query_student(students) 
        elif choice == 4:  # 删除学生
            delete_student(students)
        elif choice == 5:  # 统计信息
            count_info(students)
        elif choice == 6:  # 保存到文件
            save_to_file(students)
        elif choice == 7:  # 从文件加载
            students = load_from_file("students.txt")
        elif choice == 0:  # 退出系统
            exit_system()
            break
        else:
            print("输入错误，请重新输入！")


if __name__ == "__main__":
    main()  # 调用main函数