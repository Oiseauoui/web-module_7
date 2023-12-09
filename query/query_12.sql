-- Додаткові 12. Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT d.name, g.grade, s.fullname AS student_name
FROM grades g
JOIN disciplines d ON g.discipline_id = d.id
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = 'ТП-05-1' AND d.name = 'Програмування'
ORDER BY g.date_of DESC
LIMIT 1;
