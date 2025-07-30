-- SQLite
ALTER TABLE invoices 
    ADD COLUMN buyer_phone_number VARCHAR(20) NOT NULL DEFAULT '0000-0000';

ALTER TABLE invoices 
    ADD COLUMN employee_code VARCHAR(20) NOT NULL DEFAULT 'EMP-000';




