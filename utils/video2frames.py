def sepVideo(videoPath,saveFolderName,frameRate=20):

    try:    
        import cv2,os

        os.chdir(".")
        cap = cv2.VideoCapture(videoPath)
        frameNum = 0
      
        if os.path.isdir(saveFolderName) == False:
            os.mkdir(saveFolderName)

        videoInf = True
    
        while videoInf:

            videoInf,frame = cap.read()

            if frameNum%frameRate == 0 and videoInf == True:
                cv2.imwrite(saveFolderName+"/{}-{}.jpg".format(videoPath.split("/")[-1],frameNum//frameRate),frame)
            
            frameNum +=1
        
        
    except Exception as e: 
        print("Something wrong + ",e)
    
    finally:
        cap.release()
        print("Process was successfully")

        

