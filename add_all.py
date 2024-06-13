import sqlite3

con = sqlite3.connect("instance/database.db")
cur = con.cursor()

Professor = [
    (
        1,
        "leejs@fcu.edu.tw",
        "李榮三",
        '''李榮三教授是逢甲大學資訊工程系的一位教授，專注於資訊工程領域的教學和研究。他在逢甲大學擔任多項重要職務，並參與多個研究計畫，致力於推動資訊技術的發展和應用。李教授的研究興趣包括人工智慧、機器學習、資料探勘等領域，他在這些方面發表了多篇學術論文，為學術界做出了重要貢獻。

        此外，李教授積極參與學術交流與合作，不僅在國內舉辦和參加各類學術研討會，還經常出國交流，拓展國際視野，為學生和同行提供寶貴的學術資源和指導''',
        """分機號碼 | #3767""",

        """無線通訊
Wireless Communications
資訊安全
Information Security
電子商務
E-Commerce
密碼學
Cryptography
數位影像處理
Image Processing
區塊鏈技術與應用
Blockchain technique and its application""",

    )
]
cur.executemany("INSERT INTO Professor VALUES(?, ?, ?, ?, ?, ?)", Professor)
con.commit()


class_schedule = [
    (1, 1, 7, "請益時間", 1),
    (2, 1, 8, "請益時間", 1),
    (3, 2, 5, "專題研究(一)", 1),
    (4, 3, 5, "專題研究(一)", 1),
    (5, 2, 8, "資訊專題研討(四)", 1),
    (6, 2, 9, "資訊專題研討(四)", 1),
    (7, 4, 5, "獨立研究", 1),
    (8, 5, 2, "資訊保密與安全", 1),
    (9, 5, 3, "資訊保密與安全", 1),
    (10, 5, 4, "資訊保密與安全", 1),
    (11, 5, 5, "獨立研究", 1),
]

cur.executemany("INSERT INTO class_schedule VALUES(?, ?, ?, ?, ?)", class_schedule)
con.commit()


school_experience = [
    (1,"中正大學", "資訊工程學系", "博士",1),
    (2,"中正大學", "資訊工程學系", "學士",1),
]
cur.executemany("INSERT INTO SchoolExperience VALUES(?, ?, ?, ?, ?)", school_experience)
con.commit()

work_experience = [
    (1,"校務企劃組", "組長", 1),
    (2,"系統維運組", "組長", 1),
    (3,"資通安全研究中心", "副主任", 1),
    (4,"資源管理中心", "主任", 1),
    (5,"資通安全研究中心", "主任", 1),
    (6,"資訊教學中心", "主任", 1),
    (7,"資訊工程學系", "系主任", 1),
    (8,"逢甲大學帆宣智慧城市5G實驗室", "研究員", 1),
    (9,"資訊工程學系", "助理教授", 1),
    (10,"資訊工程學系", "副教授", 1),
    (11,"資訊工程學系", "教授", 1),
    (12,"資訊工程學系", "特聘教授", 1),
]
cur.executemany("INSERT INTO WorkExperience VALUES(?, ?, ?, ?)", work_experience)
con.commit()


award = [
    (1,"2024 GiCS第4屆尋找資安女婕思競賽第一名", "國科會與教育部", 112, "2024-4", 1),
    (2,"逢甲大學論文著作獎勵傑出獎", "逢甲大學", 112, "2023-11", 1),
    (3,"2023 GiCS第3屆尋找資安女婕思競賽第一名", "國科會與教育部", 111, "2023-5", 1),
    (4,"2023 GiCS第3屆尋找資安女婕思競賽優勝", "逢甲大學", 111, "2023-5", 1),
    (5,"最佳學生論文", "International Computer Symposium 2022", 111, "2022-12", 1),
    (6,"資安技能金盾獎競賽 大專校院組嶄露頭角獎", "行政院技術服務中心", 111, "2022-11", 1),
    (7,"111年度國科會補助大專校院研究獎勵", "研究發展處", 111, "2022-10", 1),
    (8,"第52屆全國技能競賽網路安全類第二名", "勞動部", 111, "2022-8", 1),
    (9,"逢甲大學優良教材獎勵優等獎", "逢甲大學", 110, "2021-11", 1),
    (10,"110年度科技部補助大專校院研究獎勵", "產學合作處", 110, "2021-10", 1),
]
cur.executemany("INSERT INTO Award VALUES(?, ?, ?, ?, ?, ?)", award)
con.commit()

""""""