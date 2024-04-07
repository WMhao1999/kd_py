# 用户详情 /userinfo
userInfoData = {
    'openid': 'wx12345678',
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
