#스티커리스트　코드
#sticker/ 파일에　있는　스티커　경로

stickerMaps=[(1,'red_heart', 'sticker/01_red_heart.png'),
             (2,'orange_heart', 'sticker/02_orange_heart.png'),
             (3,'yellow_heart', 'sticker/03_yellow_heart.png'),
             (4,'green_heart', 'sticker/04_green_heart.png'),
             (5,'blue_heart', 'sticker/05_blue_heart.png'),
             (6,'purple_heart', 'sticker/06_purple_heart.png'),
             (7,'pink_heart', 'sticker/07_pink_heart.png'),
             (8,'sunglasses', 'sticker/08_sunglasses.png'),
             (9,'rabbitears', 'sticker/09_rabbitears.png'),
             (10,'catears', 'sticker/10_catears.png'),
             (11,'apple', 'sticker/11_apple.png'),
             (12,'flower', 'sticker/12_flower.png'),
             (13,'bear', 'sticker/13_bear.png'),
             (14,'sinamorol', 'sticker/14_sinamorol.png'),
             (15,'8bit_twoheart', 'sticker/15_8bit_twoheart.png'),
             (16,'many_purpleheart', 'sticker/16_many_purpleheart.png'),
             (17,'colorfulcloud', 'sticker/17_colorfulcloud.png'),
             (18,'rabbitwithcloud', 'sticker/18_rabbitwithcloud.png'),
             (19,'urhandsome', 'sticker/19_urhandsome.png'),
             (20,'frame1', 'sticker/20_frame1.png'),
             (21,'frame2', 'sticker/21_frame2.png'),
             (22,'frame3', 'sticker/22_frame3.png'),
             (23,'frame4', 'sticker/23_frame4.png'),
             (24,'frame5', 'sticker/24_frame5.png'),
             (25,'neonheart', 'sticker/25_neonheart.png')
            ]

stickerNumber=[x[0] for x in stickerMaps]
stickerName=[x[1] for x in stickerMaps]
stickerPath=[x[2] for x in stickerMaps]

currentStickers={0:'None', 1:'None',2:'None',3:'None',4:'None',5:'None',6:'None',7:'None',8:'None',9:'None',10:'None'}
currentSticker=0
