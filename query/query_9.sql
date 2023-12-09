-- 9. Знайти список курсів, які відвідує студент.
SELECT DISTINCT disciplines.name, students.fullname
FROM disciplines
JOIN groups ON disciplines.id = groups.id
JOIN students ON groups.id = students.group_id
WHERE students.fullname = 'David Calderon';
