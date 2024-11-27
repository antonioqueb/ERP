-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL
);

-- Insertar usuario inicial
INSERT INTO users (username, hashed_password)
VALUES ('admin', '$2b$12$eIX/gOxlP.xNvLPwVFRHNOcFCtCZB5WQG4R1t5j6lfYB61Zm1S6nG'); -- "password"
