# coding: utf-8

# Import libraries and download any missing
import os, sys, time, multiprocessing

os.system("pip install -r requirements.txt")
import pillow, numpy, ffmpeg, pafy, vlc, cv2
from image_to_ascii import ImageToAscii

GrayScale = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". """ # 70 shades of gray

VideoUrl = input("Enter video url: ")
Video = pafy.new(VideoUrl)
BestVideo = Video.getbest(preftype="mp4")

Capture = cv2.VideoCapture(BestVideo.url)

