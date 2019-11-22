"""
分析log
"""
import re
import os
import shutil
import csv
import logging

check_nation_config = {
    '-A-': ['0x0000', '0x000B'],
    '-B-': ['0x0000', '0x0029'],
    '-C-': ['0x0001', '0x0016'],
    '-D-': ['0x0000', '0x002F'],
    '-E-': ['0x0001', '0x000C'],
    '-F-': ['0x0031', '0x0032'],
    '-G-': ['0x0001', '0x0036'],
    '-H-': ['0x0001', '0x0033'],
    '-I-': ['0x0001', '0x001A'],
    '-K-': ['0x0001', '0x0017'],
    '-N-': ['0x0000', '0x0015'],
    '-P-': ['0x002D', '0x0039'],
    '-Q-': ['0x002D', '0x002E'],
    '-R-': ['0x0001', '0x002A'],
    '-S-': ['0x0001', '0x000E'],
    '-T-': ['0x0000', '0x0019'],
    '-Z-': ['0x0000', '0x0030'],
}

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class Analysis(object):

    def __init__(self, log_path):
        self.log_path = log_path

    @staticmethod
    def write_csv_data(write_info, file_name='csv_file.csv', headers=None):
        with open('{}'.format(file_name), 'w', encoding='utf-8', newline='') as wf:
            dict_write = csv.DictWriter(wf, fieldnames=headers)
            dict_write.writeheader()
            for i in write_info:
                dict_write.writerow(i)

    def main(self):
        log_folder = os.listdir(self.log_path)
        logger.info('Log folder length: {}'.format(len(log_folder)))

        result_info = []
        for index, each_log in enumerate(log_folder):
            result_dict = {}
            logger.debug('Start {}: {}'.format(index + 1, each_log))

            with open(os.path.join(self.log_path, each_log), 'r') as file:
                log = file.read()

            radio_carrier_set = re.search('set_cookie RADIO_CARRIER_SET (.+)', log)
            radio_5g_carrier_set = re.search('set_cookie 5G_RADIO_CARRIER_SET (.+)', log)
            uut_type = re.search('uut_type:(AIR-.+?-.+?-.+)', log)
            serial_number = re.search(r'serial_number:(FGL\w{8})', log)

            if radio_carrier_set:
                result_dict['radio_carrier_set'] = radio_carrier_set.group(1)
            else:
                result_dict['radio_carrier_set'] = 'None'

            if radio_5g_carrier_set:
                result_dict['radio_5g_carrier_set'] = radio_5g_carrier_set.group(1)
            else:
                result_dict['radio_5g_carrier_set'] = 'None'

            if uut_type:
                result_dict['uut_type'] = uut_type.group(1)
            else:
                result_dict['uut_type'] = 'None'

            if serial_number:
                result_dict['serial_number'] = serial_number.group(1)
            else:
                result_dict['serial_number'] = 'None'

            if result_dict['serial_number'] == each_log.split('.')[0]:
                result_dict['sn_match_status'] = 'Pass'
            else:
                result_dict['sn_match_status'] = 'Fail'

            for key, value in check_nation_config.items():
                if key in result_dict['uut_type']:
                    result_dict['radio_carrier_correct_value'] = value[0]
                    if result_dict['radio_carrier_set'] == value[0]:
                        result_dict['radio_carrier_match_status'] = 'Pass'
                    else:
                        result_dict['radio_carrier_match_status'] = 'Fail'

                    result_dict['radio_5g_carrier_correct_value'] = value[1]
                    if result_dict['radio_5g_carrier_set'] == value[1]:
                        result_dict['radio_5g_carrier_match_status'] = 'Pass'
                    else:
                        result_dict['radio_5g_carrier_match_status'] = 'Fail'
                    break
            else:
                result_dict['radio_carrier_correct_value'] = 'Not found the area'
                result_dict['radio_carrier_match_status'] = 'Not found the area'
                result_dict['radio_5g_carrier_correct_value'] = 'Not found the area'
                result_dict['radio_5g_carrier_match_status'] = 'Not found the area'

            # 如果result_dict里有Fail状态就移出去
            for i in result_dict.values():
                if 'Fail' in i or 'Not found the area' in i:
                    result_info.append(result_dict)
                    logger.error('{}: {} is Fail, Now move the files'.format(index + 1, each_log))
                    before_path = os.path.join(self.log_path, each_log)
                    # TODO 转移的文件夹名称
                    after_path = os.path.join(os.path.dirname(self.log_path), 'AP2802_AP3802_error_logs')
                    shutil.move(before_path, after_path)
                    break

            logger.debug('{}: {} Analysis done'.format(index + 1, each_log))
            # break

        logger.info('result_info length: {}'.format(len(result_info)))
        root_path, file_name = os.path.split(self.log_path)
        csv_file_name = os.path.join(root_path, '{}.csv'.format(file_name))
        headers = ['uut_type', 'serial_number', 'sn_match_status', 'radio_carrier_set', 'radio_carrier_correct_value',
                   'radio_carrier_match_status', 'radio_5g_carrier_set', 'radio_5g_carrier_correct_value',
                   'radio_5g_carrier_match_status']
        self.write_csv_data(result_info, file_name=csv_file_name, headers=headers)
        logger.debug('Write csv data done')


if __name__ == '__main__':
    # TODO 分析的log文件夹
    analysis = Analysis(log_path=r'C:\Users\evaliu\Desktop\record_analysis\AP2802_AP3802_result\AP2802_AP3802')
    analysis.main()
