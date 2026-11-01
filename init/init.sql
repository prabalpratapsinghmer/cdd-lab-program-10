
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

INSERT INTO students (name, department)
VALUES
('Rahul', 'CSE'),
('Priya', 'ISE'),
('Arjun', 'ECE');
