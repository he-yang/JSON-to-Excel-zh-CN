
# 简介

[English](https://json-to-excel.wtsolutions.cn/en/latest/quickstart.html)

JSON to Excel 是一个可以将 JSON 转换为 Excel 的 Microsoft Excel 插件。

# 系统要求
此插件支持以下版本：Excel 2013 Service Pack 1 或更高版本、Excel 2016 for Mac、Excel 2016 或更高版本、Excel Online、Office 365 等。

# 快速入门
本快速入门适用于 v 2.1.0 版本

## 获取插件
* 在 Excel 2013/2016、Excel Online 或 Office 365 中打开新的数据表。
* **开始**选项卡或**插入**选项卡 > 加载项
* 在搜索框中输入 "JSON to Excel"
* 按照屏幕上的说明安装插件，安装完成后您将在**开始**选项卡中看到 JSON-to-Excel 按钮。
* **开始**选项卡 > JSON to Excel > 转换Convert
* 现在您可以开始使用此插件了。

## 视频演示

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114350819906550&bvid=BV1VE5azhETJ&cid=29457450569&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

## 使用插件
* 准备您的 JSON 数据
* 将您的 JSON 数据填入 JSON-to-Excel 的文本区域
* 选择转换模式，然后点击Go按钮



```
[
    {
        "name":"David",
        "age":20
    },
    {
        "name":"Lily",
        "age":22
    }
]
```

> 注意，只能处理常规 JSON 数据。只有 JSON 第一个元素中的键会被解析为表头。除了上述要求外，无需担心其他问题。

> 注意：您的 JSON 数据必须用数组 [] 包裹，请参考以下示例。请尽量按照下面的格式调整，以避免错误。

## 可接受的JSON格式

### 格式
输入必须是包含对象的有效JSON数组。数组中的每个对象代表Excel输出中的一行。

```json
[
    {"property1": value1, "property2": value2, ...},
    {"property1": value3, "property2": value4, ...}
]
```

### 规则
1. 必须用方括号[]包裹，作为数组
2. 必须包含至少一个对象{}
3. 每个对象必须至少有一个属性

### 支持的值类型
- 字符串: "text"
- 数字: 123 , 45.67
- 布尔值: true , false
- Null: null
    - 在Excel中会转换为空白单元格
- 数组: [1, 2, 3]
    - 在Excel中会转换为字符串形式 "[1,2,3]"
- 对象: {"x": 1}
    - 如果选择Flat JSON模式，会在Excel中转换为字符串形式 '{"x": 1}'
    - 如果选择Nested JSON模式，会被展开

# 模式选择
> 请先参考下方示例以帮助理解两种模式
1. Flat JSON模式   
   - 用于没有嵌套结构的简单JSON对象
   - 每个属性成为Excel中的一列
2. Nested JSON模式   
   - 用于有嵌套结构的JSON对象
   - 嵌套属性使用点表示法展开
   - 示例：contact.email将成为列名
   - 使用[专业版功能](profeatures.md)中的嵌套分隔符设置来自定义分隔符(点号、下划线、斜杠)
   - 使用[专业版功能](profeatures.md)中的最大嵌套深度设置来自定义嵌套对象的最大深度(1到20)，超过设定深度的嵌套对象将被转换为字符串格式

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

# 示例

## 有效的JSON示例
```json
// 简单的扁平对象
[
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]

// 具有不同属性的对象
[
    {"name": "John", "age": 30},
    {"name": "Jane", "city": "New York"}
]

// 具有嵌套结构的对象(使用嵌套JSON模式)
// - 使用专业版功能中的嵌套分隔符设置来自定义分隔符(点号、下划线、斜杠)
// - 使用专业版功能中的最大嵌套深度设置来自定义嵌套对象的最大深度(4到10)
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

## 无效的JSON示例
```json
// 未被数组包裹
{"name": "John"}

// 空数组
[]

// 数组包含非对象元素
[1, 2, 3]
["a", "b", "c"]

// 数组包含空对象
[{}]

// 数组包含null值
[null]

// 数组包含混合类型
[{"name": "John"}, "text"]
```

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
#### Output
> 使用 Flat JSON mode

|name|contact|
|--|--|
|John|{"email":"john@example.com","phone":"1234567890"}|
|Jane|{"email":"jane@example.com","phone":"0987654321"}|

> 使用 Nested JSON mode

|name|contact.email|contact.phone|
|--|--|--|
|John|john@example.com|1234567890|
|Jane|jane@example.com|987654321|

- 使用[专业版功能](profeatures.md)中的嵌套分隔符设置来自定义分隔符(点号、下划线、斜杠)
- 使用[专业版功能](profeatures.md)中的最大嵌套深度设置来自定义嵌套对象的最大深度(4到10)


# 限制条件
- 每次转换最多1000个对象（行）
- 每个数据集最多100个唯一属性（列）
- 数组类型的值将在Excel中转换为字符串


# 错误提示

## 无效的JSON

当插件弹出无效JSON的错误提示时，表示JSON不符合JSON架构要求。以下两个步骤可以帮助你获得此插件可接受的JSON数据。

### JSON有效性预检查
* 使用[免费网络服务](https://jsononline.net/json-validator)进行JSON有效性预检查，请确保该网站显示你的JSON文件**JSON是有效的**。

### 插件检查
* 插件将进一步检查你的JSON数据是否符合上述插件要求的可接受JSON格式。

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

## 列数过多

当出现列数过多的错误提示时，表示在单个元素中包含了过多的键值对。

一个元素中包含两个键值对，
```
    {
        "name":"Lily",
        "age":22
    }
```
插件目前最多可接受100个键值对。


## 微信公众号
![微信公众号](https://invest.wtsolutions.cn/wechat.png)