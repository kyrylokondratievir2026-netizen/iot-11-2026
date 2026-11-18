class Bug:
    def __init__(self, bug_id, description, severity, deadline, assignee,
                 status="OPEN"):
        self.__bug_id = bug_id
        self.__description = description
        self.__severity = severity
        self.__deadline = deadline
        self.__assignee = assignee
        self.__status = status

    def __del__(self):
        print(f"Баг №{self.__bug_id} видалено з пам'яті")

    def get_bug_id(self):
        return self.__bug_id

    def get_description(self):
        return self.__description

    def get_severity(self):
        return self.__severity

    def get_deadline(self):
        return self.__deadline

    def get_assignee(self):
        return self.__assignee

    def get_status(self):
        return self.__status

    def set_assignee(self, assignee):
        self.__assignee = assignee

    def set_status(self, status):
        self.__status = status

    def show(self):
        print(f"Баг №{self.__bug_id}: {self.__description}")
        print(f"  Важливість: {self.__severity}, дедлайн: {self.__deadline}")
        print(f"  Статус: {self.__status}, розробник: {self.__assignee}")


class Backlog:
    def __init__(self, name):
        self.__name = name
        self.__bugs = []

    def __del__(self):
        print(f"Беклог '{self.__name}' видалено з пам'яті")

    def add_bug(self, bug):
        self.__bugs.append(bug)

    def find_bug(self, bug_id):
        found = None
        for bug in self.__bugs:
            if bug.get_bug_id() == bug_id:
                found = bug
        return found

    def remove_bug(self, bug_id):
        bug = self.find_bug(bug_id)
        if bug is not None:
            self.__bugs.remove(bug)
            print(f"Баг №{bug_id} видалено з беклогу")
        else:
            print(f"Бага з id {bug_id} немає в беклозі")

    def sort_by_severity(self):
        self.__bugs.sort(key=lambda bug: bug.get_severity(), reverse=True)

    def show_all(self):
        print(f"Беклог: {self.__name}")
        for bug in self.__bugs:
            bug.show()

    def show_resolved_by(self, assignee):
        found = False
        for bug in self.__bugs:
            is_owner = bug.get_assignee() == assignee
            is_resolved = bug.get_status() == "RESOLVED"
            if is_owner and is_resolved:
                bug.show()
                found = True
        if not found:
            print(f"У розробника {assignee} немає виправлених багів")


def main():
    backlog = Backlog("Мобільний застосунок")
    bug1 = Bug(1, "Не відкривається екран входу", 5, "2026-11-20", "Олег")
    bug2 = Bug(2, "Неправильний колір кнопки", 1, "2026-12-01", "Ірина",
               "RESOLVED")
    bug3 = Bug(3, "Застосунок вилітає при збереженні", 4, "2026-11-25",
               "Олег", "RESOLVED")
    bug4 = Bug(4, "Повільно вантажиться список", 3, "2026-12-10", "Ірина")
    bug5 = Bug(5, "Помилка в перекладі меню", 2, "2026-12-15", "Олег",
               "RESOLVED")

    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    backlog.add_bug(bug3)
    backlog.add_bug(bug4)
    backlog.add_bug(bug5)

    print("--- Усі баги ---")
    backlog.show_all()

    print("--- Після сортування за важливістю ---")
    backlog.sort_by_severity()
    backlog.show_all()

    print("--- Виправлені баги розробника Олег ---")
    backlog.show_resolved_by("Олег")

    print("--- Змінюємо статус бага №1 ---")
    bug1.set_status("RESOLVED")
    backlog.show_resolved_by("Олег")

    print("--- Видаляємо баг №2 ---")
    backlog.remove_bug(2)
    backlog.remove_bug(10)
    backlog.show_all()


if __name__ == "__main__":
    main()
