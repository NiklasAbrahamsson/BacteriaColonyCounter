import cv2
gray = cv2.imread("./screenshot.png", 0)

## threshold
th, threshed = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

## findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


## filter by area
s1= 3
s2 = 20
xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
        xcnts.append(cnt)

print("Dots number: {}".format(len(xcnts)))
#Dots number: 23



## Code for cloud function
# import cv2
# def hello_gcs(event, context):
#     """Triggered by a change to a Cloud Storage bucket.
#     Args:
#          event (dict): Event payload.
#          context (google.cloud.functions.Context): Metadata for the event.
#     """
#     file = event
#     print('event', event)
#     link = event['selfLink']
#     print('selflink', link)
#     path = event["id"].rsplit("/",2) 

#     path = path[0]
    
#     gray = cv2.imread(link, 0)

#     ## threshold
#     th, threshed = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

#     ## findcontours
#     cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


#     ## filter by area
#     s1= 3
#     s2 = 20
#     xcnts = []
#     for cnt in cnts:
#         if s1<cv2.contourArea(cnt) <s2:
#             xcnts.append(cnt)

#     print("Dots number: {}".format(len(xcnts)))
#     #Dots number: 23
