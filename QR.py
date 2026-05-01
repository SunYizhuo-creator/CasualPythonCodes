from MyQR import myqr
myqr.run(
    words="https://www.bilibili.com/video/BV1qU4y1F73A/?spm_id_from=333.337.search-card.all.click",
    version=10,
    picture=r"C:\Users\Administrator\Pictures\Saved Pictures\小猫头像.jpg",
colorized = True,
save_name = "What_can_I_say.png",
save_dir = r"C:\Users\Administrator\OneDrive\编程成果"
)
print("生成成功")