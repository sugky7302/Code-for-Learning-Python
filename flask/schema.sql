CREATE TABLE stations (
    id INTEGER,
    name TEXT NOT NULL,
    type INTEGER,
    go_action TEXT NOT NULL,
    go_laser INTEGER,
    go_ultrasonic INTEGER,
    back_action TEXT NOT NULL,
    back_laser INTEGER,
    back_ultrasonic INTEGER
);