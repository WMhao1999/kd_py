# “朱佩娘”小程序接口交互文档

### 版本号：V1.0.0

#### 撰写日期：2024/01/30

#### 撰写人：武明皓

#### 域名：https://zhupeiniang.com

---

##### 用预登录: /userinfo

用户首次使用小程序默认自动登录，无需认证手机号等实名信息。

##### 请求

**请求类型** ：POST

**requset 请求参数说明**

| 参数名      | 类型   | 必填 | 说明                             |
| ----------- | ------ | ---- | -------------------------------- |
| openid      | string | 是   | 用户登录凭证，登录默认为空       |
| code        | string | 是   | 微信用户唯一 id 标识             |
| provider    | string | 否   | 登录服务商，默认'weixin'         |
| deviceBrand | string | 否   | 设备品牌，如：apple、huawei      |
| deviceId    | string | 否   | 当前设备 id                      |
| deviceModel | string | 否   | 当前设备型号                     |
| deviceType  | string | 否   | 当前设备类型，如：phone、pad、pc |
| system      | string | 否   | 操作系统及版本                   |

**data 返回参数说明**

| 参数名       | 类型   | 说明                                         |
| ------------ | ------ | -------------------------------------------- |
| status_code  | number | 请求返回状态，成功: 200、失败: 500           |
| openId       | string | 用户服务端唯一 id 标识                       |
| username     | string | 用户名                                       |
| icon         | string | 用户头像地址                                 |
| phone_number | number | 用户绑定手机号                               |
| user_status  | number | 用户账号信息，例：1=白名单用户、0=黑名单用户 |

**示例**

```
requset({
    url: 'https://zhupeiniang.com/userinfo',
    method: 'POST',
    data:{
        code: '0a121qHa14GpRGBu10Ha1s6RML821qH2'
    },
    success(res){
        console.log(res)
    }
})
```

---

##### 获取电站列表信息 /getChargingStationList

根据用户当前位置，推送附近充电站信息。

##### 请求

**请求类型** ：POST

**requset 请求参数说明**

| 参数名     | 类型   | 必填 | 说明                      |
| ---------- | ------ | ---- | ------------------------- |
| openid     | string | 是   | 用户唯一标识              |
| latitude   | number | 是   | 纬度                      |
| longitude  | number | 是   | 经度                      |
| cityCode   | string | 否   | 城市编码                  |
| country    | string | 否   | 国家名称                  |
| province   | string | 否   | 省份名称                  |
| city       | string | 否   | 城市名称                  |
| address    | string | 是   | 详细地址                  |
| pagesize   | number | 否   | 列表数量，默认全部        |
| pagenumber | number | 否   | 当前页下表，默认为第 0 页 |

**data 返回参数说明**

| 参数名     | 类型   | 说明                               |
| ---------- | ------ | ---------------------------------- |
| statusCode | number | 请求返回状态，成功: 200、失败: 500 |
| list       | array  | 见下方 list 参数详细说明           |

**list 参数说明**

| 参数名        | 类型    | 说明                 |
| ------------- | ------- | -------------------- |
| id            | number  | 唯一标识             |
| title         | string  | 充电站名称           |
| round_date    | string  | 营业时间             |
| price         | number  | 非会员充电价格       |
| vip_price     | number  | 会员充电价格         |
| special_offer | boolean | 是否为特价优化充电站 |
| distance      | string  | 距离当前位置距离     |
| car_count     | number  | 车位总数             |
| used          | number  | 已使用车位数         |
| p_tips        | string  | 停车收费提示信息     |

**示例**

```
requset({
    url: 'https://zhupeiniang.com/getChargingStationList',
    method: 'POST',
    data:{
        latitude: 0,
        longitude: 0,
        address: '北京市海淀区中关村软件园'
    },
    success(res){
        console.log(res)
    }
})
```
