import pygame as pg
import sys
import math

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_10_img = pg.transform.rotate(kk_img, 10)
    kk_list = (kk_img, kk_10_img)
    bg_re_img = pg.transform.flip(bg_img, True, False)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_re_img, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(pg.transform.rotate(kk_img,10*math.cos(tmr/20)), [300, 200])
        

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()