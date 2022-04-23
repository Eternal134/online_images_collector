<template>
  <meta name="referrer" content="no-referrer" />

  <el-container>
    <!-- 侧边栏 -->
    <el-aside width="300px">
      <AsideMenu></AsideMenu>
    </el-aside>
    <el-container>
      <!-- 头部 -->
      <el-header class="header">
        <div>
          <el-input type="text" v-model="requestUrls" @keyup.enter="triggerImgCrawler" class="search"
                    placeholder="请输入想要爬取图片网址"
                    clearable
                    :prefix-icon="Search"
                    maxlength="200"
          />
        </div>
        <div>
          <el-button type="primary" round class="btn_search" @click="triggerImgCrawler">获取</el-button>
          <el-button type="primary" round class="btn_clear" @click="clearAll">清空</el-button>
          <el-button type="primary" round class="btn_download" @click="downloadImg">下载</el-button>
          <el-button type="primary" round class="btn_select_all" @click="selectAll">全选</el-button>
          <el-button type="primary" round class="btn_invert_select" @click="invertSelect">反选</el-button>
        </div>
      </el-header>
      <!-- 核心内容区 -->
      <el-main  v-loading="loading">
        <template v-if="!imgObj.length">
          <el-empty></el-empty>
        </template>
        <!-- 显示全部图片 -->
        <el-scrollbar height="500px">
          <template v-for="obj in imgObj" :key="obj.id">
            <ImgItem :model-value="obj"
                     :id="obj.id"
                     :downloadSingleImg="downloadSingleImg"
                     :isShowLoadingErrorImg="isShowLoadingErrorImg"
                     :widthRange="widthRange"
                     :heightRange="heightRange"
                     :goalsSelected="goalsSelected"
                     :clickImg="clickImg"
                     @update:modelValue="updateObj"
            />
          </template>
        </el-scrollbar>
      </el-main>
      <!--    footer   -->
      <el-footer class="footer">
        <MyFooter :dataCount="imgObj.length"></MyFooter>
      </el-footer>
    </el-container>
  </el-container>

  <el-backtop :right="100" :bottom="100" />
  
</template>

<script setup>

  import ImgItem from "@/components/ImgItem";
  import AsideMenu from "@/components/AsideMenu";
  import { Search } from '@element-plus/icons-vue';
  import { onMounted, provide, ref } from "vue";
  import { ElMessage, ElMessageBox, ElNotification } from 'element-plus'
  import MyFooter from "@/components/MyFooter";

  /* ---------------- 数据 ---------------- */

  // 保存图片结果
  const imgObj = ref([]);
  // 最大数据量
  const maxDataCount = 300;
  // 数据更新计数
  let updateOrder = 0;
  // 保存请求地址
  const requestUrls = ref('');
  // 向后端发送请求的唯一id
  const requestId = ref('')
  // 后端服务地址
  const backendBaseUrl = ref('http://127.0.0.1:5000/')
  // 定时器
  const interval = ref(null)
  // 图中目标筛选
  const goalsSelected = ref([])
  // 后端请求表单
  const form = ref(new FormData());
  // 数据展示区正在加载状态
  const loading = ref(false);
  // 数据更新时发送提醒，是否开启
  const notify = ref(true);
  // 是否显示加载失败的图片
  const isShowLoadingErrorImg = ref(false);
  // 图片显示的宽度范围
  const widthRange = ref([0, 4800]);
  // 图片显示的高度范围
  const heightRange = ref([0, 2800]);

  /* ---------------- 生命周期 ---------------- */

  onMounted(() => {
    console.log('app组件挂载')
    clearInterval(interval)
  })

  /* ---------------- 供给 ---------------- */

  // 供给数据和对应的更新方法
  provide('goalsSelected', goalsSelected)
  provide('updateGoals', updateGoalsSelected)
  provide('form', form)
  provide('setForm', setForm)
  provide('notify', notify)
  provide('isShowLoadingErrorImg', isShowLoadingErrorImg)
  provide('widthRange', widthRange)
  provide('heightRange', heightRange)

  /* ---------------- 计算属性 ---------------- */

  /* ---------------- 消息通知 ---------------- */

  /*提示服务错误信息*/
  function displayServerErrorMessage() {
    ElMessageBox.confirm(
        '服务暂不可用！请联系管理员！',
        '遇到了一个错误',
        {
          type: 'error',
          confirmButtonText: '发送报错信息',
          cancelButtonText: '取消',
          showClose: false
        }
    ).then(() => {
      ElMessage({
        message: '感谢您的反馈',
        type: 'success'
      })
    }).catch(() => {

    })
  }

  /*取消确认消息框的提示信息*/
  function cancelConfirmBox() {
    ElMessage({
      message: '已取消',
      type: 'success'
    })
  }

  /*数据更新通知*/
  function displayDataUpdateNotification() {
    ElNotification({
      title: '数据更新',
      message: '成功获取到新数据',
      // 通知停留时间，单位：毫秒
      duration: 3 * 1000
    })
  }

  /* ---------------- 方法 ---------------- */

  /*触发后端图片爬虫*/
  function triggerImgCrawler() {

    if (requestUrls.value.length === 0) {
      ElMessage({
        message: '还未输入网址',
        type: 'error'
      })
      return
    }

    // 重置数据版本
    updateOrder = 0;
    closeInterval();
    requestId.value = require('shortid').generate();
    form.value.set("requestId", requestId.value);
    form.value.set("urls", requestUrls.value);
    let xhr = new XMLHttpRequest();
    let url = '/api/trigger';
    xhr.open('POST', backendBaseUrl.value + url, true);
    xhr.onload = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          // 设置定时器获取后端结果
          interval.value = setInterval(obtainResult, 1*1000);
          console.log('创建定时器获取后端数据,id=' + interval.value);
          loading.value = true;
          // 提示消息
          ElMessage({
            message: '正在获取',
            type: 'success'
          })
        } else {
          alert('服务异常！');
        }
      }
    };
    xhr.onerror = function() {
      displayServerErrorMessage()
    }
    try {
      xhr.send(form.value);
    } catch (e) {
      alert('服务异常！');
    }
  }

  /*获取后端处理结果*/
  function obtainResult() {
    let url = '/api/obtain';
    let xhr = new XMLHttpRequest();
    xhr.open('GET', backendBaseUrl.value + url + `?requestId=${requestId.value}`, true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        let res = JSON.parse(xhr.response)
        // 如果后端返回了错误信息
        if (res.code !== 0) {
          console.log(res.msg)
          closeInterval()
          displayServerErrorMessage()
          loading.value = false;
          return
        }
        let _updateOrder = res.data.updateOrder;
        // 如果数据为更新版本
        if (updateOrder < _updateOrder) {
          console.log('数据更新！updateOrder=' + _updateOrder)
          // 新建一个空的goalObjMap用于保存新的数据，对应goalObjMap
          // let newGoalObjMap = new Map()
          let list = res.data.itemList;
          // 临时存储结果
          let resList = [];
          for (const item of list) {
            item.selected = false;
            item.show = true;
            // 如果图片没有被检测出任何一种目标，增加一个'其他'标签
            item.goals = item.goals.length ? item.goals : ['others'];
            // 如果已经超出最大数据量，结束循环，不再接收数据
            if (resList.length > maxDataCount) {
              break
            } else {
              resList.push(item)
            }
          }
          updateOrder = _updateOrder;
          // 新数据覆盖旧数据
          imgObj.value = resList;
          if (notify.value) {
            displayDataUpdateNotification();
          }
          // 正在加载状态设置为假
          loading.value = false;
          }
      } else {
        alert('服务异常！')
      }
    }
    xhr.send();
  }

  /*鼠标点击图片区域时*/
  function clickImg(event) {
    let targetSrc = event.target.src;
    let targetObj = imgObj.value.filter(item => item.src === targetSrc)[0];
    targetObj.selected = !targetObj.selected;
  }

  /*清空所有结果*/
  function clearAll() {
    ElMessageBox.confirm(
        '确定清空当前所有内容吗？',
        '清空',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
    )  // 用户选择确认时
        .then(() => {
      imgObj.value = [];
      loading.value = false;
      closeInterval();
      ElMessage({
        type: 'success',
        message: '已清空'
      })
    }) // 用户选择取消时
      .catch(() => {
        ElMessage({
          type: 'info',
          message: '已取消'
        })
      })
  }

  /*关闭定时器*/
  function closeInterval() {
    console.log('清除定时器id=' + interval.value)
    clearInterval(interval.value);
  }

  /*下载所有已选中的图片*/
  function downloadImg() {
    ElMessageBox.confirm(
        '所有选中图片将通过浏览器默认方式下载，建议不要设置浏览器中"每次下载文件时提醒我"选项，是否继续？',
        '确认下载文件',
        {
          type: 'info',
          confirmButtonText: '继续',
          cancelButtonText: '取消',
          showClose: false
        }
    ).then(() => {
      // 是否下载了至少一张图片标记
      let isDownloadedAnyOne = false;
      for (let i = 0; i < imgObj.value.length; i ++) {
        let obj = imgObj.value[i];
        if (obj.selected === true) {
          isDownloadedAnyOne = true;
          downloadSingleImg(obj.src, obj.alt ? obj.alt : obj.id)
        }
      }
      // 如果一张照片都没有下载，弹出提示
      if (!isDownloadedAnyOne) {
        ElMessageBox.alert(
            // 第一个参数：提示内容
            '<span style="{font-size: 20px}">请选择至少一张图片</span>',
            // 第二个参数：标题
            '提示',
            // ElMessageBox配置项
            {
              // 确认按钮文字
              confirmButtonText: '好的',
              // 提示框类型
              type: 'warning',
              // 文字居中
              center: false,
              // 将消息解释为html文本
              dangerouslyUseHTMLString: true,
              // MessageBox 是否显示右上角关闭按钮
              showClose: false,
            })
      } else {
        ElMessage({
          message: '正在下载',
          type: 'success'
        })
      }
    }).catch(() => {
      cancelConfirmBox()
      return
    })
  }

  /*下载单张图片
  * @targetSrc 目标地址
  * @alt 图片描述信息，用于生成文件名*/
  function downloadSingleImg(targetSrc, alt) {
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
      let fileName = alt;
      a.download = fileName + '.' + fileSuffix;
      a.click()
    }
    imgXhr.send()
  }

  /*全选*/
  function selectAll() {
    imgObj.value.forEach(item => item.selected = true)
  }

  /*反选*/
  function invertSelect() {
    imgObj.value.forEach(item => item.selected = !item.selected)
  }

  /*更新goalsSelected数据*/
  function updateGoalsSelected(newData) {
    goalsSelected.value = newData;
  }
  
  /*设置表单*/
  function setForm(key, value) {
    form.value.set(key, value)
  }

  function updateObj(newObj) {
    let target = imgObj.value.filter(_ => _.id==newObj.id)[0];
    target.selected = newObj.selected;
  }
</script>

<style>

  .header {
    text-align: center;
    margin: 50px 60px;
  }

  button {
    margin-top: 30px;
  }

  button:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }

  .footer{
    height:50px;
    position:absolute;
    bottom:0px;
    left:0px;
    border-top: solid 1px var(--el-border-color);
  }


</style>
