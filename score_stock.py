def penalty_funct(row,ratings_name):
    score=row[ratings_name]
    if row['Close']<=5000:
        score=min(score,0.8)
    elif row['Close']==10000:
        score=min(score,0.85)
    elif row['Close']<=20000:
        score=min(score,0.9)
    else:
        score=score
    
    if row['Market']=='HNX':
        score=min(score,0.95)
    elif row['Market']=='UPCOM':
        score=min(score,0.85)
    else:
        score=score
    
    if row['Av_marketcap_60']<=0.7:
        score=min(score,0.6)
    elif row['Av_marketcap_60']<=0.75:
        score=min(score,0.75)
    elif row['Av_marketcap_60']<=0.8:
        score=min(score,0.8)
    elif row['Av_marketcap_60']<=0.85:
        score=min(score,0.85)
    elif row['Av_marketcap_60']<=0.9:
        score=min(score,0.9)
    else:
        score=score
    
    cond1=row['Market']!='UPCOM'
    cond2=row['Av_trading_60']>0.9
    cond3=row['Av_marketcap_60']>0.9
    cond4=row['LAST']>20000
    cond5=row['Av_trading_20']>0
    cond6=row['Trading_vol']>=1.5*['Av_trading_volume_20']

    if cond1&cond2&cond3&cond4&cond5&cond6:
        score=min(1,score+0.2)
    return score    