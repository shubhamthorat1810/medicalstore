from django.db import models

# Create your models here.




class Company(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	license_no=models.CharField(max_length=250)
	address=models.CharField(max_length=250)
	contact_no=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	description=models.CharField(max_length=250)
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class Medicine(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	medical_type=models.CharField(max_length=250)
	buy_price=models.CharField(max_length=250)
	sell_price=models.CharField(max_length=250)
	c_gst=models.CharField(max_length=250)
	s_gst=models.CharField(max_length=250)
	batch_no=models.CharField(max_length=250)
	shelf_no=models.CharField(max_length=250)
	exp_date=models.DateField()
	mfg_date=models.DateField()
	comapny_id=models.ForeignKey(Company,on_delete=models.CASCADE)
	description=models.CharField(max_length=250)
	in_stoc_total=models.IntegerField()
	qty_in_strip=models.IntegerField()
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class MedicalDetails(models.Model):
	id=models.AutoField(primary_key=True)
	medicine_id=models.ForeignKey(Medicine,on_delete= models.CASCADE)
	salt_name=models.CharField(max_length=100)
	salt_qty=models.IntegerField()
	salt_qty_type=models.CharField(max_length=100)
	added_on=models.DateTimeField(auto_now_add=True)
	description=models.CharField(max_length=250)
	objects=models.Manager()


class Employee(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	joining_date=models.DateField()
	phone=models.CharField(max_length=250)
	address=models.CharField(max_length=250)
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class Customer(models.Model):
	id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	address=models.CharField(max_length=250)
	contact=models.CharField(max_length=250)
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class Bill(models.Model):
	id=models.AutoField(primary_key=True)
	customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class EmployeeSalary(models.Model):
	id=models.AutoField(primary_key=True)
	employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
	salary_date=models.DateField()
	salary_amount=models.CharField(max_length=250)
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class BillDetails(models.Model):
	id=models.AutoField(primary_key=True)
	bill_id=models.ForeignKey(Bill,on_delete=models.CASCADE)
	medicine_id=models.ForeignKey(Medicine,on_delete=models.CASCADE)
	qty=models.IntegerField()
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()


class CustomerRequest(models.Model):
	id=models.AutoField(primary_key=True)
	customer_name=models.CharField(max_length=250)
	phone=models.CharField(max_length=250)
	medicine_details=models.ForeignKey(Medicine,on_delete=models.CASCADE)
	status=models.BooleanField(default=False)
	request_date=models.DateField()
	objects=models.Manager()


class CompanyAccount(models.Model):
	choices=((1,"Debit"),(2,"Credit"))
	id=models.AutoField(primary_key=True)
	comapny_id=models.ForeignKey(Company,on_delete=models.CASCADE)
	transaction_type=models.CharField(choices= choices,max_length=250)
	transaction_amount=models.CharField(max_length=250)
	transaction_date=models.DateField()
	payment_mode=models.CharField(max_length=250)
	objects=models.Manager()


class CompanyBank(models.Model):
	id=models.AutoField(primary_key=True)
	bank_account_no=models.CharField(max_length=250)
	ifsc_no=models.CharField(max_length=250)
	comapny_id=models.ForeignKey(Company,on_delete=models.CASCADE)
	objects=models.Manager()


class EmployeeBank(models.Model):
	id=models.AutoField(primary_key=True)
	bank_account_no=models.CharField(max_length=250)
	ifsc_no=models.CharField(max_length=250)
	employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
	added_on=models.DateTimeField(auto_now_add=True)
	objects=models.Manager()






