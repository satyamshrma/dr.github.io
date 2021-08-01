#!/usr/bin/env python
# coding: utf-8

# In[42]:


from disease1 import maleria,covid,typhoid,piles,pcod,colitis,uti,jaundice
su={"fever","chills","fatigue","paininurination","pain in lower abdomen"}
sm={"high grade fever","vomiting","weakness","chills","chest pain","headache","cough","fever"}
scovi={"high grade fever","low grade fever","sorethroat","runnynose","high weakness","fatigue","chestpain","lowoxygen level","loss of taste and smell"}
st={"persistent low grade fever","loose motions","stomachpain"}
sc={"frequent motions","digestion issues","stomachache"}
sj={"nausea","weightloss","stomachfullness","yellow skin","yellow eyes"}
sp={"irregular menstrual cycle","increase in weight","moodswing","hairfall"}
spile={"pain during passing stool","bleeding from colon","constipation"}
import sys
def d(*symptoms):
    while(True):
        ch=list(symptoms)
        ch=set(ch)
        if ch.issubset(su)==True:
            return(uti())
            break
        elif ch.issubset(sm)==True:
            return(maleria()) 
            break
        elif ch.issubset(scovi)==True:
            return covid()
            break
        elif ch.issubset(st):
            return typhoid()
            break
        elif ch.issubset(sc)==True:
            return colitis()
            
        elif ch.issubset(sj)==True:
            return jaundice()
        elif ch.issubset(sp)==True:
            return pcod()
        elif ch.issubset(spile)==True:     
            return piles()
        elif ch==set("thankyou"):
            return("THANK YOU  FOR USING DR BANSAL'S AI BASED CLINIC APPLICATION","GET WELL SOON")
            sys.exit()
        else:
            return("invalid input")
import gradio
gradio.Interface(d,inputs=["text","text","text"],outputs="text",title="WELCOME TO DR BANSAL'S AI BASED CLINIC",description="ENTER  THREE MAJOR SYMPTOMS , USE ONLY SMALL LETTERS").launch(share=True)   


# In[ ]:





# In[32]:



        


# In[ ]:





# In[ ]:




