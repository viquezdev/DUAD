CREATE TABLE lyfter_car_rental.cars
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
	make character varying(50) NOT NULL,
	model character varying(100) NOT NULL,
    manufacture_year smallint NOT NULL,
    car_status character varying(30) NOT NULL,
    PRIMARY KEY (id)
);

insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Ford', 'F350', 2003, 'reserved');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Suzuki', 'Sidekick', 1992, 'reserved');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('BMW', '7 Series', 2010, 'available');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Dodge', 'Ram Van B150', 1993, 'unavailable');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Chrysler', 'LeBaron', 1992, 'unavailable');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Ford', 'E150', 2009, 'maintenance');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('BMW', 'X5', 2002, 'rented');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Honda', 'Element', 2009, 'sold');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Mazda', '626', 1993, 'sold');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Nissan', 'Titan', 2011, 'rented');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Volkswagen', 'GTI', 2012, 'sold');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Mazda', 'MPV', 1994, 'sold');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Chevrolet', 'Silverado 3500', 2009, 'rented');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Toyota', 'T100 Xtra', 1997, 'reserved');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('BMW', 'Z3', 1996, 'rented');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Mercury', 'Marauder', 2004, 'unavailable');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Saturn', 'VUE', 2003, 'available');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Nissan', '200SX', 1996, 'available');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Mitsubishi', 'GTO', 1998, 'reserved');
insert into lyfter_car_rental.cars (make, model, manufacture_year, car_status) values ('Lexus', 'SC', 1998, 'unavailable');
