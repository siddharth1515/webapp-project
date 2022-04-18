from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

    ############### admin
    path('add/',views.addadmin,name='addadmin'),
    path('loginadmin/',views.login_check,name='login_checkadmin'),
    path('loginadminview/',views.loginviewadmin,name='loginadminview'),




    path('logincustomer/',views.customerlogin_check,name='login_checkcustomer'),
    path('logincustomerview/',views.loginviewcustomer,name='logincustomerview'),
    path('dashboardview/',views.dashboardview,name='dashboardview'),






    path('addapi/',views.AddCustomer,name='AddCustomer'),
    path('viewallapi/',views.ViewCustomerall,name='ViewCustomerall'),
    path('viewapi/<id>',views.ViewCustomer,name='ViewCustomer'),
    path('upload/',views.upload,name='upload'),
    path('upload_image/',views.upload_image,name='upload_image'),



    #####################################################################################################


    path('register/',views.register,name='register'),
    path('searchview/',views.search_customer,name='search_customer'),
    path('search/',views.searchapi,name='searchapi'),
    path('view/',views.viewall,name='viewall'),

    path('update/',views.update,name='update'),
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('update_search_api/',views.update_search_api,name='update_search_api'),

    path('delete_search_api/',views.delete_search_api,name='delete_search_api'),
    path('delete/',views.delete,name='delete'),
    path('delete_api/',views.delete_data_read,name='delete_data_read'),



    ### HTML
    # path('welcome/',views.myHeaderPage,name='myHeaderPage'),

    path('prepaidplans/',views.myPrepaidplans,name='myPrepaidplans'),
    path('postpaidplans/',views.myPostpaidplans,name='myPostpaidplans'),

    path('viewallprepaidplans/',views.myViewAllPrepaidplans,name='myViewAllPrepaidplans'),
    path('viewallpostpaidplans/',views.myViewAllPostpaidplans,name='myViewAllPostpaidplans'),

    path('deleteprepaidplans/',views.myDeleteprepaidplans,name='myDeleteprepaidplans'),
    path('deletepostpaidplans/',views.myDeletepostpaidplans,name='myDeletepostpaidplans'),

    

    #### API 
    path('add_prepaidplans/',views.Prepaidplans_Page,name='Prepaidplans_Page'),
    path('add_postpaidplans/',views.Postpaidplans_Page,name='Postpaidplans_Page'),
    
    path('viewall_prepaidplans/',views.Prepaidplans_List,name='Prepaidplans_List'),
    path('viewall_postpaidplans/',views.Postpaidplans_List,name='Postpaidplans_List'),

    path('delete_prepaidplans/<id>',views.Prepaidplans_Delete,name='Prepaidplans_Delete'),
    path('delete_postpaidplans/<id>',views.Postpaidplans_Delete,name='Postpaidplans_Delete'),

    path('deletereadprepaidplans/',views.DeleteReadprepaidplans,name='Deleteprepaidplans'),
    path('deletereadpostpaidplans/',views.DeleteReadpostpaidplans,name='Deletepostpaidplans'),

    path('delete_prepaidplans/',views.DeleteSearchprepaidplans,name='DeleteSearchprepaidplans'),
    path('delete_postpaidplans/',views.DeleteSearchpostpaidplans,name='DeleteSearchpostpaidplans'),


#############QUERY######################
    path('addquery/',views.AddQuery,name='Addqueryapi'),
    path('deletequery/<id>',views.Query_Delete,name='query_Deleteapi'),
    path('viewallq/',views.Query_List,name='Query_List'),
    path('deletereadquery/',views.DeleteReadQuery,name='DeleteReadquery'),
    path('deletequeries/',views.DeleteSearchQuery,name='DeleteSearchprepaidplans'),
    path('updatequery/<id>',views.Query_Update,name='Query_Update'),
    path('updatereadquery/',views.UpdateReadQuery,name='UpdateReadQuery'),
    path('updatequeries/',views.UpdateSearchQuery,name='UpdateSearchQuery'),
    path('updatequery/',views.myUpdateQuery,name='myUpdateQuerypage'),
    path('registerquery/',views.registerquery,name='registerquerypage'),
    path('viewallqueries/',views.myViewAllQuery,name='myViewAllQuerypage'),
    path('searchquery/',views.mySearchQuery,name='mySearchQuery'),
    path('query_search/',views.Query_Search,name='Query_search'),
    path('searchqueryapi/',views.Search_QueryAPI,name='Search_QueryAPI'),


##########DONGLE HTML##################
    path('dongleprepaidplans/',views.myDonglePrepaidplans,name='myDonglePrepaidplans'),
    path('donglepostpaidplans/',views.myDonglePostpaidplans,name='myDonglePostpaidplans'),

    path('dongleviewallprepaidplans/',views.myDongleViewAllPrepaidplans,name='myDongleViewAllPrepaidplans'),
    path('dongleviewallpostpaidplans/',views.myDongleViewAllPostpaidplans,name='myDongleViewAllPostpaidplans'),

    path('dongledeleteprepaidplans/',views.myDongleDeleteprepaidplans,name='myDongleDeleteprepaidplans'),
    path('dongledeletepostpaidplans/',views.myDongleDeletepostpaidplans,name='myDongleDeletepostpaidplans'),





#####DONGLE API#################
    path('add_dongleprepaidplans/',views.DonglePrepaidplans_Page,name='DonglePrepaidplans_Page'),
    path('add_donglepostpaidplans/',views.DonglePostpaidplans_Page,name='DonglePostpaidplans_Page'),

    path('viewall_dongleprepaidplans/',views.DonglePrepaidplans_List,name='DonglePrepaidplans_List'),
    path('viewall_donglepostpaidplans/',views.DonglePostpaidplans_List,name='DonglePostpaidplans_List'),
 
    path('delete_dongleprepaidplans/<id>',views.DonglePrepaidplans_Delete,name='DonglePrepaidplans_Delete'),
    path('delete_donglepostpaidplans/<id>',views.DonglePostpaidplans_Delete,name='DonglePostpaidplans_Delete'),

    path('dongledeletereadprepaidplans/',views.DongleDeleteReadprepaidplans,name='DongleDeleteprepaidplans'),
    path('dongledeletereadpostpaidplans/',views.DongleDeleteReadpostpaidplans,name='DongleDeletepostpaidplans'),

    path('dongledelete_prepaidplans/',views.DongleDeleteSearchprepaidplans,name='DongleDeleteSearchprepaidplans'),
    path('dongledelete_postpaidplans/',views.DongleDeleteSearchpostpaidplans,name='DongleDeleteSearchpostpaidplans'),




    ##############CUSTOMER HOMPAGE URLS#####################3
    path('home/',views.Home_Page,name='Home_Page'),
    path('contactus/',views.contact_us,name='contact_us'),
    path('aboutus/',views.About_us,name='about_us'),
    path('contactuslogin/',views.contact_uslogin,name='contact_uslogin'),
    path('aboutuslogin/',views.About_uslogin,name='about_uslogin'),


    path('rechargeprepaidplans/',views.customerrechargepre,name='customerrechargepre'),
    path('rechargeprepaid/',views.myprepaidrecharge,name='myprepaidrecharge'),

    path('prepaidviewonly/',views.myViewonlyPrepaidplans,name='myprepaidrecharge'),
    path('postpaidviewonly/',views.myViewonlyPostpaidplans,name='myprepaidrecharge'),

    path('prepaidviewonlylogin/',views.myViewonlyPrepaidplanslogin,name='myprepaidrechargelogin'),
    path('postpaidviewonlylogin/',views.myViewonlyPostpaidplanslogin,name='myprepaidrechargelogin'),




    path('logout/',views.logout_user,name='logout_user'),
    path('logoutadmin/',views.logout_admin,name='logout_admin'),




    ##### update prepaid postpaid dongle (API)
    path('update_prepaidplans/<id>',views.Prepaidplans_Update,name='Prepaidplans_Update'),
    path('update_postpaidplans/<id>',views.Postpaidplans_Update,name='Postpaidplans_Update'),

    path('update_dongleprepaidplans/<id>',views.DonglePrepaidplans_Update,name='DonglePrepaidplans_Update'),
    path('update_donglepostpaidplans/<id>',views.DonglePostpaidplans_Update,name='DonglePostpaidplans_Update'),

    path('updatereadprepaidplans/',views.UpdateReadprepaidplans,name='Updateprepaidplans'),
    path('updatereadpostpaidplans/',views.UpdateReadpostpaidplans,name='Updatepostpaidplans'),

    path('update_prepaidplan/',views.UpdateSearchprepaidplans,name='UpdateSearchprepaidplans'),
    path('update_postpaidplan/',views.UpdateSearchpostpaidplans,name='UpdateSearchpostpaidplans'),

    path('dongleupdatereadprepaidplans/',views.DongleUpdateReadprepaidplans,name='DongleUpdateprepaidplans'),
    path('dongleupdatereadpostpaidplans/',views.DongleUpdateReadpostpaidplans,name='DongleUpdatepostpaidplans'),

    path('dongleupdate_prepaidplans/',views.DongleUpdateSearchprepaidplans,name='DongleUpdateSearchprepaidplans'),
    path('dongleupdate_postpaidplans/',views.DongleUpdateSearchpostpaidplans,name='DongleUpdateSearchpostpaidplans'),


    ##### update pre post dongle (HTML)
    path('updateprepaidplans/',views.myUpdateprepaidplans,name='myUpdateprepaidplans'),
    path('updatepostpaidplans/',views.myUpdatepostpaidplans,name='myUpdatepostpaidplans'),

    path('dongleupdateprepaidplans/',views.myDongleUpdateprepaidplans,name='myDongleUpdateprepaidplans'),
    path('dongleupdatepostpaidplans/',views.myDongleUpdatepostpaidplans,name='myDongleUpdatepostpaidplans'),



    path('donglepostpaidviewonly/',views.myDongleViewonlyPostpaidplans,name='mypostpaidviewonlydongle'),
    path('dongleprepaidviewonly/',views.myDongleViewonlyPrepaidplans,name='myprepaidviewonlydongle'),


    path('donglepostpaidviewonlylogin/',views.myDongleViewonlyPostpaidplanslogin,name='mypostpaidviewonlydonglelogin'),
    path('dongleprepaidviewonlylogin/',views.myDongleViewonlyPrepaidplanslogin,name='myprepaidviewonlydonglelogin'),


    path('dashboard/',views.dashboard,name='dashboard'),





#############recharge################
    path('prepaidrecharge2/',views.PrepaidplansRecharge,name="PrepaidpalnsRecharge"),
    path('recharge2/',views.UpdateSearchprepaidplansrecharge,name='UpdateSearchprepaidplansrecharge'),


##dongle rechargre
    path('rechargedongle/',views.mydonglerecharge,name='mydonglerecharge'),
    path('prepaidrechargedongle/',views.PrepaiddongleRecharge,name="PrepaiddongleRecharge"),
    path('rechargedongleplans/',views.DongleUpdateSearchprepaiddongle,name='DongleUpdateSearchprepaiddongle'),


####### Buy  plans post,update,html

    path('postpaidbroughtplan_page/',views.Postpaidbroughtplan_Page,name='Postpaidbroughtplan_Page'),
    path('postpaidbroughtplan/',views.Postpaidbroughtplanapi,name='Postpaidbroughtplan'),
    path('myupdatepostpaidbuy/',views.myUpdatepostpaidbuy,name='myUpdatepostpaidbuy'),



####### Buy dongle plans post,update,html

    path('donglepostpaidbroughtplan_page/',views.DonglePostpaidbroughtplan_Page,name='DonglePostpaidbroughtplan_Page'),
    path('donglepostpaidbroughtplan/',views.DonglePostpaidbroughtplan,name='DonglePostpaidbroughtplan'),
    path('Donglepostpaidbuy/',views.Donglepostpaidbuy,name='Donglepostpaidbuy'),
    

    path('emailapi/',views.send_emailasfile,name='send_emailasfile'),
    path('customeremail/',views.customeremail,name='customeremail'),


   
###################################     bills
    # path('pdf/<Newnumber>',views.venue_pdf,name='pdfview'),
    # path('searchbill/',views.searchapibill,name='searchapi'),
    # path('searchviewbill/',views.search_customerbill,name='search_customerpage'),


    ###########pdf
	# path('', views.index),
    # path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('pdf_download2/', views.DownloadPDF2.as_view(), name="pdf_download2"),


############################ TAMIL IMPLEMENTATION TO SEARCH BILL URL ########################

    path('pdf/<mobilenumber>',views.venue_pdf,name='pdfview1'),
    path('searchapipostpaidbuy/',views.SearchAPIpostpaidbuy,name='SearchAPIpostpaidbuy'),
    path('mysearchpostbuy/',views.mySearchpostbuy,name='mySearchpostbuy'),
    
    
    path('searchpostpaidbuy/',views.SearchPostpaidbuy,name='SearchPostpaidbuy'),
    
    

    path('pdf2/<mobilenumber>',views.venue_pdf2,name='pdfview2'),
    path('donglesearchapipostpaidbuy/',views.DongleSearchAPIpostpaidbuy,name='DongleSearchAPIpostpaidbuy'),
    path('donglemysearchpostbuy/',views.DonglemySearchpostbuy,name='DonglemySearchpostbuy'),

    path('donglesearchpostpaidbuy/',views.DongleSearchPostpaidbuy,name='DongleSearchPostpaidbuy'),

############################ TAMIL IMPLEMENTATION TO SEARCH BILL URL ENDED ######################## 


    path('postpaidplansbuy_List/',views.buyPostpaidplans_List,name='buyPostpaidplans_List'),
    path('myviewallpostpaidplansbuy/',views.myViewAllPostpaidplansbuy,name='myViewAllPostpaidplansbuy'),
    path('myviewpostpaidbuy/',views.myViewpostpaidbuy,name='myViewpostpaidbuy'),
    path('updatebuy/',views.myViewpostpaidbuyupdate,name='myViewpostpaidbuyupdate'),
    path('updateReadpostbuy/',views.UpdateReadpostpaidplansbuy,name='UpdateReadpostpaidplansbuy'),
    path('updatesearchpostbuy/',views.UpdateSearchpostpaidplansbuy,name='UpdateSearchpostpaidplansbuy'),
    path('updatebuyapi/<fetchid>',views.postpaidplansbuy_Update,name='postpaidplansbuy_Update'),





##for admin postbuy ,view buyplan postpaid dongle

    path('postpaidplansbuydongle_List/',views.buyPostpaidplansdongle_List,name='buyPostpaidplansdongle_List'),
    path('myviewallpostpaidplansbuydongle/',views.myViewAllPostpaidplansbuydongle,name='myViewAllPostpaidplansbuydongle'),
    path('myviewpostpaidbuydongle/',views.myViewpostpaidbuydongle,name='myViewpostpaidbuydongle'),

##### update buyplan postpaid dongle

    path('updatebuydongle/',views.myViewpostpaidbuydongleupdate,name='myViewpostpaidbuydongleupdate'),
    path('updateReadpostbuydongle/',views.UpdateReadpostpaidplansbuydongle,name='UpdateReadpostpaidplansbuydongle'),
    path('updatesearchpostbuydongle/',views.UpdateSearchpostpaidplansbuydongle,name='UpdateSearchpostpaidplansbuydongle'),
    path('updatebuyapidongle/<fetchid>',views.postpaidplansbuydongle_Update,name='postpaidplansbuydongle_Update'),


#################tamil kanchana sindhu implementation for customer postpaid dashboard##
    path('successpostbuy/',views.Successpostbuy,name='Successpostbuy'),
    path('successdonglebuy/',views.Successdonglebuy,name='Successdonglebuy'),

    path('searchapipostpaidcustbuy/',views.SearchAPIpostpaidcustbuy,name='SearchAPIpostpaidcustbuy'),
    path('mysearchpostcustbuy/',views.mySearchpostcustbuy,name='mySearchpostcustbuy'),

    path('donglesearchapipostpaidcustbuy/',views.DongleSearchAPIpostpaidcustbuy,name='DongleSearchAPIpostpaidcustbuy'),
    path('donglemysearchpostcustbuy/',views.DonglemySearchpostcustbuy,name='DonglemySearchpostcustbuy'),


############################################ FAQ ###############################
    path('faq/',views.faq,name='faq'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)