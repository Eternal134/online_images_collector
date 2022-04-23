<template>
  <div class="block"
       @mouseenter="mouseIn=true"
       @mouseleave="mouseIn=false"
       v-show="isShow">
    <el-image :src="modelValue.src"
              class="item"
              :class="{selected : modelValue.selected}"
              :alt="modelValue.alt"
              :fit="'scale-down'"
              lazy
              @click="clickImg"
              @error="isLoadSuccess=false"
              @load="onload"
    >
    </el-image>
    <div class="size">
      {{ width }} * {{ height }}
    </div>
    <!-- 拓展菜单过渡动画 -->
    <transition name="el-zoom-in-bottom">
      <div class="expand" v-show="mouseIn">
        <!-- 页面链接 -->
        <span class="button">
          <el-link :href="modelValue.linkUrl"
                    target="_blank"
                    class="link"
          >
            <el-tooltip
                class="box-item"
                content="打开此图片指向的页面（如果有的话）"
                placement="left"
            >
              <el-button :icon="Link"
                         type="primary">
              </el-button>
            </el-tooltip>
          </el-link>
        </span>

        <span class="button">
          <el-link :href="modelValue.webUrl"
                   target="_blank"
                   class="link"
          >
            <el-tooltip
                class="box-item"
                content="打开此图片所在的页面"
                placement="top"
            >
              <el-button :icon="Link"
                         type="primary">
              </el-button>
            </el-tooltip>
          </el-link>
        </span>

        <!-- 单张图片下载 -->
        <span class="button">
        <el-tooltip
            content="下载这张图片"
            placement="right"
        >
          <el-button
            :icon="Download"
            type="primary"
            @click="downloadSingleImg(modelValue.src, modelValue.alt ? modelValue.alt : modelValue.id)"
          >
          </el-button>
        </el-tooltip>
      </span>
      </div>
    </transition>
  </div>
</template>

<script>
import { Link, Download } from '@element-plus/icons-vue'
export default {
  name: "ImgItem",

  props: {
    modelValue: Object,

    // 用户做的目标筛选
    goalsSelected: Array,
    downloadSingleImg: Function,
    // 是否显示加载错误的图片
    isShowLoadingErrorImg: Boolean,
    widthRange: Array,
    heightRange: Array
  },

  data() {
    return {
      width: 0,
      height: 0,
      // 用户鼠标是否在组件上
      mouseIn: false,
      // 图片是否加载成功
      isLoadSuccess: true,
      objLocal: this.modelValue,
    }
  },

  emits: ['update:modelValue'],

  setup() {
    return {
      Link, Download
    }
  },

  computed: {
    isShow() {

      // 如果此图片加载失败，而且设置不显示加载失败的图片
      if (!this.isLoadSuccess && !this.isShowLoadingErrorImg) {
        return false;
      }

      // 如果图片大小不符合要求
      if (!(this.width >= this.widthRange[0] && this.width <= this.widthRange[1] &&
          this.height >= this.heightRange[0] && this.height <= this.heightRange[1])) {
        return false;
      }

      // 如果图片的目标没有被选中
      if (this.goalsSelected.length !== 0 &&
          this.modelValue.goals.filter(item => this.goalsSelected.indexOf(item) > -1).length === 0) {
        return false;
      }

      return true;
    }
  },

  methods: {
    // 图片加载成功时
    onload() {
      const img = new Image();
      img.src = this.modelValue.src;
      const that = this;
      img.onload = function () {
        that.width = img.width;
        that.height = img.height;
      }
    },

    clickImg() {
      this.objLocal.selected = !this.objLocal.selected;
    }
  },

  watch: {
    // 向父组件同步obj
    objLocal: {
      handler(newObjLocal) {
        this.$emit('update:modelValue', newObjLocal)
        console.log('更新数据')
      },
      deep: true
    }
  }

}
</script>

<style scoped>

  .size {
    font-size: 14px;
    color: var(--el-text-color-secondary);
  }

  .block {
    padding: 20px 5px;
    text-align: center;
    /*border-right: solid 1px var(--el-border-color);*/
    /*把border、margin等距离算到box的大小里*/
    box-sizing: border-box;
    width: 10%;
    min-height: 150px;
    display: inline-block;
    align-items: center;
    vertical-align: top;
    position: relative;

  }

  .item {
    border: 3px solid #ddd;
    border-radius: 4px;
    padding: 4px;
    text-align: left;
    margin: 5px;
    /*设置填充到盒子中时的缩放策略*/
    object-fit: contain;
  }

  .selected {
    border: 3px solid #32f2ff;
  }

  .expand {
    width: 100%;
    height: 40px;
    bottom:0px;
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 70%;
    padding-right: 3px;
    padding-right: 10px;
    box-sizing: border-box;
  }

  .expand .button  {
    width: 50%;
  }

</style>