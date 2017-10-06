
# 爬虫分析

imuseum 数据格式分为两层： view 和 data 层。

view 里包含一个个块（cell），每个块里有点击动作（action）。
cell 的 数据都在 data 层里。


## Model


### City
城市
### Museum
博物馆
### Event
展览
### User
用户


关系：

- City - Museum
一对多，一个城市有多个博物馆。
- Museum - Event
一对多， 一个博物馆有多个展览。
- User - User
多对多。Follow;对话
- User - Event
多对多。
用户对展览的行为有： 参观，标记，评论，照片。









