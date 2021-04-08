import datetime

current_time = datetime.datetime.now()
print('当前时间：{}'.format(current_time))
print('当前时间减8小时：{}'.format(current_time - datetime.timedelta(hours=8)))
print('当前时间减1天：{}\n'.format(current_time - datetime.timedelta(days=1)))


# 时间计算
now_time = datetime.datetime.now() + datetime.timedelta(days=1)
print('两个时间差（秒）：{}'.format((now_time - current_time).total_seconds()))
print('两个时间差（天）：{}\n'.format((now_time - current_time).days))


# 时间转化
print('取起始整点：{}'.format(current_time.replace(minute=0, second=0, microsecond=0)))
print('转化为时间戳：{}'.format(current_time.timestamp()))
print('时间戳转换为datetime：{}\n'.format(datetime.datetime.fromtimestamp(current_time.timestamp())))


# 时区转化：UTC0为世界标准时间，夏令时比冬令时快1小时，夏令时比北京时间慢15小时，冬令时慢16小时
print('北京时间转换为UTC0时间：{}'.format(current_time.astimezone(datetime.timezone(datetime.timedelta(hours=0)))))
print('北京时间转换为西八区时间：{}'.format(current_time.astimezone(datetime.timezone(datetime.timedelta(hours=-8)))))
print('转换为可计算的datetime类型：{}\n'.format(current_time.astimezone(datetime.timezone(datetime.timedelta(hours=-8))).replace(tzinfo=None)))


# 类型转化
print('字符转换为datetime类型：{}'.format(datetime.datetime.strptime('2020-12-01 08:00:00', '%Y-%m-%d %H:%M:%S')))
print('datetime类型转换为字符：{}'.format(current_time.strftime('%Y-%m-%d %H:%M:%S')))
