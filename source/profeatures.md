# 专业版功能 Pro Features

[English](https://json-to-excel.wtsolutions.cn/en/latest/profeatures.html)

JSON-to-Excel 插件提供了一系列专业版功能，这些功能可以增强插件的功能性。这些功能仅对订阅了插件的用户开放。

## 订阅

7天免费试用，之后您将按以下月费率之一支付专业版功能费用。您可以在第7天之前随时取消订阅，且不会被收取费用：
- USD US$2.66 / 月
- CNY ¥19.90 / 月
- EUR €2.36 / 月
- HKD HK$21.80 / 月
- 您的本地货币（如果 Stripe 支持）

每个Pro Code可以为10台设备提供专业版功能访问权限。在7天试用期后，您可以随时取消订阅，取消将在当前计费周期结束时生效。

每个Pro Code对 WTSolutions 提供的 Excel-to-JSON 插件和 JSON-to-Excel 插件都有效。

通过 Stripe 订阅，点击这里 [https://buy.stripe.com/00gdQT2iz0Vp32E002](https://buy.stripe.com/00gdQT2iz0Vp32E002)

支付方式：
- 银行卡（Visa、Mastercard、American Express、JCB、银联）
- Apple Pay（需要使用您的 Apple/IOS/Mac 设备打开上述链接）
- Google Pay（需要使用您的 Google/Android 设备打开上述链接）
- Link

关于订阅条款，请参阅[使用条款](termsofuse.md)

## 专业版代码 Pro Code

专业版代码Pro Code 是您在 Stripe 上完成 Excel-to-JSON 插件结账过程时使用的`电子邮件地址`。访问专业版功能需要此代码。

## 专业版功能 Pro Features

### 嵌套分隔符

嵌套分隔符指定如何处理 JSON 中的嵌套对象。您可以选择：
- 点号 (.) - 默认
- 下划线 (_)
- 正斜杠 (/)

例如，对于这个 JSON：

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

将被转换为 Excel 如下：

使用点号(.)作为分隔符：
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

最大深度设置控制插件将处理嵌套对象的深度：
- 默认：无限制深度
- 可接受范围：1 ~ 20（需要专业版功能）

注意：当最大深度设置为1到20之间的值时，您必须使用嵌套 JSON 模式。

例如，对于这个 JSON：

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

当最大深度设置为3时，第4级嵌套对象（address）将被转换为字符串格式。如果有第5级、第6级等嵌套对象，它们也将被转换为字符串格式。

Excel 输出将如下所示：

使用点号(.)作为分隔符：
|id|student.name|student.contact.email|student.contact.phone|student.contact.address|
|---|---|---|---|---|
|1|Meimei|meimei@school.com|123-456-7890|{"street":"123 School St","city":"Beijing"}|
|2|Lily|lily@school.com|098-765-4321|{"street":"456 School Ave","city":"Shanghai"}|

### 加载本地JSON文件，用于批量处理

加载JSON文件功能允许您将多个JSON文件加载到插件中，然后将它们批量转换为Excel表。此功能仅对订阅了插件的用户开放。

注意：每次转换最多支持20个文件。

## 更多功能

如果您已订阅，并希望看到更多功能，请发送电子邮件至 he.yang@wtsolutions.cn

## 售后服务

如有任何问题或疑虑，您可以通过电子邮件 he.yang@wtsolutions.cn 联系我们。我们将尽最大努力在24小时内回复您，但不会超过72小时。如果您的问题与订阅相关，请在邮件中包含您的`专业版代码Pro Code`。