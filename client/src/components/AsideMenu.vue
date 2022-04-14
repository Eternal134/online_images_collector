<template>


  <el-switch
      v-model="isRadio"
      active-text="单选模式"
      inactive-text="多选模式"
      @change="update"
      class="switch center-item"
  />

  <el-menu
      class="el-menu-vertical-demo"
  >
    <!-- 图片内容筛选 -->

    <div class="menu">

      <!--    单选    -->
      <template v-if="isRadio">
        <el-radio-group
            v-model="radio"
            :class="groupClass"
        >
          <el-radio v-for="goal in presetGoals" :key="goal.label" :label="goal.label"
                    border
                    class="item button"
          >
            {{ goal.name }}
          </el-radio>
        </el-radio-group>
      </template>

      <!-- 多选 -->
      <template v-if="!isRadio">

        <el-checkbox
            v-model="isAllChecked"
            :indeterminate="indeterminate"
            @change="checkAll"
            class="check-all center-item"
        >全选
        </el-checkbox>

        <el-checkbox-group
            v-model="checkbox"
            :class="groupClass"
        >
          <el-checkbox v-for="goal in presetGoals" :key="goal.label" :label="goal.label"
                       border
                       class="item button"
          >{{ goal.name }}
          </el-checkbox>

        </el-checkbox-group>
      </template>
    </div>
  </el-menu>
</template>

<script setup>
import {computed, reactive, ref, watch} from "vue";

  const props = defineProps(['goalsSelected']);
  // 多选框选择结果
  const checkbox = ref(props.goalsSelected);
  // 单选框选择结果
  const radio = ref(checkbox.value[0]);
  // 是否是单选模式
  const isRadio = ref(false);
  // 绑定按钮组的属性
  const groupClass = reactive({
    group: true
  })

  class goal {
    constructor(label, name) {
      this.label = label;
      this.name = name;
    }
  }
  // 可供选择的选项
  const presetGoals = ref([
      new goal('person', '人'),
      new goal('cat', '猫'),
      new goal('dog', '狗'),

      new goal('others', '其他')
  ])

  const emit = defineEmits(['update:goalsSelected']);

  /* ---------------- 方法 ---------------- */

  /*向父组件更新数据*/
  function update() {
    const data = isRadio.value ? [radio.value] : checkbox.value;
    emit('update:goalsSelected', data);
  }

  /*全选，仅适用于多选模式*/
  function checkAll() {
    checkbox.value = isAllChecked.value ? [] : presetGoals.value.map(item => item.label);
  }

  /* ---------------- 侦听器 ---------------- */

  /*监听radio和checkboxList，他们的值改变时，自动向父组件传递数据*/
  watch([radio, () => checkbox.value], () => {
    update();
  })

  /* ---------------- 计算属性 ---------------- */

  /*判断是否是全选状态*/
  const isAllChecked = computed(() => {
    return checkbox.value.length === presetGoals.value.length;
  })

  /*控制全选按钮是否处于不确定状态：有选项且未全选*/
  const indeterminate = computed(() => {
    return checkbox.value.length > 0 && checkbox.value.length < presetGoals.value.length;
  })

</script>

<style>
  el-radio-group {
    height: 32px ;
  }

  .item {
    /*width: 30%;*/
    margin: 5px 0 5px 5%;
    text-align: center;
  }

  .check-all {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0%);
  }

  .center-item {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translate(-50%, 0%);
  }

  .group {
    padding-left: 15%;
  }
</style>