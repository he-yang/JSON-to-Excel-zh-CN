# 4. WPS 加载项（JSON转WPS工作表 WPS加载项）
[English](https://json-to-excel.wtsolutions.cn/en/latest/WPSAddIn.html)

WTSolutions的JSON转Excel是一系列可将JSON转换为Excel的工具，支持平级和嵌套JSON转换为Excel。它提供了“JSON转Excel”的全场景解决方案，包括Excel加载项、Web应用程序、WPS加载项：

* [Web应用：直接在浏览器中转换JSON到Excel。](WebApp.md)
* [Excel加载项：在Excel中转换JSON为Excel，与Excel环境无缝集成。](ExcelAddIn.md)
* <mark>WPS加载项：在WPS中转换JSON到WPS工作表，与WPS环境无缝协作。</mark>(<-- 您当前所在位置)    
* [API：通过HTTPS POST请求在API中转换JSON到Excel](API.md)
* [MCP服务器：在MCP服务器中转换JSON到Excel](MCP.md)

## 4.1 系统要求

* WPS(Windows), 最新版
* WPS(Linux), 最新版

## 4.2 获取方式

* 获取 WPS 加载项（在 WPS 中旁加载）需要几个步骤
* 访问 [https://json-to-wps-workbook.wtsolutions.cn/publish.html](https://json-to-wps-workbook.wtsolutions.cn/publish.html) 查看详细步骤。


### 获取加载项的视频指南

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114350819906550&bvid=BV1VE5azhETJ&cid=29457450569&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

[更多视频](https://s.wtsolutions.cn/images/videoqrcodes.png)



## 4.3 使用方法

* 准备您的JSON数据
* 在[转换设置](profeatures.md)中，选择转换模式等。
* 加载您的JSON数据（选择以下两种方式之一）
    1. 将JSON数据复制粘贴到文本区域，或
    2. 点击“加载JSON文件”选择器，从本地计算机选择JSON文件进行批量处理[专业功能](pricing.md)，一次最多可加载20个文件。
* 点击“开始”按钮
* 您的JSON数据将被转换为WPS工作表，您将看到WPS中新增一个工作表。

### 使用加载项的视频指南（在WPS中旁加载）

WPS加载项和Excel加载项的使用方法相同，参见Excel加载项的使用演示视频。

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114549948814092&bvid=BV1T4J7ztE87&cid=30087253525&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>


<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114350819906550&bvid=BV1VE5azhETJ&cid=29457450569&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>


<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115658553562052&bvid=BV1Ky2hB2EfB&cid=34486682667&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

[更多视频](https://s.wtsolutions.cn/images/videoqrcodes.png)

## 4.4 JSON数据和转换设置

有关更多详细信息，请参阅[JSON数据和转换设置](profeatures.md)。


<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8772217510669640"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-8772217510669640"
     data-ad-slot="2653271427"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## 3.5 限制条件
- 每次转换最多1000个对象（行）
- 每个数据集最多100个唯一属性（列）
- 值中的数组将转换为WPS工作表中的字符串
- 一次最多可转换20个加载的本地JSON文件[专业功能](pricing.md)