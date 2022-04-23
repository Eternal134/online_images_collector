<template>
  <el-menu class=el-menu-vertical-demo>

    <span class="menu-title radius" :style="{
          borderRadius: 'var(--el-border-radius-round)'}"
    >高级参数设置</span>
    <!--深度参数-->
    <div class="slider-block"
    >
      <span class="demonstration">深度</span>
      <el-tooltip class="tooltip">
        <template #content>
          此参数用于指定爬虫是否进行深度递归爬取以及指定爬取深度 <br>
          深度递归爬取是指自动将网页上的外部链接作为新的目标网页爬取图片内容
        </template>
        <el-icon class="explain-icon">
          <warning/>
        </el-icon>
      </el-tooltip>
      <el-input-number v-model="depth"
                        :max="depthMaxNum"
                        :min="0"
                        :step="1"
                       class="input-number"
      />
      <template v-if="depth > 1">
        <el-tooltip>
          <template #content>
            此参数数值会使获取结果指数级增长，设置过高可能会导致返回结果过多以及速度过慢的问题
          </template>
          <el-icon>
            <warning-filled/>
          </el-icon>
        </el-tooltip>
      </template>
    </div>
<!--翻页按钮指定-->
    <div class="page-turn">
      <div class="explain">
        <span class="demonstration">指定翻页按钮</span>
        <el-tooltip class="tooltip">
          <template #content>
            输入页面上的翻页按钮文本，工具可以完成自动翻页 <br>
            例如想要在网页https://book.douban.com/top250上使用自动翻页功能，可以在下面输入框内输入：后页>
          </template>
          <el-icon class="explain-icon">
            <warning/>
          </el-icon>
        </el-tooltip>
      </div>

      <el-input v-model="nextPageLinkText"
                maxlength="30"
                placeholder="输入页面上的翻页按钮文本"
                clearable
      >
      </el-input>
    </div>
    <!--提醒参数设置-->
    <div>
      <span class="demonstration">当数据更新时在页面上提醒我</span>
      <el-switch v-model="notify"
                 inline-prompt
                 active-text="Y"
                 inactive-text="N">
      </el-switch>
    </div>
  </el-menu>
</template>

<script setup>
import {computed, inject, ref, watch} from "vue";
import { Warning } from '@element-plus/icons'
import {ElNotification} from "element-plus";

  /* ---------------- 数据 ---------------- */
  const depth = ref(0);
  const nextPageLinkText = ref('');

  /* ---------------- 注入 ---------------- */
  // 函数注入
  const setForm = inject('setForm')
  // 数据更新时发送提醒，是否开启
  const notify = inject('notify');

  /* ---------------- 侦听器 ---------------- */

  /*监听radio和checkboxList，他们的值改变时，自动向父组件传递数据*/
  watch([depth, () => nextPageLinkText.value], () => {
    if (nextPageLinkText.value.length > 0 && depth.value > 0) {
      depth.value = 0;
      ElNotification({
        title: '已自动更改参数',
        message: '深度参数和翻页按钮不能同时指定',
        type: 'warning',
        position: 'top-left'
      })
    }
    updateForm();
  })

  /* ---------------- 方法 ---------------- */
  function updateForm() {
    setForm('depth', depth.value);
    setForm('nextPageLinkText', nextPageLinkText.value);
  }

  /* ---------------- 计算属性 ---------------- */
  // 深度参数的最大值
  const depthMaxNum = computed(() => {
    // 如果nextPageLinkText有值，则最大为0，否则为1
    return nextPageLinkText.value.length > 0 ? 0 : 1;
  })
</script>

<style scoped>
  .slider-block {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .input-number {
    margin: 20px 15px;
  }

  .demonstration {
    font-size: 14px;
    color: var(--el-text-color-secondary);
    line-height: 44px;
    flex: 1;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-bottom: 0;
    margin-right: 5px;
  }

  .page-turn {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    height: 100px;
  }

  .menu-title {
    margin: 10px 0px;
    color: var(--el-color-white);
  }

  /*not()：不选括号内的参数类*/
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    min-height: 400px;
    display: flex;
    flex-wrap: wrap;
    margin-top: 20px;
    justify-content: center;
  }

  .radius {
    height: 40px;
    width: 70%;
    border: 1px solid var(--el-border-color);
    border-radius: 0;
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color:  #409EFF;
  }
</style>