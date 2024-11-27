DO $$ BEGIN
   IF NOT EXISTS (
      SELECT 1 FROM pg_roles WHERE rolname = 'user'
   ) THEN
      CREATE ROLE "user" WITH LOGIN PASSWORD 'password';
   END IF;
END $$;

DO $$ BEGIN
   IF NOT EXISTS (
      SELECT 1 FROM pg_database WHERE datname = 'gestpro_db'
   ) THEN
      CREATE DATABASE "gestpro_db" OWNER "user";
   END IF;
END $$;
