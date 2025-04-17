# JSON to Excel

JSON to Excel是一款Microsoft Excel插件，可以在Excel环境中将JSON数据转换为Excel表格，支持扁平模式和嵌套模式两种转换方式。

## 文档
[https://json-to-excel.wtsolutions.cn/zh-cn/latest/](https://json-to-excel.wtsolutions.cn/zh-cn/latest/)

## 系统要求
本插件支持以下版本：Excel 2013 Service Pack 1或更高版本、Excel 2016 for Mac、Excel 2016或更高版本、Excel Online、Mac版Excel、Office 365等。

## 获取插件
* 在Excel 2013/2016、Excel Online或Office 365中打开新工作表
* **开始**标签或**插入**标签 > 加载项
* 在搜索框中输入"JSON-to-Excel"
* 按照屏幕提示安装插件，安装完成后会在**开始**标签中看到JSON-to-Excel按钮
* **开始**标签 > JSON转Excel > 转换
* 现在可以开始使用本插件

## 使用插件
* 准备您的JSON数据
* 将JSON数据填入JSON-to-Excel的文本区域
* 选择转换模式，点击Go按钮

## 转换示例

### JSON转Excel示例

#### 输入
```json
[
    {
        "name": "John",
        "contact": {
            "email": "john@example.com",
            "phone": "1234567890"
        }
    },
    {
        "name": "Jane",
        "contact": {
            "email": "jane@example.com",
            "phone": "0987654321"
        }
    }
]
```
#### 输出
> 使用Flat JSON模式

|name|contact|
|--|--|
|John|{"email":"john@example.com","phone":"1234567890"}|
|Jane|{"email":"jane@example.com","phone":"0987654321"}|

> 使用Nested JSON模式

|name|contact.email|contact.phone|
|--|--|--|
|John|john@example.com|1234567890|
|Jane|jane@example.com|987654321|

## 文档
[https://json-to-excel.wtsolutions.cn/zh-cn/latest/](https://json-to-excel.wtsolutions.cn/zh-cn/latest/)
