<template>
  <meta name="referrer" content="no-referrer" />
  <div class="head">
    <div>
      <input type="text" v-model="requestUrls" @keyup.enter="getCrawlImagesApi" class="search"
                placeholder="请输入网址">
    </div>
    <div>
      <button class="btn_search" @click="getCrawlImagesApi">获取</button>
    </div>
  </div>
  <div class="display">
    <img v-for="imgSrc in imgUrls" :key="imgSrc.id" :src="imgSrc">
  </div>
  
</template>

<script>

export default {
  name: 'App',
  components: {

  },

  data () {
    return {
      imgUrls: [],
      requestUrls: ''
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
        if (xhr.status === 200) {
          console.log(xhr.response)
          // 得到返回结果的原始字符串
          let listString = JSON.parse(xhr.response).urls
          // 删除开头和结尾的[]字符
          let res = listString.slice(1, -1)
          that.imgUrls = res
        } else {
          alert('服务异常！')
        }
      };
      xhr.send(form);
    }
  }
}
</script>

<style>
  img {
    height: 90px;
    aspect-ratio: auto 135 / 90;
    width: 135px;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 4px;
    text-align: left;
    margin: 5px;
  }

  div.display {
    text-align: left;
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

  .btn_search {
    width: 30%;
    height: 30px;
    margin-top: 30px;
    border: 0px;
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
    border-bottom: 2px solid #f44336;
  }

  .btn_search:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }

</style>
