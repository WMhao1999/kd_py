# “朱佩娘”小程序接口交互文档
### 版本号：V1.0.0
#### 撰写日期：2024/01/30
#### 撰写人：武明皓
#### 域名：https://zhupeiniang.com

* * *
##### 用预登录:  /userinfo
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
| openId | string | 用户服务端唯一id标识 |  
| username |string  |用户名  |  
| icon | string | 用户头像地址 |
|phone_number |number |用户绑定手机号 |
|user_status |number |用户账号信息，例：1=白名单用户、0=黑名单用户 |

* * *
##### 获取广告位数据 /getBannerListData
首页广告位广告推送。
**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| openid |string  |是  |用户唯一标识  |

**data返回参数说明**
type: <u>Array</u>
| 参数名 | 类型 |说明  |
| --- | --- | --- |
|id | number|唯一id |
|type | string|可选类型 image/video|
|url |string |封面链接 (若type类型为video则为视频资源链接)|
|href | string|跳转广告资源链接 |

* * *
##### 获取筛选功能详细配置数据选项 /getFilterDetailOption
首页筛选功能，更多筛选内容数据。

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| openid |string  |是  |用户唯一标识  |

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
##### 设置筛选功能详细配置选项 /setFilterDetailOption
设置首页详细筛选功能。

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| openid |string  |是  |用户唯一标识  |
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
##### 设置快捷筛选功能配置选项 /setQuickFilterOption
首页3个分类快捷筛选选项设置 (价格较低、订车费、快慢充)。

**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| openid |string  |是  |用户唯一标识  |
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
##### 获取电站列表信息 /getChargingStationList
根据用户当前位置，推送附近充电站信息。

##### 请求
**请求类型** ：POST

**requset 请求参数说明**

| 参数名 | 类型 |必填  |说明  |
| --- | --- | --- | --- |
| openid |string  |是  |用户唯一标识  |
| latitude |number  |是  |纬度  |
| longitude |number  |是  |经度 |
| cityCode |  string| 否 |城市编码  |
| country |string  | 否 | 国家名称 |
| province | string |否  | 省份名称 |
| city | string | 否 |城市名称 |
| address | string | 是 | 详细地址 |
| pagesize| number|否|列表数量，默认全部
|pagenumber |number |否 |当前页下表，默认为第0页|

**data 参数说明**
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