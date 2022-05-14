import re
def solution(new_id):
    new_id = new_id.casefold()
    print("#1",new_id)
    new_id =re.sub('[^a-z-_.0-9]', '', new_id)
    print("#2",new_id)
    while(new_id.find('..')!=-1 and len(new_id)!=0):
        new_id=new_id.replace('..','.')
    print("#3",new_id)
    while(len(new_id)!=0 and new_id[0]=='.' ):
        new_id=new_id[1:]
    print("#4",new_id)
    while(len(new_id)!=0 and new_id[len(new_id)-1]=='.' ):
        new_id=new_id[:len(new_id)-1]
    print("#4",new_id)
    
    if(len(new_id)==0):
        new_id+='a'
    print("#5",new_id)
    
    if(len(new_id)>=16):
        new_id = new_id[0:15]
    print("#6",new_id)
    
    while(len(new_id)!=0 and new_id[len(new_id)-1]=='.'):
        new_id=new_id[:len(new_id)-1]
    print("#7",new_id)
    
    while(len(new_id)<=2):
        new_id+=new_id[len(new_id)-1]
    print("#8",new_id)
    
    
    print(new_id)
    return new_id
