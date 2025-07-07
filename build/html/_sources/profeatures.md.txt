# 6. 专业功能

[English](https://json-to-excel.wtsolutions.cn/en/latest/profeatures.html)

JSON-to-Excel 提供了一系列增强功能的专业功能。这些功能仅适用于已订阅 JSON to Excel 的用户。

## 6.1 订阅、支付和取消

7 天免费试用，之后您将按以下费率每月收取专业功能费用。您可以在第 7 天之前的任何时间取消订阅，并且不会被收费：
- 美元 US$2.66 / 月，
- 人民币 ¥19.90 / 月，
- 欧元 €2.36 / 月，
- 港币 HK$21.80 / 月
- 如果 Stripe 支持，则为您的当地货币。

每个专业代码可提供 10 台设备访问专业功能。7 天试用期结束后，您可以随时取消订阅，这将在当前计费周期结束时生效。

每个专业代码对 WTSolutions 提供的 Excel-to-JSON 加载项和 JSON-to-Excel 均有效。

通过 Stripe 订阅，链接在此 [https://buy.stripe.com/00gdQT2iz0Vp32E002](https://buy.stripe.com/00gdQT2iz0Vp32E002)

支付方式：
- 银行卡（Visa、Mastercard、American Express、JCB、银联）
- Apple Pay（需要使用您的 Apple/IOS/Mac 设备打开上述链接）
- Google Pay（需要使用您的 Google/Android 设备打开上述链接）
- Link

有关订阅条款，请参阅 [使用条款](termsofuse.md)



## 6.2 专业功能


### 无广告

使用有效的专业代码成功转换后，从下次启动开始（您可以关闭 JSON to Excel 然后再次启动），JSON to Excel 将不再显示广告。
如果您没有有效的专业代码，或者您没有有效的 JSON to Excel 订阅，则会显示广告。

> 注意，如果您仍然不时看到广告，请尝试使用有效的专业代码进行转换，然后重新启动 JSON to Excel。

### 嵌套分隔符

嵌套分隔符指定如何处理 JSON 中的嵌套对象。您可以选择：
- 点 (.) - 默认
- 下划线 (_)
- 双下划线 (__)
- 斜杠 (/)

例如，对于此 JSON：

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

将转换为 Excel，如下所示：

使用点 (.) 作为分隔符：
|id|student.name|student.familyname|student.age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

使用下划线 (_):
|id|student_name|student_familyname|student_age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

使用斜杠 (/):
|id|student/name|student/familyname|student/age|
|---|---|---|---|
|1|Meimei|Han|12|
|2|Lily|Jaskson|15|

### 最大嵌套深度

最大深度设置控制 JSON to Excel 处理嵌套对象的深度：
- 默认：无限深度
- 可接受范围：1 ~ 20（需要专业功能）

注意：当最大深度设置为 1 到 20 之间的值时，您必须使用嵌套 JSON 模式。

例如，对于此 JSON：

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

当最大深度设置为 3 时，第 4 级嵌套对象（地址）将转换为字符串格式。如果存在第 5 级、第 6 级等嵌套对象，它们也将转换为字符串格式。

Excel 输出将如下所示：

使用点 (.) 作为分隔符：
|id|student.name|student.contact.email|student.contact.phone|student.contact.address|
|---|---|---|---|---|
|1|Meimei|meimei@school.com|123-456-7890|{"street":"123 School St","city":"Beijing"}|
|2|Lily|lily@school.com|098-765-4321|{"street":"456 School Ave","city":"Shanghai"}|

### 加载 JSON 文件

加载 JSON 文件功能允许您将多个 JSON 文件加载到 JSON to Excel 中，然后将它们转换为 Excel 工作表。此功能仅适用于已订阅 JSON to Excel 的用户。

每次转换后，将生成一份报告，其中包括：
- 所选 JSON 文件的文件名
- 转换结果（成功或失败）
- 如果成功，则为工作表名称
- 如果失败，则为错误消息

注意：每次转换最多 20 个文件。

#### 加载 JSON 文件视频演示
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114549948814092&bvid=BV1T4J7ztE87&cid=30087253525&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

## 6.3 更多功能

如果您已订阅，并希望看到更多功能，请发送电子邮件至 he.yang@wtsolutions.cn

## 6.4 专业代码

专业代码是您在 Stripe 上结账 JSON to Excel 时使用的“电子邮件地址”。此代码是访问专业功能所必需的。

## 6.5 售后服务

您可以通过电子邮件 he.yang@wtsolutions.cn 联系我们，提出任何问题或疑虑。我们将尽力在 24 小时内回复您，但不迟于 72 小时。如果您的问题与您的订阅有关，请在电子邮件中包含您的“专业代码”。