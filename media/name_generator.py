import uuid

def generate_name(filename):
<<<<<<< HEAD
  return "{}/{}/".format("uploads", uuid.uuid4())

=======
	return "{}/{}".format(
		"uploads",
		uuid,uuid4(),
		filename)
>>>>>>> 61eda2c20993700952d18dc68c0c07c2a0acc3cc
