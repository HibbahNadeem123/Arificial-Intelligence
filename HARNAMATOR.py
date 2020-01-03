questions=["Is your character a male?",
           "Is your character older than 20?",
           "Does your character like programming?",
           "Does your character like coffee?",
		   "Does your character like tea?",
           "Does your character have colored eyes?",
		   "Does your character speak Punjabi?",
           "Does your character speak Sindhi?",
		   "Does your character speak Pashto?",
           "Does your character know Turkish language?",
		   "Does your character like Continental food?",
		   "Does your character like Asian food?",
		   "Is your character's favorite cartoon Tom?",
		   "Is your character's favorite cartoon Jerry?", 
		   "Is your character's favorite cartoon Popeye?",
		   "Does your character like to read books?",
		   "Does your character like to watch movies?",
		   "Is your character's hobby dancing?",
           "Is your character's hobby gaming?",
		   "Is your character's hobby cooking and baking?",
		   "Is your character's hobby martial art?",
		   "Is your character's hobby writting?",
		   "Does your character prefer to live in the UK?",
		   "Does your character prefer to live in Moscow?",
		   "Does your character prefer to live in Nothern Areas of Pakistan?",
		   "Does your character prefer to live in  Karachi?",
		   "Does your character prefer to live in Islamabad?",
		   "Does your character prefer to live in Thiland?",
		   "Does your character prefer to live in Turkey?",
		   "Does your character prefer to live in Australia?",
		   "Does your character prefer to live in America?",
		   "Does your character prefer to live in Bahria Town?",
		   "Does your character prefer to live in Makka?",
		   "Does your character prefer to live in Europe?",
		   "Is your character's favorite food Biryani?",
		   "Is your character's favorite food Saag?",
		   "Is your character's favorite food Pasta?",
		   "Is your character's favorite food Pulao?",
		   "Is your character's favorite food Curry?",
		   "Does your character often come late?",
           "Does your character fear of animal?",
		   "Does your character fear of height?",
           "Does your character fear of darkness?"
		   ]

students=['Shahzar','Sajid','Farwa','Ammar','Ahmed Ammar','Gul',
          'Anas','Wajeha','Ali Hassan Ghori','Mohsin','Rukhma','Hibbah',
		  'M Uzair','Haseeb','Taha','M Ali Hassan','Bushra','Bisma',
		  'Aqsa Usman','Ahsan Mustafa','Hassam','Uzair Mehmood','Rabiya',
		  'Aqsa Mehreen','Duha','Aimen','Noman','Asad','Hammad','Ahsan Ishtiaq',
		  'Nameera']

male=['Shahzar','Sajid','Ammar','Ahmed Ammar','Gul',
     'Anas','Ali Hassan Ghori','Mohsin','M Uzair','Haseeb','Taha','M Ali Hassan',
	 'Ahsan Mustafa','Hassam','Uzair Mehmood','Noman','Asad','Hammad','Ahsan Ishtiaq',]

lessOrEqualtwenty=['Shahzar','Ahmed Ammar','Gul',
                 'Anas','Wajeha','Ali Hassan Ghori','Rukhma',
		         'M Uzair','Haseeb','M Ali Hassan','Bushra','Hassam','Uzair Mehmood',
		         'Noman','Asad','Ahsan Ishtiaq','Nameera']
			
programming=['Shahzar','Sajid','Farwa','Ammar','Ahmed Ammar','Gul',
          'Anas','Wajeha','Rukhma','Hibbah',
		  'M Uzair','M Ali Hassan','Bushra','Bisma',
		  'Hassam','Uzair Mehmood','Rabiya',
		  'Asad','Ahsan Ishtiaq','Nameera']

coffee=['Shahzar','Farwa','Ammar','Anas','Wajeha','Hibbah',
		  'M Uzair','Haseeb','M Ali Hassan','Bushra','Bisma',
		  'Aimen','Asad','Hammad']

tea=['Sajid','Ahmed Ammar','Gul','Anas','Mohsin','Rukhma',
	 'M Uzair','Taha','Aqsa Usman','Ahsan Mustafa','Hassam',
	 'Uzair Mehmood','Rabiya','Aqsa Mehreen','Noman','Ahsan Ishtiaq','Nameera']

coloredeyes=['Ammar','Mohsin','Ahsan Mustafa','Aimen']

punjabi=['Wajeha','Mohsin','Rukhma','Aqsa Usman','Aqsa Mehreen']
pashto=['Haseeb','Aimen']
sindhi=['Shahzar','Duha']
turkish=['Shahzar']

continental=['Shahzar','Farwa','Wajeha','Hibbah','Bushra','Bisma','Hassam','Aimen','Nameera']
asian=['Sajid','Farwa','Ammar','Ahmed Ammar','Gul',
         'Anas','Wajeha','Ali Hassan Ghori','Mohsin','Rukhma','Hibbah',
		 'M Uzair','Haseeb','Taha','M Ali Hassan',
		 'Aqsa Usman','Ahsan Mustafa','Uzair Mehmood','Rabiya',
		 'Aqsa Mehreen','Duha','Aimen','Noman','Asad','Hammad','Ahsan Ishtiaq']

tom=['Ahmed Ammar','Gul','Anas','Wajeha','Haseeb','M Ali Hassan','Ahsan Ishtiaq']
jerry=['Ahmed Ammar','Taha','Ahsan Mustafa','Hassam','Duha','Ahsan Ishtiaq']
popeye=['Noman','Asad','Hammad']

book=['Sajid','Farwa','Anas','Wajeha','Haseeb','Taha','Bisma',
	 'Uzair Mehmood','Rabiya','Aimen','Hammad','Nameera']

movie=['Shahzar','Ammar','Ahmed Ammar','Gul',
         'Anas','Wajeha','Mohsin','Rukhma','Hibbah',
		  'M Uzair','Taha','M Ali Hassan','Bushra',
		  'Aqsa Usman','Ahsan Mustafa','Hassam',
		  'Aqsa Mehreen','Duha','Aimen','Noman','Asad','Ahsan Ishtiaq']

#hobbies
dance=['M Ali Hassan']
martialart=['Aqsa Usman']
games=['Ahmed Ammar','Gul','Anas','Mohsin','Hibbah',
	   'Taha','Ahsan Mustafa','Hassam','Uzair Mehmood','Rabiya',
	    'Noman','Ahsan Ishtiaq']
writing=['Ammar']
cooking=['Wajeha','Hibbah','Aqsa Mehreen','Duha']

#favplacetolive
uk=['Bisma', 'Ahsan Mustafa']
northernareas=['Ahmed Ammar', 'Haseeb', 'Aqsa Usman']
moscow=['Noman']
islamabad=['Sajid', 'Wajeha', 'Ali Hassan Ghori', 'Mohsin', 'M Uzair','Aqsa Mehreen','Aimen']
Karachi=['Shahzar','Ammar','Gul', 'Wajeha','M Ali Hassan', 'Hassam', 'Uzair Mehmood', 'Rabiya', 'Duha','Nameera']
thailand=['Asad']
turkey=['Rukhma']
australia=['Hibbah']
america=['Bushra']
bahriatown=['Taha']
makka=['Hammad']
europe=['Anas']

#favfood
curry=['Ahsan Mustafa']
pulao=['Hibbah']
pasta=['Wajeha', 'Bisma', 'Bushra', 'Aimen']
biryani=['Shahzar','Sajid','Farwa','Ammar', 'Ahmed Ammar', 'Gul','Anas','Rukhma', 'Haseeb','Taha', 'Aqsa Mehreen','Hassam','Uzair Mehmood','Rabiya', 'Aqsa Usman','Duha','Aimen','Asad', 'Hammad','Ahsan Ishtiaq']
saag=['Mohsin']

late=['Farwa','Ammar','Ahmed Ammar','Gul', 'Wajeha','Ali Hassan Ghori','Hibbah','M Uzair','Haseeb','Taha','Bushra','Bisma','Aqsa Usman','Ahsan Mustafa','Hassam', 'Rabiya','Asad']

#biggestfear
darkness=['Ammar']
animalorinsects=['Anas','Wajeha','Rukhma','Bushra','Rabiya','Aqsa Mehreen']
height=['Hibbah','Bisma','Duha']

#searching
def askQues(count):
    print(questions[count])

i=0
ans=[]
index=0

askQues(0)
rep=input()
if (rep=="no"): #if female
    for std in students:
        if (std not in male):
            ans.append(std)  
    askQues(1)
    rep=input()
    if (rep=="yes"):#if older than 20
        for i in range(0,len(ans)):
            if (ans[index] in lessOrEqualtwenty):
                ans.remove(ans[index])
            else:
                index=index+1  
        index=0
        askQues(2)
        rep=input()
        if (rep=="yes"): #if likes programing
            for i in range(0,len(ans)):
                if (ans[index] not in programming):
                    ans.remove(ans[index])
                else:
                    index=index+1 
            index=0
            askQues(3)
            rep=input()
            if (rep=="yes"):# if std likes coffee
                for i in range(0,len(ans)):
                    if (ans[index] not in coffee):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                askQues(19)
                rep=input()
                if (rep=="yes"):#if likes cooking
                    for i in range(0,len(ans)):
                        if (ans[index] not in cooking):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #hibbah found
                else:
                    for i in range(0,len(ans)):
                        if (ans[index] in cooking):
                            ans.remove(ans[index])
                        else:
                            index=index+1 
                    index=0
                    askQues(41)
                    rep=input()
                    if (rep=="yes"):#if fears from height
                        for i in range(0,len(ans)):
                            if (ans[index] not in height):
                                ans.remove(ans[index])
                            else:
                                index=index+1
                                #bisma found
                        index=0
                    else:#if do not fear from height
                        for i in range(0,len(ans)):
                            if (ans[index] in height):
                                ans.remove(ans[index])
                            else:
                                index=index+1 
                            #Farwa found
            else:
                for i in range(0,len(ans)):
                    if (ans[index] in coffee):
                        ans.remove(ans[index])
                    else:
                        index=index+1 
                        #rabia found
                index=0
                
        else:#if do not likes programming
            for i in range(0,len(ans)):
                if (ans[index] in programming):
                    ans.remove(ans[index])
                else:
                    index=index+1 
            index=0
            askQues(19)
            rep=input()
            if (rep=="yes"):#if likes cooking and baking
                for i in range(0,len(ans)):
                    if (ans[index] not in cooking):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #[aqsa and duha]
                askQues(41)
                rep=input()
                if (rep=="yes"):#if fears from height
                    for i in range(0,len(ans)):
                        if (ans[index] not in height):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                            #duha found
                    index=0
                else:#if do not fear from height
                    for i in range(0,len(ans)):
                        if (ans[index] in height):
                            ans.remove(ans[index])
                        else:
                            index=index+1 
                        #aqsa found
            else:# if not in cooking and baking
                for i in range(0,len(ans)):
                    if (ans[index] in cooking):
                        ans.remove(ans[index])
                    else:
                        index=index+1 
                index=0
                #[aqsa usman and aimen]
                askQues(20)
                rep=input()
                if (rep=="yes"):#martial art
                    for i in range(0,len(ans)):
                        if (ans[index] not in martialart):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                            #aqsa usman found
                    index=0
                else:#if not in martial art
                    for i in range(0,len(ans)):
                        if (ans[index] in martialart):
                            ans.remove(ans[index])
                        else:
                            index=index+1 
                        # found aimen
    else:# if not older than 20
        for i in range(0,len(ans)):
            if (ans[index] not in lessOrEqualtwenty):
                ans.remove(ans[index])
            else:
                index=index+1 
        index=0
        askQues(3)
        rep=input()
        if (rep=="yes"):# if std likes coffee
            for i in range(0,len(ans)):
                if (ans[index] not in coffee):
                    ans.remove(ans[index])
                else:
                    index=index+1
                    #[wajeha bushra]
            index=0
            askQues(6)
            rep=input()
            if (rep=="yes"):#if speaks punjabi
                for i in range(0,len(ans)):
                    if (ans[index] not in punjabi):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                        #wajeha found
                index=0
            else:#if do not speaks punjabi
                for i in range(0,len(ans)):
                    if (ans[index] in punjabi):
                        ans.remove(ans[index])
                    else:
                        index=index+1 
                    #bushra found
        else:
            for i in range(0,len(ans)):
                if (ans[index] in coffee):
                    ans.remove(ans[index])
                else:
                    index=index+1 
                        #[rukhma nameera]
            index=0
            askQues(6)
            rep=input()
            if (rep=="yes"):#if speaks punjabi
                for i in range(0,len(ans)):
                    if (ans[index] not in punjabi):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                        #rukhma found
                index=0
            else:#if do not speaks punjabi
                for i in range(0,len(ans)):
                    if (ans[index] in punjabi):
                        ans.remove(ans[index])
                    else:
                        index=index+1 
                        #nameera found
                index=0
if(rep=="yes"): #male
    for std in students:
        ans.append(std)
    askQues(1) #older than 20
    rep=input()
    if(rep=="yes"):
        for i in range(0,len(ans)):
            if(ans[index] in lessOrEqualtwenty):
                ans.remove(ans[index])
            else:
                index=index+1
        index=0

        askQues(5)
        rep=input()
        if(rep=="yes"):#colored eyes
            for i in range(0,len(ans)):
                if(ans[index] not in coloredeyes):
                    ans.remove(ans[index])
                else:
                    index=index+1
            index=0
            #ammar mohsin ahsanm

            askQues(18)
            rep=input()
            if(rep=="yes"):#play games
                for i in range(0,len(ans)):
                    if(ans[index] not in games):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #mohsin, ahsanm

                askQues(38)
                rep=input()
                if(rep=="yes"):
                    for i in range(0,len(ans)):
                        if(ans[index] not in curry):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #ahsanM found
                else:
                    for i in range(0,len(ans)):
                        if(ans[index] in curry):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #mohsin found
            else:
                for i in range(0,len(ans)):
                    if(ans[index] in games):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #ammar found

        else:#not colored eyes
            for i in range(0,len(0,ans)):
                if(ans[index] in coloredeyes):
                    ans.remove(ans[index])
                else:
                    index=index+1
            index=0
            #taha, sajid, hammad

            askQues(32)
        rep=input()
        if (rep=="yes"):
            for i in range(0,len(ans)):
                if(ans[index] not in makka):
                    ans.remove(ans[index])
                else:
                    index=index+1
            #hammad found
        else:
            for i in range(0,len(ans)):
                if(ans[index] in makka):
                    ans.remove(ans[index])
                else:
                    index=index+1
            index=0
            #[sajid,taha]

            askQues(31)
            rep=input()
            if(rep=="yes"):
                for i in range(0,len(ans)):
                    if(ans[index] not in bahriatown):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #taha found
            else:
                for i in range(0,len(ans)):
                    if(ans[index] in bahriatown):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #sajid found

else: #younger than 20
        for i in range(0,len(ans)):
            if(ans[index] not in lessOrEqualtwenty):
                ans.remove(ans[index])
            else:
                index=index+1
        index=0

        askQues(2)
        rep=input()
        if(rep=="yes"):#likes programming
            for i in range(0,len(ans)):
                if(ans[index] not in programming):
                    ans.remove(ans[index])
                else:
                    index=index+1
            index=0

            askQues(18)
            rep=input()
            if(rep=="yes"):#gaming
                for i in range(0,len(ans)):
                    if(ans[index] not in games):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0

                askQues(3)
                rep=input()
                if(rep=="yes"):#coffee
                    for i in range(0,len(ans)):
                        if(ans[index] not in coffee):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                #anas found
                else: #not likes coffee
                    for i in range(0,len(ans)):
                        if(ans[index] in coffee):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #Ahmedammar Gul Hassam UzairM AhsanI

                    askQues(24)
                    rep=input()
                    if(rep=="yes"):
                        for i in range(0,len(ans)):
                            if(ans[index] not in northernareas):
                                ans.remove(ans[index])
                            else:
                                index=index+1
                        index=0
                        #ahmedammar found
                    else:
                        for i in range(0,len(ans)):
                            if(ans[index] in northernareas):
                                ans.remove(ans[index])
                            else:
                                index=index+1
                        index=0
                        #Gul hassam uzairM AhSanI
                        askQues(10)
                        rep=input()
                        if(rep=="yes"):#like continental food
                            for i in range(0,len(ans)):
                                if(ans[index] not in continental):
                                    ans.remove(ans[index])
                                else:
                                    index=index+1
                            index=0
                            #Hassam found
                        else:
                            for i in range(0,len(ans)):
                                if(ans[index] in continental):
                                    ans.remove(ans[index])
                                else:
                                    index=index+1
                            index=0
                        #GUL uzairM ahsanI

                            askQues(15)
                            rep=input()
                            if(rep=="yes"):#books 
                                for i in range(0,len(ans)):
                                    if(ans[index] not in book):
                                        ans.remove(ans[index])
                                    else:
                                        index=index+1
                                        #uzair mehmood found                                  
                            else:#not likes book reading
                                for i in range(0,len(ans)):
                                    if(ans[index] in book):
                                        ans.remove(ans[index])
                                    else:
                                        index=index+1
                                index=0
                                #ahsanI gul 
                                askQues(25)
                                rep=input()
                                if(rep=="yes"):#karachi 
                                    for i in range(0,len(ans)):
                                        if(ans[index] not in Karachi):
                                            ans.remove(ans[index])
                                        else:
                                            index=index+1
                                        #gul found                                  
                                else:
                                    for i in range(0,len(ans)):
                                        if(ans[index] in Karachi):
                                            ans.remove(ans[index])
                                        else:
                                            index=index+1
                                        #ahsan I
#########
            else:
                for i in range(0,len(ans)):
                    if(ans[index] in games):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #shahzar muzair mali asad

                askQues(25)
                rep=input()
                if(rep=="yes"):#PREFERS TO LIVE IN KARACHI
                    for i in range(0,len(ans)):
                        if(ans[index] not in Karachi):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #shahzar mali

                    askQues(9)
                    rep=input()
                    if (rep=="yes"):
                        for i in range(0,len(ans)):#can speak turkish
                            if(ans[index] not in turkish):
                                ans.remove(ans[index])
                            else:
                                index=index+1
                        index=0
                        #shahzar found
                    else:#can not speak turkish
                        for i in range(0,len(ans)):
                            if(ans[index] in turkish):
                                ans.remove(ans[index])
                            else:
                                index=index+1
                        index=0
                        #m ali hassan found
                else:#not prefers to live in karachi
                    for i in range(0,len(ans)):
                        if(ans[index] in Karachi):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #muzair asad

                    askQues(26)
                    rep=input()
                    if(rep=="yes"):#prefered place to live is islamabad
                        for i in range(0,len(ans)):
                            if(ans[index] not in islamabad):
                                ans.remove(ans[index])
                            else:
                                index=index+1
                        index=0
                        #muzair found
                    else:#prefered place to live is islamabad
                        for i in range(0,len(ans)):
                            if(ans[index] in islamabad):
                                ans.remove(ans[index])
                            else:
                                index=index+1
                        index=0
                        #asad found
        else:#do not like prog
            for i in range(0,len(ans)):
                if(ans[index] in programming):
                    ans.remove(ans[index])
                else:
                    index=index+1
            index=0
            #ghori haseeb noman
            askQues(8)
            rep=input()
            if(rep=="yes"):
                for i in range(0,len(ans)):
                    if(ans[index] not in pashto):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #haseeb found
            else:
                for i in range(0,len(ans)):
                    if(ans[index] in pashto):
                        ans.remove(ans[index])
                    else:
                        index=index+1
                index=0
                #ghori noman
                askQues(4)
                rep=input()
                if(rep=="yes"):
                    for i in range(0,len(ans)):
                        if(ans[index] not in tea):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #noman found
                else:
                    for i in range(0,len(ans)):
                        if(ans[index] in tea):
                            ans.remove(ans[index])
                        else:
                            index=index+1
                    index=0
                    #ghori found

    
    




print (ans)