import threading as thr
import concurrent.futures
import time
import os
import pandas as pd
import cv2, time


CCTV_all = pd.read_pickle('C:/Users/jerry/Desktop/opencv/traffic_volume_predict/CCTV_full_all.pkl')


def capture_frames(a):
    res = []
    for i in range(a,a+10):
        cap = cv2.VideoCapture(CCTV_all['VideoStreamUrl'][i])
        print(cap.isOpened())


if __name__ == '__main__':
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as exec:
        results = exec.map(capture_frames,[0,10,20,30,40,50,60,70,80,90])
        # for f in results:
        #     print(f)

    end = time.perf_counter()

    print(f'It takes {round(end - start)} seconds')

