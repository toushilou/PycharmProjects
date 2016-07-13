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
    def __init__(self, id, name, password, date, start, end, docName, hp_code):
        self.id = id
        self.name = name
        self.password = password
        self.date = date
        self.start = start
        self.end = end
        self.docName = docName
        self.hp_code = hp_code

