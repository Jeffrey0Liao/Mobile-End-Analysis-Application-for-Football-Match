// pages/trackSet/trackSet.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    items: [
      { name: '1', value: 'Shooting' },
      { name: '2', value: 'Passing' },
      { name: '3', value: 'Run' },
    ],
    //seleted: ""

    x: 0,
    y:0,
    scale:2,

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  upload: function () {
    wx.navigateTo({
      url: '../mainPage/mainPage'
    })
  },

  record: function () {
    wx.navigateTo({
      url: '../record/record'
    })
  },

  me: function () {
    wx.navigateTo({
      url: '../me/me'
    })
  },


  radioChange: function (e) {
    console.log('radio发生change事件，携带value值为：', e.detail.value)
    let value = e.detail.value;
    /*this.setData({
      seleted: "选中的value：" + value
    })*/
  },


  onChange(e){
    console.log(e.detail)
  },

  onScale(e){
    console.log(e.detail)
  },


  queryMultipleNodes: function(){
      //var taht = this;
      var query = wx.createSelectorQuery()
      query.select('#trackTarget').boundingClientRect()
      query.selectViewport().scrollOffset()
      
      query.exec(function (res) {
        res[0].top     // #the-id节点的上边界坐标
        res[1].scrollTop// 显示区域的竖直滚动位置
      })

},

  uploadCoord: function () {
    var query = wx.createSelectorQuery();
    var that = this;
    query.select('#trackTarget').boundingClientRect(function (rect) {
      console.log(rect.left - 7.5, rect.top - 100, rect.height, rect.width, )
      //console.log(rect.width)
      that.setData({
        height: rect.height,
        width: rect.width,
        top: rect.top,
        left: rect.left

      })
    }).exec();
  }

})