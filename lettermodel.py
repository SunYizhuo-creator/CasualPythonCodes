# 导入所需模块
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# 连接邮箱，然后使用QQ邮箱账号和授权码登录邮箱
qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465)
mailUser = "1563661768@qq.com" 
mailPass = "xxxx" 
qqMail.login(mailUser, mailPass)

# 设置收发件人
sender = "1563661768@qq.com" 
receiver = "yequbiancheng@baicizhan.com"
message = MIMEMultipart()
# 整合主题和收发件人到邮件对象中
message["Subject"] = Header("给夜曲的一封信——xx") 
message["From"] = Header(f"xx<{sender}>")
message["To"] = Header(f"yqbc<{receiver}>") 

# 设置邮件的内容
textContent = "xxxx"
mailContent = MIMEText(textContent, "plain", "utf-8")
# 读取图片文件
filePath = "xxxx" 
with open(filePath, "rb") as imageFile:
    fileContent = imageFile.read()
# 设置邮件附件，并添加标题
attachment = MIMEImage(fileContent)
attachment.add_header("Content-Disposition", "attachment", filename="入门课成绩单.jpg")

# 添加正文和附件
message.attach(mailContent)
message.attach(attachment)
# 发送邮件
qqMail.sendmail(sender, receiver, message.as_string())
print("发送成功")