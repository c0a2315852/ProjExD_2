import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))


DERUTA = {pg.K_UP: (0, -5), pg.K_DOWN: (0, +5),
         pg.K_LEFT: (-5, 0), pg.K_RIGHT: (+5, 0)}  # 移動量辞書 練習1

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    bg_img = pg.image.load("fig/pg_bg.jpg")   
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()

    vx, vy = +5, +5

    kk_rct.center = 900, 400

    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    bd_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)


    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0])
        bd_rct.move_ip(vx, vy) 
        screen.blit(bd_img, bd_rct)
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        '''
        if key_lst[pg.K_UP]:
            sum_mv[1] -= 5
        if key_lst[pg.K_DOWN]:
            sum_mv[1] += 5
        if key_lst[pg.K_LEFT]:
            sum_mv[0] -= 5
        if key_lst[pg.K_RIGHT]:
            sum_mv[0] += 5
        '''
        for k, v in DERUTA.items():  # 練習1
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()