import pygame as pg
#Inicializa o pygame e os módulos necessários
pg.init()
pg.joystick.init()
pg.display.init()
#window width and height
Init_Width, Init_Height = 1000, 800
#window setting
root = pg.display.set_mode((Init_Width, Init_Height), pg.RESIZABLE)
pg.display.set_caption("AZ Controller Keys")
#colors
BLACK= (0, 0, 0)
running = True
def draw_controller_game():
    root.fill(BLACK)
if pg.joystick.get_count() == 0:
    print("❌ Nenhum controle detectado!")
else:
    controle = pg.joystick.Joystick(0)
    controle.init()
    print(f"✅ Controle detectado: {controle.get_name()}")
    print("Pressione botões para ver os eventos...")
while running:
    draw_controller_game()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.JOYBUTTONDOWN:
            print(f"🎮 Botão pressionado: {event.button}")
            if event.button == 6:
               running = False
    pg.display.flip()
pg.quit()