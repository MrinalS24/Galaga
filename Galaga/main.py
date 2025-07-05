import pgzrun
import random

WIDTH = 1000
HEIGHT = 700

aliens = []
level = 1
end_game = False


bullets =[]

fighter = Actor("fighter")
mothership = Actor("mothership")

#bullets = [bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_6, bullet_7, bullet_8, bullet_9, bullet_10]

fighter.pos = WIDTH/2, HEIGHT - 80


def draw():
    screen.clear()
    screen.blit("sky", (0,0))
    for b in bullets:
        b.draw()
    fighter.draw()
    for i in aliens:
        i.draw()
    screen.draw.text(str(level), (800, 0), color = "white")
    



def create_alien():
    if level == 1:
        soldier_1 = Actor("green")
        soldier_2 = Actor("green")
        soldier_3 = Actor("green")
        x_value = random.randint(50, 750)
        y_value = 0
        soldier_1.pos = x_value,y_value
        soldier_2.pos = x_value + 75, y_value + 75
        soldier_3.pos = x_value + 150, y_value
        aliens.append(soldier_1)
        aliens.append(soldier_2)
        aliens.append(soldier_3)
    
    elif level > 1:
        soldier_1 = Actor("green")
        soldier_2 = Actor("green")
        soldier_3 = Actor("green")
        x_value = random.randint(50, 350)
        y_value = 0
        soldier_1.pos = x_value,y_value
        soldier_2.pos = x_value + 75, y_value + 75
        soldier_3.pos = x_value + 150, y_value
        aliens.append(soldier_1)
        aliens.append(soldier_2)
        aliens.append(soldier_3)

        soldier_4 = Actor("green")
        soldier_5 = Actor("green")
        soldier_6 = Actor("green")
        x_value = random.randint(400, 750)
        y_value = 0
        soldier_4.pos = x_value,y_value
        soldier_5.pos = x_value + 75, y_value + 75
        soldier_6.pos = x_value + 150, y_value
        aliens.append(soldier_4)
        aliens.append(soldier_5)
        aliens.append(soldier_6)



def update():
    global bullets, fighter, level
    if aliens:
        for a in aliens:
            a.y += 1
        if keyboard.d:
            fighter.x += 4
        elif keyboard.a:
            fighter.x -= 4
        
        for j in bullets:
            j.y -= 4
            if j.y <=0:
                bullets.remove(j)
                print(bullets)
            for g in aliens:
                if j.colliderect(g):
                    aliens.remove(g)
                    bullets.remove(j)
                    sounds.explosion.play()
    else:
        level += 1
        create_alien()
    



    

def on_mouse_down():
    bullet = Actor("bullet")
    bullets.append(bullet)
    bullet.pos = fighter.pos
    sounds.gunshot.play()


    



        


















create_alien()


pgzrun.go()