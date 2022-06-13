# pylint: skip-file
import unittest
from testing_imports import *
from HTMLTestRunner import HTMLTestRunner

"""
- Comproveu que la funció 2a dóna el resultat correcte quan cols_to_return conté, com a mínim, dues columnes (per exemple, short_name i potential).
- Comproveu que la funció 2a dóna el resultat correcte si el resultat inclou més d'una fila.
- Comproveu que la funció calculate_BMI dóna el resultat correcte quan gender = ‘F’
- Comproveu que la funció clean_up_players_dict dóna el resultat correcte si la query conté l'operació “one”.
"""


class PrivateTestsEx2(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2016])

    def test_private_ex2a1(self):
        filtered_df = find_max_col(self.data, "potential", ["short_name", "potential"])
        expected = pd.DataFrame({"short_name": "L. Messi", "potential": [95]})
        self.assertTrue(
            (filtered_df.reset_index(drop=True) == expected.reset_index(drop=True)).all().all())

    """# TODO:: Find max col no pot donar més d'una fila
    def test_private_ex2a2(self):
        filtered_df = find_max_col(self.data, "potential", ["short_name", "potential"])
        expected = pd.DataFrame({"short_name": "L. Messi", "potential": [95]})
        self.assertTrue(
            (filtered_df.reset_index(drop=True) == expected.reset_index(drop=True)).all().all())"""


class PrivateTestsEx3(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Create some fake data
        cls.data = pd.DataFrame({"short_name": ["L. Messi", "A. Putellas", "A. Hegerberg"],
                                 "gender": ["M", "F", "F"],
                                 "year": [2021, 2021, 2022],
                                 "height_cm": [169, 171, 177],
                                 "weight_kg": [67, 66, 70]})

    def test_private_ex3a(self):
        female_bmi = calculate_bmi(self.data, "F", 2021, ["short_name"])
        self.assertEqual(female_bmi["short_name"].iloc[0], "A. Putellas")
        self.assertEqual(female_bmi["BMI"].iloc[0], 66 / (1.71 * 1.71))


class PrivateTestsEx4(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2016, 2017, 2018])

    def test_private_ex4b(self):
        ids = [176580, 168542]
        columns_of_interest = ["overall", "short_name"]
        data_dict = players_dict(self.data, ids, columns_of_interest)
        data_dict = clean_up_players_dict(data_dict, [("short_name", "one")])
        self.assertEqual(len([data_dict[168542]["short_name"]]), 1)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PrivateTestsEx2))
    suite.addTest(unittest.makeSuite(PrivateTestsEx3))
    suite.addTest(unittest.makeSuite(PrivateTestsEx4))
    runner = HTMLTestRunner(log=True, verbosity=2, output='reports',
                            title='PAC4', description='PAC4 public tests',
                            report_name='Public tests', open_in_browser=True)
    runner.run(suite)
