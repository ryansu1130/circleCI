import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 10 == calculator.add(5,5)

    def test_subtract(self):
        assert 10 == calculator.subtract(15,5)
