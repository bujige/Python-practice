import os

# def search(path, fileName):
#     for file in os.listdir(path):
#         if os.path.isfile(path + '\\' + file):
#             if fileName in file:
#                 print(file, '=>', path + '\\' + file)
#         else:
#             search(path + '\\' + file, fileName)





# 查找path 路径下，包含 fileName 的所有文件，并打印 路径
def search(path, fileName):
    # 递归遍历当前目录
    def searchCurrent(path, fileName, virgule):
        if os.path.isdir(path): # 当前路径为目录
            for file in os.listdir(path):
                if os.path.isfile(path + virgule + file):   # 当前路径为文件
                    if fileName in file:   # 当前文件包含 fileName
                        print(file, '=>', path + virgule + file)
                else:   # 当前路径为目录，则递归遍历
                    searchCurrent(path + virgule + file, fileName, virgule)
        else:
            if fileName in file:  # 当前文件包含 fileName
                print(file, '=>', path + virgule + file)

    virgule = ''
    # 根据系统判断分隔符
    if os.name == 'posix':
        virgule = '//'
    else:
        virgule = '\\'
    searchCurrent(path, fileName, virgule)


search('/Users/doc88/Desktop', 'xml')