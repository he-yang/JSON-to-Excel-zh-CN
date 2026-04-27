# API（通过HTTPS POST请求将JSON转换为Excel）

[English](https://json-to-excel.wtsolutions.cn/en/latest/API.html)

WTSolutions的JSON-to-Excel是一系列可以将JSON转换为Excel的工具，无论是扁平JSON还是嵌套JSON都可以转换。它提供了"将JSON转换为Excel"的全场景解决方案，包括Excel加载项、Web应用程序：

* 网络版方案
     * [Web应用：直接在Web浏览器中转换JSON到Excel。](WebApp.md)
     * [Excel加载项：在Excel中转换JSON到Excel，与Excel环境无缝协作。](ExcelAddIn.md)
     * [WPS加载项：在WPS中转换JSON到WPS工作表，与WPS环境无缝协作。](WPSAddIn.md)
     * <mark>API：通过HTTPS POST请求在API中转换JSON到Excel</mark>（<-- 您在此处）
     * [MCP服务器：在MCP服务器中转换JSON到Excel](MCP.md)
* 本地化方案
    
     * [本地化应用：在本地化应用中转换JSON到Excel，支持离线转换](LocalApp.md)
     * 本地化Excel加载项，即将发布
     * 本地化WPS加载项，即将发布
     


## 要求

需要HTTPS POST请求工具，如Postman、Curl、Python Requests、Javascript fetch等。
确保通过设置CORS头正确处理CORS问题。

## 访问点

向访问点 `https://mcp2.wtsolutions.cn/json-to-excel-api` 发送`POST`请求，并在请求中包含下面使用部分描述的必要参数。


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

## 使用方法 - 专业版

### 请求格式

API 接受带有 `application/json` 主体的 POST 请求，主体包含以下参数之一：

| 参数 | 类型 | 是否必需 | 描述 |
|------|------|----------|------|
| data | 字符串 | 否 | 要转换为 CSV 的 JSON 数据字符串。必须是有效的 JSON 数组或对象。 |
| url | 字符串 | 否 | 指向 JSON 文件的 URL。必须提供 'data' 或 'url' 中的一个 |
| options | 对象 | 是 | 用于自定义转换过程的配置对象 |

> 注意：
> - 提供 `data` 或 `url` 中的一个，不要同时提供。
> - 如果您想使用自定义转换设置，`options` 是必需的。
> - 如果您没有有效的专业版代码，最多转换6行数据。如果有Pro Code，则不限制转换行数。

#### 对 data 和 url 的要求

发送 `data` 时
> - 输入数据必须是有效的 JSON 字符串。JSON 格式要求可在 [JSON 格式要求](profeatures.md#json-format-schema) 获取，验证器可在 [JSON 到 Excel Web 应用](https://s.wtsolutions.cn/json-to-excel.html) 获取。
> - 如果 JSON 是对象数组，每个对象将被视为 CSV 中的一行。
> - 如果 JSON 是单个对象，它将被转换为包含键值对的 CSV。
> - CSV 将包含基于 JSON 对象中键的标题。
> - 此工具返回可轻松转换/导入到 Excel 的 CSV 格式数据。

发送 `url` 时
> - URL 应该是公开可访问的。
> - JSON 文件应该是 .json 格式。
> - JSON 文件应包含有效的 JSON 数组或对象。JSON 格式要求可在 [JSON 格式要求](profeatures.md#json-format-schema) 获取，验证器可在 [JSON 到 Excel Web 应用](https://s.wtsolutions.cn/json-to-excel.html) 获取。
> - 如果 JSON 是对象数组，每个对象将被视为 CSV 中的一行。
> - 如果 JSON 是单个对象，它将被转换为包含键值对的 CSV。
> - 此工具返回可轻松转换/导入到 Excel 的 CSV 格式数据。

### 选项对象

选项对象可以包含以下属性：

| 属性 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| proCode | 字符串 | "" | 专业版代码，需要有效的 JSON 转 Excel 服务订阅。proCode可以通过options中参数传递，也可以在https请求头中传递proCode。 |
| jsonMode | 字符串 | “flat” | JSON 输出的格式模式：“nested”（嵌套）或 “flat”（扁平） |
| delimiter | 字符串 | “.” | 使用 jsonMode: “nested” 时，嵌套 JSON 键的分隔符字符，可接受的分隔符有 “.”、“_”、“__”、“/”。 |
| maxDepth | 字符串 | "unlimited" | 使用 jsonMode: “nested” 时，嵌套 JSON 对象的最大深度。maxDepth 可接受的值为 "unlimited"、"1" ~ "20"。 |

注意：
> - proCode 是可选的。如果没有提供 proCode，将最多转换6行数据。
> - proCode 可以通过 options 中参数传递，也可以在 https 请求头中传递 proCode。
> - 详细的转换规则可在 [转换规则](profeatures.md) 中找到。

### 响应格式
API 返回具有以下结构的 JSON 对象：

| 字段 | 类型 | 描述 |
|------|------|------|
| isError | 布尔值 | 指示处理请求时是否出错 |
| msg | 字符串 | 'success'（成功）或错误描述 |
| data | 字符串 | 转换后的 CSV 数据字符串，如果出错则为空。此 CSV 数据可轻松导入到 Excel。 |

### 示例

#### 使用 'data' 的请求示例

请求：

```json
{ 
     "data": "[{\"name\":\"John\",\"contact\":{\"email\":\"john@example.com\",\"phone\":\"1234567890\"}},{\"name\":\"Jane\",\"contact\":{\"email\":\"jane@example.com\",\"phone\":\"0987654321\"}}]",
     "options":{
          "proCode": "input your Pro Code here",
          "jsonMode": "nested",
          "delimiter": ".",
          "maxDepth": "unlimited"
     }
}
```

响应：

```json
{
     "isError": false,
     "data": "name,contact.email,contact.phone\nJohn,john@example.com,1234567890\nJane,jane@example.com,0987654321",
     "msg": "success"
}
```


#### 错误回复示例

```json
{
     "isError": true,
     "msg": "Invalid JSON format",
     "data": ""
}
```
### 数据类型处理

API 会自动处理 JSON 中的不同数据类型：

- **数字**：转换为 CSV 中的数值
- **布尔值**：转换为 'true'/'false' 字符串
- **字符串**：必要时进行转义并加引号
- **数组**：转换为 JSON.stringify 后的数组字符串
- **对象**：转换为 JSON.stringify 后的对象字符串




## 错误处理
API为常见问题返回描述性错误消息：
- `Invalid JSON format`：当输入数据不是有效的JSON字符串时
- `Empty JSON data`：当输入数据是空的JSON字符串时
- `Network Error when fetching file`：当从提供的URL下载文件出错时
- `File not found`：当找不到提供的URL上的文件时
- `Server Internal Error`：当发生意外错误时
- `Max 6 rows processed, upgrade to Pro to process more data`：当没有提供Pro Code时，最多转换6行数据