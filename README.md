# “朱佩娘”小程序接口交互文档
### 版本号：V1.0.0
#### 撰写日期：2024/01/30
#### 撰写人：武明皓
#### 域名：https://zhupeiniang.com
* * *
#### 数据格式说明
| 字段名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
|data|json|是|返回数据内容
|status|number|是|请求状态：1=成功、0=失败
|errMsg|string|否|如status为0，返回错误提示信息
**举例：**
```
{
    "data": {}, //返回数据信息
    "status": 1, //数据请求状态信息，
    "errorMsg": "" //错误提示信息
}
```
* * *
#### 用户预登录:  /userinfo
用户首次使用小程序默认自动登录，无需认证手机号等实名信息。

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
|openid|string|是|用户登录凭证，登录默认为空|
| code |string  |是  |微信用户唯一id标识  |
| provider |string  |否  |登录服务商，默认'weixin'  |
| deviceBrand |  string| 否 |设备品牌，如：apple、huawei  |
| deviceId |string  | 否 | 当前设备id |
| deviceModel | string |否  | 当前设备型号 |
| deviceType | string | 否 |当前设备类型，如：phone、pad、pc  |
| system | string | 否 | 操作系统及版本 |

**data返回参数说明**
type: <u>JSON</u>

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| token | string | 用户服务端唯一id标识 | 
| username |string  |用户名  |  
| icon | string | 用户头像地址 |
|phone_number |number |用户绑定手机号 |
|user_status |number |用户账号信息，例：1=白名单用户、0=黑名单用户 |

#### 登录:  /login
个别功能触发真实登录获取用户信息

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
|token|string|是|用户唯一id标识 |
| number |string  |是  |登录手机号  |
| password |string  |是  |登录密码 |

**data返回参数说明**
type: <u>JSON</u>

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| token | string | 用户服务端唯一id标识 | 
| status | number | 成功:1, 失败: 0| 
| errMsg | string | 登录失败原因描述| 
| userinfo | json | 见下方userinfo描述，失败可为空| 

**userinfo返回参数说明**

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| username |string  |用户名  |  
| icon | string | 用户头像地址 |
|phone_number |number |用户绑定手机号 |
|user_status |number |用户账号信息，例：1=白名单用户、0=黑名单用户 |

#### 获取验证码:  /sendVerCode
发送上传手机号验证码

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
|token|string|是|用户唯一id标识 |
| number |string  |是  |登录手机号  |
| type |string  |是  |登录: login 注册: register  |

**data返回参数说明**
type: <u>JSON</u>

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| token | string | 用户服务端唯一id标识 | 
| status | number | 成功:1, 失败: 0| 
| errMsg | string | 验证码获取失败原因描述| 


#### 验证码登录:  /verCodeLogin
利用验证码方式登录

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
|token|string|是|用户唯一id标识 |
| number |string  |是  |登录手机号  |
| code |string  |是  |验证码  |

**data返回参数说明**
type: <u>JSON</u>

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| token | string | 用户服务端唯一id标识 | 
| status | number | 成功:1, 失败: 0| 
| errMsg | string | 登录失败原因描述| 
| userinfo | json | 见下方userinfo描述，失败可为空| 

**userinfo返回参数说明**

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| username |string  |用户名  |  
| icon | string | 用户头像地址 |
|phone_number |number |用户绑定手机号 |
|user_status |number |用户账号信息，例：1=白名单用户、0=黑名单用户 |

#### 注册:  /setRegisterPassword
设置注册账号验证码

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
|token|string|是|用户唯一id标识 |
| number |string  |是  |登录手机号  |
| password |string  |是  |登录密码  |


**data返回参数说明**
type: <u>JSON</u>

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| token | string | 用户服务端唯一id标识 | 
| status | number | 成功:1, 失败: 0| 
| errMsg | string | 登录失败原因描述| 
| userinfo | json | 见下方userinfo描述，失败可为空| 

**userinfo返回参数说明**

| 参数名 | 类型 |说明  |  
| --- | --- | --- | 
| username |string  |用户名  |  
| icon | string | 用户头像地址 |
|phone_number |number |用户绑定手机号 |
|user_status |number |用户账号信息，例：1=白名单用户、0=黑名单用户 |


* * *
#### 获取广告位数据 /getBannerListData
首页广告位广告推送。
**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |

**data返回参数说明**
type: <u>Array</u>
| 参数名 | 类型 |说明  |
| --- | --- | --- |
|id | number|唯一id |
|type | string|可选类型 image/video|
|url |string |封面链接 (若type类型为video则为视频资源链接)|
|href | string|跳转广告资源链接 |

* * *
#### 获取筛选功能详细配置数据选项 /getFilterDetailOption
首页筛选功能，更多筛选内容数据。

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |

**data返回参数说明**
type: <u>Array</u>
| 参数名 | 类型 |说明  |
| --- | --- | --- |
|title | string|筛选项分组标题 |
|options | array|见下方options描述|
|type | string|默认为 (normal)选项模式，(slider暂不支持)为滑块模式 |

**options返回参数说明**
type: <u>Array</u>
| 参数名 | 类型 |说明  |
| --- | --- | --- |
|name | string|筛选选项名称 |
|active | boolean|当前选项是否选中激活|

* * *
#### 设置筛选功能详细配置选项 /setFilterDetailOption
设置首页详细筛选功能。

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |
| data |array  |是  |设置筛选项配置信息，见下方data描述  |

**data参数说明**
数据格式同上(/getFilterDetailOption)接口返回值相同
只更改active参数数据
| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| active |boolean  |是  |true/false 启用/未启用当前筛选项  |

**data返回参数说明**
type: <u>JSON</u>
返回基本状态信息

* * *
#### 设置快捷筛选功能配置选项 /setQuickFilterOption
首页3个分类快捷筛选选项设置 (价格较低、订车费、快慢充)。

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |
| data |json  |是  |设置筛选项配置信息，见下方data描述  |

**data参数说明**
| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| filter |array  |是  |0:智能推荐 1:距离较近 2: 价格较低 3: 充电较快 4: 空闲较多, 例: 单选[1] 多选[0,1] |
| price |array  |是  |0:收停车费 1:限时免费停车 2: 免费停车, 例: 单选[1] 多选[0,1]|
| slowHigh |array  |是  |0:快充 1:慢充, 例: 单选[1] 多选[0,1]|

**data返回参数说明**
type: <u>JSON</u>
返回基本状态信息

* * *
#### 获取首页用户常用筛选项数据/getInCommonUseFilter
首页用户常用筛选项

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |

**data返回参数说明**
type <u>Array</u>

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|id|number|唯一标识|
|name|string|筛选标题名称|
|active|boolean|当前选项是否激活|

* * *
#### 设置首页用户常用筛选项数据/setInCommonUseFilter
首页用户常用筛选项

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |
| data |array  |是  |常用筛选项数据，见下方data描述 |

**data参数说明**
数据格式同上(/getInCommonUseFilter)接口返回值相同
只更改active参数数据
| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| active |boolean  |是  |true/false 启用/未启用当前筛选项  |

**data返回参数说明**
type: <u>JSON</u>
返回基本状态信息

* * *
#### 获取电站列表信息 /getChargingStationList
根据用户当前位置，推送附近充电站信息。

##### 请求
**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |
| latitude |number  |是  |纬度  |
| longitude |number  |是  |经度 |
| cityCode |  string| 否 |城市编码  |
| country |string  | 否 | 国家名称 |
| province | string |否  | 省份名称 |
| city | string | 否 |城市名称 |
| address | string | 是 | 详细地址 |
| pagesize| number|否|列表数量，默认全部
|pagenumber |number |否 |当前页下表，默认为第0页|

**data 返回参数说明**
type: <u>Array</u>

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|id|number|唯一标识|
|title |string |充电站名称 |
|round_date | string|营业时间 |
|price |number | 非会员充电价格|
| vip_price|number |会员充电价格 |
|special_offer |boolean |是否为特价优化充电站 |
|distance |string |距离当前位置距离 |
|car_count|number|车位总数|
|used|number|已使用车位数|
|p_tips|string|停车收费提示信息|

* * *
#### 获取当前电站详细信息数据/getChargingStationDetail
选择电站条目，获取详细数据信息。

##### 请求
**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |
| id |  number| 是 |电站标识  |
| name |  string| 是 |电站名称  |

**data 返回参数说明**
type: <u>JSON</u>

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|name|string|充电站名称|
|icon|string|电站缩略图|
|images|array|电站位置指引图，见下方images描述|
|parking_charge|string|停车收费状态|
|p_charge_tips|string|停车收费状态描述|
|invoice|string|开票方式|
|invoice_tips|string|开票描述|
|curr_price|number|当前充电价格|
|describe|array|电站描述标签|
|distance|string|距离电站距离|
|position|json|电站位置信息，见下方position描述|
|tips|string|电站广播提示|
|site|array|充电桩分类，见下方site描述|
|price|json|收费规格，见下方price描述|

**images 返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|title|string|指引图标题|
|datas|array|指引图数据，见下方datas描述|

**images >> datas返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|step|number|步骤序号|
|url|string|指引图链接|

**position 返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|title|string|电站位置描述|
|longitude|number|经度|
|latitude|number|纬度|

**site返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|type|string|充电桩类型|
|count|number|充电桩总数|
|unused|number|未使用充电桩数量|
|max_power|string|最大功耗|

**price返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|normal|number|常规充电价格|
|normal|number|vip充电价格|
|price_tips|string|充电价格描述|
|price_detail|array|充电价格详情，见下方price_detail描述|
|charging_pile|array|充电桩状态，见下方charging_pile描述|
|around_service|array|周边服务，见下方around_service描述|

**price >> price_detail返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|time|string|时间段|
|type|string|电价类型|
|price|number|此时段价格|
|electricity|number|此时段电费|
|service_charge|number|此时段服务费|

**price >> charging_pile返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|id|number|唯一标识|
|status|string|充电桩状态|
|max_power|string|最大功率|
|code|string|充电枪编码|

**price >> around_service返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|id|number|唯一标识|
|title|string|周边分类标题|
|data|array|分类数据，见下方data描述|

**price >> around_service >> data返回参数说明**

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|id|number|唯一标识|
|name|string|场景名称|
|position|string|场景位置描述|
|distance|string|距场景距离|

* * *
#### 获取支付订单信息/getPayInfo
生成支付订单信息
##### 请求
**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| token |string  |是  |用户唯一标识  |
| orderType |string  |是  |订单类型，见下方orderType类型描述  |
| order |json  |是  |订单数据信息，见下方order描述  |

**orderType类型说明**
| 类型标识 | 说明 |
| --- | ---|
| balance |账户余额充值  |
| recharge |充电支付  |

**order数据说明**
| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| id |number  |是  |商品id标识  |
| count |number  |是  |商品数量  |
| price |number  |是  |商品单价  |
| discount_coupon |json  |否  |优惠券  |

**data 返回参数说明**
type: <u>JSON</u>

| 参数名 | 类型 |说明  |
| --- | --- | --- |
|appid|string|小程序id|
|noncestr|string|随机字符串|
|package|string|固定值|
|partnerid|string|微信支付商户号|
|prepayid|string|统一下单订单号|
|timestamp|number|时间戳 (单位: 秒)|
|sign|string|签名 MD5/RSA |