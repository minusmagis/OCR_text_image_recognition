import pytesseract
from tkinter import filedialog
import os
import cv2
from PIL import Image
import Small_Functions as sf

frames_directory = r'M:\EQE_Frames'
#frames_directory = r'C:\Users\minus\Documents\PhD\EQE_NXG\Frames'
frames_array_dir = os.listdir(frames_directory)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
(left, upper, right, lower) = (32, 100, 200, 160)
threshold = 140
Timer_1 = sf.Timer()
Wavelengths_list = list()

for index,frame_dir in enumerate(frames_array_dir):
    if frame_dir.endswith('png'):
        Timer_1.Update_progress(index,len(frames_array_dir),True,True)
        frame_dir = frames_directory+'\\'+frame_dir
        frame = Image.open(frame_dir)
        frame = frame.crop((left, upper, right, lower))
        frame= frame.convert('L')
        frame = frame.point(lambda p: p > threshold and 255)
        #frame.show()
        text = pytesseract.image_to_string(frame)
        Wavelengths_list.append(text)
        #print(text)

print(*Wavelengths_list, sep='\n')

# We set a name and path for the translated file with the destination language to easily differentiate the files within the save directory
Full_Scan_File = sf.Full_path_adder(('Full Scan.txt'),frames_directory)

# Finally we open or create the file and we write line by line the translated file with a new line character per line, and of course we close the file to avoid crashes
Full_Scan_File_1 = open(Full_Scan_File,'w',encoding="utf-8")
for line in Wavelengths_list:
    Full_Scan_File_1.write(str(line) + '\n')
    # print(current_image_hash)
    # print(file_duplicate_list)
Full_Scan_File_1.close()



