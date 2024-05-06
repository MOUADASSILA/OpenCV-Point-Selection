#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:20:15 2024

@author: mac
"""

import cv2

# Initialize a list to store coordinates
points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)  # Draw a red circle at the clicked position
        points.append((x, y))
        print(f"Point selected: ({x}, {y})")
        cv2.imshow('image', img)

if __name__=="__main__":
    # Path to your screenshot image
    image_path = "/Users/mac/Downloads/plaka.jpg"  # Change <your-username> to your actual username
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found.")
        exit()

    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Printing all selected points
    print("Selected points:")
    for point in points:
        print(point)
