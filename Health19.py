from tkinter import *
from tkinter import messagebox
import requests 
import json
import webbrowser
import yagmail
global data,res


def english():
    rootm.destroy()
    states=[]
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    state2=data['region']
    state3=state2.lower()

    res1 = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    data1 = res1.json()
    res2=requests.get('https://api.rootnet.in/covid19-in/contacts')
    data2=res2.json()
    for i in range(0,32):
            
            state=(data1['data']['regional'][i]['loc'])
            state=state.lower()
            states.append(state)
            if state3 in states:
                o=states.index(state3)
                num=(data2['data']['contacts']['regional'][o]['number'])
        
    state1='Helpline number according to your location(state-number): '+state2+'-'+num
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'


    
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
      req_params = {
      'apikey':apiKey,
      'secret':secretKey,
      'usetype':useType,
      'phone': phoneNo,
      'message':textMessage,
      'senderid':senderId
      }
      return requests.post(reqUrl, req_params)
    def schemew():
        webbrowser.open('https://wcd.nic.in/schemes-listing/2405')
    def scheme():
        webbrowser.open('https://www.nhp.gov.in/national-health-insurance-schemes_pg')
    def schemec():
        webbrowser.open('https://nhm.gov.in/index1.php?lang=1&level=3&sublinkid=1179&lid=363')
    def schemes():
        webbrowser.open('https://www.thebetterindia.com/192312/government-scheme-senior-citizen-pension-investment-income-india/')
    def hospitals():
        

        webbrowser.open('https://www.google.com/search?rlz=1C1EJFC_enIN891IN891&sxsrf=ALeKk02pZ88S2rvsWQgrMD67L-RREddarA:1588345829020&q=hospitals+near+me&spell=1&sa=X&ved=2ahUKEwiZ-6yn-ZLpAhXJxzgGHR9bADwQBSgAegQIDxAn&biw=1920&bih=920')
    def chemists():
        webbrowser.open('https://www.google.com/search?q=chemists+near+me&rlz=1C1EJFC_enIN891IN891&oq=chemists+&aqs=chrome.0.0l2j69i57j0l5.5322j0j9&sourceid=chrome&ie=UTF-8')
    def pathology():
        webbrowser.open('https://www.google.com/search?q=pathology+labs+near+me&rlz=1C1EJFC_enIN891IN891&oq=patholo&aqs=chrome.1.69i57j0l7.7053j0j9&sourceid=chrome&ie=UTF-8')
    def free():
        webbrowser.open('https://www.google.com/search?q=free+health+camps+near+me&rlz=1C1EJFC_enIN891IN891&oq=free+health+camps+near+me&aqs=chrome..69i57j0.11456j0j9&sourceid=chrome&ie=UTF-8')


    def statemap():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona '
        webbrowser.open("https://maps.mapmyindia.com/corona")
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
    def treat():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_treatment_centre  '
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_treatment_centre")
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 
    def dist():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?districts_containment_zone  '
        webbrowser.open("https://maps.mapmyindia.com/corona?districts_containment_zone")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 
    def sample():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_sample_collection_centre  '
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_sample_collection_centre")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def testing():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_testing_centre '
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_testing_centre")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def isolation():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_isolation_ward '
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_isolation_ward")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def containment():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?containment_zone_gradient'
        webbrowser.open("https://maps.mapmyindia.com/corona?containment_zone_gradient")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 


    def lockissue():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?issues-nearby'
        webbrowser.open("https://maps.mapmyindia.com/corona?issues-nearby")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def hunger():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?hunger-relief-centers'
        webbrowser.open("https://maps.mapmyindia.com/corona?hunger-relief-centers")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def shelter():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?food-shelter-homes'
        webbrowser.open("https://maps.mapmyindia.com/corona?food-shelter-homes")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    root=Tk()
    root.title("Health19+")
    root.geometry("1920x1080")
    root.configure(background="black")
    root.resizable(0,0)
    em,sms=IntVar(),IntVar()



    l1=Label(root,text="- - - - Health19+ - - - -",font=('Quantum',20,"bold","underline"),fg='Steelblue2',bg="black")
    l1.pack()

    e1=Entry(root)
    
    e1.pack(pady=30)
    
    le1=Label(root,text='Phone number!->',font=('Arial',10,"bold"),fg='light green',bg="black")
    le1.place(x=700,y=65)
    
    g1=Label(root,text='Government health schemes',font=('Arial',15,"bold"),fg='light green',bg="black")
    g1.place(x=180,y=50)
    f1=Label(root,text='Health Facilities',font=('Arial',15,"bold"),fg='light green',bg="black")
    f1.place(x=1550,y=50)
    bg1=Button(root,text='Schemes for All',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=scheme)
    bg1.place(x=230,y=100)
    bg2=Button(root,text='Schemes for Children',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=schemec)
    bg2.place(x=200,y=150)
    bg3=Button(root,text='Schemes for Women',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=schemew)
    bg3.place(x=202,y=200)
    bg4=Button(root,text='Schemes for Senior Citizens',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=schemes)
    bg4.place(x=170,y=250)
    bf1=Button(root,text='Hospitals Near me',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=hospitals)
    bf1.place(x=1530,y=100)
    bf2=Button(root,text='Chemists Near me',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=chemists)
    bf2.place(x=1530,y=150)
    bf3=Button(root,text='Pathology labs',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=pathology)
    bf3.place(x=1545,y=200)
    bf4=Button(root,text='Free health camps',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=free)
    bf4.place(x=1530,y=250)
    cov=Label(root,text='- - - - Covid-19 Dashboard - - - -',font=('Arial',20,"bold"),fg='Steelblue2',bg="black")
    cov.pack(pady=150)
    cov1=Button(root,text='State Updates',font=('Arial',15,"bold"),fg='green4',bg="black",command=statemap)
    cov1.place(x=230,y=525)
    cov2=Button(root,text='Districtwise zones',font=('Arial',15,"bold"),fg='green4',bg="black",command=dist)
    cov2.pack(pady=2)
    cov3=Button(root,text='Treatment centres',font=('Arial',15,"bold"),fg='green4',bg="black",command=treat)
    cov3.place(x=1530,y=525)
    cov4=Button(root,text='Sample collection',font=('Arial',15,"bold"),fg='green3',bg="black",command=sample)
    cov4.place(x=230,y=600)
    cov5=Button(root,text='Testing Labs',font=('Arial',15,"bold"),fg='green3',bg="black",command=testing)
    cov5.pack(pady=35)
    cov6=Button(root,text='Isolation centres',font=('Arial',15,"bold"),fg='green3',bg="black",command=isolation)
    cov6.place(x=1545,y=600)
    cov7=Button(root,text='Containment zones',font=('Arial',15,"bold"),fg='green2',bg="black",command=containment)
    cov7.place(x=230,y=675)
    cov8=Button(root,text='  Hunger relief centres  ',font=('Arial',15,"bold"),fg='green2',bg="black",command=hunger)
    cov8.pack(pady=2)
    cov9=Button(root,text='Lockdown issues',font=('Arial',15,"bold"),fg='green2',bg="black",command=shelter)
    cov9.place(x=1540,y=675)
    covl1=Label(root,text=state1,font=('Arial',20,"bold"),fg='Steelblue2',bg="black")
    covl1.place(x=50,y=800)
    root.mainloop()
def hindi():
    rootm.destroy()
    states=[]
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    state2=data['region']
    state3=state2.lower()

    res1 = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    data1 = res1.json()
    res2=requests.get('https://api.rootnet.in/covid19-in/contacts')
    data2=res2.json()
    for i in range(0,32):
            
            state=(data1['data']['regional'][i]['loc'])
            state=state.lower()
            states.append(state)
            if state3 in states:
                o=states.index(state3)
                num=(data2['data']['contacts']['regional'][o]['number'])
        
    state1='हेल्‍पलाइन नंबर : '+state2+'-'+num
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'


    
      
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
      req_params = {
      'apikey':apiKey,
      'secret':secretKey,
      'usetype':useType,
      'phone': phoneNo,
      'message':textMessage,
      'senderid':senderId
      }
      return requests.post(reqUrl, req_params)
    def schemew():
        webbrowser.open('https://nhm.gov.in/message.php?lang=2')
    def scheme():
        webbrowser.open('https://hi.nhp.gov.in/hindi-national-health-insurance-schemes_pg')
    def schemec():
        webbrowser.open('https://nhm.gov.in/index1.php?lang=1&level=3&sublinkid=1179&lid=363')
    def schemes():
        webbrowser.open('https://www.thebetterindia.com/192312/government-scheme-senior-citizen-pension-investment-income-india/')
    def hospitals():
        
        webbrowser.open('https://www.google.com/search?sxsrf=ALeKk006LfqfAGjU7xYHVgp3R9nwESvXZw%3A1588347032141&source=hp&ei=mECsXqbVBvyP4-EPo72vwAk&q=hospitals+near+me&btnK=Google+%E0%A4%B8%E0%A4%B0%E0%A5%8D%E0%A4%9A')
    def chemists():
        webbrowser.open('https://www.google.com/search?sxsrf=ALeKk03-_WIQ9aNr6GS8_x1rd38GSksMRg%3A1588347058548&ei=skCsXpuIIY-C4-EP96uTyA8&q=chemists+near+me&oq=chemists+near+me&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBUOfqBFiClgVggZwFaABwAHgAgAGjBYgB9QmSAQM1LTKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwibqdHx_ZLpAhUPwTgGHffVBPkQ4dUDCAw&uact=5')
    def pathology():
        webbrowser.open('https://www.google.com/search?sxsrf=ALeKk02WljbUKoyuOAvGVb4xZ2RWsHN67w%3A1588347197214&ei=PUGsXv3cDKSL4-EPv72gqA8&q=pathology+near+me+open+today&oq=pathology+near+me&gs_lcp=CgZwc3ktYWIQARgBMgQIIxAnMgUIABDLATIGCAAQBxAeMgUIABDLATIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHlAAWABg0zpoAHAAeACAAdECiAGFBJIBBzAuMS4wLjGYAQCqAQdnd3Mtd2l6&sclient=psy-ab')
    def free():
        webbrowser.open('https://www.google.com/search?sxsrf=ALeKk01os-ZmBVJN0b5QOyZMK_g9tQ2TAg%3A1588347209366&ei=SUGsXvf3FfSb4-EPtpy68Ak&q=free+health+camps+near+me&oq=&gs_lcp=CgZwc3ktYWIQARgEMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnOgQIIxAnOgYIABAHEB46BggAEBYQHjoECAAQQzoCCAA6BggAEAoQQ1Dk5AFYpvcBYKuRAmgBcAB4AYABhgaIAbgWkgENMC4yLjMuMC4xLjEuMZgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab')


    def statemap():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona '
        webbrowser.open("https://maps.mapmyindia.com/corona")
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
    def treat():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_treatment_centre  '
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_treatment_centre")
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 
    def dist():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?districts_containment_zone  '
        webbrowser.open("https://maps.mapmyindia.com/corona?districts_containment_zone")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 
    def sample():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_sample_collection_centre  '
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_sample_collection_centre")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def testing():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_testing_centre '
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_testing_centre")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def isolation():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?corona_isolation_ward '
        webbrowser.open("https://maps.mapmyindia.com/corona?corona_isolation_ward")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def containment():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?containment_zone_gradient'
        webbrowser.open("https://maps.mapmyindia.com/corona?containment_zone_gradient")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 


    def lockissue():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?issues-nearby'
        webbrowser.open("https://maps.mapmyindia.com/corona?issues-nearby")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def hunger():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?hunger-relief-centers'
        webbrowser.open("https://maps.mapmyindia.com/corona?hunger-relief-centers")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    def shelter():
        number=e1.get()
        message1='Get updates here: https://maps.mapmyindia.com/corona?food-shelter-homes'
        webbrowser.open("https://maps.mapmyindia.com/corona?food-shelter-homes")
        sendPostRequest(URL, 'OKVA4IY8L1PKILDEWWIPWYOJJRSRRDGN', '5RE3KC1APRY7TRDZ', 'stage', number, 'leo', message1 )
        yag.send(to=e2.get(), subject='Health19+', contents=message1) 

    root=Tk()
    root.title("Health19+")
    root.geometry("1920x1080")
    root.configure(background="black")
    root.resizable(0,0)
    em,sms=IntVar(),IntVar()



    l1=Label(root,text="- - - - Health19+ - - - -",font=('Quantum',20,"bold","underline"),fg='Steelblue2',bg="black")
    l1.pack()

    e1=Entry(root)
    
    e1.pack(pady=30)
    
    le1=Label(root,text='फोन नंबर->',font=('Arial',10,"bold"),fg='light green',bg="black")
    le1.place(x=700,y=65)
    
    g1=Label(root,text=' स्‍वास्‍थ्‍य योजनाएं -:',font=('Arial',15,"bold"),fg='light green',bg="black")
    g1.place(x=180,y=50)
    f1=Label(root,text='स्‍वास्‍थ्‍य',font=('Arial',15,"bold"),fg='light green',bg="black")
    f1.place(x=1550,y=50)
    bg1=Button(root,text='नागरिक योजनाएं ',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=scheme)
    bg1.place(x=230,y=100)
    bg2=Button(root,text='बच्चों के लिए योजनाएं',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=schemec)
    bg2.place(x=200,y=150)
    bg3=Button(root,text='महिला योजनाएं',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=schemew)
    bg3.place(x=202,y=200)
    bg4=Button(root,text='वृद्धों के लिए योजनाए',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=schemes)
    bg4.place(x=170,y=250)
    bf1=Button(root,text='अस्पताल',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=hospitals)
    bf1.place(x=1530,y=100)
    bf2=Button(root,text='दवा की दुकानों',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=chemists)
    bf2.place(x=1530,y=150)
    bf3=Button(root,text='पैथोलॉजी लैब',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=pathology)
    bf3.place(x=1545,y=200)
    bf4=Button(root,text='नि:शुल्क स्वास्थ्य शिविर',font=('Arial',15,"bold"),fg='Steelblue4',bg="black",command=free)
    bf4.place(x=1530,y=250)
    cov=Label(root,text='- - - - Covid-19 Dashboard - - - -',font=('Arial',20,"bold"),fg='Steelblue2',bg="black")
    cov.pack(pady=150)
    cov1=Button(root,text='राज्य समाचार',font=('Arial',15,"bold"),fg='green4',bg="black",command=statemap)
    cov1.place(x=230,y=525)
    cov2=Button(root,text='जिला समाचार',font=('Arial',15,"bold"),fg='green4',bg="black",command=dist)
    cov2.pack(pady=2)
    cov3=Button(root,text='उपचार केंद्र',font=('Arial',15,"bold"),fg='green4',bg="black",command=treat)
    cov3.place(x=1530,y=525)
    cov4=Button(root,text='प्रतिदर्श संग्रह',font=('Arial',15,"bold"),fg='green3',bg="black",command=sample)
    cov4.place(x=230,y=600)
    cov5=Button(root,text='परिक्षण लैब',font=('Arial',15,"bold"),fg='green3',bg="black",command=testing)
    cov5.pack(pady=35)
    cov6=Button(root,text='आइसोलेशन सेंटर',font=('Arial',15,"bold"),fg='green3',bg="black",command=isolation)
    cov6.place(x=1545,y=600)
    cov7=Button(root,text='कंटेनमेंट जोन',font=('Arial',15,"bold"),fg='green2',bg="black",command=containment)
    cov7.place(x=230,y=675)
    cov8=Button(root,text='   हंगर रिलीफ सेंटर  ',font=('Arial',15,"bold"),fg='green2',bg="black",command=hunger)
    cov8.pack(pady=2)
    cov9=Button(root,text='लॉकडाउन',font=('Arial',15,"bold"),fg='green2',bg="black",command=shelter)
    cov9.place(x=1540,y=675)
    covl1=Label(root,text=state1,font=('Arial',20,"bold"),fg='Steelblue2',bg="black")
    covl1.place(x=50,y=800)
    root.mainloop()
rootm=Tk()
rootm.geometry('500x500')
rootm.title('Health19+')
rootm.configure(background='black')
lm3=Label(rootm,text='Health19+',font=('Arial',20,'italic'),fg='green4',bg='black')
lm3.pack(pady=50)
lm1=Button(rootm,text='ENGLISH',font=('Arial',20,'bold'),fg='green2',command=english)
lm1.pack(pady=50)
lm2=Button(rootm,text='HINDI',font=('Arial',20,'bold'),fg='green3',command=hindi)
lm2.pack(pady=50)

rootm.mainloop()

