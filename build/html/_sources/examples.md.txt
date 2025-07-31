# 5. 示例

[English](https://json-to-excel.wtsolutions.cn/en/latest/examples.html)

## 5.1 有效的JSON示例
```json
// 简单的扁平对象
{"name": "John", "age": 30}

// 简单的扁平对象数组
[
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]

// 具有不同属性的对象
[
    {"name": "John", "age": 30},
    {"name": "Jane", "city": "New York"}
]

// 具有嵌套结构的对象（使用嵌套JSON模式）
// 使用专业功能中的嵌套分隔符设置自定义分隔符（点、下划线、斜杠）
// 使用专业功能中的嵌套最大深度设置自定义嵌套对象的最大深度（1到20，或无限制）
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
## 5.2 无效的JSON示例

```json
// 未使用数组包裹
{"name": "John"},{"name": "Lily", "age": 30}

// 空数组
[]

// 包含非对象元素的数组
[1, 2, 3]
["a", "b", "c"]

// 包含空对象的数组
[{}]

// 包含null的数组
[null]

// 包含混合类型的数组
[{"name": "John"}, "text"]

```

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

## 5.3 转换示例

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
> 使用平面JSON模式

|name|contact|
|--|--|
|John|{"email":"john@example.com","phone":"1234567890"}|
|Jane|{"email":"jane@example.com","phone":"0987654321"}|

> 使用嵌套JSON模式

|name|contact.email|contact.phone|
|--|--|--|
|John|john@example.com|1234567890|
|Jane|jane@example.com|987654321|

   - 使用[专业功能](profeatures.md)中的嵌套分隔符设置自定义分隔符（点、下划线、双下划线、斜杠）
   - 使用[专业功能](profeatures.md)中的嵌套最大深度设置自定义嵌套对象的最大深度（1到20，或无限制）
   

