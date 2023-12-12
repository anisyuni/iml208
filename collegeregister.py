import tkinter
from tkinter import ttk 
from tkinter import messagebox

def enter_data():
    accepted =  accept_var.get()
def delete_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # Get data from the GUI widgets for deletion
        delete_firstname = first_name_entry.get()
        delete_lastname = last_name_entry.get()

        # Find and remove the data from the global list
        for student in stud_info_frame:
            if student["firstname"] == delete_firstname and student["lastname"] == delete_lastname:
                stud_info_frame.remove(student)
                break

        # Display a success message
        tkinter.messagebox.showinfo(title="Success!", message="Data deleted successfully.")
    else:
        tkinter.messagebox.showwarning(title="Error!", message="You have not accepted the terms.")

    if accepted == "Accepted" :

         #students information
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname :
            
            gender = gender_combobox.get()
            age = age_spinbox.get()
            state = state_combobox.get()
            college = college_combobox.get()
            matricno = matricno_label_entry.get()
            programcode = programcode_label_entry.get()
            phone_no = phone_no_label_entry.get()

            #course information
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemester = numsemester_spinbox.get()

            print("First name: ", firstname, "Last name: ", lastname, "Phone No: ", phone_no)
            print("Gender: ", gender, "Age: ", age, "State: ", state)
            print("College: ", college, "Matric No:", matricno, "Program Code: ", programcode)
            print("Courses: ", numcourses, "Semester: ", numsemester)
            print("Registration status: ", registration_status)
            print("--------------------------------------------")
           
            tkinter.messagebox.showinfo(title = "Success !", message = "Your college registration has been made.")

        else :
            tkinter.messagebox.showwarning(title = "Error !", message = "First name and last name are required.")

    else :
        tkinter.messagebox.showwarning(title = "Error !" , message = "You have not accepted the terms.")


window = tkinter.Tk()
window.title("College Registration Form")

frame = tkinter.Frame(window)
frame.pack()

#saving students information
stud_info_frame = tkinter.LabelFrame(frame, text = "College Registration Form" )
stud_info_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

first_name_label = tkinter.Label(stud_info_frame, text = "First Name")
first_name_label.grid(row = 0, column = 0)
last_name_label = tkinter.Label(stud_info_frame, text = "Last Name")
last_name_label.grid(row = 0, column = 1)

first_name_entry = tkinter.Entry(stud_info_frame)
last_name_entry = tkinter.Entry(stud_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

gender_label = tkinter.Label(stud_info_frame, text = "Gender")
gender_combobox = ttk.Combobox(stud_info_frame, values = ["Male", "Female"])
gender_label.grid(row = 0, column = 2)
gender_combobox.grid(row = 1, column = 2)

age_label = tkinter.Label(stud_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(stud_info_frame, from_ = 18, to = 30)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)

matricno_label = tkinter.Label(stud_info_frame, text = "Matric No")
matricno_label.grid(row = 4, column = 0)
matricno_label_entry = tkinter.Entry(stud_info_frame)
matricno_label_entry.grid(row = 5, column = 0)

programcode_label = tkinter.Label(stud_info_frame, text = "Program Code")
programcode_label.grid(row = 4, column = 1)
programcode_label_entry = tkinter.Entry(stud_info_frame)
programcode_label_entry.grid(row = 5, column = 1)

phone_no_label= tkinter.Label(stud_info_frame, text = "Phone No")
phone_no_label.grid(row = 4, column = 2)
phone_no_label_entry = tkinter.Entry(stud_info_frame)
phone_no_label_entry.grid(row = 5, column = 2)

state_label = tkinter.Label(stud_info_frame, text = "State")
state_combobox = ttk.Combobox(stud_info_frame, values =["Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", "Sarawak", "Selangor", "Terengganu", "Wilayah Persekutuan"])
state_label.grid(row = 2, column = 1)
state_combobox.grid(row = 3, column = 1)

college_label = tkinter.Label(stud_info_frame, text = "College")
college_combobox = ttk.Combobox(stud_info_frame, values = ["Malinja", "Masria", "Mahsuri", "Murni"])
college_label.grid(row = 2, column = 2)
college_combobox.grid(row = 3, column = 2)

for widget in stud_info_frame.winfo_children() :
    widget.grid_configure(padx = 10, pady = 5)

#saving course information
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

registered_label = tkinter.Label(courses_frame, text = "Registration Status")

reg_status_var = tkinter.StringVar(value = "Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered", variable = reg_status_var, onvalue = "Registered" , offvalue = "Not registered")

registered_label.grid(row = 0, column = 0)
registered_check.grid(row = 1, column = 0)

numcourses_label = tkinter.Label(courses_frame, text = "Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = 'infinity')
numcourses_label.grid(row = 0, column = 1)
numcourses_spinbox.grid(row = 1, column = 1)

numsemester_label = tkinter.Label(courses_frame, text = "Semester")
numsemester_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numsemester_label.grid(row = 0, column = 2)
numsemester_spinbox.grid(row = 1, column = 2)

for widget in courses_frame.winfo_children() :
    widget.grid_configure(padx = 10, pady = 5)

#accept terms
terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)

accept_var = tkinter.StringVar(value = "Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept the terms and conditions.", variable = accept_var, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row = 0, column = 0)
delete_var = tkinter.StringVar(value = "Accepted")
update_var = tkinter.StringVar(value = "Accepted")

#button
button = tkinter.Button(frame, text = "Enter data", command = enter_data)
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10)
button = tkinter.Button(frame, text = "Delete data", command = delete_data)
button.grid(row = 4, column = 0, sticky = "news", padx = 20, pady = 10)

window.mainloop()