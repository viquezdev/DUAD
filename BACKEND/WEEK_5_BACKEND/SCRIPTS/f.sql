--f
UPDATE lyfter_car_rental.cars
	SET car_status='available'
	WHERE id=10;

UPDATE lyfter_car_rental.car_rentals
	SET rental_status='completed'
	WHERE id=1;


SELECT * FROM lyfter_car_rental.car_rentals