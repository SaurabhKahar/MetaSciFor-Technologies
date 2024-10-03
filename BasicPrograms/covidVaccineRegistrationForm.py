import tkinter as tk
from tkinter import messagebox

def submit():
    # Retrieve values from the input fields
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_entry.get("1.0", tk.END).strip()  # Get text from the Text widget
    email = email_entry.get()
    contact = contact_entry.get()
    country = country_entry.get()
    state = state_entry.get()
    country_code = country_code_var.get()
    
    # Check if all required fields are filled
    if not (name and age and gender and address and email and contact and country and state):
        messagebox.showerror("Error", "Please fill out all required fields.")
        return

    # Check which checkboxes are selected
    diseases = []
    if cold_var.get():
        diseases.append("Cold")
    if cough_var.get():
        diseases.append("Cough")
    if fever_var.get():
        diseases.append("Fever")
    if headache_var.get():
        diseases.append("Headache")

    # Print the retrieved data
    print("Form Submitted \n")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender if gender else 'Not selected'}")    
    print(f"Address: {address}")
    print(f"Email Id: {email}")
    print(f"Contact No: {country_code} {contact}")
    print(f"Country: {country}")
    print(f"State: {state}")
    print(f"Diseases: {', '.join(diseases) if diseases else 'None'}")

    # Clear the entries, checkboxes, and radio buttons
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)
    gender_var.set(None)  # Reset the gender radio button
    cold_var.set(False)
    cough_var.set(False)
    fever_var.set(False)
    headache_var.set(False)
    country_code_var.set("+91")  # Reset the country code dropdown to default

root = tk.Tk()
root.title("COVID Vaccine Registration Form")

# Main container frame
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20, expand=True, fill='both')

# Helper function to create label and entry pairs
def create_labeled_entry(frame, label_text, entry_widget, row, column):
    tk.Label(frame, text=label_text).grid(row=row, column=column, padx=10, pady=5, sticky='w')
    entry_widget.grid(row=row, column=column+1, padx=10, pady=5, sticky='w')

# Create and place widgets
name_entry = tk.Entry(main_frame)
age_entry = tk.Entry(main_frame)
address_entry = tk.Text(main_frame, height=4, width=20)
email_entry = tk.Entry(main_frame)
contact_entry = tk.Entry(main_frame)
country_entry = tk.Entry(main_frame)
state_entry = tk.Entry(main_frame)

create_labeled_entry(main_frame, "Name of the Visitor:", name_entry, 0, 0)
create_labeled_entry(main_frame, "Age of the Visitor:", age_entry, 1, 0)
tk.Label(main_frame, text="Address:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
address_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')
create_labeled_entry(main_frame, "Email Id:", email_entry, 3, 0)

# Country Code Dropdown
country_code_var = tk.StringVar()
country_code_var.set(" ")  # Default value
country_codes = ["+91", "+44", "+1", "+971", "+7"]
tk.Label(main_frame, text="Country Code:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
country_code_menu = tk.OptionMenu(main_frame, country_code_var, *country_codes)
country_code_menu.grid(row=4, column=1, padx=5, pady=5, sticky='w')

tk.Label(main_frame, text="Contact No:").grid(row=4, column=2, padx=10, pady=5, sticky='w')
contact_entry.grid(row=4, column=3, padx=5, pady=5, sticky='w')

create_labeled_entry(main_frame, "Country:", country_entry, 5, 0)
create_labeled_entry(main_frame, "State:", state_entry, 6, 0)

# Gender Radio Buttons
gender_var = tk.StringVar()
gender_var.set(None)  # Ensure no gender is selected initially
gender_frame = tk.Frame(main_frame)
gender_frame.grid(row=7, column=1, padx=10, pady=5, sticky='w')
tk.Label(main_frame, text="Gender:").grid(row=7, column=0, padx=10, pady=5, sticky='w')
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side='left', padx=5)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side='left', padx=5)

# Checkboxes
disease_frame = tk.Frame(main_frame)
disease_frame.grid(row=8, column=1, padx=10, pady=5, sticky='w')
tk.Label(main_frame, text="Do you have any of the following diseases:").grid(row=8, column=0, padx=10, pady=5, sticky='w')
cold_var = tk.BooleanVar()
cough_var = tk.BooleanVar()
fever_var = tk.BooleanVar()
headache_var = tk.BooleanVar()

tk.Checkbutton(disease_frame, text="Cold", variable=cold_var).pack(side='left', padx=5)
tk.Checkbutton(disease_frame, text="Cough", variable=cough_var).pack(side='left', padx=5)
tk.Checkbutton(disease_frame, text="Fever", variable=fever_var).pack(side='left', padx=5)
tk.Checkbutton(disease_frame, text="Headache", variable=headache_var).pack(side='left', padx=5)

# Submit Button
tk.Button(main_frame, text="Submit", command=submit).grid(row=9, column=1, padx=10, pady=20)

root.mainloop()
