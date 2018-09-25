#coding=utf8
import itchat
from itchat.content import  TEXT,FRIENDS
import json

private_auto=json.load(open("private_auto.json",encoding="utf8"))
# group_auto=json.load(open("group_auto.json"))
friend_auto=json.load(open("friend_verify.json",encoding="utf8"))
friend_auto=friend_auto["friend_verify"]
@itchat.msg_register(TEXT)
def text_reply(msg):
    if msg['Content'] in private_auto:
        return '%s'%private_auto[msg['Content']]

# 以下四类的消息的Text键下存放了用于下载消息内容的方法，传入文件地址即可
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
    # msg['Text'](msg['FileName'])
    # return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 收到好友邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('%s'%friend_auto, msg['RecommendInfo']['UserName'])

# 在注册时增加isGroupChat=True将判定为群聊回复
# @itchat.msg_register(TEXT, isGroupChat = True)
# def groupchat_reply(msg):
    # if msg['isAt']:
        # itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login(False,enableCmdQR=True)
itchat.run()