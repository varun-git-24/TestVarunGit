class TestCase:
    def __init__(self, name, func):
        self.name = name
        self.func = func
        self.result = None
        self.error = None

    def run(self):
        try:
            self.func()
            self.result = "Passed"
        except Exception as e:
            self.result = "Failed"
            self.error = str(e)

class TestSuite:
    def __init__(self, name):
        self.name = name
        self.test_cases = []

    def add_test_case(self, test_case):
        self.test_cases.append(test_case)

    def run(self):
        print(f"Running Test Suite: {self.name}")
        for test_case in self.test_cases:
            test_case.run()
            print(f"Test Case: {test_case.name} - {test_case.result}")
            if test_case.result == "Failed":
                print(f"Error: {test_case.error}")

    def report(self):
        passed = sum(1 for test in self.test_cases if test.result == "Passed")
        failed = sum(1 for test in self.test_cases if test.result == "Failed")
        total = len(self.test_cases)
        print(f"\nTest Suite: {self.name} - Report")
        print(f"Total: {total}, Passed: {passed}, Failed: {failed}")

# Example usage
def test_case_1():
    assert 1 + 1 == 2

def test_case_2():
    assert 1 / 0 == 1  # This will raise an exception

def test_case_3():
    assert "hello".upper() == "HELLO"

# Create a test suite
suite = TestSuite("Example Test Suite")

# Add test cases to the suite
suite.add_test_case(TestCase("Test Case 1", test_case_1))
suite.add_test_case(TestCase("Test Case 2", test_case_2))
suite.add_test_case(TestCase("Test Case 3", test_case_3))

# Run the test suite
suite.run()

# Report the results
suite.report()
