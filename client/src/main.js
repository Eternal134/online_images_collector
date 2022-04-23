import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as Icons from '@element-plus/icons-vue'

const app = createApp(App);
// 全局注册el-icon资源
Object.keys(Icons).forEach(key => {
    app.component(key, Icons[key])
})
// 导入element-ui
app.use(ElementPlus)
app.mount('#app')

