COMP 2043.GRP Software Engineering Group Project-
WeChat Based Football Movement Analysis applet

----------------------------------------------------------------------------



*Introduction
This is the software developed by Group 14 aiming at processing football videos and analyzing the movements of a single pllayer on the pitch based on deep learning strategies. 

The applet could: 
-Let users access it through WeChat offical channel (log in required)
-Let users upload videos
-Let users choose a target with bounding boxes
-Let users get visualized statistics 

-Let admins update UIs
-Let admins update classification net



*dependencies
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
- django==3.0.5



* set up
For setting up the project, please refer to chapter 3 -- How to Install the Application in the user manual. 



* APIs
======================================================================================
Basic APIs:


wx.canIUse(): determine if the API, callbacks, parameters, components, etc. are available in the current version

wx.navigateTo(): implement the page jumping

.setData(): set the data of the current page 

wx.getUserInfo(): get the WeChat basic information of the user

console.log(): print information on console

wx.request(): implement the interaction between the client and the server

wx.showModal(): display the pop-up windows (in this project: used to show the guide text)

---------------------------------------------------------------------------------------

Used for login:


wx.login(): log in the mini-program by WeChat account

wx.getSetting: request permission and get the user's current settings

wx.getUserInfo(): get the WeChat basic information of the user

---------------------------------------------------------------------------------------

Used for uploading the video and downloading the new tracked video:


wx.chooseVideo(): allow user to choose a video from user's album.

wx.uploadFile(): used to upload the file or data

wx.downloadFile(): used to download the file 

---------------------------------------------------------------------------------------

Used for getting the coordinate of the tracking target and uploading the coordinate:


wx.createSelectorQuery(): create a selector query implement

query.select().boundingClientRect(): get the callback data (height and width) of the selector


---------------------------------------------------------------------------------------

Used when waiting for analyzing the video in the beck-end algorithms:


wx.showLoading(): display the loading pop-up (in this project: used to show loading pop-up when waiting for analyzing the video)

wx.hideLoading(): hide the loading pop-up (if get the data successfully, the loading pop-up will be hide)

---------------------------------------------------------------------------------------

Used for showing the visual analyzing result:


wxCharts(): used to show different kinds of charts (column chart, pie chart, ring chart, line chart, etc., set by canvasId and type)

---------------------------------------------------------------------------------------

receive_video(request): 
obtain video from frontend and store video into proper positions(folder 'Video' in SiamMask)

index(request):         
get parameters of bounding-box from frontend and start tracking process by calling execute.sh

download(request):      
send the result of processed video back to frontend

result(request):        
send the result of predictions of movements back to frontend(which will be 4 numbers representing frequency of doing each action)


* Note that there are also specific readme files for different parts of the software in corresponding folders.
