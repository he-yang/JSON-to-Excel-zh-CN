# 7. JSON 数据和转换设置

[中文](https://json-to-excel.wtsolutions.cn/zh-cn/latest/profeatures.html)

JSON-to-Excel提供了一系列增强功能的专业特性。这些标记为[专业功能](pricing.md)的规则仅对已订阅工具的用户开放。


## 7.1 JSON数据
||[Web App](WebApp.md)|[Excel 加载项](ExcelAddIn.md)|[WPS 加载项](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|❌|❌|

加载JSON数据有三种方式：
- 将JSON数据复制粘贴到文本区域
- 点击"加载JSON文件"选择器，从本地计算机选择JSON文件进行批量处理[专业功能](pricing.md)，一次最多可加载20个文件
- 从Web URL加载JSON文件，进行批量处理[专业功能](pricing.md)，一次最多可加载20个URL
> 注意，JSON数据必须满足下面[可接受的JSON格式](profeatures.md#id4)部分列出的要求。

### 复制粘贴JSON数据将JSON数据复制粘贴到文本区域，您可以在文本区域下方看到JSON数据预览。
> 注意，JSON数据必须满足下面[可接受的JSON格式](profeatures.md#id4)部分列出的要求。

### 加载JSON文件

"加载JSON文件"功能允许您将多个JSON文件加载到JSON转Excel中，然后将它们转换为Excel工作表。

每次转换后，将生成一份报告，包括：
- 所选JSON文件的文件名
- 转换结果（成功或失败）
- 成功时的工作表名称
- 失败时的错误消息

> 注意，每次转换最多20个文件。
> 注意，JSON数据必须满足下面可接受的JSON格式部分列出的要求。

#### 加载JSON文件视频演示
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114549948814092&bvid=BV1T4J7ztE87&cid=30087253525&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

[更多视频](https://s.wtsolutions.cn/images/videoqrcodes.png)



### 从Web URL加载JSON文件

从Web URL加载JSON文件功能允许您将多个JSON文件加载到JSON转Excel中，然后将它们转换为Excel工作表。

每次转换后，将生成一份报告，包括：
- 所选URL
- 转换结果（成功或失败）
- 成功时的工作表名称
- 失败时的错误消息

> 注意，每次转换最多20个URL。
> 注意，JSON数据必须满足下面可接受的JSON格式部分列出的要求。

#### 从Web URL加载JSON文件视频演示
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114996642060948&bvid=BV1u6tszgEdL&cid=31579504790&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

[更多视频](https://s.wtsolutions.cn/images/videoqrcodes.png)



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

### 可接受的JSON格式

#### 必需格式

输入必须是包含对象的有效JSON数组。数组中的每个对象代表Excel输出中的一行。

```json
[
    {"property1": "value1", "property2": "value2"},
    {"property1": "value3", "property2": "value4"}
]
```

#### JSON格式规则

JSON数据必须符合以下结构之一：

1. **对象数组**：
   - 必须用方括号 `[]` 包裹
   - 必须包含 1 到 1000 个条目
   - 每个条目必须是一个包含 1 到 100 个属性的对象 `{}`
   - 数组不能包含数组、空值、字符串、数字、布尔值或空对象

2. **单个对象**：
   - 必须用花括号 `{}` 包裹
   - 必须包含 1 到 100 个属性
   - 不能是数组、空值、字符串、数字、布尔值或空对象

所有对象都可以包含架构中定义之外的额外属性。

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "oneOf": [
    {
      "type": "array",
      "minItems": 1,
      "maxItems": 1000,
      "items": {
        "type": "object",
        "minProperties": 1,
        "maxProperties": 100,
        "additionalProperties": true
      },
      "not": {
        "contains": {
          "anyOf": [
            {
              "type": "array"
            },
            {
              "type": "null"
            },
            {
              "type": "string"
            },
            {
              "type": "number"
            },
            {
              "type": "boolean"
            },
            {
              "type": "object",
              "maxProperties": 0
            }
          ]
        }
      }
    },
    {
      "type": "object",
      "minProperties": 1,
      "maxProperties": 100,
      "additionalProperties": true,
      "not": {
        "anyOf": [
          {
            "type": "array"
          },
          {
            "type": "null"
          },
          {
            "type": "string"
          },
          {
            "type": "number"
          },
          {
            "type": "boolean"
          },
          {
            "type": "object",
            "maxProperties": 0
          }
        ]
      }
    }
  ]
}
```



#### 支持的值类型

- 字符串: "text"
- 数字: 123 , 45.67
- 布尔值: true , false
- 空值: null
    - 在Excel中将转换为空白单元格
- 数组: [1, 2, 3]
    - 在Excel中将转换为字符串，如"[1,2,3]"
- 对象: {"x": 1}
    - 如果选择平面模式，在Excel中将转换为字符串，如'{"x": 1}'
    - 如果选择嵌套模式，将被展平

### 有效和无效的JSON数据示例

有关有效和无效的JSON数据示例，请参阅[示例](examples.md)。

## 7.2 转换设置

### 转换模式
||[Web App](WebApp.md)|[Excel 加载项](ExcelAddIn.md)|[WPS 加载项](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|❌|❌|

有两种转换模式：平面JSON模式和嵌套JSON模式。有关这两种模式之间的区别，请参阅[示例](examples.md#output)。


- 平面JSON模式
   - 用于没有嵌套结构的简单JSON对象
   - 每个属性成为Excel中的一列，属性名称作为列名
- 嵌套JSON模式
   - 用于具有嵌套结构的JSON对象
   - 使用点/下划线/双下划线/斜杠分隔符展平嵌套属性[专业功能](pricing.md)
   - 默认转换无限深度。使用[专业功能](pricing.md)的最大嵌套深度设置自定义嵌套对象的最大深度（1到20，或无限）

### 嵌套分隔符
||[Web App](WebApp.md)|[Excel 加载项](ExcelAddIn.md)|[WPS 加载项](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|❌|❌|

嵌套分隔符指定如何处理JSON中的嵌套对象。您可以选择：
- 点(.) - 默认
- 下划线(_) [专业功能](pricing.md)
- 双下划线(__) [专业功能](pricing.md)
- 正斜杠(/) [专业功能](pricing.md)

例如，对于以下JSON：

```json
[{
    "id": 1,
    "student": {
        "name": "Meimei",
        "familyname": "Han",
        "age": 12
    }
}, {
    "id": 2,
    "student": {
        "name": "Lily",
        "familyname": "Jaskson",
        "age": 15
    }
}]
```

将转换为Excel如下：

使用点(.)作为分隔符：
|id|student.name|student.familyname|student.age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

使用下划线(_)：
|id|student_name|student_familyname|student_age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

使用正斜杠(/)：
|id|student/name|student/familyname|student/age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

### 最大嵌套深度
||[Web App](WebApp.md)|[Excel 加载项](ExcelAddIn.md)|[WPS 加载项](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|❌|❌|

最大深度设置控制JSON转Excel处理嵌套对象的深度：
- 默认：无限深度
- 可接受范围：1 ~ 20 [专业功能](pricing.md)

> 注意：当最大深度设置为1到20之间的值时，必须使用嵌套JSON模式。

例如，对于以下JSON：

```json
[{
    "id": 1,
    "student": {
        "name": "Meimei",
        "contact": {
            "email": "meimei@school.com",
            "phone": "123-456-7890",
            "address": {
                "street": "123 School St",
                "city": "Beijing"
            }
        }
    }
}, {
    "id": 2,
    "student": {
        "name": "Lily",
        "contact": {
            "email": "lily@school.com",
            "phone": "098-765-4321",
            "address": {
                "street": "456 School Ave",
                "city": "Shanghai"
            }
        }
    }
}]
```

当最大深度设置为3时，第4级嵌套对象（address）将转换为字符串格式。如果有第5级、第6级等嵌套对象，它们也将转换为字符串格式。

Excel输出将如下所示：

使用点(.)作为分隔符：
|id|student.name|student.contact.email|student.contact.phone|student.contact.address|
|---|---|---|---|---|
|1|Meimei|meimei@school.com|123-456-7890|{"street":"123 School St","city":"Beijing"}|
|2|Lily|lily@school.com|098-765-4321|{"street":"456 School Ave","city":"Shanghai"}|


## 7.3 无广告
||[Web App](WebApp.md)|[Excel 加载项](ExcelAddIn.md)|[WPS 加载项](WPSAddIn.md)|[API](API.md)|[MCP](MCP.md)|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Applicable|✅|✅|✅|❌|❌|

如果您拥有有效的JSON转Excel订阅，在使用有效的专业代码成功转换后，您将不会看到广告。

从下次启动开始（您可以关闭JSON转Excel然后重新启动），JSON转Excel将不再显示广告。

如果您没有有效的专业代码，或者没有有效的JSON转Excel订阅，将显示广告。

> 注意，如果您仍然时不时看到广告显示，请尝试使用有效的专业代码进行转换，然后重新启动JSON转Excel。


## 7.4 更多功能

如果您已订阅并希望看到更多功能，请发送电子邮件至he.yang@wtsolutions.cn

## 7.5 专业代码

专业代码是您在Stripe或Paddle上购买JSON转Excel时使用的`电子邮件地址`。访问专业功能需要此代码。


