from django.shortcuts import render
from . import selection
from . import ibmcloud

# Create your views here.
def cropprediction(request):
    if request.method=='POST':
        N=request.POST['N']
        P=request.POST['P']
        K=request.POST['K']
        temperature=request.POST['temperature']
        humidity=request.POST['humidity']
        ph=request.POST['ph']
        rainfall=request.POST['rainfall']
        
        croppredict=ibmcloud.croppredict(N,P,K,temperature,humidity,ph,rainfall)
        
        image="images/crops/"+selection.images(croppredict)
        return render(request,"cropresult.html",{"croppredict":croppredict,"image":image})
        
    return render(request,"cropprediction.html")

def yieldprediction(request):
    
    default_list=['select state','select district','select season','select crop']
    states=selection.states()
    districts=[]
    seasons=[]
    crops=[]
    state=default_list[0]
    district=default_list[1]
    season=default_list[2]
    crop=default_list[3]
    
    if request.method=='POST':
        state=str(request.POST["state"])
        district=request.POST['district']
        season=request.POST['season']
        crop=request.POST['crop']
        area=request.POST['area']

        #print('posted=',state,district,season,crop)

        if(state!='select' and district!='select' and season!='select' and crop!='select' and area!=""):
            #print('in 0')
            area=float(area)
            state=[i for i in selection.states() if state in i][0]
            states=[]
            district=[i for i in selection.districts(state) if district in i][0]
            season=[i for i in selection.seasons(state,district) if season in i][0]
            crop=[i for i in selection.crops(state,district,season) if crop in i][0]
            
            yieldperarea=ibmcloud.yieldperarea(state,district,season,crop)
            if(yieldperarea<0): yieldperarea*=-1
            
            production = round(yieldperarea*area,2)
            yieldperarea=round(yieldperarea,2)
            
            return render(request,'yieldresult.html',{'state':state,'district':district,'season':season,'crop':crop,'yieldperarea':yieldperarea,'yield':production})

        if(state!='select' and district!='select' and season!='select' and crop!='select'):
            #print('in 1')
            state=[i for i in selection.states() if state in i][0]
            states=[]
            district=[i for i in selection.districts(state) if district in i][0]
            season=[i for i in selection.seasons(state,district) if season in i][0]
            crop=[i for i in selection.crops(state,district,season) if crop in i][0]
            
            
            #messages.info(request,yieldperarea)
            return render(request,'yieldprediction.html',{'state':state,'district':district,'season':season,'crop':crop,'states':states,'districts':districts,'seasons':seasons,'crops':crops})

        if(state!='select' and district!='select' and season!='select'):
            #print('in 1')
            state=[i for i in selection.states() if state in i][0]
            states=[]
            district=[i for i in selection.districts(state) if district in i][0]
            season=[i for i in selection.seasons(state,district) if season in i][0]
            crops=selection.crops(state,district,season)
            return render(request,'yieldprediction.html',{'state':state,'district':district,'season':season,'crop':crop,'states':states,'districts':districts,'seasons':seasons,'crops':crops})
            
        elif(state!='select' and district!='select'):
            #print('in 2')
            state=[i for i in selection.states() if state in i][0]
            states=[]
            district=[i for i in selection.districts(state) if district in i][0]
            seasons=selection.seasons(state,district)
            return render(request,'yieldprediction.html',{'state':state,'district':district,'season':season,'crop':crop,'states':states,'districts':districts,'seasons':seasons,'crops':crops})
            
        elif(state!='select'):
            #print('in 3')
            state=[i for i in selection.states() if state in i][0]
            states=[]
            districts=selection.districts(state)
            return render(request,'yieldprediction.html',{'state':state,'district':district,'season':season,'crop':crop,'states':states,'districts':districts,'seasons':seasons,'crops':crops})
        
        

        #print('in out')
        
        return render(request,'yieldprediction.html',{'state':state,'district':district,'season':season,'crop':crop,'states':states,'districts':districts,'seasons':seasons,'crops':crops})
        
    else:
        return render(request,'yieldprediction.html',{'state':state,'district':district,'season':season,'crop':crop,'states':states,'districts':districts,'seasons':seasons,'crops':crops})
