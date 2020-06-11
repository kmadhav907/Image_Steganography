import cv2
import numpy as np


        



try:
            print("Enter the file name")
            str1=input()
            img=cv2.imread(str1)
            B,G,R=cv2.split(img)
                
            #print(B)
            #print(G)
            #print(R)
            
            y=np.zeros(img.shape[:2],dtype="uint8")
            cb=np.zeros(img.shape[:2],dtype="uint8")
            cr=np.zeros(img.shape[:2],dtype="uint8")
            dup=np.zeros(img.shape[:2],dtype="uint8")
            
            for i in  range(len(y)):
                for j in range(len(y[i])):
                    y[i][j]=(0.299*R[i][j]+0.587*G[i][j]+0.114*B[i][j])
                    cb[i][j]=(128-0.169*R[i][j]-0.331*G[i][j]+0.5*B[i][j])
                    cr[i][j]=(128+0.5*R[i][j]-0.419*G[i][j]-0.081*B[i][j])
            
                    
                
            #cv2.imshow("Y Component",y)
            #cv2.waitKey(0)
            
            print("Enter the string")
            print()
            INPUT_STR=input()
            print()
            print("Entered string is ",INPUT_STR,end="")
            print()
            
            BIN_STR=''.join(format(i,'b') for i in bytearray(INPUT_STR, encoding=' utf-8'))
            
            print(BIN_STR)
            print(type(BIN_STR))
            WATER_MARK=""
            
            for i in range(len(BIN_STR)):
             if BIN_STR[i]=="1":
              dup[i][i]=y[i][i]+1
             else:
              dup[i][i]=y[i][i]-1
              
              
            for i in range(len(y)):
             for j in range(len(y[i])):
              if (dup[i][j]==y[i][j]+1) or(dup[i][j]==y[i][j]-1):
               continue
              else:
               dup[i][j]=y[i][j]
               
               
            for i in range(len(y)):
                for j in range(len(y[i])):
                 if dup[i][j]==y[i][j]+1:
                  WATER_MARK+="1"
                 elif dup[i][j]==y[i][j]-1:
                  WATER_MARK+="0"
                  
                    
                
            
               
               
              
              
                
             
                
            
            
            print(WATER_MARK)
            
            
             
            
            
            
            
            cv2.imshow("WATER",dup)
            cv2.waitKey(0)
except:
 print("Error,File Not Found")
 
 
  
   
    
     
   
     
      
 
       
         
     
 
