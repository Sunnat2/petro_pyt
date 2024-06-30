class Teacher:
    def init(self, id, name, subject):
        self.id = id
        self.name = name
        self.subject = subject

class TeacherService:
    def init(self):
        self.teachers = []

    def create_teacher(self, id, name, subject):
        teacher = Teacher(id, name, subject)
        self.teachers.append(teacher)

    def edit_teacher(self, id, name=None, subject=None):
        for teacher in self.teachers:
            if teacher.id == id:
                if name:
                    teacher.name = name
                if subject:
                    teacher.subject = subject
                return teacher
        return None

    def get_teachers(self):
        return self.teachers

    def get_teacher_by_id(self, id):
        for teacher in self.teachers:
            if teacher.id == id:
                return teacher
        return None

class TeacherView:
    @staticmethod
    def display_teacher(teacher):
        if teacher:
            print(f"ID: {teacher.id}, Name: {teacher.name}, Subject: {teacher.subject}")
        else:
            print("Teacher not found.")

    @staticmethod
    def display_teachers(teachers):
        for teacher in teachers:
            TeacherView.display_teacher(teacher)

    @staticmethod
    def get_teacher_details():
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        subject = input("Enter Subject: ")
        return id, name, subject

    @staticmethod
    def get_teacher_id():
        return input("Enter Teacher ID: ")

class TeacherController:
    def init(self, service, view):
        self.service = service
        self.view = view

    def create_teacher(self):
        id, name, subject = self.view.get_teacher_details()
        self.service.create_teacher(id, name, subject)
        print("Teacher created successfully.")

    def edit_teacher(self):
        id = self.view.get_teacher_id()
        name = input("Enter new name (or leave blank to keep current): ")
        subject = input("Enter new subject (or leave blank to keep current): ")
        teacher = self.service.edit_teacher(id, name, subject)
        if teacher:
            print("Teacher updated successfully.")
        else:
            print("Teacher not found.")

    def display_teachers(self):
        teachers = self.service.get_teachers()
        self.view.display_teachers(teachers)

    def display_teacher(self):
        id = self.view.get_teacher_id()
        teacher = self.service.get_teacher_by_id(id)
        self.view.display_teacher(teacher)

if name == "main":
    service = TeacherService()
    view = TeacherView()
    controller = TeacherController(service, view)

    while True:
        print("\n1. Create Teacher\n2. Edit Teacher\n3. Display Teachers\n4. Display Teacher by ID\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            controller.create_teacher()
        elif choice == '2':
            controller.edit_teacher()
        elif choice == '3':
            controller.display_teachers()
        elif choice == '4':
            controller.display_teacher()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")