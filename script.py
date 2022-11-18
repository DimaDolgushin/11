CREATE TABLE IF NOT EXISTS manufactures(
    id INTEGER PRIMARY KEY UNIQUE,
    manifacture_name VARCHAR(100) UNIQUE);

CREATE TABLE IF NOT EXISTS names_of_the_technique(
    id INTEGER PRIMARY KEY UNIQUE,
    video_card VARCHAR(50) NOT NULL,
    cooler VARCHAR(50) NOT NULL,
    motherboard VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS suppliers(
    id INTEGER PRIMARY KEY UNIQUE,
    title VARCHAR(100));

CREATE TABLE IF NOT EXISTS lots_of_goods(
    id INTEGER PRIMARY KEY UNIQUE,
    supplier_id INTEGER NOT NULL,
    time_date DATE NOT NULL,
    FOREIGN KEY(supplier_id)
        REFERENCES suppliers(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS technics(
    id INTEGER PRIMARY KEY UNIQUE,
    manifacture_id INTEGER NOT NULL,
    tech_name_id INTEGER NOT NULL,
    batch_id INTEGER NOT NULL,
    model VARCHAR(100) NOT NULL,
    warranty VARCHAR(100) NOT NULL,
    price INTEGER NOT NULL,
    FOREIGN KEY(manifacture_id)
        REFERENCES manufactures(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(tech_name_id)
        REFERENCES names_of_the_technique(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(batch_id)
        REFERENCES lots_of_goods(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS buyers(
    id INTEGER PRIMARY KEY UNIQUE,
    surname VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    patronymic VARCHAR(100) NOT NULL,
    telephone VARCHAR(100) NOT NULL);

CREATE TABLE IF NOT EXISTS accounts(
    id INTEGER PRIMARY KEY UNIQUE,
    buyer_id INTEGER NOT NULL,
    discount VARCHAR(100) NOT NULL,
    date_time DATE NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY(buyer_id)
        REFERENCES buyers(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);

CREATE TABLE sale(
    id INTEGER PRIMARY KEY UNIQUE,
    account_id INTEGER NOT NULL,
    tech_id INTEGER NOT NULL,
    quantity VARCHAR(100),
    discount VARCHAR(100),
    FOREIGN KEY(account_id)
        REFERENCES accounts(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(tech_id)
        REFERENCES technics(id)
        ON DELETE SET NULL ON UPDATE NO ACTION);
