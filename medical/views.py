from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from medical.models import Company , CompanyBank ,Medicine , MedicalDetails
from medical.serializers import CompanySerializer , CompanyBankSerializer , MedicineSerializer , MedicalDetailsSerializerSimple , MedicalDetailsSerializer



class CompanyViewSet(viewsets.ViewSet):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	# queryset=Company.objects.all()
	# serializer_class=CompanySerializer

	def list(self,request):
		company=Company.objects.all()
		serializer=CompanySerializer(company,many=True,context={"request":request})
		response_dict={"error":"False","message":"All company list done " ,"data":serializer.data}
		return Response(response_dict)


	def create(self,request):
		try:
			serializer=CompanySerializer(data=request.data,context={"request":request})
			serializer.is_valid()
			serializer.save()
			dict_response={"error":"False","message":"company data save succesfully "}
		except:
			dict_response={"error":"True","message":"error during data save "}
		return Response(dict_response)


	def update(self,request,pk=None):
		try:
			queryset=Company.objects.all()
			company=get_object_or_404(queryset,pk=pk)
			serializer=CompanySerializer(company,data=request.data,context={"request":request})
			serializer.is_valid()
			serializer.save()
			dict_response={"error":"False","message":"company data updated succesfully "}
		except:
			dict_response={"error":"True","message":serializer.error}

		return Response(dict_response)



company_list=CompanyViewSet.as_view({"get","list"})
company_create=CompanyViewSet.as_view({"post","create"})
company_update=CompanyViewSet.as_view({"put","update"})


class CompanyBankViewSet(viewsets.ViewSet):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def list(self,request):
		company_bank=CompanyBank.objects.all()
		serializer=CompanyBankSerializer(company_bank,many=True,context={"request":request})
		response_dict={"error":"False","message":"All company bank list done " ,"data":serializer.data}
		return Response(response_dict)

	def create(self,request):
		try:
			serializer=CompanyBankSerializer(data=request.data,context={"request":request})
			serializer.is_valid(raise_exception=True)
			serializer.save()
			dict_response={"error":"False","message":"company bank data save succesfully "}
		except:
			dict_response={"error":"True","message":"error during company bank data save "}
		return Response(dict_response)

	def retrieve(self,request,pk=None):
		queryset=CompanyBank.objects.all()
		company_bank=get_object_or_404(queryset,pk=pk)
		serializer=CompanyBankSerializer(company_bank,context={"request":request})
		dict_response={"error":"False","message":"single company bank data fetch ", "data":serializer.data}
		return Response(dict_response)
		

	def update(self,request,pk=None):
		try:
			queryset=CompanyBank.objects.all()
			company_bank=get_object_or_404(queryset,pk=pk)
			serializer=CompanyBankSerializer(company_bank,data=request.data,context={"request":request})
			serializer.is_valid(raise_exception=True)
			serializer.save()
			dict_response={"error":"False","data":"company bank data succesfully updated"}
		except:
			dict_response={"error":"False","data":"fail to company bank data update"}
		return Response (dict_response)


class CompanyNameViewSet(generics.ListAPIView):

	serializer_class=CompanySerializer

	def get_queryset(self):
		name=self.kwargs["name"]
		return Company.objects.filter(name=name)



class MedicineViewSet(viewsets.ViewSet):

	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def list(self,request):
		medicine=Medicine.objects.all()
		serializer=MedicineSerializer(medicine,many=True)
		
		medicine_data=serializer.data
		newmedicinelist=[]

		# adding extra key for medicine details in medicine
		for medicine in medicine_data:
			# accessing all the  medicine details of  current medicine id
			medicine_details=MedicalDetails.objects.filter(medicine_id=medicine["id"])
			# print(medicine_details)
			medicine_details_serializer=MedicalDetailsSerializerSimple(data=medicine_details,many=True)
			medicine_details_serializer.is_valid()
			# print(medicine_details_serializer)
			medicine["medicine_details"]=medicine_details_serializer.data
			newmedicinelist.append(medicine)

		# print(newmedicinelist)	
		response_dict={"error":"False","message":"All medicine list done " ,"data":newmedicinelist}
		return Response(response_dict)

	def create(self,request):
		try:
			serializer=MedicineSerializer(data=request.data,context={"request":request})
			print("2222222222")
			serializer.is_valid(raise_exception=True)
			serializer.save()
			print("1111")
			# access the serializer id which is saved in the database
			medicine_id=serializer.data['id'];
			print(medicine_id)

			# adding and saving id into medicine details table
			medicine_details_list=[]
			for medicine_detail in request.data["medicine_details"]:
				# print(medicine_detail)
				# adding medicine id which will work for medicine details serializer
				medicine_detail['medicine_id']=medicine_id
				medicine_details_list.append(medicine_detail)
				print(medicine_detail)
			serializer2=MedicalDetailsSerializer(data=medicine_details_list,many=True)
			serializer2.is_valid(raise_exception=True)
			serializer2.save()		

			dict_response={"error":"False","message":"medicine data save succesfully ", "data":serializer2.data}
		except Exception as e:
			print(e)
			dict_response={"error":"True","message":"error during medicine data save "}
		return Response(dict_response)

	def retrieve(self,request,pk=None):
		
		queryset=Medicine.objects.all()
		medicine=get_object_or_404(queryset,pk=pk)
		serializer=MedicineSerializer(medicine,context={"request":request})
		print(serializer.data)
		# serializer_data=serializer.data
		# medicine_details=MedicalDetails.objects.filter(medicine_id=serializer_data["id"])
		# medicine_details_serializer=MedicalDetailsSerializerSimple(data=medicine_details,many=True)
		# serializer_data["medicine_details"]=medicine_details_serializer.data


		dict_response={"error":"False","message":"single medicine data fetch ", "data":serializer.data}
		return Response(dict_response)
		

	def update(self,request,pk=None):
		try:
			queryset=Medicine.objects.all()
			medicine=get_object_or_404(queryset,pk=pk)
			serializer=MedicineSerializer(medicine,data=request.data,context={"request":request})
			serializer.is_valid(raise_exception=True)
			serializer.save()
			dict_response={"error":"False","data":"medicine data succesfully updated"}
		except:
			dict_response={"error":"False","data":"fail to Medicine data update"}
		return Response (dict_response)



