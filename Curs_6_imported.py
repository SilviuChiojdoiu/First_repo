# importarea
class Test_case1:
    # definirea metodei
    def printeaza_test_case1(self):
        print("Running Test Case 1")

class Test_case2:
    def printeaza_test_case2(self):
        print("Running Test Case 2")

class Test_case3:
    def __init__(self, name , summary):
        # aici construim un atribut de tip name si altul de tip summary
        self.name = name
        self.summary = summary
    def return_name(self):
        return self.name
    def return_summary(self):
        return self.summary
    def printeaza_test_case(self):
        print("Running Test case 3")

