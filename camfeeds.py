import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
import cv2

url = 'http://192.168.1.32:4200/cam'
cap = cv2.VideoCapture(url)
#Function to display camera feed without overlay
def update_camera_feed(bottom_left_frame,top_left_frame):

    # def detection(frame2):
    # 
    #     # Grayscale
    #     gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # 
    #     # Gaussion Blur
    #     blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # 
    #     # Find Canny edges
    #     edged = cv2.Canny(blurred, 30, 200)
    # 
    #     r_x, r_y, r_width, r_height = 100, 100, 300, 300  # camera at home
    #     # r_x, r_y, r_width, r_height = 300, 100, 800, 500 #camera at school
    # 
    #     # Draw a rectangle around the ROI on the original frame
    #     # cv2.rectangle(frame2, (r_x, r_y), (r_x + r_width, r_y + r_height), (255, 0, 0), 2)
    #     #
    #     # # Apply the defined ROI on the processed edge image
    #     # roi_edges = edged[r_y:r_y + r_height, r_x:r_x + r_width]
    # 
    #     # Finding Contours
    #     contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # 
    #     # Ensure that contours are found before proceeding
    #     if len(contours) >= 2:
    #         # Sort contours by area to find the largest ones (2 curved lines)
    #         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:4]
    # 
    #         # Draw all contours within the ROI
    #         for contour in contours:
    #             contour += (r_x, r_y)  # Offset contour points to match ROI in the original frame
    #             cv2.drawContours(frame2, [contour], -1, (0, 255, 0), 4)
    # 
    #     # # draw midline
    #     # try:
    #     #     cv2.polylines(frame, [np.array(midCalc(contours))], False, (0, 0, 255), 4)
    #     # except cv2.error:
    #     #     pass
    # 
    #     # display frame
    #     return frame2


    # Function to convert OpenCV image to Tkinter PhotoImage
    def convert_to_photo_image(frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)
        return photo


    # Create a label within top_left_frame for displaying the camera feed
    camera_feed_label = tk.Label(bottom_left_frame)
    camera_feed_label.pack()

    ret, frame = cap.read()
    photo = convert_to_photo_image(frame)
    camera_feed_label.configure(image=photo)
    camera_feed_label.image = photo



