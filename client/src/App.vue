<template>
  <meta name="referrer" content="no-referrer" />
  <div class="head">
    <div>
      <input type="text" v-model="requestUrls" @keyup.enter="getCrawlImagesApi" class="search"
                placeholder="请输入网址">
    </div>
    <div>
      <button class="btn_search" @click="getCrawlImagesApi">获取</button>
      <button class="btn_clear" @click="clearAll">清空</button>
      <button class="btn_download" @click="downloadImg">下载</button>
      <button class="btn_select_all" @click="selectAll">全选</button>
      <button class="btn_cancel_select_all" @click="cancelSelectAll">全不选</button>
      <button class="btn_invert_select" @click="invertSelect">反选</button>
    </div>

  </div>
  <div class="display">
    <ImgItem v-for="obj in imgObj" v-bind="obj" :key="obj.id" :id="obj.id" @click="clickImg"/>
  </div>
  
</template>

<script>

import ImgItem from "@/components/ImgItem";
// import download from 'ly-downloader'
export default {
  name: 'App',
  components: {
    ImgItem
  },

  data () {
    return {
      imgObj: [],
      requestUrls: 'https://www.bilibili.com/'
    }
  },

  methods: {
    getCrawlImagesApi() {
      let form = new FormData();
      form.append('maximum', '100');
      form.append("urls", this.requestUrls);
      let xhr = new XMLHttpRequest();
      let baseUrl = 'http://127.0.0.1:5000/';
      let url = '/api/crawlImages';
      xhr.open('POST', baseUrl + url, true);
      // 将that指定为App组件，否则onload回调函数内部无法访问App组件*重要操作*
      const that = this
      xhr.onload = function() {

        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            // 得到返回结果的原始字符串
            let res = JSON.parse(xhr.response)
            console.log(res)
            if (res.code !== 0) {
              alert(res.msg)
            }
            let list = res.data.data;
            list.forEach(item => item.selected = true);
            that.imgObj = that.imgObj.concat(list);
          } else {
            alert('服务异常！');
          }
        }
      };
      try {
        xhr.send(form);
      } catch (e) {
        alert('服务异常！');
      }
    },

    clickImg(event) {
      let targetSrc = event.target.src;
      let targetObj = this.imgObj.filter(item => item.src === targetSrc)[0];
      targetObj.selected = !targetObj.selected;
    },

    clearAll() {
      this.imgObj = []
    },

    /*下载所有已选中的图片*/
    downloadImg() {
      // let selectedSrc = [];
      for (let i = 0; i < this.imgObj.length; i ++) {
        let obj = this.imgObj[i];
        if (obj.selected === true) {
          let targetSrc = obj.src
          let imgXhr = new XMLHttpRequest();
          imgXhr.open('GET', targetSrc, true)
          imgXhr.responseType = 'blob'
          imgXhr.onload = function() {
            let url = window.URL.createObjectURL(imgXhr.response)
            let a = document.createElement('a');
            a.href = url
            // 支持的图片文件格式罗列在这里
            let supportImgFormat = ['jpg', 'png', 'gif'];
            // 尝试从图片链接中解析出原图的文件格式
            let targetImgFormat = targetSrc.split('.').pop();
            // 文件后缀指定一个默认值
            let fileSuffix = targetImgFormat.toLowerCase() in supportImgFormat ? targetImgFormat : 'png';
            // 指定文件名
            let fileName = obj.alt ? obj.alt : obj.id;
            a.download = fileName + '.' + fileSuffix;
            a.click()
          }
          imgXhr.send()
        }
      }
    },

    /*全选*/
    selectAll() {
      this.imgObj.forEach(item => item.selected = true)
    },

    /*全不选*/
    cancelSelectAll() {
      this.imgObj.forEach(item => item.selected = false)
    },

    /*反选*/
    invertSelect() {
      this.imgObj.forEach(item => item.selected = !item.selected)
    }
  }
}
</script>

<style>

  div.display {
    /*text-align: left;*/
    caret-color: rgba(0,0,0,0);
    margin: 50px 100px 0;
  }

  div.head {
    text-align: center;
    margin: 50px 600px;
  }

  input.search {
    text-align: left;
    outline-style: none;
    padding: 10px 0px 10px 10px;
    width: 100%;
    border: 0px;
    border-bottom: 2px solid #f44336;
    border-radius: 3px;
  }

  button {
    width: 30%;
    height: 30px;
    margin-top: 30px;
    margin-right: 30px;
    border: 0px;
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
    border-bottom: 2px solid #f44336;
  }

  button:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }

</style>
