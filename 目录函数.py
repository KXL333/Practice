
#获取一个目录大小的函数
import os

total_size = 0
file_num = 0
dir_num = 0
#定义一个统计目录大小的函数
def dir_size(path):
    '''用于统计目录大小'''
    global total_size
    global file_num
    global dir_num

    for lists in os.listdir(path):
        sub_path = os.path.join(path,lists)
        print(sub_path)
        if os.path.isfile(sub_path):
            file_num += 1    #统计文件的数量
            total_size = total_size + os.path.getsize(sub_path)  #统计文件的大小
        elif os.path.isdir(sub_path):
            dir_num += 1     #统计文件夹的数量
            dir_size(sub_path)   #递归遍历子文件夹

def output(path):
    print('The total size of '+path+' is:',total_size)
    print('The total number of files in '+path+' is:',file_num)
    print('The total number of directories in '+path+' is:',dir_num)

dir_size("D:\\CSDN\\课件\\第二周\\14节-Python文件操作\\dd")
output("D:\\CSDN\\课件\\第二周\\14节-Python文件操作\\dd")