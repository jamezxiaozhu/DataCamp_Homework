
--List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT 
	e.emp_no AS "Employee Number",
	e.last_name AS "Last Name",
	e.first_name AS "First Name",
	e.gender AS "Gender",
	s.salary AS "Salary"
FROM employees AS e
JOIN salaries AS s
ON e.emp_no=s.emp_no;

--List employees who were hired in 1986.
SELECT
	emp_no AS "Employee Number",
	last_name AS "Last Name",
	first_name AS "First Name",
	gender AS "Gender",
	hire_date AS "Hire Date"
FROM employees
WHERE hire_date >= '19860101'
AND hire_date <= '19861231'
ORDER BY hire_date;

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT
    dm.dept_no "Department Number",
    d.dept_name "Department Name",
    dm.emp_no "Manager Employee Number",
    e.last_name "Last Name",
    e.first_name "First name",
    dm.from_date "Start Employeement Date",
    dm.to_date "End Employeement Date"
FROM dept_manager dm
LEFT JOIN departments d 
ON dm.dept_no = d.dept_no
LEFT JOIN employees e
ON dm.emp_no = e.emp_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT
    de.emp_no "Employee Number",
    e.last_name "Last Name",
    e.first_name "First name",
    d.dept_name "Department Name"
FROM dept_emp de
LEFT JOIN departments d 
ON de.dept_no = d.dept_no
LEFT JOIN employees e
ON de.emp_no = e.emp_no;

--List all employees whose first name is "Hercules" and last names begin with "B."
SELECT
    emp_no AS "Employee Number",
	last_name AS "Last Name",
	first_name AS "First Name",
	gender AS "Gender",
	hire_date AS "Hire Date"
FROM employees
WHERE first_name LIKE 'Hercules'
AND last_name LIKE 'B%';

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT
    de.emp_no "Employee Number",
    e.last_name "Last Name",
    e.first_name "First name",
    d.dept_name "Department Name"
FROM dept_emp de
LEFT JOIN departments d 
ON de.dept_no = d.dept_no
LEFT JOIN employees e
ON de.emp_no = e.emp_no
WHERE d.dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT
    de.emp_no "Employee Number",
    e.last_name "Last Name",
    e.first_name "First name",
    d.dept_name "Department Name"
FROM dept_emp de
LEFT JOIN departments d 
ON de.dept_no = d.dept_no
LEFT JOIN employees e
ON de.emp_no = e.emp_no
WHERE d.dept_name = 'Sales'
OR d.dept_name = 'Development';

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT
	last_name "Last Name",
    COUNT(last_name) "Total Count"
FROM employees
GROUP BY last_name
ORDER BY count(last_name) DESC;
