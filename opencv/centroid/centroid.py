import cv2
def show(img):
    cv2.imshow("www", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
i = cv2.imread("../imgs/zeroth-order.png")
show(i)
gr = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
show(gr)
gr.shape
show(gr)
xi, yi = gr.shape
pts = 0
sumx = 0; sumy = 0
for x in range(xi):
    for y in range(yi):
        if gr[x][y] == 255:
            sumx = sumx +x
            sumy = sumy +y
            pts = pts +1
cx = sumx / pts
cy = sumy / pts
cx
cy
cx = int(cx)
cy = int(cy)
cntr = cv2.circle(gr, (cx,cy),5,(255,0,0),-1)
show(cntr)
"""

%history

In [39]: center = %history
import cv2
i = cv2.imread("zeroth-order.png")
cv2.imshow(i)
cv2.imshow("tits", i)
def show(img):
    cv2.imshow("www", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
show(i)
i
gr = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
show(gr)
import numpy as np
gt
gr
len(gr)
type(gr)
gr.shape
show(gr)
 xi, yi = gr.shape
sumx = 0; sumy = 0
for x in range(xi):
    for y in range(yi):
        if gr[x][y] == 255:
            sumx = sumx +x
            sumy = sumy +y
sumy
sumx
pts = 0
sumx = 0; sumy = 0
for x in range(xi):
    for y in range(yi):
        if gr[x][y] == 255:
            sumx = sumx +x
            sumy = sumy +y
            pts = pts +1
pts
240*320
cx = sumx / pts
cy = sumy / pts
cx
cy
show(gr)
import matplotlib.pyplot as plt
plt.plot(gr)
cntr = cv2.center(gr, (cx,cy),5,(255,0,0),-1)
cntr = cv2.circle(gr, (cx,cy),5,(255,0,0),-1)
cx = int(cx)
cy = int(cy)
show(cntr)
%history

"""
