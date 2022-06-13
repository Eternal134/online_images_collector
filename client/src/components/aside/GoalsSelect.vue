<template>
    <el-menu
        class=el-menu-vertical-demo
    >
      <div class="menu-title radius"
             :style="{
        borderRadius: 'var(--el-border-radius-round)'}"
      >图片内容筛选</div>

      <div class="collapse-block">
        <el-collapse accordion>
          <el-collapse-item title="目标检测" name="1">
            <el-switch
                v-model="isRadio"
                active-text="单选模式"
                inactive-text="多选模式"
                @change="update"
                class="switch"
            />
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
                  <template v-for="goal in presetGoals" :key="goal.label">
                    <el-tooltip>
                      <template #content>
                        {{getGoalImgCount(goal)}}
                      </template>
                      <el-checkbox :label="goal.label"
                                   border
                                   class="item button"
                      >{{ goal.name }}
                      </el-checkbox>
                    </el-tooltip>
                  </template>

                </el-checkbox-group>
              </template>
            </div>
          </el-collapse-item>
          <el-collapse-item title="分辨率" name="2">
            <div class="slider-block">
              <span class="demonstration">宽度</span>
              <!-- 折叠菜单 -->
              <el-menu :collapse="true">
                <el-sub-menu index="1">
                  <template #title>
                    <el-icon>
                      <Edit></Edit>
                    </el-icon>
                  </template>
                  <div class="width-height-input-line">
                    <span class="demonstration">最小宽度</span>
                    <el-input-number v-model="widthRange[0]"></el-input-number>
                  </div>
                  <div class="width-height-input-line">
                    <span class="demonstration">最大宽度</span>
                    <el-input-number v-model="widthRange[1]"></el-input-number>
                  </div>
                </el-sub-menu>
              </el-menu>
              <el-slider v-model="widthRange" class="slider" range :max="4800"></el-slider>
            </div>
            <div class="slider-block">
              <span class="demonstration">高度</span>
              <!-- 折叠菜单 -->
              <el-menu :collapse=true>
                <el-sub-menu index="1">
                  <template #title>
                    <el-icon>
                      <Edit></Edit>
                    </el-icon>
                  </template>
                  <div class="width-height-input-line">
                    <span class="demonstration">最小高度</span>
                    <el-input-number v-model="heightRange[0]"></el-input-number>
                  </div>
                  <div class="width-height-input-line">
                    <span class="demonstration">最大高度</span>
                    <el-input-number v-model="heightRange[1]"></el-input-number>
                  </div>
                </el-sub-menu>
              </el-menu>
              <el-slider v-model="heightRange" class="slider" range :max="2800"></el-slider>
            </div>
          </el-collapse-item>
<!--          是否显示加载失败图片-->
          <el-collapse-item title="加载失败图片" name="3">
            <span class="demonstration">显示加载失败的图片</span>
            <el-switch v-model="isShowLoadingErrorImg"
                       inline-prompt active-text="Y"
                       inactive-text="N">
            </el-switch>
          </el-collapse-item>
        </el-collapse>
      </div>
    </el-menu>
</template>

<script setup>
import {computed, inject, reactive, ref, watch} from "vue";
import { Edit } from '@element-plus/icons';

  /* ---------------- 数据 ---------------- */

  // 注入app组件供给的数据和更新方法
  const goals = inject('goalsSelected');
  const updateGoals = inject('updateGoals');
  const isShowLoadingErrorImg = inject('isShowLoadingErrorImg');
  // 宽度范围
  const widthRange = inject('widthRange');
  // 高度范围
  const heightRange = inject('heightRange');
  // 每种目标的图像个数统计
  const prop = defineProps(['imgCount']);

  // 多选框选择结果
  const checkbox = ref(goals);
  // 单选框选择结果
  const radio = ref('others');
  // 是否是单选模式
  const isRadio = ref(false);
  // 绑定按钮组的属性
  const groupClass = reactive({
    group: true
  });


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
    new goal('clock', '时钟'),
    new goal('tie', '领带'),
    new goal('airplane', '飞机'),
    new goal('cup', '水杯'),
    new goal('umbrella', '雨伞'),

    new goal('others', '其他')
  ])

  /* ---------------- 方法 ---------------- */

  /*向父组件更新数据*/
  function update() {
    const data = isRadio.value ? [radio.value] : checkbox.value;
    // emit('update:goalsSelected', data);
    updateGoals(data)
  }


  /*全选，仅适用于多选模式*/
  function checkAll() {
    checkbox.value = isAllChecked.value ? [] : presetGoals.value.map(item => item.label);
  }


  // 返回某目标的图像数量
  function getGoalImgCount(goal) {
    return prop.imgCount.goalsImgCount.get(goal.label) ?? 0
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

<style scoped>

  .width-height-input-line {
    margin: 0 10px;
  }

  .slider-block {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .slider-block .slider {
    margin: 0 20px;
  }

  .item {
    margin-top: 10px;
    width: 75px;
    text-align: center;
  }

  .group {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }

  .menu-title {
    margin: 10px 0px;
    color: var(--el-color-white);
    width: 100%;
  }

  .switch {
    border-bottom: solid 1px var(--el-border-color);
    margin-bottom: 10px;
    padding-bottom: 5px;
  }

  .menu {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }

  .collapse-block {
    width: 100%;
  }

  /*not()：不选括号内的参数类*/
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    min-height: 400px;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 20px;
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
</style>