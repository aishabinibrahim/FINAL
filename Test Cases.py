from Classes import Employee, Manager, Salesperson, Event, Client, Guest, Venue, Supplier
from datetime import datetime

# Test Case 1: Employees
# creating employee manager objects
susan_meyers = Employee(name="Susan Meyers", employee_id=47899, department="Sales", job_title="Manager", salary=37500.0)
joy_rogers = Employee(name="Joy Rogers", employee_id=81774, department="Sales", job_title="Manager", salary=24000.0)

# creating employees salesperson objects
shyam_sundar = Employee(name="Shyam Sundar", employee_id=11234, department="Sales", job_title="Salesperson", salary=20000.0, manager_id = 47899)
mariam_khalid = Employee(name="Mariam Khalid", employee_id=98394, department="Sales", job_title="Salesperson", salary=20000.0, manager_id = 81774)
salma_j_sam = Employee(name="Salma J Sam", employee_id=98637, department="Sales", job_title="Salesperson", salary=20000.0, manager_id = 47899)

# updating employees' details
susan_meyers.set_salary(38000.0)
joy_rogers.set_salary(28000.0)

print("TEST CASE 1:")
print(susan_meyers.display_employee_details())
print(joy_rogers.display_employee_details())
print(shyam_sundar.display_employee_details())
print(mariam_khalid.display_employee_details())
print(salma_j_sam.display_employee_details())


# Test Case 2: Events
from datetime import datetime

# Assuming you've already defined classes for Event, Guest, Supplier, etc., as per previous discussions

# Creating guest instances
guest1 = Guest(guest_id=1, guest_name="Aisha", guest_address="Dubai", guest_contact_details="050-000-1111")
guest2 = Guest(guest_id=2, guest_name="Smith", guest_address="Sharjah", guest_contact_details="050-111-0000")

# Creating supplier instances
catering = Supplier(supplier_id=1, supplier_name="HomeBakery", supplier_address="Dubai", supplier_contact_details="04-2020")
cleaning = Supplier(supplier_id=2, supplier_name="Cleaning and Co", supplier_address="Sharjah", supplier_contact_details="06-0404")

# Creating an event
event = Event(
    event_id="1001",
    type="Party",
    theme="Wedding",
    date=str(datetime.now().date()),
    time=str(datetime.now().time()),
    duration=180,
    venue="Ballroom",
    client_id=101,
    guests=[guest1],
    catering_company=catering,
    cleaning_company=cleaning,
    decorations_company=None,
    entertainment_company=None,
    furniture_company=None
)

# Function to display the details of the event
def display_event_details(event):
    print("Event Details:")
    print(f"ID: {event.event_id}, Type: {event.type}, Theme: {event.theme}")
    print(f"Date: {event.date}, Time: {event.time}, Duration: {event.duration} minutes")
    print(f"Venue: {event.venue}, Client ID: {event.client_id}")
    print("Guest List:")
    for guest in event.guests:
        print(f"{guest.guest_name} from {guest.guest_address}")
    print("Suppliers:")
    if event.catering_company:
        print(f"Catering: {event.catering_company.supplier_name}")
    if event.cleaning_company:
        print(f"Cleaning: {event.cleaning_company.supplier_name}")

# Test adding a new guest
new_guest = Guest(guest_id=3, guest_name="Maitha", guest_address="Nad al Sheba", guest_contact_details="055-555-0505")
event.guests.append(new_guest)

# Test updating venue
event.set_venue("Luxury Event Hall")

# Display event details to check updates
print("\nTEST CASE 2:")
display_event_details(event)

# Test Case 3: Client
client1 = Client(client_id=1181, client_name="EM Corporation", client_address="Dubai, Mirdif", client_contact_details="800-1181", client_budget=50000.0)

# Display initial details
print("\nTEST CASE 3")
print("Initial Client Details:")
print(client1.display_client_details())

# Update client's budget
client1.update_budget(100000.0)

# Display updated details to confirm changes
print("Updated Client Details:")
print(client1.display_client_details())

# Test Case 4: Suppliers
# Creating supplier instances
supplier1 = Supplier(supplier_id=1, supplier_name="Fancy Resturant Catering", supplier_address="Al Khawaneej", supplier_contact_details="04-12321")
supplier2 = Supplier(supplier_id=2, supplier_name="Wedding Decorations", supplier_address="Al Barsha", supplier_contact_details="04-88888")

# Adding services to suppliers
supplier1.add_service("3 meal catering for events")
supplier1.add_service("Custom menu planning")
supplier2.add_service("Wedding and party event decorations")

# Displaying services
print("\nTEST CASE 4")
print(supplier1.display_services())
print(supplier2.display_services())

# Test Case 5: Event Management
# Create suppliers
catering = Supplier(supplier_id=1, supplier_name="By Mara Catering")
catering.add_service("Full Buffet")
catering.add_service("Mara Café Dessert Menu")

decorations = Supplier(supplier_id=2, supplier_name="Wedding Decorations")
decorations.add_service("Floral arrangements")
decorations.add_service("Lighting setup")

entertainment = Supplier(supplier_id=3, supplier_name="Live Entertainment Inc.")
entertainment.add_service("DJ services")
entertainment.add_service("Live singing")

# Create an event
wedding_event = Event(event_id="W004", event_name="Hessa Wedding", venue="Grand Ballroom", date="2024-12-12")

# Add suppliers to the event
print("\nTEST CASE 5")
wedding_event.add_supplier(catering)
wedding_event.add_supplier(decorations)
wedding_event.add_supplier(entertainment)

# Display event details
wedding_event.display_event_details()