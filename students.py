class student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.age = age
        self.department = department

    def dispaly_info(self):
        print("\n---- Student Information ----")
        print("Name            :",self.name)
        print("Student_ID      :", self.student_id)
        print("Email           :", self.email)
        print("Age             :", self.age)
        print("Department      :", self.department)

    def calculate_result(self, marks):
        if marks >=33:
            return " Pass "
        else:
            return " Fail"

    def get_student_type(self):
        return " general student "       

class undergraduatestudent(student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    def get_student_type(self):
        return "Undrgradute Student" 

    def dispaly_info(self):
        super().dispaly_info()
        print("semester       :", self.semester)
        print("Type           :", self.get_student_type())   

class graduatestudent(student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"
    
    def dispaly_info(self):
        super().dispaly_info()
        print("research_topic   :", self.research_topic)
        print("Typer            :", self.get_student_type())


studentU = undergraduatestudent (
    "matiur rahman",
    "MA123456",
    "matiur11@hmail.com",
    36,
    "business",
    3
)

studentG = graduatestudent (
   "Suny Rahman",
   "SR654123",
   "sunny221@gmail.com",
   34,
   "webdevelopment",
   "python"
)

studentU.dispaly_info()

print('\n------------------------------------------')

studentG.dispaly_info()