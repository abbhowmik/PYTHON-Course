# PascleCase
#     Employeename --> PascalCase

#     camelCase
#     isNumerec, isFloat-->camelCase
# #

class RailwayForm:
    formType = 'RailwayForm'

    def allData(self):
        print(f'Name is {self.name}')
        print(f'Train is {self.train}')


harrysApplication = RailwayForm()
harrysApplication.name = "Ashis"
harrysApplication.train = 'Rajdhani Express'
harrysApplication.allData()


# class Exam:
#     ExamType = 'MCQ'

#     def allData(self):
#         print(
#             f"Student name is {self.name}.\n{self.name}'s marks is {self.marks} out of 100")


# ashisApplication = Exam()
# ashisApplication.name = 'Ashis'
# ashisApplication.marks = 99
# ashisApplication.allData()
