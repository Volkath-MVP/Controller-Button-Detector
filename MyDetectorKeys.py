import pygame as pg
# Inicializa o pygame e os módulos necessários
pg.init()
pg.joystick.init()
running = True
if pg.joystick.get_count() == 0:
        print("❌ Nenhum controle detectado!")
else:
    controle = pg.joystick.Joystick(0)
    controle.init()
    print(f"✅ Controle detectado: {controle.get_name()}")
    print("Pressione botões para ver os eventos...")
def quit_program():
    global running
    if event.type == pg.QUIT:
        running = False
while running:
    for event in pg.event.get():
        if event.type == pg.JOYBUTTONDOWN:
            print(f"🎮 Botão pressionado: {event.button}")
            if event.button == 6:
                running = False
pg.QUIT