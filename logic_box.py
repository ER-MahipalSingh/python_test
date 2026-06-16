def generate_pattern():
    print("\n--- Pattern Generator ---")
    print("Choose a pattern type:")
    print("1. Right-angled triangle")
    print("2. Pyramid")
    print("3. Left-angled triangle")
    
    pattern_choice = input("Enter your choice (1/2/3): ")
    
    while True:
        rows = int(input("Enter the number of rows for the pattern: "))
        
        if rows <= 0:
            print("Invalid input! Row count must be positive. Stopping generation.")
            break   
            
        if pattern_choice == '1':
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print("*", end=" ")
                print()  
                
        elif pattern_choice == '2':
            for i in range(1, rows + 1):
                for j in range(rows - i):
                    print(" ", end="")
                for k in range(2 * i - 1):
                    print("*", end="")
                print()
                
        elif pattern_choice == '3':
            for i in range(1, rows + 1):
                for j in range(rows - i):
                    print("  ", end="") 
                for k in range(1, i + 1):
                    print("* ", end="")
                print()
                
        else:
            print("Invalid pattern choice.")
            pass 
        break

def analyze_numbers():
    print("\n--- Number Analyzer ---")
    
    while True:
        start_num = int(input("Enter the start of the range: "))
        end_num = int(input("Enter the end of the range: "))
        
        if start_num >= end_num:
            print("Error: The end of the range must be greater than the start. Try again.")
            continue
        else:
            break
            
    total_sum = 0
    
    print("\n--- Analysis Results ---")
    for num in range(start_num, end_num + 1):
        if num % 2 == 0:
            print(f"Number {num} is Even")
        else:
            print(f"Number {num} is Odd")
            
        total_sum += num
        
    print(f"Sum of all numbers from {start_num} to {end_num} = {total_sum}")


print("Welcome to the Pattern Generator & Number Analyzer!") 

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    main_choice = input("Enter your choice (1/2/3): ")
    
    if main_choice == '1':
        generate_pattern() 
    elif main_choice == '2':
        analyze_numbers()
    elif main_choice == '3':
        print("Exiting the program. Goodbye!") 
        break
    else:
        print("Invalid selection. Please enter 1, 2, or 3.")