from datetime import datetime
class Employee:
    """A class to represent an Employee"""

    def __init__(self, name="", employee_id=0, department="", job_title="", salary=0.0, age=0, event_assignment="", manager_id=None):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.salary = salary
        self.age = age
        self.event_assignment = event_assignment
        self.manager_id = manager_id

    def update_employee_details(self):
        pass
    def display_employee_details(self):
        # Ensure that the information is returned, not printed
        return (f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, "
                f"Job Title: {self.job_title}, Salary: DHS {self.salary:.2f}, Age: {self.age}, "
                f"Manager ID: {self.manager_id if self.manager_id else 'N/A'}")


    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_employee_id(self):
        return self.employee_id
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_department(self):
        return self.department
    def set_department(self, department):
        self.department = department

    def get_job_title(self):
        return self.job_title
    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_salary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

    def get_event_assignment(self):
        return self.event_assignment
    def set_event_assignment(self, event_assignment):
        self.event_assignment = event_assignment

    def get_manager_id(self):
        return self.manager_id
    def set_manager_id(self, manager_id):
        self.manager_id = manager_id

class Manager(Employee):
    """A class to represent a Manager"""

    def __init__(self, name="", employee_id=0, department="", job_title="", salary=0.0, age=0, manager_type="", employees_managed=None):
        super().__init__(name, employee_id, department, job_title, salary, age)
        self.manager_type = manager_type
        self.employees_managed = []

    def GetEmployees_managed(self):
        pass

    def get_manager_type(self):
        return self.name
    def set_manager_type(self, manager_type):
        self.manager_type = manager_type

    def get_employees_managed(self):
        return self.employees_managed
    def set_employees_managed(self, employees_managed):
        self.employees_managed = employees_managed


class Salesperson(Employee):
    """A class to represent a Salesperson"""

    def __init__(self, name="", employee_id=0, department="", job_title="", salary=0.0, age=0, manager_id=""):
        super().__init__(name, employee_id, department, job_title, salary, age)
        self.manager_id = manager_id


class Event:
    """A class to represent an Event"""

    def __init__(self, event_id=0, event_name="", type="", theme="", date=datetime, time=datetime, duration=0, venue="", client_id="", guests=[],
                 catering_company=None, cleaning_company=None, decorations_company=None, entertainment_company=None, furniture_company=None):
        self.event_id = event_id
        self.event_name = event_name
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue
        self.client_id = client_id
        self.guests = guests
        self.suppliers = []
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_company = furniture_company

    def calculate_cost(self):
        pass

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def display_event_details(self):
        print(f"Event ID: {self.event_id}, Name: {self.event_name}")
        print(f"Venue: {self.venue}, Date: {self.date}")
        print("Suppliers and Services:")
        for supplier in self.suppliers:
            print(f"{supplier.supplier_name} provides: {supplier.display_services()}")

    def get_event_id(self):
        return self.event_id
    def set_event_id(self, event_id):
        self.event_id = event_id

    def get_type(self):
        return self.type
    def set_type(self, type):
        self.type = type

    def get_theme(self):
        return self.theme
    def set_theme(self, theme):
        self.theme = theme

    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date

    def get_time(self):
        return self.time
    def set_time(self, time):
        self.time = time

    def get_duration(self):
        return self.duration
    def set_duration(self, duration):
        self.duration = duration

    def get_venue(self):
        return self.venue
    def set_venue(self, venue):
        self.venue = venue

    def get_client_id(self):
        return self.client_id
    def set_client_id(self, client_id):
        self.client_id = client_id

    def get_guests(self):
        return self.guests
    def set_guests(self, guests):
        self.guests = guests

    def get_catering_company(self):
        return self.catering_company
    def set_catering_company(self, catering_company):
        self.catering_company = catering_company

    def get_cleaning_company(self):
        return self.cleaning_company
    def set_cleaning_company(self, cleaning_company):
        self.cleaning_company = cleaning_company

    def get_decorations_company(self):
        return self.decorations_company
    def set_decorations_company(self, decorations_company):
        self.decorations_company = decorations_company

    def get_entertainment_company(self):
        return self.entertainment_company
    def set_entertainment_company(self, entertainment_company):
        self.entertainment_company = entertainment_company

    def get_furniture_company(self):
        return self.furniture_company
    def set_furniture_company(self, furniture_company):
        self.furniture_company = furniture_company


class Client:
    def __init__(self, client_id=0, client_name="", client_address="", client_contact_details="", client_budget=0.0):
        self.client_id = client_id
        self.client_name = client_name
        self.client_address = client_address
        self.client_contact_details = client_contact_details
        self.client_budget = client_budget

    def update_budget(self, new_budget):
        pass

    def display_client_details(self):
        return (f"Client ID: {self.client_id}, Name: {self.client_name}, Address: {self.client_address}, "
                f"Contact Details: {self.client_contact_details}, Budget: DHS {self.client_budget:.2f}")

    def get_client_id(self):
        return self.client_id
    def set_client_id(self, client_id):
        self.client_id = client_id

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address

    def get_contact_details(self):
        return self.contact_details
    def set_contact_details(self, contact_details):
        self.contact_details = contact_details

    def get_budget(self):
        return self.budget
    def set_budget(self, budget):
        self.budget = budget


class Guest:
    def __init__(self, guest_id=0, guest_name="", guest_address="", guest_contact_details=""):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.guest_address = guest_address
        self.guest_contact_details = guest_contact_details

    def __str__(self):
        return f"Guest ID: {self.guest_id}, Name: {self.guest_name}, Address:{self.guest_address}, Contact Details: {self.guest_contact_details}"

    def get_guest_id(self):
        return self.guest_id
    def set_guest_id(self, guest_id):
        self.guest_id = guest_id

    def get_guest_name(self):
        return self.guest_name
    def set_guest_name(self, guest_name):
        self.guest_name = guest_name

    def get_guest_address(self):
        return self.guest_address
    def set_guest_address(self, guest_address):
        self.guest_address = guest_address

    def get_guest_contact_details(self):
        return self.guest_contact_details
    def set_guest_contact_details(self, guest_contact_details):
        self.guest_contact_details = guest_contact_details

class Venue:
    def __init__(self, venue_id=0, venue_name="", venue_address="", venue_contact="", min_guests=0, max_guests=0):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.venue_address = venue_address
        self.venue_contact = venue_contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    def availability_check(self):
        pass


class Supplier:
    def __init__(self, supplier_id=0, supplier_name="", supplier_address="", supplier_contact_details=""):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.supplier_address = supplier_address
        self.supplier_contact_details = supplier_contact_details
        self.services = []

    def display_services(self):
        if not self.services:
            return f"No services listed for {self.supplier_name}."
        service_list = ', '.join(self.services)
        return f"Services provided by {self.supplier_name}: {service_list}"

    def add_service(self, service_description):
        self.services.append(service_description)

    def get_supplier_id(self):
        return self.supplier_id
    def set_supplier_id(self, supplier_id):
        self.supplier_id = supplier_id

    def get_supplier_name(self):
        return self.supplier_name
    def set_supplier_name(self, supplier_name):
        self.supplier_name = supplier_name

    def get_supplier_address(self):
        return self.supplier_address
    def set_supplier_address(self, supplier_address):
        self.supplier_address = supplier_address

    def get_supplier_contact_details(self):
        return self.supplier_contact_details
    def set_supplier_contact_details(self, supplier_contact_details):
        self.supplier_contact_details = supplier_contact_details

