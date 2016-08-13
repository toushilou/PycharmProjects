__author__ = 'sweety'
class DoctorInfo:
    def __init__(self, docmName, docmId, docmTitle, deptId, deptName, areaId):
        self.docmName = docmName
        self.docmId = docmId
        self.docmTitle = docmTitle
        self.deptId = deptId
        self.deptName = deptName
        self.areaId = areaId



class UserInfo:
    def __init__(self, name, id, password, telephone, docName, date, workType):
        self.telephone = telephone
        self.name = name
        self.id = id
        self.workType = workType
        self.password = password
        self.date = date
        self.docName = docName

