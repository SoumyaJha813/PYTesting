def fuzzy_math(num1, operator, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('We need to do fuzzy maths on ints')

    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception(f"I don't know how to do math with {operator}")

    if result < 0:
        return 'A negative number, what does that even mean?'
    elif result < 10:
        return 'A small number, I can deal with that.'
    elif result < 20:
        return 'A medium-sized number. OK.'
    else:
        return 'A really big number, way too big for me.'

class TestFuzzyMath:
    def test_non_int_input_for_num1(self):
        pass
    def test_non_int_input_for_num2(self):
        pass
    def test_addition_with_negative_result(self):
        pass
    def test_addition_with_small_result(self):
        assert fuzzy_math(2, '+', 2) == 'A small number, I can deal with that.' #asserting that output of fuzzy math is equal to the number(on left).
    def test_addition_with_medium_result(self):
        pass
    def test_addition_with_large_result(self):
        pass
    def test_with_invalid_operator(self):
        pass
    def test_multiplication_with_negative_result(self):
        pass
    def test_multiplication_with_small_result(self):
        pass
    def test_multiplication_with_medium_result(self):
        pass
    def test_multiplication_with_large_result(self):
        pass


