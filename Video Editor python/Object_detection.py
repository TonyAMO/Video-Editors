from imageai.Detection import VideoObjectDetection
import os
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("C:\Datasets\yolov3.pt")
detector.loadModel()
detector.useCPU()
execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "C:\Datasets\yolov3.pt"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "C:\Datasets\MLB.mp4"),
                            output_file_path=os.path.join(execution_path, "MLB_detection")
                            , frames_per_second=20, log_progress=True)
print(video_path)
