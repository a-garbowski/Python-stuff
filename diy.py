class Employee():
    """Basic information about an employee."""
    def __init__(self, name, surname, yearly_salary):
        self.name = name
        self.surname = surname
        self.yearly_salary = yearly_salary

    """The method responsible for incrementing the 'yearly_salary' attribute by either a given 
    or the default amount."""
    def give_raise(self, s_raise=5000):
        self.yearly_salary += s_raise

