# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MxdxloveItem(Item):
    # define the fields for your item here like:
    userid = Field()
    name = Field()
    profession = Field()
    is_vip = Field()
    gender = Field()
    age = Field()
    head_pic = Field()
    location = Field()
    height = Field()
    salary = Field()
    marriage_state = Field()
    when_to_get_married= Field()
    house_location = Field()
    car_location = Field()

    photos = Field()                        # []
    face_score = Field()                    # 颜值,float
    self_introduce = Field()

    # 详细资料
    weight = Field()                        # 体重,float,kg
    accept4long_distance_love = Field()     # 是否接受异地恋,int:0,1
    domicile_place = Field()                # 户籍地,str
    hometown = Field()                      # 老家,str
    parents_state = Field()
    smoke = Field()                         # 是否吸烟
    is_only = Field()                       # 是否是独生子女

    # 择偶标准
    age_limits = Field()
    education_limits = Field()
    profession_limits = Field()
    house_limits = Field()
    car_limits = Field()
    salary_limits = Field()
    height_limits = Field()
    domicile_place_limits = Field()
    location_limits = Field()
    hometown_limits = Field()
    marriage_state_limits = Field()
    hobbies = Field()                       # [{'food':['','',...]},{'films':[]}]


    # 话题
    opinion_id = Field()
    opinion_initiator = Field()             # 发起者 {'name':'abc','gender':'0','userid':'xxx'}
    opinion_title = Field()                 # 标题
    opinion_content = Field()               # 话题内容详情
    reply = Field()  # [{'userid':'content','liked':3,},{}]

