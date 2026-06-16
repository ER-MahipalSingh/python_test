students_list = []     
student_dict = {}     
unique_subjects = set() 

def add_student():
    print("\n--- Add Student ---")
    student_id = input("Student ID: ")
    name = input("Name: ")
    
    
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age. Please enter a valid number.")
        return
        
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    subjects_input = input("Subjects (comma-separated): ")
    
    subjects = [sub.strip() for sub in subjects_input.split(",")]
    for sub in subjects:
        unique_subjects.add(sub)
        
    immutable_info = (student_id, dob)
    
    student_info = {
        'name': name,
        'age': age,
        'grade': grade,
        'subjects': subjects,
        'immutable_data': immutable_info 
    }
    
    student_dict[student_id] = student_info

    students_list.append({student_id: student_info})
    
    print("\nStudent added successfully!") [cite: 166]

def display_all_students():
    print("\n--- Display All Students ---") [cite: 170]
    if not students_list:
        print("No student records found.")
        return
        
    for record in students_list:
        for s_id, info in record.items():
            subjects_str = ", ".join(info['subjects'])
            print(f"Student ID: {s_id} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']} | Subjects: {subjects_str}") [cite: 171]

def update_student():
    print("\n--- Update Student Information ---")
    s_id = input("Enter Student ID to update: ")
    
    if s_id in student_dict:
        print("1. Update Age")
        print("2. Update Subjects")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            new_age = int(input("Enter new age: ")) 
            student_dict[s_id]['age'] = new_age
            print("Age updated successfully!")
        elif choice == '2':
            new_subjects = input("Enter new subjects (comma-separated): ")
            subjects_list = [sub.strip() for sub in new_subjects.split(",")]
            student_dict[s_id]['subjects'] = subjects_list
            
            for sub in subjects_list:
                unique_subjects.add(sub)
            print("Subjects updated successfully!")
        else:
            print("Invalid choice.")
    else:
        print("Student ID not found.")

def delete_student():
    print("\n--- Delete Student ---")
    s_id = input("Enter Student ID to delete: ")
    
    if s_id in student_dict:
        del student_dict[s_id]
        
        for i in range(len(students_list)):
            if s_id in students_list[i]:
                del students_list[i]
                break
                
        print("Student record deleted successfully!")
    else:
        print("Student ID not found.")

def display_subjects():
    print("\n--- Subjects Offered ---") [cite: 154]
    if not unique_subjects:
        print("No subjects are currently listed.")
    else:
        print(", ".join(unique_subjects))



print("Welcome to the Student Data Organizer!") [cite: 133, 148]

while True:
    print("\nSelect an option:") [cite: 149]
    print("1. Add Student") [cite: 150]
    print("2. Display All Students") [cite: 151]
    print("3. Update Student Information") [cite: 152]
    print("4. Delete Student") [cite: 153]
    print("5. Display Subjects Offered") [cite: 154]
    print("6. Exit") [cite: 154]
    
    main_choice = input("Enter your choice: ") [cite: 155]
    
    if main_choice == '1':
        add_student() [cite: 140]
    elif main_choice == '2':
        display_all_students() [cite: 141]
    elif main_choice == '3':
        update_student() [cite: 142]
    elif main_choice == '4':
        delete_student() [cite: 143]
    elif main_choice == '5':
        display_subjects() [cite: 144]
    elif main_choice == '6':
        print("Thank you for using the Student Data Organizer. Goodbye!") [cite: 146]
        break
    else:
        print("Invalid selection. Please enter a number from 1 to 6.")