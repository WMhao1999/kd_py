loginData = {
    'token': '1324654esa5d41432',
    'status': 1,
    'errMsg': '',
    'userinfo': {
        'username': '鲸要我保护海',
        'icon': 'https://img1.baidu.com/it/u=1696401964,991779968&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=500',
        'phone_number': '17600000000',
        'user_status': 1
    }
}

verCodeData = {
    'code': '874562',
    'token': '1324654esa5d41432',
    'status': 1,
}

# 用户详情 /userinfo
userInfoData = {
    'openid': 'wx12345678',
    'token': '1324654esa5d41432',
    'username': '鲸要我保护海',
    'icon': 'https://img1.baidu.com/it/u=1696401964,991779968&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=500',
    'phone_number': '17600000000',
    'user_status': 1
}

# 首页广告位数据
bannerListData = [
    {
        'id': 0,
        'type': 'image',
        'url': 'https://ossweb-img.qq.com/images/lol/web201310/skin/big84000.jpg',
        'href': ''
    }, {
        'id': 1,
        'type': 'image',
        'url': 'https://ossweb-img.qq.com/images/lol/web201310/skin/big37006.jpg',
        'href': ''
    }, {
        'id': 2,
        'type': 'image',
        'url': 'https://ossweb-img.qq.com/images/lol/web201310/skin/big39000.jpg',
        'href': ''
    }, {
        'id': 3,
        'type': 'image',
        'url': 'https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg',
        'href': ''
    }
]

# 首页筛选项详细数据
filterDetailOptions = [
    {
        'title': "运营类型",
        'options': [{
            'name': "公共站",
            'active': False
        }, {
            'name': "个人站",
            'active': False
        }]
    },
    {
        'title': "电桩类型",
        'options': [{
            'name': "快充",
            'active': False
        }, {
            'name': "慢充",
            'active': False
        }]
    },
    {
        'title': "停车费",
        'options': [{
            'name': "收费停车",
            'active': False
        }, {
            'name': "限时免费停车",
            'active': False
        }, {
            'name': "免费停车",
            'active': False
        }]
    },
    {
        'title': "营销活动",
        'options': [{
            'name': "天天特价",
            'active': False
        }, {
            'name': "限时特价",
            'active': False
        },
            {
                'name': "818特价站",
                'active': False
            },
            {
                'name': "充电险",
                'active': False
            },
            {
                'name': "休闲配套",
                'active': False
            },
            {
                'name': "特患站",
                'active': False
            }
        ]
    },
    {
        'title': "位置",
        'options': [{
            'name': "地上",
            'active': False
        }, {
            'name': "地下",
            'active': False
        }, {
            'name': "室内",
            'active': False
        }]
    },
    {
        'title': "站点设施",
        'options': [{
            'name': "卫生间",
            'active': False
        }, {
            'name': "休息室",
            'active': False
        }, {
            'name': "大车能充电",
            'active': False
        }, {
            'name': "便利店",
            'active': False
        }, {
            'name': "餐饮",
            'active': False
        }, {
            'name': "饮用水",
            'active': False
        }, {
            'name': "750V",
            'active': False
        }, {
            'name': "自动售货机",
            'active': False
        }, {
            'name': "有人值守",
            'active': False
        }, {
            'name': "洗车免费",
            'active': False
        }, {
            'name': "共享充电宝",
            'active': False
        }, {
            'name': "洗车",
            'active': False
        }, {
            'name': "雨棚",
            'active': False
        }, {
            'name': "可降地锁",
            'active': False
        }]
    },
    {
        'title': "站点等级",
        'options': [{
            'name': "普通",
            'active': False
        }, {
            'name': "优选",
            'active': False
        }, {
            'name': "精选",
            'active': False
        }, {
            'name': "星级",
            'active': False
        }]
    },
    {
        'title': "其它",
        'options': [{
            'name': "精品站",
            'active': False
        }, {
            'name': "快电优选",
            'active': False
        }, {
            'name': "出租车特惠",
            'active': False
        }, {
            'name': "进门需登记",
            'active': False
        }, {
            'name': "油车占位严重",
            'active': False
        }, {
            'name': "低价特惠",
            'active': False
        }, {
            'name': "商家会员卡",
            'active': False
        }, {
            'name': "只对内部开放",
            'active': False
        }, {
            'name': "超时占位收费",
            'active': False
        }]
    }
]

# 获取电站列表信息 /getChargingStationList
chargingListData = [
    {
        'title': "开迈斯充电站(北京市海淀区大南路)",
        'round_date': 24,
        'price': 1.48,
        'special_offer': True,
        'vip_price': 1.42,
        'tips': ["碳积分最高抵1.00元", "充电险"],
        'distance': 3.76,
        'car_count': 8,
        'used': 6,
        'p_tips': "限时免费停车: 绑定车牌,充电，1小时内免费,超时按电费算",
        'id': 0
    },
    {
        'title': "开迈斯充电站(北京市海淀区龙德购物广场)",
        'round_date': 24,
        'price': 1.91,
        'special_offer': False,
        'vip_price': 1.84,
        'tips': ["充电险"],
        'distance': 4.49,
        'car_count': 5,
        'used': 3,
        'p_tips': "收费停车: 8元每小时",
        'id': 1
    },
    {
        'title': "开迈斯充电站(北京市国家体育馆南门)",
        'round_date': 12,
        'price': 1.50,
        'special_offer': True,
        'vip_price': 1.42,
        'tips': [],
        'distance': 8.71,
        'car_count': 84,
        'used': 64,
        'p_tips': "限时免费停车: 绑定车牌",
        'id': 2
    },
    {
        'title': "开迈斯充电站(北京市海淀区大南路)",
        'round_date': 24,
        'price': 1.48,
        'special_offer': True,
        'vip_price': 1.42,
        'tips': ["碳积分最高抵1.00元", "充电险"],
        'distance': 3.76,
        'car_count': 8,
        'used': 6,
        'p_tips': "限时免费停车: 绑定车牌,充电，1小时内免费,超时按电费算",
        'id': 3
    },
    {
        'title': "开迈斯充电站(北京市海淀区龙德购物广场)",
        'round_date': 24,
        'price': 1.91,
        'special_offer': False,
        'vip_price': 1.84,
        'tips': ["充电险"],
        'distance': 4.49,
        'car_count': 5,
        'used': 3,
        'p_tips': "收费停车: 8元每小时",
        'id': 4
    },
    {
        'title': "开迈斯充电站(北京市国家体育馆南门)",
        'round_date': 12,
        'price': 1.50,
        'special_offer': True,
        'vip_price': 1.42,
        'tips': [],
        'distance': 8.71,
        'car_count': 84,
        'used': 64,
        'p_tips': "限时免费停车: 绑定车牌",
        'id': 5
    }
]

# 获取常用筛选信息 /getInCommonUseFilter
inCommonUseFilterData = [
    {
        'name': "快速稳定",
        'id': 0,
        'active': False
    },
    {
        'name': "VIP站",
        'id': 1,
        'active': False
    },
    {
        'name': "免费停车",
        'id': 2,
        'active': False
    },
    {
        'name': "快电优选",
        'id': 3,
        'active': False
    },
    {
        'name': "饮用水",
        'id': 4,
        'active': False
    }
]

chargingdetaildata = {
    'name': '澳门中心充电站',
    'icon': 'https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2023%2F0515%2Fe79896dbj00rup4ln00bhc000hs009rg.jpg&thumbnail=660x2147483647&quality=80&type=jpg',
    'images': [
        {
            'title': '室外引导',
            'datas': [
                {
                    'step': 1,
                    'url': 'https://inews.gtimg.com/newsapp_bt/0/14836123749/641'
                },
                {
                    'step': 2,
                    'url': 'https://img-issue.yunnan.cn/uploadfile/test/2021/0915/202109151626077135.jpg'
                }
            ]
        },
        {
            'title': '室内引导',
            'datas': [
                {
                    'step': 1,
                    'url': 'https://inews.gtimg.com/newsapp_bt/0/14836123749/641'
                },
                {
                    'step': 2,
                    'url': 'https://img-issue.yunnan.cn/uploadfile/test/2021/0915/202109151626077135.jpg'
                }
            ]
        }
    ],
    'parking_charge': '限时免费停车',
    'p_charge_tips': '一小时以内免费，超过一小时 2元/时',
    'invoice': '公司开票',
    'invoice_tips': '24小时内免费开票',
    'service_time': '24小时',
    'service_status': '运营中',
    'curr_price': 1.14,
    'describe': [
        '极客能源',
        '超级快充',
        '底下车库'
    ],
    'distance': '500m',
    'position': {
        'title': '北京市昌平区沙河站地铁站',
        'longitude': 116.291560,
        'latitude': 40.158619
    },
    'tips': '三分钟前有人充电',
    'site': [
        {
            'type': '快充',
            'count': 10,
            'unused': 2,
            'max_power': '120Kw'
        },
        {
            'type': '慢充',
            'count': 10,
            'unused': 2,
            'max_power': '60Kw'
        }
    ],
    'price': {
        'normal': 1.14,
        'vip': 1.09,
        'price_tips': 'VIP优惠价格有幅度限制，VIP价格服务优惠0.05元/度',
        'price_detail': [
            {
                'time': '00:00 - 06:00',
                'type': '朱佩娘价格',
                'price': 1.89,
                'electricity': 0.84,
                'service_charge': 1.05
            },
            {
                'time': '06:00 - 12:00',
                'type': '朱佩娘价格',
                'price': 1.89,
                'electricity': 0.84,
                'service_charge': 1.05
            },
            {
                'time': '12:00 - 24:00',
                'type': '朱佩娘价格',
                'price': 1.89,
                'electricity': 0.84,
                'service_charge': 1.05
            }
        ],
        'charging_pile': [
            {
                'status': '空闲',
                'max_power': '360Kw',
                'code': '000100214000168A0',
                'id': 0
            },
            {
                'status': '空闲',
                'max_power': '360Kw',
                'code': '000100214000169A0',
                'id': 1
            },
            {
                'status': '空闲',
                'max_power': '360Kw',
                'code': '000100214000177A0',
                'id': 2
            }
        ],
        'around_service': [
            {
                'title': '卫生间',
                'id': 0,
                'data': [
                    {
                        'id': 0,
                        'name': '公共厕所',
                        'postion': '地铁站旁公厕',
                        'distance': '300m'
                    },
                    {
                        'id': 1,
                        'name': '公共厕所',
                        'postion': '地铁站旁商场公厕',
                        'distance': '600m'
                    }
                ]
            },
            {
                'title': '洗车',
                'id': 1,
                'data': [
                    {
                        'id': 0,
                        'name': '公共厕所',
                        'postion': '地铁站旁公厕',
                        'distance': '300m'
                    },
                    {
                        'id': 1,
                        'name': '公共厕所',
                        'postion': '地铁站旁商场公厕',
                        'distance': '600m'
                    }
                ]
            },
            {
                'title': '美食',
                'id': 2,
                'data': [
                    {
                        'id': 0,
                        'name': '公共厕所',
                        'postion': '地铁站旁公厕',
                        'distance': '300m'
                    },
                    {
                        'id': 1,
                        'name': '公共厕所',
                        'postion': '地铁站旁商场公厕',
                        'distance': '600m'
                    }
                ]
            }
        ]
    }
}
