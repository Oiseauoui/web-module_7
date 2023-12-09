-- 6. Знайти список студентів у певній групі.

SELECT students.fullname, groups.name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE groups.name = 'Group A';
