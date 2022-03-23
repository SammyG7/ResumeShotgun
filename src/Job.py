class Job:

    id = ""
    title = ""
    company = ""
    link = ""

    def __init__(self):
        self.title = ""
        self.company = ""
        self.link = ""

    def setId(self, newId):
        self.id = newId

    def setTitle(self, newTitle):
        self.title = newTitle

    def setCompany(self, newCompany):
        self.company = newCompany

    def setLink(self, newLink):
        self.link = newLink