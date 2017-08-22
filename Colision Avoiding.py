from CarControls import *
if CarControls.front_distance < CarControls.min_distance :
	if CarControls.left_distance < (CarControls.min_distance + CarControls.car_width) :
		CarControls.startavoiding(direction= "left") 
		while CarControls.right_distance < (CarControls.car_length*3) :
			print "still avoiding"
		CarControls.endavoiding(direction= "left")
	elseif CarControls.right_distance < (CarControls.min_distance + CarControls.car_width) :
		CarControls.startavoiding(direction= "right") 
		while CarControls.left_distance < (CarControls.car_length*3) :
			print "still avoiding"
		CarControls.endavoiding(direction= "right")
	else 
		CarControls.brake(priority= "height")