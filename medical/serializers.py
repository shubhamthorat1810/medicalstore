from rest_framework import serializers
from medical.models import ( Company , Medicine , MedicalDetails , Employee , Customer , Bill ,
						   EmployeeSalary , BillDetails ,CustomerRequest , CompanyAccount , CompanyBank ,
						   EmployeeBank )


class CompanySerializer(serializers.ModelSerializer):

	class Meta:
		model=Company
		fields="__all__"


class MedicineSerializer(serializers.ModelSerializer):

	class Meta:
		model=Medicine
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Company']=CompanySerializer(instance.comapny_id).data
		return response


class MedicalDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model=MedicalDetails
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response["Medicine"]=MedicineSerializer(instance.medicine_id).data
		return response
	
class MedicalDetailsSerializerSimple(serializers.ModelSerializer):

	class Meta:
		model=MedicalDetails
		fields="__all__"


class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model=Employee
		fields="__all__"

	
class CustomerSerializer(serializers.ModelSerializer):

	class Meta:
		model=Customer
		fields="__all__"


class BillSerializer(serializers.ModelSerializer):

	class Meta:
		model=Bill
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Customer']=CustomerSerializer(instance.customer_id).data
		return response



class EmployeeSalarySerializer(serializers.ModelSerializer):

	class Meta:
		model=EmployeeSalary
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Employee']=EmployeeSerializer(instance.employee_id).data
		return response


class BillDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model=BillDetails
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Bill']=BillSerializer(instance.bill_id).data
		return response

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Medicine']=MedicineSerializer(instance.medicine_id).data
		return response


class CustomerRequestSerializer(serializers.ModelSerializer):

	class Meta:
		model=CustomerRequest
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Medicine']=MedicineSerializer(instance.medicine_details).data
		return response


class CompanyAccountSerializer(serializers.ModelSerializer):

	class Meta:
		model=CompanyAccount
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Company']=CompanySerializer(instance.comapny_id).data
		return response


class CompanyBankSerializer(serializers.ModelSerializer):

	class Meta:
		model=CompanyBank
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Company']=CompanySerializer(instance.comapny_id).data
		return response


class EmployeeBankSerializer(serializers.ModelSerializer):

	class Meta:
		model=EmployeeBank
		fields="__all__"

	def to_representation(self , instance):
		response=super().to_representation(instance)
		response['Employee']=EmployeeSerializer(instance.employee_id).data
		return response

