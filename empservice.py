
import sqlite3

conn=sqlite3.connect('employees.sqlite3');
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  dept TEXT NOT NULL,
                  salary REAL NOT NULL)''')

def add_employee():
    """Add an employee with details entered from the terminal."""
    # Get employee details from the user
    name = input("Enter employee name: ")
    dept = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    cursor.execute("insert into employees(name,dept,salary) values(?,?,?)",(name,dept,salary))
    conn.commit()
    print("employee added successful")
    
    
def view_all_employess():
 cursor.execute("SELECT * FROM employees")
 employees = cursor.fetchall()
 # Display the results
 print("All Employees:")
 for employee in employees:
     print(employee)

def search_employees():     
 """Search for employees by ID or name."""
 search_query=input("enter employee id or name  search:")
 if search_query.isdigit(): 
   # Search by ID
  cursor.execute("SELECT * FROM EMPLOYEES WHERE ID =?",(int(search_query),))
  employees=cursor.fetchall()
  if employees:
    print("search results")
    print(f"employee{employees}")
  else:
    print("no employee found ith given criteria.")
 else:
 # Search by name
   cursor.execute("SELECT * FROM EMPLOYEES WHERE name LIKE ?", ('%' + search_query + '%',))
   employees=cursor.fetchall()
   if employees:
    print("n\search results")
    print(f"employee{employees}")
   else:
    print("no employee found ith given criteria.")

def update_employee():
  emp_id=int(input("enter employee id to update"))
  cursor.execute("SELECT * FROM EMPLOYEES WHERE ID=?",(emp_id,))
  employee=cursor.fetchone()
  if employee is None:
    print(f"No employee found with the given ID: {emp_id}.")
    return
  print(f"current detalis:{employee}")
  print("choose a field to update:")
  print("1.department")
  print("2.salary")
  choice=input("enter your choice:")
  if choice=="1":
   new_dept=input("enter new deartment:")
   cursor.execute("UPDATE EMPLOYEES SET dept=? where id=?",(new_dept,emp_id))
  elif choice=="2":               
    new_salary=float(input("enter new salary:"))
    cursor.execute("UPDATE EMPLOYEES SET SALARY=? where id=?",(new_salary,emp_id))               
  else:
   print("Invalid choice.")

def main():
    """Main function with a menu to interact with the program."""
while True:
    print("\nChoose an option:")
    print("1. Add a new employee")
    print("2.view all employees")
    print("3. Search for an employee")
    print("4. Update an employee's details")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
            add_employee()
    elif choice =="2":   
         view_all_employess() 
    
    elif choice == "3":
            search_employees()
    
    elif choice == "4":
            update_employee()
    
    elif choice == "12":
         print("Exiting program.")
         break
    else:
        print("Invalid choice. Please try again.") 

# Run the main function
if __name__ == "__main__":
   main()