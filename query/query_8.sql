-- 8. Знайти середній бал, який ставить певний викладач за свої предмети.
SELECT AVG(grade) AS average_grade, teachers.fullname
FROM grades
JOIN disciplines ON grades.discipline_id = disciplines.id
JOIN teachers ON disciplines.teacher_id = teachers.id
WHERE teachers.fullname = 'Lori Ellis';
