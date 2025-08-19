CREATE TABLE lyfter_car_rental.car_rentals
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
	user_id INT NOT NULL REFERENCES lyter_car_rental.users(id),
	car_id INT NOT NULL REFERENCES lyter_car_rental.cars(id),
	rental_date date NOT NULL DEFAULT CURRENT_DATE,
    rental_status character varying(30) NOT NULL,
    PRIMARY KEY (id)
);


