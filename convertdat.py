# weixin_Image.dat 破解
# JPG 16进制 FF D8 FF
# PNG 16进制 89 50 4e 47
# GIF 16进制 47 49 46 38
# 微信.bat 16进制 a1 86----->jpg  ab 8c----jpg     dd 04 --->png
# 自动计算异或 值
import os

# 微信image.dat文件路径  
into_path = "./datfile/"
# picture output file
out_path = "./converted/" 


"""
    解码
    param f: 微信图片路径
    param fn:微信图片目录下的.dat
    return:
"""
def imageDecode(f, fn):
    dat_read = open(f, "rb")  						# 读取.dat 文件
    xo = Format(f)  								# 判断图片格式 并计算返回异或值 
    out = out_path + fn + ".jpg"  					# 图片输出路径
    print("文件输出路径{}".format(out), end='\n\n')
    png_write = open(out, "wb")  					# 图片写入
    dat_read.seek(0)  								# 重置文件指针位置

    for now in dat_read:  							# 循环字节
        for nowByte in now:
            newByte = nowByte ^ xo  				# 转码计算
            png_write.write(bytes([newByte]))  		# 转码后重新写入

    dat_read.close()
    png_write.close()


def findFile(f):
    """
    寻找文件
    param f:微信图片路径
    return:
    """
    fsinfo = os.listdir(f) 		 					# 把路径文件夹下的文件以列表呈现
    print(fsinfo)
    for fn in fsinfo:  								# 逐步读取文件
        temp_path = os.path.join(f, fn)  			# 拼接路径：微信图片路径+图片名
        if os.path.isfile(temp_path):  				# 判断目录还是.dat  #temp_path需为绝对路径，判断是否为文件，也可 if not os.path.isdir(temp_path):
            print('找到文件路径{}'.format(temp_path))
            fn = fn[:-4]  							# 截取字符串 去掉后缀.dat
            imageDecode(temp_path, fn)  			# 转码函数
        else:
            pass




def Format(f):
    """
    计算异或值
    各图片头部信息
    jpeg：ff d8 ff
    png：89 50 4e 47
    gif： 47 49 46 38
        """
    dat_r = open(f, "rb")

    try:
        a = [(0x89, 0x50, 0x4e), (0x47, 0x49, 0x46), (0xff, 0xd8, 0xff)]
        for now in dat_r:
            for xor in a:
                i = 0
                res = []
                nowg = now[:3]						#取前三个 数据信息
                for nowByte in nowg:
                    res.append(nowByte ^ xor[i])	#进行判断
                    i += 1
                if res[0] == res[1] == res[2]:		#三次异或值想等 说明就是那种格式
                    return res[0]					#返回异或值
    except:
        pass
    finally:
        dat_r.close()


# 运行
if __name__ == '__main__':
    findFile(into_path)