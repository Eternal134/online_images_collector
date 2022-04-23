<template>
  <div class="static-display">
    <span>总计：{{ dataCount }}个</span>
  </div>
  <div class="other-infos">开发者：18756762798@163.com</div>
</template>

<script setup>
  defineProps(['dataCount'])
</script>

<style scoped>
  .static-display  {
    font-size: 18px;
    color: var(--el-text-color-secondary);
    line-height: 44px;
  }

  .other-infos {
    font-size: 14px;
    color: var(--el-text-color-secondary);
    line-height: 44px;
  }
</style>