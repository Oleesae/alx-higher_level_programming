-- convert hbtn_0c_0 to UTF8
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE users MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci;
