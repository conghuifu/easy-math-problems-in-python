
def scoreC(frameCount, score):
    bonus=0
    
    i = 2*frameCount
    if frame[i] == 10:
        bonus = frame[i+2] + frame[i+3]
    elif frame[i]+frame[i+1] == 10:
        bonus = frame[i+2]    
    score = score + frame[i]+frame[i+1]+bonus
    return score




frame=[8,0,1,9,4,0,9,0,10,9,1,4,2,0,3,5,5,10,10,8]
i=0
print frame
while i<20:
    if frame[i]==10:
        frame.insert(i+1,0)
    i = i+2
print frame
frameCount=0
score = 0
while(frameCount<10):
    score = scoreC(frameCount,score)
    frameCount=frameCount+1

print score
