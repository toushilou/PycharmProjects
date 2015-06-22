__author__ = 'sweety'
class DoctorInfo:
    def __init__(self, name, id, code, dept, deptName):
        self.name = name
        self.id = id
        self.code = code
        self.dept = dept
        self.deptName = deptName

    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getCode(self):
        return self.code
    def getDept(self):
        return self.dept
    def getDeptName(self):
        return self.deptName



class UserInfo:
    def __init__(self, id, name, password, date, time, docName):
        self.id = id
        self.name = name
        self.password = password
        self.date = date
        self.time = time
        self.docName = docName

