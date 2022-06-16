
#Replace <ClassName>  with AppropiateClass Name
#class <ClassName>:
#    pass
"""
from enitity layer import Entity
from databaselayer import employee_data_access
create class EmployeeValidation:

    def validation_employee_list(self,List[employee]):
        validate each element for their datatype
        create two lists
        one validation failed list for
        one validation pass list 

        return {
            "invalid-employee_data":[],
            "valid_employee_data":[],
        }


    def save_employee_list(self,List[Employee]):
        response=self.validation_employee_list(List[Employee])

        resposne= employee_data_access.EmployeeDataAccess.save(response["validation_employe_list"])
        





"""