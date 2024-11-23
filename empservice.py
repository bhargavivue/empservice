import sqlite3

class EmployeeDatabase:
    def __init__(self, db_name='employees.sqlite3'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES(
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  dept TEXT NOT NULL,
                  salary REAL NOT NULL)''')

    def add_employee(self):
       """Add an employee with details entered from the terminal."""
       # Get employee details from the user
       name = input("Enter employee name: ")
       dept = input("Enter employee department: ")
       salary = float(input("Enter employee salary: "))
       self.cursor.execute("insert into employees(name,dept,salary) values(?,?,?)",(name,dept,salary))
       self.conn.commit()
       print("employee added successful")
    
    
    def view_all_employees(self):
       """Display all employees in the database."""
       self.cursor.execute("SELECT * FROM employees")
       employees = self.cursor.fetchall()
       print("All Employees:")
       for employee in employees:
         print(employee)

    def search_employees(self):     
      """Search for employees by ID or name."""
      search_query=input("enter employee id or name  search:")
      if search_query.isdigit(): 
       self.cursor.execute("SELECT * FROM EMPLOYEES WHERE ID =?",(int(search_query),))
       employees=self.cursor.fetchall()
       if employees:
         print("search results")
         print(f"employee{employees}")
       else:
        print("no employee found with given criteria.")
      else:
        self.cursor.execute("SELECT * FROM EMPLOYEES WHERE name LIKE ?", ('%' + search_query + '%',))
        employees=self.cursor.fetchall()
        if employees:
         print("n\search results")
         print(f"employee{employees}")
        else:
         print("no employee found ith given criteria.")

    def update_employee(self):
      """Update an employee's department or salary."""
      emp_id=int(input("enter employee id to update"))
      self.cursor.execute("SELECT * FROM EMPLOYEES WHERE ID=?",(emp_id,))
      employee=self.cursor.fetchone()
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
        self.cursor.execute("UPDATE EMPLOYEES SET dept=? where id=?",(new_dept,emp_id))
      elif choice=="2":               
        new_salary=float(input("enter new salary:"))
        self.cursor.execute("UPDATE EMPLOYEES SET SALARY=? where id=?",(new_salary,emp_id))               
      else:
        print("Invalid choice.")
    def delete_employee(self):
      """Remove an employee record from the database using their unique ID."""
      emp_id=int(input("enter employee the employee id to delete:"))  
      self.cursor.execute("SELECT * FROM EMPLOYEES WHERE ID=?",(emp_id,))
      employee=self.cursor.fetchone()
      if employee is None:
        print(f"No employee found with the given ID: {emp_id}.")
        return
      confirm = input(f"Are you sure you want to delete employee {employee}? (yes/no): ")
      if confirm == "yes":
          self.cursor.execute("DELETE FROM EMPLOYEES WHERE ID=?", (emp_id,))
          print(f"Employee with ID {emp_id} has been deleted successfully.")
      else:
       print("Deletion cancelled.")
def main():
      """Main function with a menu to interact with the program."""
      db= EmployeeDatabase()
      while True:
        print("\nChoose an option:")
        print("1. Add a new employee")
        print("2.view all employees")
        print("3. Search for an employee")
        print("4. Update an employee's details")
        print("5. Delete an employee")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
          db.add_employee()
    
        elif choice =="2":   
         db.view_all_employees() 
    
        elif choice == "3":
            db.search_employees()
    
        elif choice == "4":
            db.update_employee()
    
        elif choice == "5":
          db.delete_employee()
       
        elif choice == "12":
         print("Exiting program.")
         break
        else:
          print("Invalid choice. Please try again.") 

# Run the main function
if __name__ == "__main__":
  main() 