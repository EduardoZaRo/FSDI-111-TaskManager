CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

-- Generate some dummy data
INSERT INTO task(
    summary, 
    description
) VALUES 
(
    "Dishes bru",
    "Clean the dishes with sulfuric acid"
),
(
    "Do homework",
    "3 final projects before tuesday"
),
(
    "Blink",
    "Don't forget to blink every day"
);