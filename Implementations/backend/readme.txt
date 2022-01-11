
This is the explanation file in details for developers who would transplant this core function algorithm.
If you want to know how to install applications please go to user_manual.doc.



Third-party dependencies:
- Cython==0.29.4
- colorama==0.3.9
- numpy==1.15.4
- requests==2.21.0
- fire==0.1.3
- torch==0.4.1
- matplotlib==2.2.3
- numba==0.39.0
- scipy==1.1.0
- h5py==2.8.0
- pandas==0.23.4
- tqdm==4.29.1
- tensorboardX==1.6
- opencv_python==3.4.3.18
- torch==0.4.1
- torchvision==0.2.1

* note that these dependencies are provided by the file 'requirements.txt' appended in the source code of Siammask
* note that the version of each library does not need to strictly conform with the recommandation. However, the version of the library 'Pillow' (maybe a sub-library in one of these libraries) should be less than 7.0.0, otherwise it causes problems.



source code structure:
grp_backend/Siammask/data/...
                    /datasets/...
                    /experiments/...
                    /models/...
                    /tools/demo.py
                	  /test.py
                    /utils/...
                    /Video/xxxxx.mp4
                          /00001.jpg~000xx.jpg
                          /processed/1.jpg~xx.jpg
                                    /processed.mp4
                                    /Result.txt
                          /Result/1.jpg~xx.jpg
           /Django/manage.py
                  /include/..
                  /Lib/..
                  /myDjango/view.py
                  /NewDjango/url.py
                  /Scripts/..
                  /templates/..
           /execute.sh
           /readme.txt


* folder 'SiamMask' contains neural networks and algorithms for calculating and data processing, 
  while folder 'Django' contains python based Web framework used to interact with frontend. The 'execute.sh' plays roles of making bridge between two parts.

*********SiamMask********
* This folder contains both SiamMask network(for tracking object) and Lenet(for predicting movements)
* you should invoke the program by using execute.sh :"bash execute.sh x y height width"
                                                     (x y height width is four properties of bounding box)
  before starting program, the original video should be stored in folder'Video'
* The two highlighted files (grp_backend/Siammask/tools/demo.py, test.py) are mainly modified.
  As in test.py we changed the pattern of the returning bounding box, from totating rect to right rect.
  In demo.py, we implement main functions required by this project.

* Elaboration of important lines of code:
  (note that the line number could not be precise)
	In demo.py:
	line 59: location = state['ploygon'] (returns the index of current bounding box with the structure of [left-upper X, left-upper Y, width, hight])
	line 62: save_path = '../resultSet/'+str(f)+'.jpg' (the save path of tracking result by pictures, could be porperly modified)
	line 68: cv2.imwrite(save_path, resized) (save the resized picture)
	line 85: data = [cv2.imread(imf, cv2.IMREAD_GRAYSCALE) for imf in data_files] (load pictures for classification with the structure of [img])
	line 89: lenet = torch.load('net.pkl') (load pretrained classification network from the path)
	line 100: result.append(prediction_y) ('result' is the array contains the classification results in enumerate order)

* Note that the three path appeared are encouraged to be modified as relative paths.
* Note that 'net.pkl' is the net model file.
* Note that the folder 'Video' is used to store both original videos as well as processed data and all the result files
  Inside folder 'Video': xxxx.mp4 is original video(which should exist before execution of program).
  After execution of program: 00001.jpg-000xx.jpg is the image which will be generated which is each frame of original video.
                              The folder 'processed' will be generated which contains:
                                      1.jpg-xx.jpg:  each frame which has added bounding box and mask on target
                                      processed.mp4: output video after execution(which has bounding box and mask on target)
                                      Result.txt:    the prediction result on each frame (0 1 2 3 represents no-ball, passing, shooting and dribbling respectively)
                              The folder 'Result' contains 1.jpg-xx.jpg which is 50*50 gray size image which is cut from bounding-box (only have target in the image)
  

*********Django**********
* This folder contains Django used to build up local sever
* The manager.py is used to acitvate sever: "python3 manage.py runserver 0.0.0.0:8000"
* In folder 'NewDjango', the file 'urls.py' gives lists of urls and will call corresponding funtions in MyDjango/views.py based on each url
* In folder 'myDjango', the file 'views.py' manipulate each request from frontend:
                receive_video(request): obtain video from frontend and store video into proper positions(folder 'Video' in SiamMask)
                index(request):         get parameters of bounding-box from frontend and start tracking process by calling execute.sh
                download(request):      send the result of processed video back to frontend
                result(request):        send the result of predictions of movements back to frontend(which will be 4 numbers representing frequency of doing each action)
 




