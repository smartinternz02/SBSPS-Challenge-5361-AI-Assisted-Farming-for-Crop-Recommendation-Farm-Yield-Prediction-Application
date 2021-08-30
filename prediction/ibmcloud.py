import joblib
import numpy as np


def yieldperarea(state,district,season,crop):
    cls=joblib.load('finalized_yieldmodel.sav')
    lis=np.array([[state,district,season,crop,None,None]])
    ans=int(cls.predict(lis))
    print('Answer===',ans)
    return(ans)



def croppredict(N,P,K,temperature,humidity,ph,rainfall):
    
    cls=joblib.load('finalized_cropmodel.sav')
    lis=np.array([[N,P,K,temperature,humidity,ph,rainfall]],dtype=np.float64)
    ans=cls.predict(lis)[0]
    print('Answer===',ans)
    return(ans)

if __name__=="__main__":
    yieldperarea("Andaman and Nicobar Islands","NICOBARS","Whole Year ","Tapioca")
    croppredict(50,50,50,30,50,6,60)