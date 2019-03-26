import os,time

def main(): #用函数封装，可复用性会高一些
    content = '风变编程，陪你一起学python' #广告词可自定义
    while True:
        os.system('cls') #完成清屏：清屏和打印结合起来，形成滚动效果
        print(content)
        content = content[1:] + content[0] #把字符串第一个元素移到了最后一个
        time.sleep(0.25)

if __name__ == '__main__':
    main()