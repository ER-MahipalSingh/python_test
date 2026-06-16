global_summary = {
    'total_values': 0,
    'overall_mean': 0.0
}

def store_data(*args):
    data = list(args)
    
    global global_summary
    global_summary['total_values'] = len(data)
    if len(data) > 0:
        global_summary['overall_mean'] = sum(data) / len(data)
        
    return data

def display_kwargs_summary(**kwargs):
    print("\n--- Dataset Characteristics ---")
    for key, value in kwargs.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

def get_dataset_statistics(data):
    if not data:
        return 0, 0, 0
    minimum = min(data) 
    maximum = max(data)
    average = sum(data) / len(data)
    return minimum, maximum, average


def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def main():
    data_list = []
    
    print("Welcome to the Data Analyzer and Transformer Program")
    
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")
        print("8. View Function Documentation (__doc__)")
        
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            user_input = input("Enter data for a 1D array (separated by spaces): ")
          
            try:
                parsed_data = [int(x) for x in user_input.split()]
                data_list = store_data(*parsed_data) 
                print("Data has been stored successfully!")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                
        elif choice == '2':
            if not data_list:
                print("Please input data first.")
                continue
            print("\nData Summary:")
            print(f"- Total elements: {len(data_list)}")
            print(f"- Minimum value: {min(data_list)}")
            print(f"- Maximum value: {max(data_list)}")
            print(f"- Sum of all values: {sum(data_list)}")
            print(f"- Average value (from global var): {global_summary['overall_mean']:.2f}")
            
        elif choice == '3':
            num = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {num} is: {calculate_factorial(num)}")
            
        elif choice == '4':
            if not data_list:
                print("Please input data first.")
                continue
            threshold = int(input("Enter a threshold value to filter out data below this value: "))
            filtered_data = list(filter(lambda x: x >= threshold, data_list))
            print(f"Filtered Data (values >= {threshold}):")
            print(", ".join(map(str, filtered_data)))
            
        elif choice == '5':
            if not data_list:
                print("Please input data first.")
                continue
            print("Choose sorting option:\n1. Ascending\n2. Descending")
            sort_choice = input("Enter your choice: ")
            
            if sort_choice == '1':
                data_list.sort()
                print("Sorted Data in Ascending Order:")
                print(", ".join(map(str, data_list)))
            elif sort_choice == '2':
                sorted_list = sorted(data_list, reverse=True)
                print("Sorted Data in Descending Order:")
                print(", ".join(map(str, sorted_list)))
                
        elif choice == '6':
            if not data_list:
                print("Please input data first.")
                continue
            minimum, maximum, average = get_dataset_statistics(data_list)
            print("\nDataset Statistics:")
            print(f"- Minimum value: {minimum}")
            print(f"- Maximum value: {maximum}")
            print(f"- Average value: {average:.2f}")
            
            display_kwargs_summary(min_val=minimum, max_val=maximum, avg_val=round(average, 2), elements=len(data_list))
            
        elif choice == '7':
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
            
        elif choice == '8':
            print("\n--- Function Documentation ---")
            print(f"store_data: {store_data.__doc__}")
            print(f"get_dataset_statistics: {get_dataset_statistics.__doc__}")
            print(f"calculate_factorial: {calculate_factorial.__doc__}")
            print(f"display_kwargs_summary: {display_kwargs_summary.__doc__}")
            
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()