<template>
  <div class="static-display">
    <div>总计：{{imgCount.showedCount}}个</div>
    <div class="separated">|</div>
    <div>选中：{{imgCount.selectedCount}}</div>
  </div>
  <div class="other-infos">开发者：18756762798@163.com</div>
</template>

<script setup>

  defineProps(['imgCount']);
</script>

<style scoped>
  .static-display  {
    font-size: 18px;
    color: var(--el-text-color-secondary);
    line-height: 44px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .other-infos {
    font-size: 14px;
    color: var(--el-text-color-secondary);
    line-height: 44px;
  }

  .separated {
    /*border-right: solid 2px var(--el-text-color-secondary);*/
    margin:0px 10px;
  }
</style>