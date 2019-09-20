import json
import csv
import pandas


def write_json_data(msg=None, file_name='json_file', do_read=False):
    if do_read:
        with open('{}.json'.format(file_name), 'r', encoding='utf-8') as rf:
            read_file = rf.read()
            file = json.loads(read_file)
            print('find json data:\n', file)
            return file
    else:
        with open('{}.json'.format(file_name), 'w', encoding='utf-8') as wf:
            wf.write(json.dumps(msg, ensure_ascii=False, indent=2) + '\n')


def write_csv_data(msg=None, file_name='csv_file', header=None, do_read=False):
    if do_read:
        # 用csv格式读取
        with open('{}.csv'.format(file_name), 'r', encoding='utf-8') as rf:
            reader = csv.reader(rf)
            print('find csv data: ')
            for line in reader:
                print(line)

        # 用pandas格式读取
        result = pandas.read_csv('{}.csv'.format(file_name))
        print(result)
    else:
        with open('{}.csv'.format(file_name), 'w', encoding='utf-8', newline='') as wf:
            # TODO 这个是普通格式的写入
            write = csv.writer(wf)
            for i in msg:
                # 循环写入每行数据
                write.writerow(i)
            # 同时写入多行数据
            write.writerows(msg)
            # TODO 这个是字典格式的写入
            dict_write = csv.DictWriter(wf, fieldnames=header)
            dict_write.writeheader()
            # 写入单行字典数据
            msg = {'name': 'evan', 'id': '66'}
            dict_write.writerow(msg)
            # 同时写入多行字典数据
            msg = [{'name': 'evan', 'id': '66'}, {'name': 'jane', 'id': '99'}]
            dict_write.writerows(msg)


if __name__ == '__main__':
    # run write json file
    write_json_data(msg={'name': 'evan'})
    # run write csv file
    header = ['name', 'id']
    write_csv_data(msg=[['name', 'evan'], ['id', '66']], header=header)
