from ctypes import cdll


def run_dll(dll_path, execute_file):
    """
    此函数用于执行DLL文件
    DLL文件为动态链接库(英语: Dynamic-link library, 缩写为DLL)
    它是微软公司在微软视窗操作系统中实现共享函数库概念的一种实现方式
    :param dll_path: DLL文件的所在路径
    :param execute_file: 要被执行的程序名
    :return:
    """
    dll_object = cdll.LoadLibrary(dll_path)  # 实例化DLL对象
    eval('dll_object.{}()'.format(execute_file))  # 调用DLL文件内的指定程序


if __name__ == '__main__':
    path = r'C:\Users\evaliu\Desktop\backups\new_dll\Barbados_3K_BPM2_DLL\builds\Barbados_3K_BPM2.dll'
    run_dll(dll_path=path, execute_file='CPP_CleanUp')
