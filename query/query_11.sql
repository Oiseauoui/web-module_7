-- Додаткові 11. Середній бал, який певний викладач ставить певному студентові.

SELECT t.fullname AS teacher_name, s.fullname AS student_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN disciplines d ON g.discipline_id = d.id
JOIN teachers t ON d.teacher_id = t.id
JOIN students s ON g.student_id = s.id
WHERE t.fullname = 'Lori Ellis' AND s.fullname = 'Darrell Ellis'
GROUP BY t.fullname, s.fullname;
