--h

SELECT lyfter_car_rental.cars.id
	FROM lyfter_car_rental.cars
	INNER JOIN lyfter_car_rental.car_rentals
	ON lyfter_car_rental.cars.id=lyfter_car_rental.car_rentals.car_id



SELECT lyfter_car_rental.cars.id,lyfter_car_rental.cars.make
	FROM lyfter_car_rental.cars
	WHERE lyfter_car_rental.cars.car_status='available'

