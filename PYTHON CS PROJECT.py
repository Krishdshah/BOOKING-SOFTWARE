dvi={'ID14541':'ANAY','ID16543':'ANUJ'}
dvid={'ID14541':['ANAY',100],'ID16543':['ANUJ',101]}
dv={'ID14541':[100,'TK travels','ANAY'],'ID16543':[101,'PKtravels','ANUJ']}
detv={'ID14541':['ANAY','TK travels','NUMBER:+919*****9','mail:tkt@email.com','Price[in INR]:12005'],'ID16543':['ANUJ','PKtravels','NUMBER:+919*****9','mail:tkt@email.com','Price[in INR]:12345']}
df={'KOLKATA-MUMBAI':45,'KOLKATA-DELHI':13}
dt={'KOLKATA-MUMBAI':['ID14541','ID16543']  ,  'KOLKATA-DELHI':['ID14541','ID16543']}
dc={'C180286':[['KRISH','Kds@101'],['Number:+919***9','Email:kds@gmail.com','DOB:15/09/2006']],'C131403':[['SRINJAY','Srinjay_121'],['Number:+919**48','Email:srinjay@gmail.com','DOB:10/10/2006']]}                                 
print('YOU ARE ON THE HOME PAGE')

secno=101           #check line 123 [used for vendors only]

cont=True

while cont==True or cont=='':
  p=1
  while p==1:
    print('''Enter :
  'C' for signing in as customer
  'V' for signing as vendor''')
    ent=input('Please enter Sign in type: ')
    if ent.upper()=='C':
      x,p=1,0
    elif ent.upper()=='V':
      x,p=2,0
    else:
      print('Please Enter a valid sign in type')
      p=1
    print()

  if x==1:
    print('You are administered as CUSTOMER')
    y=1
    while y==1:
      print('''Enter:
  'L' for logging in as existing customer
  'S' for signing up as new customer
  'U' for updating your Information''')
      log=input('Please enter log in type:')
      if log.upper()=='L':
        q,y=1,0
      elif log.upper()=='S':
        q,y=2,0
      elif log.upper()=='U':
        q,y=3,0
      else:
        print()
        print('Please Enter a valid log in type')
        y=1
    print()

    a=0
    while a==0:
      if q==1:
        name=input('Enter Registered Name:')
        cid=input('Please Enter customer ID:')
        pw=input('Please Enter Password:')
        if ('C'+cid) in dc.keys():
          if dc['C'+cid][0]==[name.upper(),pw]:
            print('Welcome' , name.upper())
            a=1
            break
          else:
            print('Log in Credentials do not match please re enter')
            p=1
            a=0

      elif q==2:
        print('Please Register By entering important details')
        name=input('Please Enter Your Full Name:')
        cid=input('Please Enter a Customer ID[containing integers only]')
        while cid.isdigit()==False or (('C'+cid) in dc.keys()) :
          if cid.isdigit()==False:
            cid=input('Enter a customer user id with digits(numbers) only:')
          elif ('C'+cid) in dc.keys():
            cid=input('Enter another Customer id as this one is already taken:')
        pasw=input('Please create a password:')
        cpasw=input('Please Reenter password:')
        print()
        while pasw!=cpasw:
          pasw=input('Please Recreate a password[as Reentered password didnt match]: ')
          cpasw=input('Please Reenter password:')
        numc=int(input('Please Enter country code number[don\'t enter \'+\']:'))
        numb=int(input('Please Enter your mobile number:'))
        numb='Number:+'+str(numc)+str(numb)
        mail=input('Please Enter your email ID:')
        mail='Email:'+mail
        dob=input('Please enter D.O.B. in dd/mm/yyyy format:')
        dob='DOB'+dob
        dc['C'+cid]=[[name,pasw],[numb,mail,dob]]
        print('CONGRATS YOU ARE REGISTERED AS:',name)
        a=1

      elif q==3:
        u=1
        while u==1:
            cid=input('Enter your Existing Customer ID number:')
            cid='C'+cid
            pasw=input('Enter Current password')
            if (cid) in dc.keys() and dc[cid][0][1]==pasw:
              print('''Select field to update:
1 for updating name
2 for updating password
3 for updating phone number
4 for updating mail ID''')
              upd=input('Enter field to update')
              if upd not in '1234':
                print('Please select an appropriate option')
                u=1
              else:
                if  upd=='1':
                  name=input('Enter new name:')
                  dc[cid][0][0]=name.upper()
                elif upd=='2':
                  pasw=input('Please create a password:')
                  cpasw=input('Please Reenter password:')
                  print()
                  while pasw!=cpasw:
                    pasw=input('Please Recreate a password[as Reentered password didnt match]: ')
                    cpasw=input('Please Reenter password:')
                  else:
                    dc[cid][0][1]=pasw
                elif  upd=='3':
                  dc[cid][1][0]=input('Enter new Phone Number:')
                elif  upd=='4':
                  dc[cid][1][1]=input('Enter new Mail ID')
                print('INFO UPDATED')
                u=0
                break
              break
            break
        break        
             
              
    
    if a==1:
      st=''
      print('Wherewould you like to TRAVEL!')
      fro=input('Enter Departure Location [FROM]')
      to=input('Enter Arrival Location [TO]')
      st+=((fro.lower()).capitalize()+'-'+(to.lower()).capitalize()).upper()
      print()
      if st in df.keys():
        print('Total Searches found for your selection=',df[st])
        print('Possible Suggestions for',st,'are')
        for i in dt[st]:
          print(detv[i])
      else:
        print('Oops!   No Suggestions available')
    cont=input('Enter any key to logout to home page:')
    
        
  elif x==2:
    
    print('You are administered as VENDOR')

    y=1
    while y==1:
      print('''Enter:
'L' for logging in as existing Vendor
'S' for signing up as new Vendor''')
      log=input('Please enter log in type:')
      if log.upper()=='L':
        q,y=1,0
      elif log.upper()=='S':
        q,y=2,0
      else:
        print()
        print('Please Enter a valid log in type')
        y=1
    print()
    
    a=0
    while a==0:
      
      if q==1:
        name=input('Enter registered name:')
        vid=input('Enter Registered Vendor ID:')
        secno=int(input('Enter Your Security Number:'))
        if dvid['ID'+vid]==[name.upper(),secno]:
          print('YOU ARE LOGGED IN AS',name)
          tname=detv['ID'+vid][1]
          numb=detv['ID'+vid][2]
          mail=detv['ID'+vid][3]
          a=1
        else:
          print('INCORRECT LOGIN CREDENTIALS PLEASE RE-ENTER')
          a=0
        
          
      elif q==2:
        print('TO REGISTER AS A VENDOR PLEASE FEED THE FOLLOWING DETAILS')
        name=input('Please Enter Your Registered Name:')
        adh:input('Please Enter Your Virtual Aadhar ID(VID):')
        tname=input('Please Enter Official [Government Registered] agency name:')
        tno=input('Please Enter GST ID for official confirmation:')
        print()     
        print('NUMBER VERIFIED , WELCOME TO COMMUNITY')
        vid=input('Please Create a Vendor login ID:')
        while vid.isdigit()==False or (('ID'+vid) in dvi.keys()) :
          if vid.isdigit()==False:
            vid=input('Enter a Vendor user id with digits(numbers) only:')
          elif ('ID'+vid) in dvi.keys():
            vid=input('Enter another Vendor id as this one is already taken:')
        pasw=input('Please create a password:')
        cpasw=input('Please Reenter password:')
        while pasw!=cpasw:
          pasw=input('Please create a password:')
          cpasw=input('Please Reenter password:')
        numb=input('Enter contact number [with code]:')
        numb='NUMBER:'+numb
        mail=input('Enter mail ID:')
        mail='MAIL:'+mail
        secno+=1
        print('Your security number=',secno)
        dvi['ID'+vid]=name.upper()
        dvid['ID'+vid]=[name.upper(),secno]
        dv['ID'+vid]=[secno,tname,name.upper()]
        a=1
        
      while a==1 or a=='1':
        z=input('Enter \'U\' to update or enter new flights:')        
        if z.upper() != 'U':
          print('Logging you out to home page')
          print()
          break
        else:
          print('''Select Your Choice:
                A to add flight details 
                R to remove flight details''')
          ch=input('Enter update type:')
          fro=input('Enter Flight departure spot:')
          to=input('Enter Flight arrival Destination:')
          st=fro.upper()+'-'+to.upper()

          if st in df.keys() and ch.upper()=='A':
            prange=int(input('Enter ticket Range'))
            df[st]+=1
            dt[st]=dt[st].append([name,tname,numb,mail])
            print('Flight entry updated')
          elif st in df.keys() and ch.upper()=='R':
            df[st]-=1
            dt[st]=dt[st].append([name,tname,numb,mail])
            print('Flight entry decreased')
          else:
            if ch.upper()=='A':
              prange=int(input('Enter ticket Range'))
              df[st]=1
              dt[st]=[].append([name,tname,numb,mail,prange])
              print('Flight entry done')
            elif ch.upper()=='R':
              print('Flight entry not found')
            else:
              print('Please select appropriate option for entry')
        a=input('Enter 1 to enter new entry:')
    cont=input('Enter any key to log out to home page')
      
#solely developed by K Shah (GITHUB:  Krishdshah)
      
    
     
          
      
        
        


      
      
      
      
    








