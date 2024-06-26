import os
import random
import sys
import time
import pygame as pg


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))


DERUTA = {pg.K_UP: (0, -5), pg.K_DOWN: (0, +5),
         pg.K_LEFT: (-5, 0), pg.K_RIGHT: (+5, 0)}  # 移動量辞書 練習1

#houkou = {pg.K_UP: (0, -5)}  # 演習１

accs = [a for a in range(1, 11)]  # 加速度のリスト
for r in range(1, 11):  # 演習２
    bb_img = pg.Surface((20*r, 20*r))
    pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)


cry_img = pg.image.load("fig/1.png")  # 泣いているこうかとん


def check_bound(obj_rct:pg.Rect) -> tuple[bool, bool]:  # 練習３
    """
    こうかとんRect, または、爆弾Rectの画面内外判定用の関数
    引数：こうかとんRect、または、爆弾Rect
    戻り値：横方向判定結果、縦方向判定結果（True：画面内/False：画面外）
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate


def game_over(screen):  # 演習３
    """
    こうかとんと爆弾がぶつかった際のGameOver表記とブラックアウトの描画の関数
    引数：sikaku, txt
    戻り値：GameOver表記、ブラックアウト
    """
    sikaku = pg.Surface(WIDTH, HEIGHT)  
    pg.draw.rect(sikaku, (0, 0, 0), pg.Rect(WIDTH, HEIGHT))
            
    screen.blit(cry_img, [500, 450])
    fonto = pg.font.Font(None, 80)  
    txt = fonto.render("Game Over", True, (255, 255, 255))
    screen.blit(txt, [600, 450])
    screen.blit(cry_img, [975, 450])
    sikaku.set_alpha(200)

    pg.display.update()
    #print(test)
    time.sleep(5)


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    bg_img = pg.image.load("fig/pg_bg.jpg")   
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()

    kk_rct.center = 900, 400

    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    bd_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = +5, +5

    clock = pg.time.Clock()
    tmr = 0
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bd_rct):  # 練習４
            # こうかとんと爆弾がぶつかったら(= True)
            game_over(screen)
            
            return
        
        
        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        
        #if key_lst[pg.K_UP]:
            #sum_mv[1] -= 5
        #if key_lst[pg.K_DOWN]:
            #sum_mv[1] += 5
        #if key_lst[pg.K_LEFT]:
            #sum_mv[0] -= 5
        #if key_lst[pg.K_RIGHT]:
            #sum_mv[0] += 5
        
        for k, v in DERUTA.items():  # 練習1
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)

        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)

        bd_rct.move_ip(vx, vy)  # 爆弾の移動
        screen.blit(bd_img, bd_rct)  # 爆弾の表示
        
        yoko, tate = check_bound(bd_rct)
        if not yoko :
            vx *= -1  # 横方向にはみでたら
        if not tate :
            vy *= -1  # 縦方向にはみでたら

        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
