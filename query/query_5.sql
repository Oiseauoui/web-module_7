-- 5. Знайти курси, які читає певний викладач.
SELECT DISTINCT d.name AS course_name, t.fullname
FROM disciplines d
JOIN teachers t ON d.teacher_id = t.id
WHERE t.fullname = 'Emily Hall';
