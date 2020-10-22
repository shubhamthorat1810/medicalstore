from django.contrib import admin

# Register your models here.

from medical.models import Company
from medical.models import Medicine
from medical.models import MedicalDetails
from medical.models import Employee
from medical.models import Customer
from medical.models import Bill
from medical.models import EmployeeSalary
from medical.models import BillDetails
from medical.models import CustomerRequest
from medical.models import CompanyAccount
from medical.models import CompanyBank
from medical.models import EmployeeBank



admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)
admin.site.register(EmployeeBank)
