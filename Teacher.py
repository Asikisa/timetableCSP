class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def __repr__(self):
        return f'{self.name}'