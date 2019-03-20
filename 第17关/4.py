#先导入模块
from MyQR import myqr

myqr.run(
    # 打扫二维码后，显示的内容，或是跳转的链接
    words='http://d.whgvip.com',
    # 设置容错率
    version=5,
    # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    level='H',
    picture='d://python//第17关//p54438000.gif',
    colorized=True,
    # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    contrast=1.0,
    # 用来调节图片的亮度，用法同上。
    brightness=1.0,
    # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    save_name='d://python//第17关//gg.gif',
)