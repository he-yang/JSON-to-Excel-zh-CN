
# 1. 简介

[English](https://json-to-excel.wtsolutions.cn/en/latest/quickstart.html)

JSON to Excel 是一个 **Microsoft Excel 加载项**或**Web 应用程序**，可以将 JSON 转换为 Excel。平坦/嵌套的 JSON 都可以转换。

# 2. 要求

选项 1. 在 Web 浏览器中加载 JSON to Excel
* 支持 JavaScript 的 Web 浏览器，例如 Google Chrome、Mozilla Firefox、Safari 或 Microsoft Edge。

选项 2. 在 Excel 中旁加载 JSON to Excel（推荐）
* Excel 2013 Service Pack 1 或更高版本，
* Mac 版 Excel 2016，
* Excel 2016 或更高版本，
* Excel Online，
* Office 365 等。

# 3. 快速入门
本快速入门适用于 v 3.0.0

## 3.1 （旁）加载 JSON to Excel

选项 1. 在 Web 浏览器中加载 JSON to Excel
* 打开支持 JavaScript 的 Web 浏览器，例如 Google Chrome、Mozilla Firefox、Safari 或 Microsoft Edge。
* 在您的 Web 浏览器中打开以下 URL：<a href="https://s.wtsolutions.cn/json-to-excel.html" target="_blank">https://s.wtsolutions.cn/json-to-excel.html</a>


选项 2. 在 Excel 中旁加载 JSON to Excel（推荐）
* 在 Excel 2013/2016 或 Excel Online 或 Office 365 中打开一个新的工作表。
* **主页**选项卡或**插入**选项卡 > 加载项
* 在搜索框中，输入“JSON to Excel”
* 按照屏幕上的说明安装加载项，您将在**主页**选项卡中看到一个名为 JSON-to-Excel 的按钮。
* **主页**选项卡 > JSON to Excel > 转换
* 现在您已准备好使用此加载项。




## 3.2 使用 JSON to Excel
* 准备您的 JSON 数据
* 在设置框中，选择转换模式等。
* 加载您的 JSON 数据（选择以下两种方式之一）
    1. 在文本区域中复制并粘贴您的 JSON 数据，或者
    2. 单击“加载 JSON 文件”文件选择器，并从本地计算机中选择您的 JSON 文件，用于批量处理（专业功能），一次最多可加载 20 个文件。
* 单击“Go”按钮

### 限制
- 每次转换最多 1000 个对象（行）
- 每个数据集最多 100 个唯一属性（列）
- 值中的数组将转换为 Excel 中的字符串
- 一次最多可转换 20 个加载的本地 JSON 文件（专业功能）






## 3.3 转换设置

### 转换模式
有两种转换模式：平面 JSON 模式和嵌套 JSON 模式。

> 请先参考下面的示例，以帮助您理解这两种模式

- 平面 JSON 模式
   - 用于没有嵌套结构的简单 JSON 对象
   - 每个属性都成为 Excel 中的一列
- 嵌套 JSON 模式
   - 用于具有嵌套结构的 JSON 对象
   - 嵌套属性使用点/下划线/双下划线/斜杠分隔符进行展平
   - 默认情况下转换无限深度。使用专业功能中的“最大嵌套深度”设置自定义嵌套对象的最大深度（1 到 20，或无限）。

### 嵌套分隔符

用于分隔 Excel 输出中嵌套属性的分隔符。

- 点 (.)
- 下划线 (_) [专业功能]
- 双下划线 (__) [专业功能]
- 斜杠 (/) [专业功能]

### 最大嵌套深度

要展平的嵌套对象的最大深度。

- 无限
- 1 到 20 [专业功能]





## 3.4 加载 JSON 数据

有两种加载 JSON 数据的方式：
- 在文本区域中复制并粘贴您的 JSON 数据
- 单击“加载 JSON 文件”文件选择器，并从本地计算机中选择您的 JSON 文件，用于批量处理（专业功能），一次最多可加载 20 个文件。

### 可接受的 JSON 格式
#### 所需格式
输入必须是包含对象的有效 JSON 数组。数组中的每个对象代表 Excel 输出中的一行。

```json
[
    {"property1": "value1", "property2": "value2", ...},
    {"property1": "value3", "property2": "value4", ...}
]
```

#### JSON 格式规则
- 必须用方括号 [] 包裹，作为数组
- 必须至少包含一个对象 {}
- 每个对象必须至少有一个属性

#### 支持的值类型
- 字符串: "text"
- 数字: 123 , 45.67
- 布尔值: true , false
- 空值: null
    - 将转换为 Excel 中的空白单元格
- 数组: [1, 2, 3]
    - 将转换为 Excel 中的字符串，如 "[1,2,3]"
- 对象: {"x": 1}
    - 如果选择平面模式，将转换为 Excel 中的字符串，如 '{"x": 1}'
    - 如果选择嵌套模式，将展平



# 4. 示例

## 4.1 有效 JSON 示例
```json
// 简单，一个平面对象
{"name": "John", "age": 30}

// 简单，平面对象
[
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]

// 具有不同属性的对象
[
    {"name": "John", "age": 30},
    {"name": "Jane", "city": "New York"}
]

// 具有嵌套结构的对象（使用嵌套 JSON 模式）
// 使用专业功能中的“嵌套分隔符”设置自定义分隔符（点、下划线、斜杠）
// 使用专业功能中的“最大嵌套深度”设置自定义嵌套对象的最大深度（1 到 20，或无限）
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
## 4.2 无效 JSON 示例

```json
// 未用数组包裹
{"name": "John"},{"name": "Lily", "age": 30}

// 空数组
[]

// 包含非对象元素的数组
[1, 2, 3]
["a", "b", "c"]

// 包含空对象的数组
[{}]

// 包含 null 的数组
[null]

// 混合类型的数组
[{"name": "John"}, "text"]

```

## 4.3 转换示例

### JSON 到 Excel 示例

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
> 平面 JSON 模式

|name|contact|
|--|--|
|John|{"email":"john@example.com","phone":"1234567890"}|
|Jane|{"email":"jane@example.com","phone":"0987654321"}|

> 嵌套 JSON 模式

|name|contact.email|contact.phone|
|--|--|--|
|John|john@example.com|1234567890|
|Jane|jane@example.com|987654321|

   - 使用专业功能中的“嵌套分隔符”设置自定义分隔符（点、下划线、双下划线、斜杠）
   - 使用专业功能中的“最大嵌套深度”设置自定义嵌套对象的最大深度（1 到 20，或无限）
   


# 5. 错误

## 5.1 无效 JSON

当 JSON to Excel 弹出无效 JSON 的错误提示时，表示 JSON 不符合 JSON 架构。

### 加载项检查
* 加载项将检查您的 JSON 数据是否符合上述可接受的 JSON 格式要求。如果出错，将显示错误消息。


## 5.2 列数过多

当您弹出列数过多错误时，表示您在一个元素中包含过多的键值对。

一个元素包含两个键值对，
```
    {
        "name":"Lily",
        "age":22
    }
```
并且加载项现在最多只能接受 100 个键值对。