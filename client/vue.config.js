const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  devServer:{
    proxy: {
      '/api': {  // 匹配以此开头的请求
        changeOrigin: true,  // 如果接口跨域，需要进行这个参数配置
        target: 'http://localhost:8090',  // 接口的域名
      },
      '/hello': {
        changeOrigin: true,
        target: 'http://10.1.36.248:3333',
      }
    }
  }
})
