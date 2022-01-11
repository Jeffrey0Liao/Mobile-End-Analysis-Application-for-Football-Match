======================================================================================
=            COMP 2043.GRP Software Engineering Group Project
=                         User Interface
======================================================================================
=                          Group 14
=
--------------------------------------------------------------------------------------

This document is written to expound the components and framework of the UI code.

---------------------------------------------------------------------------------------

This project can be compiled on the WeChat-developer tool platform.

---------------------------------------------------------------------------------------

The project contains four folders and some global files to implement the UI design of a WeChat mini-program.

---------------------------------------------------------------------------------------

folder - image: store the images that used in the pages.



folder - pages: store all the pages that will be shown to user. There are 4 main pages in this project
   
   1. index: show the login interface and allow user to log in the program with WeChat ID
   2. mainPage: the upload page of this program. user can upload the video and set the tracking target, then start tracking.
   3. record: the result page of this program. show users the visual result after tracking.
   4. me: show the basic information about both user and developers.

   each page has its own folder in which there are 4 files: xx.wxml, xx.wxss, xx.js, xx.jason.
    
   xx.wxml is used complete the page design, xx.wxss is to change the style, xx.js can implement the inside logic and xx.json can implement the data exchange




folder - utils: contain the js code which is called in other js.
    
    util.js: to get the date and time
    wxcharts.js: a plug-in to implement the visualization of the project. (show kinds of charts)



app.js, app.json, app.wxss are the global files that any page of this project can use the content in those file.


======================================================================================

API used

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
















