# online_images_collector
一个在线的图片采集器，复制链接，一键批量下载想要的图片


# 接口文档

## 爬取网页图片

### url
/api/crawlImages

### 入参
| 字段名 | 类型 | 是否必选 | 说明 | 备注 |
| :---:  | :---:  | :---:  | :---:  | :---:  |
|  urls | string | 是 | 要爬取的网址 | 支持多个；多个网址之间使用，分割|
|  cookies | json string | 否 | 设置cookies | 如果没有，使用默认 |
|  max_depth | int | 否 | 爬虫最大深度 | 爬虫从起始网址开始爬取数据，从页面上获取存在的链接作为新的地址爬取数据，此字段用来限制此操作最大深度。默认为1。最大为3。|
| maximum | int | 否 | 返回结果的最大数量 | 默认为300 |
| conditions | json string | 否 | 筛选条件 | 筛选结果，可选参数见下表 |

#### conditions 可选参数

| 字段名 | 类型 | 是否必选 | 说明 | 备注 |
| :---:  | :---:  | :---:  | :---:  | :---:  |
| image_length_max | int | 否 | 图片最大宽度 | 单位：像素 |
| image_height_max | int | 否 | 图片最大高度 | 单位：像素 |
| image_length_min | int | 否 | 图片最小宽度 | 单位：像素 |
| image_height_min | int | 否 | 图片最小高度 | 单位：像素 |