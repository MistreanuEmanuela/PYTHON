import copy


class Employee:
    def __init__(self, name, department, salary, experience):
        self._name = name
        self._department = department
        self._salary = salary
        self._experience = experience

    def get_role(self):
        pass

    def get_salary(self):
        return self._salary

    def display_info(self):
        print(f"Name: {self._name}, Department: {self._department}, Salary: {self._salary}, "
              f"Experience: {self._experience}")


class Engineer(Employee):
    def __init__(self, name, salary, experience, tasks):
        super().__init__(name, "engineering", salary, experience)
        self._tasks = tasks
        self._done_tasks = []
        self._in_progress_tasks = []

    def set_tasks(self, task):
        self._tasks.append(task)

    def mark_done_task(self, task):
        if task in self._in_progress_tasks:
            self._done_tasks.append(task)
            self._in_progress_tasks.remove(task)
        else:
            raise Exception("This task wasn't started yet")

    def start_task(self, task):
        if task in self._tasks:
            self._in_progress_tasks.append(task)
        else:
            raise Exception("This task wasn't yours")

    def get_done_tasks(self):
        return copy.deepcopy(self._done_tasks)

    def get_in_progress_tasks(self):
        return copy.deepcopy(self._in_progress_tasks)

    def get_role(self):
        return "Engineer"


class Salesperson(Employee):
    def __init__(self, name, salary, experience, products, profit):
        super().__init__(name, "sales", salary, experience)
        self._products = products
        self._profit = profit

    def sale_product(self, product, price):
        self._products.append(product)
        self._profit += price

    def get_products(self):
        return copy.deepcopy(self._products)

    def get_role(self):
        return "Salesperson"

    def get_profit(self):
        x = self._profit
        return x


class Manager(Employee):
    def __init__(self, name, salary, experience, engineers, tasks, projects, progress_projects):
        super().__init__(name, "management", salary, experience)
        self._tasks = tasks
        self._projects = projects
        self._progress_projects = progress_projects
        self._engineers = engineers

    def mark_done_project(self, project):
        if project in self._progress_projects:
            self._projects.append(project)
        else:
            raise Exception("This project wasn't started yet")

    def mark_done_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
        else:
            raise Exception("This task wasn't yours")

    def assign_tasks(self, n, engineer):
        if engineer in self._engineers:
            engineer.set_tasks(self._tasks[n])
        else:
            raise Exception("You can't assign task to this engineer")

    def get_new_project(self, project, tasks):
        self._tasks.append(tasks)
        self._progress_projects.append(project)

    def get_role(self):
        return "Project Manager"

    def get_projects(self):
        x = copy.deepcopy(self._projects)
        return x

    def get_progress_projects(self):
        x = copy.deepcopy(self._progress_projects)
        return x


engineer1 = Engineer("Engineer", 10000, 7, ["Task1", "Task2"])
salesperson1 = Salesperson("Sale", 6500, 3, ["Product1", "Product2"], 5000)
manager1 = Manager("Manager", 9000, 6, [engineer1], ["Task3", "Task4"], ["Project1"], ["Project2"])

engineer1.start_task("Task1")
engineer1.mark_done_task("Task1")

salesperson1.sale_product("Product3", 5000)

manager1.assign_tasks(1, engineer1)
manager1.get_new_project("Project3", ["Task5", "Task6"])

print("Informații angajați:")
engineer1.display_info()
print(f"Rol: {engineer1.get_role()}")
print(f"Task-uri terminate: {engineer1.get_done_tasks()}")
print(f"Task-uri în progres: {engineer1.get_in_progress_tasks()}\n")

salesperson1.display_info()
print(f"Rol: {salesperson1.get_role()}")
print(f"Produse vândute: {salesperson1.get_products()}")
print(f"Profit: {salesperson1.get_profit()}\n")

manager1.display_info()
print(f"Rol: {manager1.get_role()}")
print(f"Proiecte finalizate: {manager1.get_projects()}")
print(f"Proiecte în progres: {manager1.get_progress_projects()}")
