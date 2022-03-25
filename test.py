import unittest
from functions import strHour2float, tranformData
from person import Person

class test_functions(unittest.TestCase):

    def test_strHour2float(self):
        self.assertEqual(strHour2float('20:15'), 20.25)
        self.assertEqual(strHour2float('20: 15'), 20.25)
        self.assertEqual(strHour2float('1:30'), 1.5)
        self.assertGreater(strHour2float('2:01'), strHour2float('2:00'), "It works")

    def test_person_calss(self):
        lucas = Person("LUC")
        lucas.works("MO", ['10:00', '12:00'])

        self.assertEqual(lucas.name, "LUC")
        self.assertEqual(lucas.schedule, {'MO':['10:00', '12:00']})

        lucas.works("WE", ['9:00', '10:00'])

        self.assertEqual(lucas.schedule, {'MO':['10:00', '12:00'], 'WE': ['9:00', '10:00']})

    def test_transformData(self):
        new_person, days = tranformData(['RENE=MO10:00-12:00,TU10:00-12:00\n'])
        rene=Person("RENE")
        rene.works("MO", ['10:00', '12:00'])
        rene.works("TU", ['10:00', '12:00'])
      
        self.assertEqual(new_person[0].__dict__, rene.__dict__)

        new_person, days = tranformData(['RENE=MO 10:00-12:00,TU10:00- 12:00\n'])
        rene=Person("RENE")
        rene.works("MO", ['10:00', '12:00'])
        rene.works("TU", ['10:00', '12:00'])
      
        self.assertEqual(new_person[0].__dict__, rene.__dict__)

if __name__=='__main__':
    unittest.main()
