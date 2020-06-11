import cv2
import numpy as np
print("This code snipet is used to hide the information in the images ")
print("Make Sure your file is in the drive")
try:
    


    print("Enter the Image file location")
    str1=input()
    img=cv2.imread(str1)
    B,G,R=cv2.split(img)
        
    print(B)
    print(G)
    print(R)
    
    y=np.zeros(img.shape[:2],dtype="uint8")
    cb=np.zeros(img.shape[:2],dtype="uint8")
    cr=np.zeros(img.shape[:2],dtype="uint8")
    dup=np.zeros(img.shape[:2],dtype="uint8")
    
    for i in  range(len(y)):
        for j in range(len(y[i])):
            y[i,j]=(0.299*R[i,j]+0.587*G[i,j]+0.114*B[i,j])
            cb[i,j]=(128-0.169*R[i,j]-0.331*G[i,j]+0.5*B[i,j])
            cr[i,j]=(128+0.5*R[i,j]-0.419*G[i,j]-0.081*B[i,j])
    
    k=cv2.merge((y,cb,cr))
    
    kernel=np.ones((3,3),np.uint8)
    #r=cv2.Laplacian(k,cv2.CV_64F)
    #cv2.imshow("abc",r)
    #cv2.waitKey(0)
    k=cv2.erode(k,kernel,iterations=1)
    k=cv2.dilate(k,kernel,iterations=2)
    #cv2.imshow("RESULTED IMAGE",k)
    
    SOBEL_IMGy=cv2.Sobel(k,cv2.CV_64F,0,1,ksize=3)
    SOBEL_IMGx=cv2.Sobel(k,cv2.CV_64F,1,0,ksize=3)
    GRADIENT=cv2.addWeighted(SOBEL_IMGy,0.5,SOBEL_IMGx,0.5,0)
    
    
    k=cv2.erode(GRADIENT,kernel,iterations=1)
    k=cv2.dilate(GRADIENT,kernel,iterations=2)
    #cv2.imshow("EDGE DETECTION",GRADIENT)
    B,G,R=cv2.split(GRADIENT)
    #cv2.imshow("B",B)
    #cv2.waitKey(0)
    
    LIST_INDEX=[]
    
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j]==0:
                continue
            else:
                LIST_INDEX.append(i)
                LIST_INDEX.append(j)
                
                
    print()
    print()
     
    print("ENTER A STRING TO BE WATERMARKED")    
    INPUT_STR=input()
    
    print("Entered string is ",INPUT_STR,end="\n")
    
    BIN_STR=''.join(format(i,'b') for i in bytearray(INPUT_STR, encoding=' utf-8'))
    print(BIN_STR)
    G=np.zeros(img.shape[:2],dtype="uint8")
    int1=0
    int2=0
    for i in range(0,2*len(BIN_STR),2):
        int1=LIST_INDEX[i]
        int2=LIST_INDEX[i+1]
        k=int(i/2)
        if BIN_STR[k]=="1":
            G[int1][int2]=y[int1][int2]+1
        elif BIN_STR[k]=="0":
            G[int1][int2]=y[int1][int2]-1
            
    
    for i in range(len(y)):
        for j in range(len(y[i])):
            if G[i][j]==y[i][j]+1 or G[i][j]==y[i][j]-1:
                continue
            else:
                G[i][j]=y[i][j]
            
            
        
    
    
    
        
        
    
    WATER_MARK=""
    
    cv2.imshow("WATERMARK",G)
    cv2.imwrite("INFO.png",G)
    cv2.waitKey(0)
    
    
    for i in range(0,len(LIST_INDEX),2):
        int1=LIST_INDEX[i]
        int2=LIST_INDEX[i+1]
        if G[int1][int2]==y[int1][int2]+1:
            WATER_MARK=WATER_MARK+'1'
        elif  G[int1][int2]==y[int1][int2]-1:
            WATER_MARK=WATER_MARK+'0'
            
    print("WATER MARKED STRING IS")   
    print(WATER_MARK)
except:
    print("Error ,File Not Found")
    
    


    

       





            


