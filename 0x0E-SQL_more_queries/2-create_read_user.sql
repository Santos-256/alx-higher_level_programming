-- Create or ensure existence of Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or ensure existence of User, set password, and grant SELECT privilege
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
