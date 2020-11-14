def Throttling2 (event,timeline):
    drop=0
    for i in range(3,event):
        if timeline[i]==timeline[i-3]:
            drop+=1
            continue
        if i>19 and timeline[i]-timeline[i-20]<10:
            drop+=1
            continue
        if i>59 and timeline[i]-timeline[i-60]<60:
            drop+=1
            continue
    return drop