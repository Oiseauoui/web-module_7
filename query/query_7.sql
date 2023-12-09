-- 7. Знайти оцінки студентів у конкретній групі з певного предмета.

SELECT disciplines.name, groups.name, students.fullname, grades.grade
FROM students
JOIN groups ON students.group_id = groups.id
JOIN disciplines ON groups.id = disciplines.group_id
JOIN grades ON students.id = grades.student_id AND disciplines.id = grades.discipline_id
WHERE groups.name = 'Group A' AND disciplines.name = 'Mathematics';
