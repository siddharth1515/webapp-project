from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from voizfonica.models import Admin ,Customer,Prepaidplans,Postpaidplans,Query,DonglePrepaidplans,DonglePostpaidplans,PrepaidRechargeHistory,PrepaidRechargeDongle,Postpaidbroughtplan,DonglePostpaidbroughtplans,Prepaidplansusage
from voizfonica.serializers import AdminSerializer,CustomerSerializer,PrepaidplansSerializer,PostpaidplansSerializer,QuerySerializer,DonglePrepaidplansSerializer,DonglePostpaidplansSerializer,PrepaidplanusageSerializer,PrepaidRechargeHistorySerializer,PrepaidplansSerializer,PrepaidRechargeDongleSerializer,DonglePostpaidbroughtplansSerializer,PostpaidbroughtplanSerializer
from django.contrib.auth import logout
from django.core.mail import send_mail,EmailMessage
from voizfonicatelecom.settings import EMAIL_HOST_USER
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from django.core.files.storage import FileSystemStorage

@csrf_exempt
def addadmin(request):
    if (request.method=="POST"):
        
        mydata=JSONParser().parse(request)
        admin_serialize=AdminSerializer(data=mydata)
        
        if (admin_serialize.is_valid()):
            admin_serialize.save()
            
            return JsonResponse(admin_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getadmin=Admin.objects.filter(username=username,password=password)
    admin_serializer=AdminSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["adminname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'adminview.html',{"data":admin_serializer.data})
    else:
        # return HttpResponse("Invalid Credentials")
        return render(request,'invalidpage.html')


 


def loginviewadmin(request):
    return render(request,"adminlogin.html")



def logout_admin(request):
        logout(request)
        
        template='adminlogin.html'
        return render(request,template)     


################ FAQ #############
def faq(request):
    return render(request,"faq.html")

# @csrf_exempt
# def AddCustomer(request):

#Kanchana implementation

    # if(request.method=="POST"):
    #     # mydata=JSONParser().parse(request)
    #     customer_serialize=CustomerSerializer(data=request.POST)
    #     if(customer_serialize.is_valid()):
    #         customer_serialize.save()
    #         return redirect(viewall)
    #         # return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
    #     else:
    #         return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    # else:
    #     return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)
    
###############################################################################################################
#implementation from userblog preventing duplicate mobile number

    # if (request.method == "POST"):

    #     try:
    #         getCname = request.POST.get("Cname")
    #         getCadhar = request.POST.get("Cadhar")
    #         getCemail = request.POST.get("Cemail")
    #         getCaddress = request.POST.get("Caddress")
    #         getCalternatemobilenumber = request.POST.get("Calternatemobilenumber")
    #         getTypeofcustomer = request.POST.get("Typeofcustomer")
    #         getNewnumber = request.POST.get("Newnumber")
    #         getpassword = request.POST.get("password")
    #         getCustomer = Customer.objects.filter(Newnumber=getNewnumber)
    #         customer_serialiser = CustomerSerializer(getCustomer, many=True)
    #         print(customer_serialiser.data)
    #         if (customer_serialiser.data):
                
    #             return HttpResponse("customer Already Exists")


    #         else:
    #             customer_serialize = CustomerSerializer(data=request.POST)
    #             if (customer_serialize.is_valid()):
    #                 customer_serialize.save()  #Save to Db
    #                 #return redirect(loginview)
    #                 return redirect(viewall)
 
    #             else:
    #                 return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
            
            
    #     except Customer.DoesNotExist:
    #         return HttpResponse("Invalid customername or Password ", status=status.HTTP_404_NOT_FOUND)
    #     except:
    #         return HttpResponse("Something went wrong")


     
        
   

    # else:
    #     return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


################RAKESH IMPLEMENTATION FOR SHOWING PROFILE AND AADHAR DURING VIEWALL,ADDING,UPDATING########
@csrf_exempt
def AddCustomer(request):

    if (request.method == "POST"):

        # try:
        Cname = request.POST.get("Cname")
        Cadhar = request.POST.get("Cadhar")
        Cemail = request.POST.get("Cemail")
        Caddress = request.POST.get("Caddress")
        Calternatemobilenumber = request.POST.get("Calternatemobilenumber")
        Typeofcustomer = request.POST.get("Typeofcustomer")
        Newnumber = request.POST.get("Newnumber")
        password = request.POST.get("password")
        profilephoto=request.FILES['profilephoto']
        aadharphoto=request.FILES['aadharphoto']
        mydata={'Cname':Cname,'Cadhar':Cadhar,'Cemail':Cemail,'Caddress':Caddress,'Calternatemobilenumber':Calternatemobilenumber,'Typeofcustomer':Typeofcustomer,'Newnumber':Newnumber,' password':password,'profilephoto':profilephoto,'aadharphoto':aadharphoto}
        print(mydata)
        
        customer_serialize = CustomerSerializer(data=mydata)
       
        if (customer_serialize.is_valid()):
            customer_serialize.save()  #Save to Db
            return redirect(viewall)

        else:
            return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)





################################################################################################
def register(request):
    return render(request,'register.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewallapi/").json()
    return render(request,'view.html',{"data":fetchdata})

############################################################################################################

@csrf_exempt
def ViewCustomerall(request):
    if(request.method=="GET"):
        customer=Customer.objects.all()
        customer_serializer=CustomerSerializer(customer,many=True)
        return JsonResponse(customer_serializer.data,safe=False)


@csrf_exempt
def ViewCustomer(request,id):
    try:
        c1=Customer.objects.get(id=id)
        if(request.method=="GET"):
            customer_serializer=CustomerSerializer(c1)
            return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            c1.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            c_serial=CustomerSerializer(c1,data=mydata)
            if(c_serial.is_valid()):
                c_serial.save()
                return JsonResponse(c_serial.data,status=status.HTTP_200_OK)

            else:
                return JsonResponse(c_serial.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    except Customer.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)



##################### search
def search_customer(request):
    return render(request,'search.html') 

@csrf_exempt
def searchapi(request):
    try:
        getnumber=request.POST.get("Newnumber")
        getnumbers=Customer.objects.filter(Newnumber=getnumber)
        customer_serialize=CustomerSerializer(getnumbers,many=True)
        return render(request,"search.html",{"data":customer_serialize.data})
    except:   
        return HttpResponse("Invalid Mobile number",status=status.HTTP_404_NOT_FOUND)
##################################

def update(request):
    return render(request,'update.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getnumber=request.POST.get("Newnumber")
        getnumbers=Customer.objects.filter(Newnumber=getnumber)
        customer_serialize=CustomerSerializer(getnumbers,many=True)
        return render(request,"update.html",{"data":customer_serialize.data})
    except Customer.DoesNotExist:   
        return HttpResponse("Invalid Mobile number",status=status.HTTP_404_NOT_FOUND) 
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data_read(request):
    if(request.method=="POST"):

        getId=request.POST.get("newid")

        getcname=request.POST.get("newcname")    
        getcadhar=request.POST.get("newcadhar")
        getcemail=request.POST.get("newcemail")
        getcaddress=request.POST.get("newcaddress")
        getcalternatemobilenumber=request.POST.get("newalternatemobilenumber")
        gettypeofcustomer=request.POST.get("newtypeofcustomer")
        getnewnumber=request.POST.get("newcnumber")
        # getprofilephoto=request.POST.get("newprofilephoto")
        # getaadharphoto=request.POST.get("newaadharphoto")
        
        mydata={'Cname':getcname,'Cadhar':getcadhar,'Cemail':getcemail,'Caddress':getcaddress,'Calternatemobilenumber':getcalternatemobilenumber,'Typeofcustomer':gettypeofcustomer,'Newnumber':getnewnumber}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://127.0.0.1:8000/voizfonica/viewapi/" + getId
        requests.put(ApiLink,data=jsondata)
        return redirect(viewall) 
        #return HttpResponse("data has be updated successfully")

####################### delete

def delete(request):
    return render(request,'delete.html')  

@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/viewapi/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)

@csrf_exempt
def delete_search_api(request):
    try:
        getnumber=request.POST.get("Newnumber")
        getnumbers=Customer.objects.filter(Newnumber=getnumber)
        customer_serialize=CustomerSerializer(getnumbers,many=True)
        return render(request,"delete.html",{"data":customer_serialize.data})
    except:   
        return HttpResponse("Invalid mobile number")

def upload(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'register.html')

def upload_image(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document_image']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'register.html')




################PLANS###################
#### Add Prepaid Plans
@csrf_exempt
def Prepaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        prepaidplans_serialize=PrepaidplansSerializer(data=request.POST)
        if(prepaidplans_serialize.is_valid()):
            prepaidplans_serialize.save()
            return redirect(myViewAllPrepaidplans)
            # return JsonResponse(prepaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


#### Add Postpaid Plan
@csrf_exempt
def Postpaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        postpaidplans_serialize=PostpaidplansSerializer(data=request.POST)
        if(postpaidplans_serialize.is_valid()):
            postpaidplans_serialize.save()
            return redirect(myViewAllPostpaidplans)
            # return JsonResponse(postpaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


#### Viewall Prepaid Plan
@csrf_exempt
def Prepaidplans_List(request):
    if(request.method=="GET"):
        prepaidplan=Prepaidplans.objects.all()
        prepaidplans_serializer=PrepaidplansSerializer(prepaidplan,many=True)
        return JsonResponse(prepaidplans_serializer.data,safe=False)


#### Viewall Postpaid Plan
@csrf_exempt
def Postpaidplans_List(request):
    if(request.method=="GET"):
        postpaidplan=Postpaidplans.objects.all()
        postpaidplans_serializer=PostpaidplansSerializer(postpaidplan,many=True)
        return JsonResponse(postpaidplans_serializer.data,safe=False)

#### Delete Prepaid Plans
@csrf_exempt
def Prepaidplans_Delete(request,id):
    try:
        prepaidplan=Prepaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
                prepaidplan.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Prepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

#### Delete Postpaid Plans
@csrf_exempt
def Postpaidplans_Delete(request,id):
    try:
        postpaidplan=Postpaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
            postpaidplan.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Postpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

#### Delete read Prepaid Plans
@csrf_exempt
def DeleteReadprepaidplans(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_prepaidplans/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPrepaidplans)

#### Delete Search Prepaid plans
@csrf_exempt
def DeleteSearchprepaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getCalls=Prepaidplans.objects.filter(price=getPrice)
        prepaidplans_serializer=PrepaidplansSerializer(getCalls,many=True)
        return render(request,"deletepre.html",{"data":prepaidplans_serializer.data})
        #return JsonResponse(prepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Prepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

#### Delete read Postpaid Plans
@csrf_exempt
def DeleteReadpostpaidplans(request):
    getNewId=request.POST.get("id")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_postpaidplans/" + str(getNewId)
    requests.delete(ApiLink)
    return redirect(myViewAllPostpaidplans)

#### Delete Search Postpaid plans
@csrf_exempt
def DeleteSearchpostpaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getCalls=Postpaidplans.objects.filter(price=getPrice)
        postpaidplans_serializer=PostpaidplansSerializer(getCalls,many=True)
        return render(request,"deletepost.html",{"data":postpaidplans_serializer.data})
        #return JsonResponse(postpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Postpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")



#### Header page
def myHeaderPage(request):
    return render(request,'header.html')

### Register Prepaid Plans
def myPrepaidplans(request):
    return render(request,'prepaidplans.html')

### Register Postpaid Plans
def myPostpaidplans(request):
    return render(request,'postpaidplans.html')

#### Viewall Prepaid plans
def myViewAllPrepaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_prepaidplans/").json()
    return render(request,'viewallpre.html',{"data":fetchdata})

#### Viewall Postpaid plans
def myViewAllPostpaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_postpaidplans/").json()
    return render(request,'viewallpost.html',{"data":fetchdata})

### Delete Prepaid Plans
@csrf_exempt
def myDeleteprepaidplans(request):
    return render(request,'deletepre.html')

### Delete Postpaid Plans
@csrf_exempt
def myDeletepostpaidplans(request):
    return render(request,'deletepost.html')



#### Add Dongle Prepaid Plans
@csrf_exempt
def DonglePrepaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        dongleprepaidplans_serialize=DonglePrepaidplansSerializer(data=request.POST)
        if(dongleprepaidplans_serialize.is_valid()):
            dongleprepaidplans_serialize.save()
            return redirect(myDongleViewAllPrepaidplans)
            # return JsonResponse(dongleprepaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


#### Viewall Dongle Prepaid Plan
@csrf_exempt
def DonglePrepaidplans_List(request):
    if(request.method=="GET"):
        dongleprepaidplan=DonglePrepaidplans.objects.all()
        dongleprepaidplans_serializer=DonglePrepaidplansSerializer(dongleprepaidplan,many=True)
        return JsonResponse(dongleprepaidplans_serializer.data,safe=False)


#### Delete Dongle Prepaid Plans
@csrf_exempt
def DonglePrepaidplans_Delete(request,id):
    try:
        dongleprepaidplan=DonglePrepaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
                dongleprepaidplan.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except DonglePrepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


#### Delete Dongle read Prepaid Plans
@csrf_exempt
def DongleDeleteReadprepaidplans(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_dongleprepaidplans/" + getNewId
    requests.delete(ApiLink)
    return redirect(myDongleViewAllPrepaidplans)


#### Delete Dongle Search Prepaid plans
@csrf_exempt
def DongleDeleteSearchprepaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getData=DonglePrepaidplans.objects.filter(price=getPrice)
        dongleprepaidplans_serializer=DonglePrepaidplansSerializer(getData,many=True)
        return render(request,"dongledeletepre.html",{"data":dongleprepaidplans_serializer.data})
        #return JsonResponse(dongleprepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePrepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


### Register Dongle  Prepaid Plans
def myDonglePrepaidplans(request):
    return render(request,'dongleprepaidplans.html')


#### Viewall Dongle Prepaid plans
def myDongleViewAllPrepaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_dongleprepaidplans/").json()
    return render(request,'dongleviewallpre.html',{"data":fetchdata})


### Delete  Dongle Prepaid Plans
@csrf_exempt
def myDongleDeleteprepaidplans(request):
    return render(request,'dongledeletepre.html')

####################################################

#### Add Dongle Postpaid Plans
@csrf_exempt
def DonglePostpaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        donglepostpaidplans_serialize=DonglePostpaidplansSerializer(data=request.POST)
        if(donglepostpaidplans_serialize.is_valid()):
            donglepostpaidplans_serialize.save()
            return redirect(myDongleViewAllPostpaidplans)
            # return JsonResponse(donglepostpaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

#### Viewall Dongle Postpaid Plan
@csrf_exempt
def DonglePostpaidplans_List(request):
    if(request.method=="GET"):
        donglepostpaidplan=DonglePostpaidplans.objects.all()
        donglepostpaidplans_serializer=DonglePostpaidplansSerializer(donglepostpaidplan,many=True)
        return JsonResponse(donglepostpaidplans_serializer.data,safe=False)

#### Delete Dongle Postpaid Plans
@csrf_exempt
def DonglePostpaidplans_Delete(request,id):
    try:
        donglepostpaidplan=DonglePostpaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
                donglepostpaidplan.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except DonglePostpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

#### Delete Dongle read Postpaid Plans
@csrf_exempt
def DongleDeleteReadpostpaidplans(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_donglepostpaidplans/" + getNewId
    requests.delete(ApiLink)
    return redirect(myDongleViewAllPostpaidplans)

#### Delete Dongle Search Postpaid plans
@csrf_exempt
def DongleDeleteSearchpostpaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getData=DonglePostpaidplans.objects.filter(price=getPrice)
        donglepostpaidplans_serializer=DonglePostpaidplansSerializer(getData,many=True)
        return render(request,"dongledeletepost.html",{"data":donglepostpaidplans_serializer.data})
        #return JsonResponse(donglepostpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePostpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

### Register Dongle Postpaid Plans
def myDonglePostpaidplans(request):
    return render(request,'donglepostpaidplans.html')

#### Viewall Dongle Postpaid plans
def myDongleViewAllPostpaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_donglepostpaidplans/").json()
    return render(request,'dongleviewallpost.html',{"data":fetchdata})

### Delete  Dongle Postpaid Plans
@csrf_exempt
def myDongleDeletepostpaidplans(request):
    return render(request,'dongledeletepost.html')


###########################QUERY#######################################
@csrf_exempt
def AddQuery(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        Query_serialize=QuerySerializer(data=request.POST)
        if(Query_serialize.is_valid()):
            Query_serialize.save()
            #return redirect(myViewAllQuery)
            # return JsonResponse(Query_serialize.data,status=status.HTTP_200_OK)
            return render(request,'successqueryregistered.html')
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

def Successqueryregister(request):
    return render(request,'successqueryregistered.html')

def registerquery(request):
    return render(request,'registerquery.html')

@csrf_exempt
def Query_List(request):
    if(request.method=="GET"):
        q1=Query.objects.all()
        q_serializer=QuerySerializer(q1,many=True)
        return JsonResponse(q_serializer.data,safe=False)

@csrf_exempt
def Query_Delete(request,id):
    try:
        q1=Query.objects.get(id=id)
        if (request.method=="DELETE"):  
                q1.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Query.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def DeleteReadQuery(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/deletequery/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllQuery)

@csrf_exempt
def DeleteSearchQuery(request):
    try:
        getmobile=request.POST.get("mobile")
        getmob=Query.objects.filter(mobile=getmobile)
        q_serializer=QuerySerializer(getmob,many=True)
        return render(request,"deletequery.html",{"data":q_serializer.data})
        #return JsonResponse(prepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Query.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def myDeleteQuery(request):
    return render(request,'deletequery.html')

def myViewAllQuery(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewallq/").json()
    return render(request,'viewallquery.html',{"data":fetchdata})

@csrf_exempt
def Query_Update(request,id):
    q1=Query.objects.get(id=id)
    if (request.method=="PUT"):  
        mydata=JSONParser().parse(request)
        q_serializer=QuerySerializer(q1,data=mydata)
        if(q_serializer.is_valid()):
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(q_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def Query_Search(request,id):
    q1=Query.objects.get(id=id)
    if(request.method=="GET"):    
        q_serializer=QuerySerializer(q1)
        return JsonResponse(q_serializer.data,safe=False,status=status.HTTP_200_OK)


@csrf_exempt
def Search_QueryAPI(request):
    try:
        getMobile=request.POST.get("mobile")
        getName=Query.objects.filter(mobile=getMobile)
        q_serializer=QuerySerializer(getName,many=True)
        return render(request,"searchquery.html",{"data":q_serializer.data})
        #return JsonResponse(q_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Query.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")

def mySearchQuery(request):
    return render(request,'searchquery.html')

#### Update read query
@csrf_exempt
def UpdateReadQuery(request):
    NewId=request.POST.get("newid")
    print(NewId)
    Newname=request.POST.get("newname")
    print(Newname)
    getNewmobile=request.POST.get("newmobile")
    getNewmessage=request.POST.get("newmessage")
    getNewsolution=request.POST.get("newreplymessage")
    mydata={"name":Newname,"mobile":getNewmobile,"message":getNewmessage,"replymessage":getNewsolution}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/voizfonica/updatequery/" + str(NewId)
    requests.put(ApiLink,data=jsondata)
    print(requests.put(ApiLink,data=jsondata))
    return redirect(myViewAllQuery)



##### Update search query
@csrf_exempt
def UpdateSearchQuery(request):
    try:
        getMobile=request.POST.get("newid")
        getName=Query.objects.filter(id=getMobile)
        q_serializer=QuerySerializer(getName,many=True)
        return render(request,"updatequery.html",{"data":q_serializer.data})
        #return JsonResponse(q_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Query.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def myUpdateQuery(request):
    return render(request,'updatequery.html')

#############CUSTOMER HOMEPAGE#############

# Create your views here.
def Home_Page(request):
    return render(request,'home.html')

def mydonglerecharge(request):
    return render(request,'dongleprerecharge.html')    

def About_us(request):
    return render(request,'aboutus.html')
def About_uslogin(request):
    return render(request,'aboutuslogin.html')    

def contact_us(request):
    return render(request,'contact.html')
def contact_uslogin(request):
    return render(request,'contactlogin.html')

###PREPAID RECHARGE
def myprepaidrecharge(request):
    return render(request,'rechargepre.html')



#####PREPAID RECHARGE API
@csrf_exempt
def customerrechargepre(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        prepaidplansusage_serialize=PrepaidplanusageSerializer(data=request.POST)
        if(prepaidplansusage_serialize.is_valid()):
            prepaidplansusage_serialize.save()
            return HttpResponse("RECHARGED SUCCESSFULLY")
            
            #return response.JsonResponse(prepaidplansusage_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def customerlogin_check(request):
    #login check
    try:
        getmobile = request.POST.get("Newnumber")
        getPassword = request.POST.get("password")
        getUsers = Customer.objects.filter(Newnumber=getmobile, password=getPassword)
        user_serialiser = CustomerSerializer(getUsers, many=True)
        print(user_serialiser.data)
        if (user_serialiser.data):
            for i in user_serialiser.data:
                getId = i["id"]
                getName = i["Cname"]
                getmobile= i["Newnumber"]
            request.session['uid'] = getId
            request.session['uname'] = getName
            data={"Cname":getName,"Newnumber":getmobile}

            return  render(request,"customerview.html",{"data":data})
            


        else:
            # return HttpResponse("Invalid Credentials")     
            # return render(request,"home.html")
            return render(request,'invalidcustomerpage.html')     
            
            
    except Customer.DoesNotExist:
        return HttpResponse("Invalid Mobile number or Password ", status=status.HTTP_404_NOT_FOUND)
        # return render(request,'invalidcustomerpage.html')
    except:
        return HttpResponse("Something went wrong")

def loginviewcustomer(request):
    return render(request, 'customerlogin.html')

def logout_user(request):
        logout(request)
        # messages.success(request, ("You Were Logged Out!"))
        template='home.html'
        return render(request,template)     



#### Viewall Prepaid plans for customer
def myViewonlyPrepaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_prepaidplans/").json()
    return render(request,'prepaidviewonly.html',{"data":fetchdata})

#### Viewall Postpaid plans fro customer
def myViewonlyPostpaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_postpaidplans/").json()
    return render(request,'postpaidviewonly.html',{"data":fetchdata})

def myViewonlyPrepaidplanslogin(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_prepaidplans/").json()
    return render(request,'prepaidlogin.html',{"data":fetchdata})

#### Viewall Postpaid plans fro customer
def myViewonlyPostpaidplanslogin(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_postpaidplans/").json()
    return render(request,'postpaidlogin.html',{"data":fetchdata})



###### Update Prepaid plans
@csrf_exempt
def Prepaidplans_Update(request,id):
    prepaidplan=Prepaidplans.objects.get(id=id)
    if (request.method=="PUT"):  
        mydata=JSONParser().parse(request)
        prepaidplans_serialize=PrepaidplansSerializer(prepaidplan,data=mydata)
        if(prepaidplans_serialize.is_valid()):
            prepaidplans_serialize.save()
            return JsonResponse(prepaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(prepaidplans_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

###### Update Postpaid plans
@csrf_exempt
def Postpaidplans_Update(request,id):
    postpaidplan=Postpaidplans.objects.get(id=id)
    if (request.method=="PUT"):  
        mydata=JSONParser().parse(request)
        postpaidplans_serialize=PostpaidplansSerializer(postpaidplan,data=mydata)
        if(postpaidplans_serialize.is_valid()):
            postpaidplans_serialize.save()
            return JsonResponse(postpaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(postpaidplans_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

###### Update Dongle Prepaid plans
@csrf_exempt
def DonglePrepaidplans_Update(request,id):
    dongleprepaidplan=DonglePrepaidplans.objects.get(id=id)
    if (request.method=="PUT"):  
        mydata=JSONParser().parse(request)
        dongleprepaidplans_serialize=DonglePrepaidplansSerializer(dongleprepaidplan,data=mydata)
        if(dongleprepaidplans_serialize.is_valid()):
            dongleprepaidplans_serialize.save()
            return JsonResponse(dongleprepaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(dongleprepaidplans_serialize.errors,status=status.HTTP_400_BAD_REQUEST)


###### Update Dongle Postpaid plans
@csrf_exempt
def DonglePostpaidplans_Update(request,id):
    donglepostpaidplan=DonglePostpaidplans.objects.get(id=id)
    if (request.method=="PUT"):  
        mydata=JSONParser().parse(request)
        donglepostpaidplans_serialize=DonglePostpaidplansSerializer(donglepostpaidplan,data=mydata)
        if(donglepostpaidplans_serialize.is_valid()):
            donglepostpaidplans_serialize.save()
            return JsonResponse(donglepostpaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(donglepostpaidplans_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

#### Update read prepaid
@csrf_exempt
def UpdateReadprepaidplans(request):
    getNewId=request.POST.get("newid")
    getNewprice=request.POST.get("newprice")
    getNewcalls=request.POST.get("newcalls")
    getNewvalidity=request.POST.get("newvalidity")
    getNewdata=request.POST.get("newdata")
    getNewmessages=request.POST.get("newmessages")
    getNewoffers=request.POST.get("newoffers")
    mydata={'price':getNewprice,'calls':getNewcalls,'validity':getNewvalidity,'data':getNewdata,'messages':getNewmessages,'offers':getNewoffers}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/voizfonica/update_prepaidplans/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myViewAllPrepaidplans)
    
##### Update search Prepaid
@csrf_exempt
def UpdateSearchprepaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getCalls=Prepaidplans.objects.filter(price=getPrice)
        prepaidplans_serializer=PrepaidplansSerializer(getCalls,many=True)
        return render(request,"updatepre.html",{"data":prepaidplans_serializer.data})
        #return JsonResponse(prepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Prepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

#### Update read postpaid
@csrf_exempt
def UpdateReadpostpaidplans(request):
    getNewId=request.POST.get("newid")
    getNewprice=request.POST.get("newprice")
    getNewcalls=request.POST.get("newcalls")
    getNewdata=request.POST.get("newdata")
    getNewmessages=request.POST.get("newmessages")
    getNewoffers=request.POST.get("newoffers")
    mydata={'price':getNewprice,'calls':getNewcalls,'data':getNewdata,'messages':getNewmessages,'offers':getNewoffers}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/voizfonica/update_postpaidplans/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myViewAllPostpaidplans)

    
##### Update search Postpaid
@csrf_exempt
def UpdateSearchpostpaidplans(request):
    try:
        getPrice=request.POST.get("id")
        getCalls=Postpaidplans.objects.filter(id=getPrice)
        postpaidplans_serializer=PostpaidplansSerializer(getCalls,many=True)
        return render(request,"updatepost.html",{"data":postpaidplans_serializer.data})
        #return JsonResponse(postpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Postpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

#### Dongle Update read prepaid
@csrf_exempt
def DongleUpdateReadprepaidplans(request):
    getNewId=request.POST.get("newid")
    getNewprice=request.POST.get("newprice")
    getNewdata=request.POST.get("newdata")
    getNewvalidity=request.POST.get("newvalidity")
    getNewoffers=request.POST.get("newoffers")
    mydata={'price':getNewprice,'data':getNewdata,'validity':getNewvalidity,'offers':getNewoffers}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/voizfonica/update_dongleprepaidplans/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myDongleViewAllPrepaidplans)
    
#####  Dongle Update search Prepaid
@csrf_exempt
def DongleUpdateSearchprepaidplans(request):
    try:
        getPrice=request.POST.get("newid")
        getData=DonglePrepaidplans.objects.filter(id=getPrice)
        dongleprepaidplans_serializer=DonglePrepaidplansSerializer(getData,many=True)
        return render(request,"dongleupdatepre.html",{"data":dongleprepaidplans_serializer.data})
        #return JsonResponse(dongleprepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePrepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

#### Dongle Update read postpaid
@csrf_exempt
def DongleUpdateReadpostpaidplans(request):
    getNewId=request.POST.get("newid")
    getNewprice=request.POST.get("newprice")
    getNewdata=request.POST.get("newdata")
    getNewoffers=request.POST.get("newoffers")
    mydata={'price':getNewprice,'data':getNewdata,'offers':getNewoffers}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/voizfonica/update_donglepostpaidplans/" + getNewId
    print(jsondata)
    requests.put(ApiLink,data=jsondata)
    return redirect(myDongleViewAllPostpaidplans)
    
#####  Dongle Update search Postpaid
@csrf_exempt
def DongleUpdateSearchpostpaidplans(request):
    try:
        getPrice=request.POST.get("newid")
        getData=DonglePostpaidplans.objects.filter(id=getPrice)
        donglepostpaidplans_serializer=DonglePostpaidplansSerializer(getData,many=True)
        return render(request,"dongleupdatepost.html",{"data":donglepostpaidplans_serializer.data})
        #return JsonResponse(donglepostpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePostpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


#### Update postpaid html page
def myUpdateprepaidplans(request):
    return render(request,'updatepre.html')


#### Update postpaid html page
def myUpdatepostpaidplans(request):
    return render(request,'updatepost.html')

def dashboard(request):
    return render(request,'dashboard.html')

####  Dongle Update prepaid html page
def myDongleUpdateprepaidplans(request):
    return render(request,'dongleupdatepre.html')


#### Dongle Update postpaid html page
def myDongleUpdatepostpaidplans(request):
    return render(request,'dongleupdatepost.html') 



#### Viewonly Dongle Prepaid plans
def myDongleViewonlyPrepaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_dongleprepaidplans/").json()
    return render(request,'dongleviewonlypre.html',{"data":fetchdata})





#### Viewonly Dongle Postpaid plans
def myDongleViewonlyPostpaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_donglepostpaidplans/").json()
    return render(request,'dongleviewonlypost.html',{"data":fetchdata})       

#### Viewonly Dongle Prepaid plans
def myDongleViewonlyPrepaidplanslogin(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_dongleprepaidplans/").json()
    return render(request,'dongleprelogin.html',{"data":fetchdata})





#### Viewonly Dongle Postpaid plans
def myDongleViewonlyPostpaidplanslogin(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_donglepostpaidplans/").json()
    return render(request,'donglepostlogin.html',{"data":fetchdata})       



#######recharge#################

@csrf_exempt
def PrepaidplansRecharge(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        prepaidplans_serialize=PrepaidRechargeHistorySerializer(data=request.POST)
        if(prepaidplans_serialize.is_valid()):
            prepaidplans_serialize.save()
            # return redirect(myViewAllPrepaidplans)
            # return JsonResponse(prepaidplans_serialize.data,status=status.HTTP_200_OK)
            return render(request,'successpage.html')
        else:
            return HttpResponse(prepaidplans_serialize.errors)




@csrf_exempt
def PrepaiddongleRecharge(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        prepaidplans_serialize=PrepaidRechargeDongleSerializer(data=request.POST)
        if(prepaidplans_serialize.is_valid()):
            prepaidplans_serialize.save()
            # return redirect(myViewAllPrepaidplans)
            #return JsonResponse("RECHARGED SUCCESSFULLY",status=status.HTTP_200_OK,safe=False)
            return render(request,'successdonglerechargepage.html')
            
        else:
            return HttpResponse(prepaidplans_serialize.errors)
            



@csrf_exempt
def UpdateSearchprepaidplansrecharge(request):
    try:
        getPrice=request.POST.get("id")
        getCalls=Prepaidplans.objects.filter(id=getPrice)
        prepaidplans_serializer=PrepaidplansSerializer(getCalls,many=True)
        return render(request,"rechargepre.html",{"data":prepaidplans_serializer.data})
        #return JsonResponse(prepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Prepaidplans.DoesNotExist:
        return HttpResponse("Invalid")


@csrf_exempt
def DongleUpdateSearchprepaiddongle(request):
    try:
        getPrice=request.POST.get("newid")
        getData=DonglePrepaidplans.objects.filter(id=getPrice)
        dongleprepaidplans_serializer=DonglePrepaidplansSerializer(getData,many=True)
        return render(request,"dongleprerecharge.html",{"data":dongleprepaidplans_serializer.data})
    except DonglePrepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


#customer after login


def dashboardview(request):
    return render(request,'customerview.html')



####Postpaidbroughtplan
@csrf_exempt
def Postpaidbroughtplan_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        postpaidbroughtplan_serialize=PostpaidbroughtplanSerializer(data=request.POST)
        if(postpaidbroughtplan_serialize.is_valid()):
            postpaidbroughtplan_serialize.save()
            #return redirect(myViewAllPrepaidplans)
            #return JsonResponse("success",status=status.HTTP_200_OK,safe=False)
            return render(request,'successpostbeforelogin.html')
        else:
            return HttpResponse(postpaidbroughtplan_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


##### Update   Postpaidbroughtplan
@csrf_exempt
def Postpaidbroughtplanapi(request):
    try:
        getPrice=request.POST.get("id")
        getCalls=Postpaidplans.objects.filter(id=getPrice)
        postpaidplans_serializer=PostpaidplansSerializer(getCalls,many=True)
        return render(request,"postpaidbuy.html",{"data":postpaidplans_serializer.data})
        #return JsonResponse(postpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Postpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


def myUpdatepostpaidbuy(request):
    return render(request,'postpaidbuy.html')






#####DonglePostpaidbroughtplan
@csrf_exempt
def DonglePostpaidbroughtplan_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        donglepostpaidbroughtplan_serialize=DonglePostpaidbroughtplansSerializer(data=request.POST)
        if(donglepostpaidbroughtplan_serialize.is_valid()):
            donglepostpaidbroughtplan_serialize.save()
            #return redirect(myViewAllPrepaidplans)
            # return JsonResponse("success",status=status.HTTP_200_OK,safe=False)
            
            return render(request,'successdonglebeforelogin.html')
        else:
            return HttpResponse(donglepostpaidbroughtplan_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


##### Update   Postpaidbroughtplan
@csrf_exempt
def DonglePostpaidbroughtplan(request):
    try:
        getPrice=request.POST.get("id")
        getData=DonglePostpaidplans.objects.filter(id=getPrice)
        donglepostpaidplans_serializer=DonglePostpaidplansSerializer(getData,many=True)
        return render(request,"donglepostpaidbuy.html",{"data":donglepostpaidplans_serializer.data})
        #return JsonResponse(donglepostpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePostpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

def Donglepostpaidbuy(request):
    return render(request,'donglepostpaidbuy.html')

def customeremail(request):
    return render(request,'mail.html')

@csrf_exempt
def send_emailasfile(request):
    message=request.POST.get('message','')
    subject=request.POST.get('subject','')
    mail_id=request.POST.get('email','')
    email=EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id])
    email.content_subtype='html'

    file =request.FILES['file']
    email.attach(file.name,file.read(),file.content_type)

    email.send()
    # return HttpResponse("sent")
    return render(request,'successpagemail.html')



#####################adbill#########################################

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

##################### search
@csrf_exempt
def SearchPostpaidbuy(request,id):
    postpaidbroughtplans=Postpaidbroughtplan.objects.get(id=id)
    if (request.method=="GET"):    
        postpaidbroughtplan_serializer=PostpaidbroughtplanSerializer(postpaidbroughtplans)
        return JsonResponse(postpaidbroughtplan_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def SearchAPIpostpaidbuy(request):
    try:
        getMobilenumber=request.POST.get("mobilenumber")
        getPrice=Postpaidbroughtplan.objects.filter(mobilenumber=getMobilenumber)
        postpaidbroughtplan_serializer=PostpaidbroughtplanSerializer(getPrice,many=True)
        return render(request,"searchpostbuy.html",{"data":postpaidbroughtplan_serializer.data})
        #return JsonResponse(postpaidbroughtplan_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Postpaidbroughtplan.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")

def mySearchpostbuy(request):
    return render(request,'searchpostbuy.html')

##################################


@csrf_exempt
def venue_pdf(request,mobilenumber):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    p=Postpaidbroughtplan.objects.filter(mobilenumber=mobilenumber)    
   
    lines=[]
    for i in p:
        lines.append('\t \t \t \t \t \t \t \t VOIZFONICA TELECOM \t \t \t \t \t \t \t \t')
        lines.append("--------------------------------------------------------")
      
        lines.append('\t \t \t \t  Your Transaction details:')
        lines.append("--------------------------------------------------------")
        
        
       #
        lines.extend(['DATE:'+"     "+i.date])
        lines.extend(['MOBILE NUMBER:'+"      "+i.mobilenumber])
        lines.extend(['PLAN PRICE :'+"     "+i.price])
        
        lines.extend(['CALLS:'+"     "+i.calls])
        lines.extend(['DATA:'+"     "+i.data])
        lines.extend(['EXTRA DATA:'+"     "+i.edata])
        lines.extend(['MESSAGES:'+"     "+i.messages])
        lines.extend(['EXTRA MESSAGES:'+"     "+i.emessages])
        lines.extend(['EXTRA USAGE PRICE:'+"      "+i.eprice])
        lines.extend(['TOTAL PRICE:'+"      "+i.tprice])
        
        
        
       
        lines.append("--------------------------------------------------------")

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='voizfonicapostpaid.pdf')











@csrf_exempt
def DongleSearchPostpaidbuy(request,id):
    donglepostpaidbroughtplans=DonglePostpaidbroughtplan.objects.get(id=id)
    if (request.method=="GET"):    
        donglepostpaidbroughtplan_serializer=DonglePostpaidbroughtplansSerializer(donglepostpaidbroughtplans)
        return JsonResponse(donglepostpaidbroughtplan_serializer.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def DongleSearchAPIpostpaidbuy(request):
    try:
        getMobilenumber=request.POST.get("mobilenumber")
        getPrice=DonglePostpaidbroughtplans.objects.filter(mobilenumber=getMobilenumber)
        donglepostpaidbroughtplan_serializer=DonglePostpaidbroughtplansSerializer(getPrice,many=True)
        return render(request,"donglesearchpostbuy.html",{"data":donglepostpaidbroughtplan_serializer.data})
        #return JsonResponse(donglepostpaidbroughtplan_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePostpaidbroughtplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")


def DonglemySearchpostbuy(request):
    return render(request,'donglesearchpostbuy.html')

@csrf_exempt
def venue_pdf2(request,mobilenumber):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    p=DonglePostpaidbroughtplans.objects.filter(mobilenumber=mobilenumber) 
      
   
    lines=[]
    for i in p:
        lines.append('\t \t \t \t \t \t \t \t VOIZFONICA TELECOM \t \t \t \t \t \t \t \t')
        lines.append("--------------------------------------------------------")
      
        lines.append('\t \t \t \t  Your Transaction details:')
        lines.append("--------------------------------------------------------")
        
        
       #
        lines.extend(['DATE:'+"     "+i.date])
        lines.extend(['MOBILE NUMBER :'+"      "+i.mobilenumber])
        lines.extend(['PRICE :'+"     "+i.price])
        
        lines.extend(['DATA:'+"     "+i.data])
        lines.extend(['EXTRA DATA:'+"     "+i.edata])
        lines.extend(['EXTRA USAGE PRICE:'+"      "+i.eprice])
        lines.extend(['TOTAL PRICE:'+"      "+i.tprice])
        
    
       
        lines.append("--------------------------------------------------------")

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='voizfonicadonglepostpaid.pdf')




##########################pdf for prepaid recharge############################


from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.core.mail import send_mail,EmailMessage
from voizfonicatelecom.settings import EMAIL_HOST_USER


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None



#fd=Prepaidplans.objects.filter(id=4).values()
fd12=PrepaidRechargeHistory.objects.all().values()
fdata12=list(fd12)
for i in fdata12:
    fdatap=i
    print(fdatap)

#Opens up fdata as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf_template.html',fdatap)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pdf_template.html',fdatap)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def index(request):
	context ={}
	return render(request, 'index.html',context)



#######rechargedongle

def render_to_pdf2(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application2/pdf2')
	return None



#fd=Prepaidplans.objects.filter(id=4).values()
fd=PrepaidRechargeDongle.objects.all().values()
fdata1=list(fd)
for i in fdata1:
    
    print(i)

#Opens up fdata as PDF
class ViewPDF2(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf_template2.html',i)
		return HttpResponse(pdf, content_type='application2/pdf2')


#Automaticly downloads to PDF file
class DownloadPDF2(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf2('pdf_template2.html',i)

		response = HttpResponse(pdf, content_type='application2/pdf2')
		filename = "Invoicedongle_%s.pdf" %("1234")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def index22(request):
	contextd ={}
	return render(request, 'index2.html',contextd)




















#### Viewall Postpaid Plan dongle

@csrf_exempt

def buyPostpaidplansdongle_List(request):

    if(request.method=="GET"):

        donglepostpaidbroughtplan1= DonglePostpaidbroughtplans.objects.all()

        donglepostpaidbroughtplan_serializer1=DonglePostpaidbroughtplansSerializer(donglepostpaidbroughtplan1,many=True)

        return JsonResponse(donglepostpaidbroughtplan_serializer1.data,safe=False)

 

def myViewAllPostpaidplansbuydongle(request):

    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/postpaidplansbuydongle_List/").json()

    return render(request,'viewalldonglepostbuy.html',{"data":fetchdata})

 

def myViewpostpaidbuydongle(request):

    return render(request,'viewalldonglepostbuy.html')

 

##update backend donglepostbuy

###### Update Postpaid plans backend

@csrf_exempt

def postpaidplansbuydongle_Update(request,fetchid):

    postpaidplansbuydongle=DonglePostpaidbroughtplans.objects.get(id=fetchid)

    if (request.method=="PUT"):

        mydata=JSONParser().parse(request)

        postpaidplans_serialize=DonglePostpaidbroughtplansSerializer(postpaidplansbuydongle,data=mydata)

        if(postpaidplans_serialize.is_valid()):

            postpaidplans_serialize.save()

            return JsonResponse(postpaidplans_serialize.data,status=status.HTTP_200_OK)

        else:

            return JsonResponse(postpaidplans_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

 

##Upadate Postpaid buy

@csrf_exempt

def UpdateSearchpostpaidplansbuydongle(request):

    try:

        getId=request.POST.get("id")

        getCalls=DonglePostpaidbroughtplans.objects.filter(id=getId)

        postpaidplans_serializer=DonglePostpaidbroughtplansSerializer(getCalls,many=True)

        return render(request,"updatedonglepostbuy.html",{"data":postpaidplans_serializer.data})

        #return JsonResponse(postpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)

    except DonglePostpaidbroughtplans.DoesNotExist:

        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

    except:

        return HttpResponse("Something Wrong")

 

#### Update read postpaid buy

@csrf_exempt

def UpdateReadpostpaidplansbuydongle(request):

    getNewId=request.POST.get("newid")
    print(getNewId)

    getNewdate=request.POST.get("newdate")
    print(getNewdate)
    getNewmobile=request.POST.get("newmobilenumber")
    print(getNewmobile)
    getNewprice=request.POST.get("newprice")
    print( getNewprice)
    
    # getNewcalls=request.POST.get("newcalls")
    # print(getNewcalls)
    getNewdata=request.POST.get("newdata")
    print(getNewdata)
    getNewedata=request.POST.get("newedata")
    print(getNewedata)
    getNeweprice=request.POST.get("neweprice")
    print(getNeweprice)
    getNewtprice=request.POST.get("newtprice")
    print(getNewtprice)
    getNewoffers=request.POST.get("newoffers")
    print(getNewoffers)
    
    mydata={'date':getNewdate,'mobilenumber':getNewmobile,

    'price':getNewprice,'data':getNewdata,'edata':getNewedata,'eprice':getNeweprice,'tprice':getNewtprice,

    'offers':getNewoffers}

    jsondata=json.dumps(mydata)

    ApiLink="http://127.0.0.1:8000/voizfonica/updatebuyapidongle/" +getNewId

    print(jsondata)

    requests.put(ApiLink,data=jsondata)

    return redirect(myViewAllPostpaidplansbuydongle)

 

def myViewpostpaidbuydongleupdate(request):

    return render(request,'updatedonglepostbuy.html')







    




#### Viewall Postpaid Plan

@csrf_exempt

def buyPostpaidplans_List(request):

    if(request.method=="GET"):

        postpaidbroughtplan1=Postpaidbroughtplan.objects.all()

        postpaidbroughtplan_serializer1=PostpaidbroughtplanSerializer(postpaidbroughtplan1,many=True)

        return JsonResponse(postpaidbroughtplan_serializer1.data,safe=False)





def myViewAllPostpaidplansbuy(request):

    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/postpaidplansbuy_List/").json()

    return render(request,'viewallpostbuy.html',{"data":fetchdata})

 

def myViewpostpaidbuy(request):

    return render(request,'viewallpostbuy.html')





###### Update Postpaid plans backend

@csrf_exempt

def postpaidplansbuy_Update(request,fetchid):

    postpaidplansbuy=Postpaidbroughtplan.objects.get(id=fetchid)

    if (request.method=="PUT"):

        mydata=JSONParser().parse(request)

        postpaidplans_serialize=PostpaidbroughtplanSerializer(postpaidplansbuy,data=mydata)

        if(postpaidplans_serialize.is_valid()):

            postpaidplans_serialize.save()

            return JsonResponse(postpaidplans_serialize.data,status=status.HTTP_200_OK)

        else:

            return JsonResponse(postpaidplans_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

 

##Upadate Postpaid buy

@csrf_exempt

def UpdateSearchpostpaidplansbuy(request):

    try:

        getId=request.POST.get("id")

        getCalls=Postpaidbroughtplan.objects.filter(id=getId)

        postpaidplans_serializer=PostpaidbroughtplanSerializer(getCalls,many=True)

        return render(request,"updatepostbuy.html",{"data":postpaidplans_serializer.data})

        #return JsonResponse(postpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)

    except Postpaidbroughtplan.DoesNotExist:

        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

    except:

        return HttpResponse("Something Wrong")

 

#### Update read postpaid buy

@csrf_exempt

def UpdateReadpostpaidplansbuy(request):

    getNewId=request.POST.get("newid")
    print(getNewId)

    getNewdate=request.POST.get("newdate")
    print(getNewdate)

    getNewmobile=request.POST.get("newmobilenumber")
    print(getNewmobile)

    getNewprice=request.POST.get("newprice")
    print( getNewprice)

  

    getNewcalls=request.POST.get("newcalls")
    print(getNewcalls)

    getNewdata=request.POST.get("newdata")
    print(getNewdata)

    getNewedata=request.POST.get("newedata")
    print(getNewedata)

    getNewmessages=request.POST.get("newmessages")
    print(getNewmessages)

    getNewemessages=request.POST.get("newemessages")
    print(getNewemessages)

    getNeweprice=request.POST.get("neweprice")
    print(getNeweprice)

    getNewtprice=request.POST.get("newtprice")
    print(getNewtprice)

    getNewoffers=request.POST.get("newoffers")
    print(getNewoffers)

    

    mydata={'date':getNewdate,'mobilenumber':getNewmobile,

    'price':getNewprice,'calls':getNewcalls,'data':getNewdata,'edata':getNewedata,

    'messages':getNewmessages,'emessages':getNewemessages,'eprice':getNeweprice,'tprice':getNewtprice,'offers':getNewoffers,}

    jsondata=json.dumps(mydata)

    ApiLink="http://127.0.0.1:8000/voizfonica/updatebuyapi/" +getNewId

    print(jsondata)

    requests.put(ApiLink,data=jsondata)

    return redirect(myViewAllPostpaidplansbuy)

 

def myViewpostpaidbuyupdate(request):

    return render(request,'updatepostbuy.html')





############tamil kanchana sindhu implementation for customer postpaid dashboard########################
def Successpostbuy(request):
    return render(request,'successpost.html')

def Successdonglebuy(request):
    return render(request,'successdongle.html')

def Successpostbuybeforelogin(request):
    return render(request,'successpostbeforelogin.html')

def Successdonglebuybeforelogin(request):
    return render(request,'successdonglebeforelogin.html')

@csrf_exempt
def SearchAPIpostpaidcustbuy(request):
    try:
        getMobilenumber=request.POST.get("mobilenumber")
        getPrice=Postpaidbroughtplan.objects.filter(mobilenumber=getMobilenumber)
        postpaidbroughtplan_serializer=PostpaidbroughtplanSerializer(getPrice,many=True)
        return render(request,"searchpostcustbuy.html",{"data":postpaidbroughtplan_serializer.data})
        #return JsonResponse(postpaidbroughtplan_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Postpaidbroughtplan.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")

def mySearchpostcustbuy(request):
    return render(request,'searchpostcustbuy.html')

@csrf_exempt
def DongleSearchAPIpostpaidcustbuy(request):
    try:
        getMobilenumber=request.POST.get("mobilenumber")
        getPrice=DonglePostpaidbroughtplans.objects.filter(mobilenumber=getMobilenumber)
        donglepostpaidbroughtplan_serializer=DonglePostpaidbroughtplansSerializer(getPrice,many=True)
        return render(request,"donglesearchcustpostbuy.html",{"data":donglepostpaidbroughtplan_serializer.data})
        #return JsonResponse(donglepostpaidbroughtplan_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePostpaidbroughtplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Went Wrong")


def DonglemySearchpostcustbuy(request):
    return render(request,'donglesearchcustpostbuy.html')












