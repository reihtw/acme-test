from unittest import TestCase

from workhour.workhour import WorkHour


class TestWorkHour(TestCase):
    
    def setUp(self):
        self.employee1 = {
            'name': 'RODRIGO',
            'workhour_string': 'MO10:00-12:00'
        }
        
        self.employee2 = {
            'name': 'RENE',
            'workhour_string': 'MO10:00-12:00'
        }
    
    def test_should_assign_the_right_values_to_properties_when_passed_the_workhours_string(self):
        workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        
        expected_day = 'MO'
        expected_starthour = 1000
        expected_endhour = 1200
        
        self.assertEqual(expected_day, workhour.day)
        self.assertEqual(expected_starthour, workhour.starthour)
        self.assertEqual(expected_endhour, workhour.endhour)
    
    def test_should_return_true_when_compared_different_workhours_with_same_day_and_same_starthour_and_endhour(self):
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        
        expected_result = True
        result = employee1_workhour == employee2_workhour
        
        self.assertEqual(expected_result, result)
    
    def test_should_return_true_when_compared_different_workhours_with_same_day_and_different_starthour_but_same_endhour(self):
        self.employee2['workhour_string'] = 'MO11:00-12:00'
        
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        
        expected_result = True
        result = employee1_workhour == employee2_workhour
        
        self.assertEqual(expected_result, result)
    
    def test_should_return_true_when_compared_different_workhours_with_same_day_and_same_starthour_but_different_endhour(self):
        self.employee2['workhour_string'] = 'MO10:00-14:00'
        
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        
        expected_result = True
        result = employee1_workhour == employee2_workhour
        
        self.assertEqual(expected_result, result)
    
    def test_should_return_true_when_compared_different_workhours_with_same_day_and_different_starthour_and_endhour_but_worked_one_hour_together(self):
        self.employee2['workhour_string'] = 'MO11:00-13:00'
        
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        
        expected_result = True
        result = employee1_workhour == employee2_workhour
        
        self.assertEqual(expected_result, result)
    
    def test_should_return_false_when_compared_different_workhours_with_different_days(self):
        self.employee2['workhour_string'] = 'TU10:00-12:00'
        
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        
        expected_result = False
        result = employee1_workhour == employee2_workhour
        
        self.assertEqual(expected_result, result)
    
    def test_should_return_false_when_compared_different_workhours_with_same_day_but_different_work_time(self):
        self.employee2['workhour_string'] = 'MO14:00-17:00'
        
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        
        expected_result = False
        result = employee1_workhour == employee2_workhour
        
        self.assertEqual(expected_result, result)
    
    def test_should_fill_the_relations_dict_with_one_relation_when_passes_a_workhour_list_with_one_same_workhour(self):
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        
        workhour_list = [employee1_workhour,]
        relations_dict = dict()
        
        employee2_workhour.get_relations(workhour_list, relations_dict)
        
        expected_result = {
            'RENE-RODRIGO': 1
        }
        
        self.assertEqual(expected_result, relations_dict)
    
    def test_should_fill_the_relations_dict_with_two_relations_when_passes_a_workhour_list_with_two_same_workhours(self):
        employee3 = {
            'name': 'ASTRID',
            'workhour_string': 'MO11:00-13:00'
        }
        
        employee1_workhour = WorkHour(self.employee1['name'], self.employee1['workhour_string'])
        employee2_workhour = WorkHour(self.employee2['name'], self.employee2['workhour_string'])
        employee3_workhour = WorkHour(employee3['name'], employee3['workhour_string'])
        
        workhour_list = [employee1_workhour, employee2_workhour]
        relations_dict = dict()
        
        employee3_workhour.get_relations(workhour_list, relations_dict)
        
        expected_result = {
            'ASTRID-RODRIGO': 1,
            'ASTRID-RENE': 1
        }
        
        self.assertEqual(expected_result, relations_dict)
        
        
        
        