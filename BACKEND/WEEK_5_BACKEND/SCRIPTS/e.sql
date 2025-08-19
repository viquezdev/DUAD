--e

INSERT INTO lyfter_car_rental.car_rentals(
	user_id, car_id, rental_date, rental_status)
	VALUES ('6','10', '2025-08-15','active');

UPDATE lyfter_car_rental.cars
	SET car_status='rented'
	WHERE id=10;