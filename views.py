from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "1091458322msh57fea0fc2817edbp133e49jsna0b510e3734a",  #RAPID API .COM #git and request install
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json() # becoz in webpage data can go in json 

# Create your views here.

def helloworldview(request): #  6 
      mylist = []
      noofresults=int(response['results'])
      for y in range(0,noofresults):
             
             mylist.append(response['response'][y]['country'])           
      if request.method=="POST": # work when post request come 
            selectedcountry=request.POST['selectedcountry'] #here selected country we get from html page
            noofresults=int(response['results'])
            for x in range(0,noofresults):
               if selectedcountry==response['response'][x]['country'] :
                  new = response['response'][x]['cases']['new']
                  active = response['response'][x]['cases']['active']
                  critical = response['response'][x]['cases']['critical']
                  recovered = response['response'][x]['cases']['recovered']
                  total = response['response'][x]['cases']['total']
                  deaths = int(total)-int(active)-int(recovered)
            context = {'selectedcountry': selectedcountry,'mylist':mylist,'new' : new,'active' : active,'critical' : critical,'recovered' : recovered,'deaths' : deaths,'total' : total} 
            return render(request,'helloworld.html',context)  #render accept only ditionary render use for passing any data in html
                
      context={'mylist' : mylist}
      return render(request,'helloworld.html',context)
      
