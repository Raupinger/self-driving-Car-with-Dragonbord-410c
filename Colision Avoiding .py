if CarControls.front_distance < CarControls.min_distance :
	if CarControls.left_distance < (CarControls.min_distance + CarControls.car_width) :
		CarControls.avoide(direction= "left") 
	elseif CarControls.right_distance < (CarControls.min_distance + CarControls.car_width) :
		CarControls.avoide(direction= "right") 
	else 
		CarControls.brake(priority= "height")