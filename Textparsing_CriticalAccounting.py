



########################################################################

from bs4 import BeautifulSoup
import re,requests
import timeit

###############
"""
If text is writting using tag <font stylr="" > this function will capture that
"""

def getFont(li_after_cri):
    print("In font")
    all_fil_list=[]
    all_sub_heads_list=[]
    I=[]
    
    ############    get ending of critical acc. section by matching attributes of font tag  #####
    
    check_pur=li_after_cri[0].font.attrs
    cnt=0
    #check_attri_font=li_after_cri[0].font.attrs
    for k in range(len(li_after_cri[0:])):
        if li_after_cri[k].font:
            if check_pur==li_after_cri[k].font.attrs:
                if cnt<2:
                    all_fil_list=li_after_cri[:k]#getting all between critical
                    cnt+=1
    if not all_fil_list:  #could not find ending of crical acc
        all_fil_list=li_after_cri
        print("could not find ending of crical acc")
    
    #### this regex will find  sub headings; 
    #### Any text written in bold, italic, both, or underlined will be considered as sub heading
    
    regex2=re.compile(".*(font-weight:bold)|(font-style:italic)|(text-decoration:underline).*")
    y=[]
    for ll in range(len(all_fil_list)):
        y.extend(all_fil_list[ll].find_all('font'))  #get all fonts in onle list
    
    for ll in range(len(y)):
        if regex2.search(str(y[ll])):               
            all_sub_heads_list.append(y[ll].text)
            I.append(ll)
    if not all_sub_heads_list:
        print("could not find sub headings")
    #######

    all_sub_details=[]              #all test between two sub-headings are details of 1st heading, append them togeather
    for nn in range(len(I)):
        if nn<(len(I)-1):
            #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:I[nn+1]]
            all_sub_details.append(y[I[nn]:I[nn+1]])       

        if nn==(len(I)-1):
            #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:]
            all_sub_details.append(y[I[nn]:])

    sub_details=[]

    for nl in range(len(all_sub_details)):
        tl=[]
        for nx in range(len(all_sub_details[nl])):
            #print(nl)
            #print(nx)
            #if all_sub_details[nl][nx].font:
            #print("gfhdf")
            try:
                tl.append(all_sub_details[nl][nx].text)

            except:
                pass
        sub_details.append(tl)
        #print("blaa")
                #print("ty")
    lookup={}                # map heading to deatils as dict element
    #print(sub_details[0])
    #sub_details[0]
    for n in range(len(sub_details)):
        lookup[all_sub_heads_list[n]]=sub_details[n]
    
    return lookup
"""
Just like Font if tag is span following will parse that
"""
def getSpan(li_after_cri):
    all_fil_list=[]
    all_sub_heads_list=[]
    
    print(li_after_cri[0])
    check_attri=li_after_cri[0].span.attrs
    
    print(check_attri)
    ######################################### looking for Cri Section Ending
    if li_after_cri[0].span.text.isupper(): 
        
        z=[]
        
        for i in range(len(li_after_cri)):
            if li_after_cri[i].span:
                if li_after_cri[i].span.text:
                    if li_after_cri[i].span.text.isupper():
                        z.append(i)
                        
        try:

            r=z[1]
    
            all_fil_list=li_after_cri[:r]
        except:
            all_fil_list =li_after_cri
    else:
        for k in range(len(li_after_cri[0:])):
            
            if li_after_cri[k].span:
                if check_attri==li_after_cri[k].span.attrs:
                    all_fil_list=li_after_cri[:k]
        
    if len(all_fil_list)==0:
        all_fil_list=li_after_cri
    #print(all_fil_list)
    ###########################################  
    regex2=re.compile(".*(font-weight:bold)|(font-style:italic)|(text-decoration:underline).*")
    y=[]
    I=[]
    for ll in range(len(all_fil_list)):
        y.extend(all_fil_list[ll].find_all('span'))  #get all fonts in onle list
    
    for ll in range(len(y)):
        if regex2.search(str(y[ll])):               
            all_sub_heads_list.append(y[ll].text)
            I.append(ll)
    if not all_sub_heads_list:
        print("could not find sub headings")
    #print(len(y))
    #print(len(I))
    
    #######

    all_sub_details=[]              #all test between two sub-headings are details of 1st heading, append them togeather
    for nn in range(len(I)):
        if nn<(len(I)-1):
            #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:I[nn+1]]
            all_sub_details.append(y[I[nn]:I[nn+1]])       

        if nn==(len(I)-1):
            #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:]
            all_sub_details.append(y[I[nn]:])

    sub_details=[]

    for nl in range(len(all_sub_details)):
        tl=[]
        for nx in range(len(all_sub_details[nl])):
            #print(nl)
            #print(nx)
            #if all_sub_details[nl][nx].font:
            #print("gfhdf")
            try:
                tl.append(all_sub_details[nl][nx].text)

            except:
                pass
        sub_details.append(tl)
        #print("blaa")
                #print("ty")
    lookup={}                # map heading to deatils as dict element
    #print(sub_details[0])
    #sub_details[0]
    for n in range(len(sub_details)):
        lookup[all_sub_heads_list[n]]=sub_details[n]
    
    
    
    
    return lookup

"""
If p tag is used, it will either use font for styling or tags like <i><b>
so this function will take care of that
"""
def getJustP(li_after_cri):
    print("Just ptag")
    
    ######################get Crital Section heading ####
    
    all_fil_list=[]
    all_sub_heads_list=[]

    check_pur=li_after_cri[0].attrs##tag with just with P tag
    #print(check_pur)

    cnt=0
    for k in range(len(li_after_cri[0:])):
        if check_pur==li_after_cri[k].attrs:

            if cnt<2:
                all_fil_list=li_after_cri[:k]#getting all between critical
                cnt+=1
    if not all_fil_list:  #could not find ending of crical acc
            all_fil_list=li_after_cri
            print("could not find ending of crical acc")
    
    
    li=[]
    ind=[]
    whole=[]
    for elm in range(len(all_fil_list)):
        soup=BeautifulSoup(str(all_fil_list[elm]))
        if soup.i:
            li.append(soup.i.text)
            ind.append(elm)
    if len(ind)!=0:
        
        #len(all_fil_list)    #n=0,1,2,3
        new_li=[]
        for nn in range(len(ind)):

            if nn<(len(ind)-1):
                li2=[]
                y=ind[nn]     # 2
                z=ind[nn+1]   # 8
                while(y<z):
                    li2.append(all_fil_list[y].text)
                    y=y+1
                new_li.append(li2)
            if nn==(len(ind)-1):
                li2=[]
                y=ind[nn]     # 2
                z=len(all_fil_list) 
                while(y<z):
                    li2.append(all_fil_list[y].text)
                    y=y+1
                new_li.append(li2)
        #print(len(new_li))  
        #new_li[3]    

        lookup={}                # map heading to deatils as dict element
            #print(sub_details[0])
            #sub_details[0]
        for n in range(len(new_li)):
            lookup[li[n]]=new_li[n]
    #lookup
    
    else:
        y1=[]
        y2=[]
        for ll in range(len(all_fil_list)):
            if all_fil_list[ll].text:
                y1.append(all_fil_list[ll].text)
        
        regex2=re.compile(".*(font-weight:bold)|(font-style:italic)|(text-decoration:underline).*")
        
        for ll in range(len(all_fil_list)):
            if regex2.search(str(all_fil_list[ll])):
                y2.append(ll)
        
        mapped_detail=[]
        
        for nn in range(len(y2)):
            if nn<(len(y2)-1):
            #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:I[nn+1]]
                mapped_detail.append(y1[y2[nn]:y2[nn+1]])
            
            if nn==(len(y2)-1):
            
                #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:]
                mapped_detail.append(y1[y2[nn]:])
                
        lookup={}
        
        for n in range(len(y2)):
            lookup[y1[y2[n]]]=mapped_detail[n]
            #lookup
    return lookup
"""
Some times header and sub header can be same, bold and same text size with only difference that header is written using Capital letters
so we first check if header is in caps or not , if yes following code will creat dict
"""

def getALLCAPS(li_after_cri):
    print("all caps")
    
    ##############################get critical section ending #############
    all_fil_list=[]
    all_sub_heads_list=[]
    z=[]
   
    for i in range(len(li_after_cri)):
        if li_after_cri[i].font:
            if li_after_cri[i].font.text:
                if li_after_cri[i].font.text.isupper():
                    z.append(i)
    try:
        
        r=z[1]
           
        all_fil_list=li_after_cri[:r]
    except:
        all_fil_list =li_after_cri
    
    I=[]
    
    ####################################
    regex2=re.compile(".*(font-weight:bold)|(font-style:italic)|(text-decoration:underline).*")
    y=[]
    for ll in range(len(all_fil_list)):
        y.extend(all_fil_list[ll].find_all('font'))
    ####
    for ll in range(len(y)):
        if regex2.search(str(y[ll])):
            all_sub_heads_list.append(y[ll].text)
            I.append(ll)
    if not all_sub_heads_list:
        print("could not find sub headings")
    #######

    all_sub_details=[]
    for nn in range(len(I)):
        if nn<(len(I)-1):
            #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:I[nn+1]]
            all_sub_details.append(y[I[nn]:I[nn+1]])

        if nn==(len(I)-1):
            #lookup[all_sub_heads_list[nn]]=all_fil_list[I[nn]:]
            all_sub_details.append(y[I[nn]:])

    sub_details=[]

    for nl in range(len(all_sub_details)):
        tl=[]
        for nx in range(len(all_sub_details[nl])):
            #print(nl)
            #print(nx)
            #if all_sub_details[nl][nx].font:
            #print("gfhdf")
            try:
                tl.append(all_sub_details[nl][nx].text)

            except:
                pass
        sub_details.append(tl)
        #print("blaa")
                #print("ty")
    lookup={}
    #print(lookup.keys())
    #sub_details[0]
    for n in range(len(sub_details)):
        lookup[all_sub_heads_list[n]]=sub_details[n]
    #print(lookup.keys())
    
    return lookup
    

######## this is start
# get cik list from txt file

data= open("Cik_List_172.txt", 'r')
cik_N=data.read().split("\n")
data.close()

#cik_N=['0001013488']
res=[]
x={}
file=open("log-file.txt","a+")
file.write("Starting New Log.....  ")

Final_output= []
for i in range(len(cik_N)):
    start = timeit.default_timer()
    print("starting..."+  cik_N[i])
    file.write("starting..."+  cik_N[i])
    try:

        doc = next(cb.document_search(company_identifiers=[cik_N[i]],
                    full_text_search_term=None,
                    year=2017,
                    #use_fiscal_period=False,
                    document_type=2700)).get_contents()


    #res.append(doc)

    ############################################ Get  soup for 1st CIK in list ######################



        #print(doc)
        souped=BeautifulSoup(doc)                      #get soup

        for tag in souped.find_all('table'):         #delete if any table in soup
            tag.replaceWith('')
        #souped=sou_l[i]
        if souped.find_all("p"):                    	#for p tag
            div_all_nn=souped.find_all("p")

        elif souped.find_all('div'):			#for div tag
            div_all_nn=souped.find_all("div")

        div_all_nn_list=list(div_all_nn)
        #print(div_all_nn_list)

        ########################################### Looking for critical start ##########################

        li_after_cri=[]

        file.write("looking for critical acc. of...."+  cik_N[i])
        regex_1=re.compile(".*>(Critical Accounting)|(CRITICAL ACCOUNTING).*")
        regex=re.compile(".*(Critical Accounting)|(CRITICAL ACCOUNTING).*")

        for l in range(len(div_all_nn_list)):
            if regex_1.search(str(div_all_nn_list[l])):
                li_after_cri=div_all_nn_list[l:]

        if (len(li_after_cri))==0:
            for l in range(len(div_all_nn_list)):
                if regex.search(str(div_all_nn_list[l])):
                    li_after_cri=div_all_nn_list[l:]
         ###################################### Looking foe critical ending  ##############
        #print(li_after_cri[0])
        if li_after_cri:
            if li_after_cri[0].font:                     # check if "font" tag is used 
                if li_after_cri[0].font.text.isupper():       # checks if critical accounting is in all capital letters
                    x=getALLCAPS(li_after_cri)
                    file.write("headin is in capitals")               
                    if len(x)==0:
                        x=getJustP(li_after_cri)

                else:
                    x=getFont(li_after_cri)  
                    file.write("Font used")
                    if len(x)==0:
                        x=getJustP(li_after_cri)
                    # if heading is not in all caps- then run getFont function
            elif li_after_cri[0].span:                  # check if "span" tag is used
                    x=getSpan(li_after_cri)
                    file.write("Span")

            else:
                x=getJustP(li_after_cri)              #  if only p tag is used with id
        else:
            file.write("could not find critical accounting section")
        stop = timeit.default_timer()
        total=str(stop-start)
        file.write("Total times is:  ")
        file.write(total)

        ######################################## To csv individual CIK ##############################

        #df = pd.Series()
        #print(x)
        N=pd.Series(x)
        #df=df.append(N)
        N.to_csv("Todays_for_"+cik_N[i]+".csv")
    except:
        pass
        file.write("No file for this cik, error occured")
