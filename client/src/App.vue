<template>
  <meta name="referrer" content="no-referrer" />
  <div class="search">
    <input type="text" v-model="requestUrls" @keyup.enter="getCrawlImagesApi"
              placeholder="https://www.bilibili.com/">
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
      requestUrls: 'https://www.bilibili.com/'
    }
  },

  methods: {
    getCrawlImagesApi(event) {
      let form = new FormData();
      form.append('maximum', '100');
      form.append("urls", event.target.value);
      let xhr = new XMLHttpRequest();
      let baseUrl = 'http://127.0.0.1:5000/';
      let url = '/api/crawlImages';
      xhr.open('POST', baseUrl + url, true);
      // 将that指定为App组件，否则onload回调函数内部无法访问App组件*重要操作*
      const that = this
      xhr.onload = function() {
        if (xhr.status === 200) {
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
  }

  div.display {
    margin: 0 auto;
    text-align: center;
    width: 1000px;
  }

  div.search {
    text-align: center;
  }
</style>
