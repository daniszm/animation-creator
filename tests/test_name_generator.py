<<<<<<< HEAD
import unittest
from media.name_generator import generate_name

class TestNameGenerator(unittest.TestCase):

  def test_generation_of_unique_name(self):
    n1 = generate_name('epsy.jpg')
    n2 = generate_name('epsy.jpg')
    regexp = re.compile(r'^uploads\/[0-9a-f-](36)\/epsy\.jpg$')
    assert n1 != n2
    assert regexp.search(n1)
=======
import unittest from media.name_generator import generate_name
import re

class TestNameGenerator(unittest.TestCase):
	def test_generation_of_unique_name(self):
		n1 = generate_name('foo.jpg')
		n2 = generate_name('foo.jpg')
		regexp = re.compile(r'^uploads\/[0-9a-f-]{36}\/foo\.jpg$')
		assert n1 != n2
		assert regexp.search(n1)
>>>>>>> 61eda2c20993700952d18dc68c0c07c2a0acc3cc
