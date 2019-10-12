'''
5.3.1	接口介绍
接口地址	http://ip:port/api/do
接口方法	http 接口 POST 方法
接口描述	用于查询持卡人在本系统中的注册信息
接口提供者	电子健康卡管理信息系统
5.3.2	请求参数
名称	说明	数据类型及
长度	备注（Y-必填）
appId	应用唯一识别码	AN..36	Y 由卡管系统分配
orgCode	机构唯一识别码	AN..36	Y 由卡管系统分配
timestamp	请求时间戳	AN..32	Y、加密
当前秒数，与标准时间一致
nonceStr	随机数	AN..32	Y
小于16 位的整
数
version	接口版本号	AN..10	Y
同文档版本号
method	方法名称	AN..50	Y 不签名
例：getPersonInfo
headSign	头部信息数字签名	AN..32	Y 不签名
详见数据签名方法
bodySign	上传信息数据签名	AN..32	Y 不签名
详见数据签名方法
signMode	数据签名模式	AN..32	Y 不签名
详见数据签名方法
encryptMode	数据加密模式	AN..32	Y 不签名
详见数据加密方法
signature	授权签名	AN..64	不签名
详细签名方式请参考《API授权管理体系对接说明》，此参数不参与头部签名
上传数据（可根据电子健康卡 ID 或证件信息（证件类型和证件号码）其一查询）
idCardTypeCode	证件类别	N2	Y、见《身份证类别代码》
idCode	证件号码	N20	Y、加密
erhcCardNo	电子健康卡 ID	AN..128	Y
appMode	操作方式	AN..2	Y 传输代码
1、APP在线申请
2、医疗卫生机构自助机申请
3、医疗卫生机构窗口申请
4、批量预生成
5、微信服务号
6、微信小程序
7、支付宝生活号
8、支付宝小程序
9、其他;
请求格式	{
"method":"getPersonInfo",
"headSign":"3a0e580d9bc9f0c3cdd62f91fc3a075f",
"bodySign":"f10cd9f4dcf23d98a1980210f95a3001",
"orgCode":"LDWLYXGS",
"version":"V1.0.6",
"appId":"60C90F3B796B41878B8D9C393E2B6329",
"nonceStr":"122685614143641657",
"timestamp":"60C90F3B796B41878B8D9C393E2B6329",
"signMode":"MD5",
"encryptMode":"DESede/ECB/ZeroBytePadding",
"signature": "304502201368C6FF4A228EBFBE22741EBBE71D27D32DBA9E79291E99D03B42E2BC3553FD022100EBF0559D4C40D05651D015C7EE04756C1E999D2727DD86757C3775FFB5762912",
"body":{
"erhcCardNo":"3D06CB522786C96739459300C8DED9AB14805A17ABD46B79",
"appMode":"2"
}
}

'''



import requests
import json
import time
import random
#构建参数
url = 'http://222.222.40.2:8098/api/do'
#参数
appid ='bb9077b5bed64924a36e9e4eee515c9a'#应用唯一识别码	AN..36	Y 由卡管系统分配
orgCode	= '5a679bf2129541cf84596fa11835608c' #机构唯一识别码	AN..36	Y 由卡管系统分配
timestamp = time.time()        #请求时间戳	AN..32	Y、加密当前秒数，与标准时间一致
nonceStr = random.randint(1,999999999999999)	#随机数	AN..32	Y小于16 位的整数
version = 'V1.0.6'	#接口版本号	AN..10	Y同文档版本号
method	='getPersonInfo'    #方法名称	AN..50	Y 不签名例：getPersonInfo
headSign =''	#头部信息数字签名	AN..32	Y 不签名详见数据签名方法
bodySign =''	#上传信息数据签名	AN..32	Y 不签名详见数据签名方法
signMode =''	#数据签名模式	AN..32	Y 不签名详见数据签名方法
encryptMode =''	#数据加密模式	AN..32	Y 不签名详见数据加密方法
signature =''	#授权签名	AN..64	不签名详细签名方式请参考《API授权管理体系对接说明》，此参数不参与头部签名


params ={
"method":"getPersonInfo",
"headSign":"3a0e580d9bc9f0c3cdd62f91fc3a075f",
"bodySign":"f10cd9f4dcf23d98a1980210f95a3001",
"orgCode":"LDWLYXGS",
"version":"V1.0.6",
"appId":"60C90F3B796B41878B8D9C393E2B6329",
"nonceStr":"122685614143641657",
"timestamp":"60C90F3B796B41878B8D9C393E2B6329",
"signMode":"MD5",
"encryptMode":"DESede/ECB/ZeroBytePadding",
"signature": "304502201368C6FF4A228EBFBE22741EBBE71D27D32DBA9E79291E99D03B42E2BC3553FD022100EBF0559D4C40D05651D015C7EE04756C1E999D2727DD86757C3775FFB5762912",
"body":{
"erhcCardNo":"3D06CB522786C96739459300C8DED9AB14805A17ABD46B79",
"appMode":"2"
}
}
print(sorted(params.items(), key=lambda item: item[1]))