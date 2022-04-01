import csv
def write_data_to_csv():
    with open("emploee.csv", "w", newline='') as f:
        w = csv.writer(f) # returns csv writer object
        w.writerow(["EmpNo", "EmpName", "EmpSal", "EmpAddr"])
        n = int(input("Enter Number of Employees:"))
        for i in range(n):
            emp_no = input("Enter Employee No:")
            emp_name = input("Enter Employee Name:")
            emp_sal = input("Enter Employee Salary:")
            emp_addr = input("Enter Employee Address:")
            w.writerow([emp_no, emp_name, emp_sal, emp_addr])
    print("Total Employees data written to csv file successfully")
