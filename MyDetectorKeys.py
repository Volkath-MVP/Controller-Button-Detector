import pygame as pg
import os
import sys
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
message_assistant = True
message_assistant1 = True
new_controller = False
controller_get = None
def get_path_file():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.dirname(__file__)
def draw_controller_game():
    root.fill(BLACK)
    joystick_center = pg.image.load(os.path.join(base_path, "controller_sprites", "joystick_normal.png"))
    root.blit(joystick_center, (50, 50))
def controller_detected():
    global message_assistant, message_assistant1, new_controller, controller_get
    if pg.joystick.get_count() == 0 and message_assistant:
        print("❌ Nenhum controle detectado!")
        message_assistant= False
    elif pg.joystick.get_count() == 1 and not message_assistant or pg.joystick.get_count() == 1 and message_assistant and message_assistant1:
        controller_get = pg.joystick.Joystick(0)
        print(f"✅ Controle detectado: {controller_get.get_name()}")
        print("Pressione botões para ver os eventos...")
        message_assistant = True
        message_assistant1 = False
        new_controller = True
while running:
    base_path = get_path_file()
    controller_detected()
    if new_controller == True:
        controller = controller_get
        controller.init()
        new_controller = False
    draw_controller_game()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.JOYBUTTONDOWN:
            print(f"🎮 Botão pressionado: {event.button}")
            if event.button == 6:
               running = False
               print("Você saiu com sucesso!")
        elif event.type == pg.JOYAXISMOTION:
            print(f"Eixo {event.axis} movido: {event.value}")
        elif event.type == pg.JOYHATMOTION:
            print(f"D-pad: {event.value}")
    pg.display.flip()
pg.quit()