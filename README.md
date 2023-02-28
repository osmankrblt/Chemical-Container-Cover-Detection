# Chemical Container Cover Detection

> This project is my internship project made for <b>EGEROBOT - isgsis</b>

<p>Result Project</p>
<img src="static images/result.png" height="480">

<details>
<summary> Project Chart Diagram </summary>
   <br />
   <p> I used this Chart Diagram for development process </p>

// <img src="https://user-images.githubusercontent.com/59209205/204371290-11db1d23-6452-429e-a4cd-4704fb4eb624.png">
</details>

# Dataset process
> You can use dataset_process.ipynb file If you want to convert video to images (# Generally 1 second video has 30 frames.For example If frameRate value is 30.This mean is you take one frame for every second)

# Created new  Yolov7 Function
> I created this function for object to mark. (If would like to use this function.You must paste into the plots.py and you must change plot_one_box func with plot_one_marker in detect.py)


<details>
<summary> Function Result Image </summary>
  

<img src="static images/myFuncResult.jpg">
</details>

    def plot_one_marker(x, img,color=None, label=None, line_thickness=3):
        # Plots one bounding marker on image img
        tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
        color = color or [random.randint(0, 255) for _ in range(3)]
        c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
        
        makerHeight = c2[1] - c1[1]
        makerWidth = c2[0] - c1[0]
        
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 2, thickness=tf)[0]
        
        cv2.line(img,(c2[0],c1[1]),(c2[0]+t_size[0],c1[1]),color,2)
        cv2.line(img,(c1[0]+(makerWidth//2),int(c1[1]+makerHeight*0.2)),(c2[0],c1[1]),color,2)
        
        if label:
            
            
            cv2.rectangle(img, (c2[0],c1[1]), (c2[0]+t_size[0],c1[1]-t_size[1]-8), color, -1, cv2.LINE_AA)  # filled
            cv2.rectangle(img, (c2[0],c1[1]), (c2[0]+t_size[0],c1[1]+t_size[1]), color, -1, cv2.LINE_AA)  # filled

            textColor = [255,255,255] if color == [0,0,255] else [0,0,0]
            cv2.putText(img, label, (c2[0],c1[1]-8), 0, tl / 2, textColor, thickness=tf, lineType=cv2.LINE_AA)
            cv2.putText(img, "EGEROBOT - isgsis", (c2[0],c1[1]+8), 0, tl / 2, textColor, thickness=tf, lineType=cv2.LINE_AA)
            
<br />
<p> EGEROBOT - isgsis </p>

<img src="https://user-images.githubusercontent.com/59209205/204371435-90349413-4b70-441b-af1e-e8ddf105b9fa.png">
