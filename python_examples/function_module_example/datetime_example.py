import datetime

current_time = datetime.datetime.now()
print('当前时间：{}'.format(current_time))
print('当前时间减8小时：{}'.format(current_time - datetime.timedelta(hours=8)))
print('当前时间减1天：{}\n'.format(current_time - datetime.timedelta(days=1)))

# 北京时间为东八区时间(UTC+8)，美国为西八区时间(UTC-8)，UTC0为世界标准时间
print('北京时间转换为UTC0时间：{}'.format(current_time.astimezone(datetime.timezone(datetime.timedelta(hours=0)))))
print('北京时间转换为西八区时间：{}\n'.format(current_time.astimezone(datetime.timezone(datetime.timedelta(hours=-8)))))

print('字符转换为datetime类型：{}'.format(datetime.datetime.strptime('2020-12-01 08:00:00', '%Y-%m-%d %H:%M:%S')))
print('datetime类型转换为字符：{}'.format(current_time.strftime('%Y-%m-%d %H:%M:%S')))
