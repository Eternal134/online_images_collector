<template>
  <div>
    <img :src="src" class="item" :class="{selected : selected}" :alt="alt">
    <span class="size">
      {{size}}
    </span>
  </div>
</template>

<script>
export default {
  name: "ImgItem",

  props: {
    id: String,
    src: String,
    selected: Boolean,
    alt: String
  },

  data() {
    return {
      size: ''
    }
  },

  emits: ['update:obj'],

  methods: {
    clickImg() {
      console.log('clicked');
    }
  },

  mounted() {
    let img = new Image();
    img.onload = function () {
      let w = img.width;
      let h = img.height;
      this.size = `${w}*${h}`
    }
    img.src = this.src
  }

}
</script>

<style scoped>

  div {
    width: 150px;
    height: 150px;
    display: inline-block;
  }

  img {
    height: 80%;
    width: 80%;
    border: 3px solid #ddd;
    border-radius: 4px;
    padding: 4px;
    text-align: left;
    margin: 5px;
    /*设置填充到盒子中时的缩放策略*/
    object-fit: contain;
  }

  img.selected {
    border: 3px solid #32f2ff;
  }

</style>