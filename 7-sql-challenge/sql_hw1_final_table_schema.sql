CREATE TABLE employees(
    emp_no INT PRIMARY KEY NOT NULL,
    birth_date DATE,
    first_name VARCHAR(200),
    last_name VARCHAR(200),
    gender VARCHAR(5),
    hire_date DATE
);

CREATE TABLE departments(
    dept_no VARCHAR(10) PRIMARY KEY NOT NULL, 
    dept_name VARCHAR(200)
);

CREATE TABLE dept_emp(
    emp_no INT REFERENCES employees(emp_no),
    dept_no VARCHAR(10) REFERENCES departments(dept_no),
    from_date DATE,
    to_date DATE
);

CREATE TABLE dept_manager(
    dept_no VARCHAR(10) REFERENCES departments(dept_no),
    emp_no INT REFERENCES employees(emp_no),
    from_date DATE,
    to_date DATE
);

CREATE TABLE salaries(
    emp_no INT REFERENCES employees(emp_no),
    salary INT,
    from_date DATE,
    to_date DATE
);

CREATE TABLE titles(
    emp_no INT REFERENCES employees(emp_no),
    title VARCHAR(200),
    from_date DATE,
    to_date DATE
);

