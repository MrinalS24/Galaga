import pgzrun
import random

WIDTH = 1000
HEIGHT = 700

aliens = []
tanks = []
motherships = []
level = 1
message = ""
is_winning = None
count = 0


bullets =[]

fighter = Actor("fighter")



fighter.pos = WIDTH/2, HEIGHT - 80


def game_over():
    global message
    if is_winning == False:
        message = "Too bad. You Lost..."
    else:
        message = "Great Job! You Won!"
        sounds.winning.play()



def draw():
    global is_winning, count
    if level < 6:
        screen.clear()
        screen.blit("sky", (0,0))
        for b in bullets:
            b.draw()
        fighter.draw()
        for i in aliens:
            i.draw()
        for t in tanks:
            t.draw()
        if level == 5:
            for m in motherships:
                m.draw()
            if count == 5:
                motherships.remove(m)
                sounds.explosion.play()
        screen.draw.text(f"You are on level: {level}", (800, 50), color = "white")


    else:
        screen.fill(color = "black")
        screen.draw.text(message, (WIDTH/2, HEIGHT/2), color = "Yellow")
        is_winning = True
        game_over()

    



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
    else:
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
    if level > 2:
        tank_1 = Actor("purple")
        tank_2 = Actor("purple")
        tank_3 = Actor("purple")
        tx_value = random.randint(50, 300)
        ty_value = -200
        tank_1.pos = tx_value, ty_value
        tank_2.pos = tx_value + 125, ty_value + 75
        tank_3.pos = tx_value + 250, ty_value
        tanks.append(tank_1)
        tanks.append(tank_2)
        tanks.append(tank_3)
    if level > 3:
        tank_4 = Actor("purple")
        tank_5 = Actor("purple")
        tank_6 = Actor("purple")
        tx_value = random.randint(500, 800)
        ty_value = -200
        tank_4.pos = tx_value, ty_value
        tank_5.pos = tx_value + 125, ty_value + 75
        tank_6.pos = tx_value + 250, ty_value
        tanks.append(tank_4)
        tanks.append(tank_5)
        tanks.append(tank_6)
    if level > 4:
        tank_7 = Actor("purple")
        tank_8 = Actor("purple")
        tank_9 = Actor("purple")
        tx_value = random.randint(200, 800)
        ty_value = -400
        tank_7.pos = tx_value, ty_value
        tank_8.pos = tx_value + 125, ty_value + 75
        tank_9.pos = tx_value + 250, ty_value
        tanks.append(tank_7)
        tanks.append(tank_8)
        tanks.append(tank_9)

        mothership = Actor("mothership")
        mx = 500
        my = -600
        mothership.pos = mx, my
        motherships.append(mothership)








def update():
    global bullets, fighter, level, is_winning, count
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
            for g in aliens:
                if j.colliderect(g):
                    aliens.remove(g)
                    bullets.remove(j)
                    #sounds.explosion.play()
    elif tanks:
        for t in tanks:
            t.y += 1
        if keyboard.d:
            fighter.x += 4
        elif keyboard.a:
            fighter.x -= 4

        for j in bullets:
            j.y -= 4
            for s in tanks:
                if j.colliderect(s):
                    tanks.remove(s)
                    bullets.remove(j)
                    sounds.explosion.play()
            if j.y <=0:
                bullets.remove(j)
    elif motherships:
        for m in motherships:
            m.y += 1
            if keyboard.d:
                fighter.x += 4
            elif keyboard.a:
                fighter.x -= 4
            for l in bullets:
                l.y -= 4
                if l.y <= 0:
                    bullets.remove(l)
                if l.colliderect(m):
                    count += 1
                    bullets.remove(l)



    else:
        level += 1
        create_alien()
    
    for a in aliens:
        if a.y >= WIDTH or a.colliderect(fighter):
            is_winning = False
            game_over()
    for t in tanks:
        if t.y >= WIDTH or t.colliderect(fighter):
            is_winning = False
            game_over()
    for m in motherships:
        if m.y >= WIDTH or m.colliderect(fighter):
            is_winning = False
            game_over()
        
    

    



    

def on_mouse_down():
    bullet = Actor("bullet")
    bullets.append(bullet)
    bullet.pos = fighter.pos
    #sounds.gunshot.play()


    



        


















create_alien()


pgzrun.go()
