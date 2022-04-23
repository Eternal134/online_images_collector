<template>
  <div class="switch">
    <el-button v-model="isCollapse" @click="isCollapse = !isCollapse">
      <el-icon><Switch /></el-icon>
    </el-button>
  </div>

  <div v-show="!isCollapse">
    <GoalsSelect></GoalsSelect>
  </div>

  <div v-show="isCollapse">
    <ParamsSetting></ParamsSetting>
  </div>
</template>

<script setup>
  import {ref} from "vue";
  import GoalsSelect from "@/components/aside/GoalsSelect";
  import ParamsSetting from "@/components/aside/ParamsSetting";
  import { Switch } from '@element-plus/icons'

  // 是否折叠
  const isCollapse = ref(true);

</script>

<style>
  div.switch {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>