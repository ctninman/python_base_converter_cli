import unittest
import calculation_functions


class TestNumToAlpha(unittest.TestCase):

	def test_less_than_10(self):
		num = 8
		result = calculation_functions.digit_greater_than_nine(num)
		self.assertEqual(result, 8)


	def test_greater_than_10(self):
		num = 12
		result = calculation_functions.digit_greater_than_nine(num)
		self.assertEqual(result, "C")
		self.assertNotEqual(result, num)


class TestCreatePlaceValues(unittest.TestCase):
	
	def test_binary_place_values(self):
		number = 36
		number_system = 2
		result = calculation_functions.determine_place_values(number, number_system)
		self.assertEqual(result, [1,2,4,8,16,32])


	def test_hexadecimal_place_values(self):
		number = 36
		number_system = 16
		result = calculation_functions.determine_place_values(number, number_system)
		self.assertEqual(result, [1, 16])


	def test_binary_number_equals_place_values(self):
		number = 32
		number_system = 2
		result = calculation_functions.determine_place_values(number, number_system)
		self.assertEqual(result, [1,2,4,8,16,32])


	def test_place_values_for_zero(self):
		number = 0
		number_system = 8
		result = calculation_functions.determine_place_values(number, number_system)
		self.assertEqual(result, [])


	def test_place_values_for_one(self):
		number = 1
		number_system = 11
		result = calculation_functions.determine_place_values(number, number_system)
		self.assertEqual(result, [1])


class TestConversionBaseTenOrBelow(unittest.TestCase):

	def test_base_four_conversion(self):
		num = 70
		arr = [1,4,16,64]
		result = calculation_functions.num_to_new_base(num, arr)
		self.assertEqual(result, '1012')
		self.assertNotEqual(result, 1012)

	def test_base_eight_conversion(self):
		num = 70
		arr = [1,8,64]
		result = calculation_functions.num_to_new_base(num, arr)
		self.assertEqual(result, '106')
		self.assertNotEqual(result, 106)


	def test_num_equals_a_place_value(self):
		num = 125
		arr = [1,5,25,125]
		result = calculation_functions.num_to_new_base(num,arr)
		self.assertEqual(result, '1000')


	def test_one_less_than_a_place_value(self):
		num = 124
		arr = [1,5,25]
		result = calculation_functions.num_to_new_base(num,arr)
		self.assertEqual(result, '444')


	def test_one_conversion(self):
		num = 1
		arr = [1]
		result = calculation_functions.num_to_new_base(num, arr)
		self.assertEqual(result, '1')


	def test_zero_conversion(self):
		num = 0
		arr = []
		result = calculation_functions.num_to_new_base(num, arr)
		self.assertEqual(result, '0')



class TestConversionBaseElevenOrAbove(unittest.TestCase):

	def test_base_twelve_conversion(self):
		num = 170
		arr = [1, 12, 144]
		result = calculation_functions.num_to_new_base_greater_than_ten(num, arr)
		self.assertEqual(result, '122')
		self.assertNotEqual(result, 122)


	def test_base_thirteen_conversion(self):
		num = 170
		arr = [1,13,169]
		result = calculation_functions.num_to_new_base_greater_than_ten(num, arr)
		self.assertEqual(result, '101')


	def test_base_thirteen_with_alpha_conversion(self):
		num = 180
		arr = [1,13,169]
		result = calculation_functions.num_to_new_base_greater_than_ten(num, arr)
		self.assertEqual(result, '10B')


	def test_num_equals_a_place_value(self):
		num = 225
		arr = [1,15,225]
		result = calculation_functions.num_to_new_base_greater_than_ten(num,arr)
		self.assertEqual(result, '100')

	
	def test_num_one_less_than_a_place_value(self):
		num = 224
		arr = [1,15]
		result = calculation_functions.num_to_new_base_greater_than_ten(num,arr)
		self.assertEqual(result, 'EE')


	def test_one_conversion(self):
		num = 1
		arr = [1]
		result = calculation_functions.num_to_new_base_greater_than_ten(num, arr)
		self.assertEqual(result, '1')


	def test_zero_conversion(self):
		num = 0
		arr = []
		result = calculation_functions.num_to_new_base_greater_than_ten(num, arr)
		self.assertEqual(result, '0')



class TestDifficultLevel(unittest.TestCase):

	def test_perfect_many(self):
		correct = 200
		answered = 200
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (100, 1000))


	def test_perfect_some(self):
		correct = 20
		answered = 20
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (50, 500))


	def test_perfect_few(self):
		correct = 3
		answered = 3
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (10, 100))


	def test_zero_correct_many(self):
		correct = 0
		answered = 200
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (10, 100))


	def test_zero_correct_some(self):
		correct = 0
		answered = 20
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (10, 100))


	def test_zero_correct_few(self):
		correct = 0
		answered = 3
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (10, 100))


	def test_sixty_percent_many(self):
		correct = 1400
		answered = 200
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (100, 1000))


	def test_sixty_percent_some(self):
		correct = 14
		answered = 20
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (50, 500))


	def test_sixty_percent_few(self):
		correct = 3
		answered = 5
		result = calculation_functions.difficulty_level(correct,answered)
		self.assertEqual(result, (10, 100))


if __name__ == '__main__':
	unittest.main()