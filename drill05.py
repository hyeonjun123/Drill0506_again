from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():
    global TUK_ground, character
    global arrow

    arrow = load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, cx, cy, frame
    global t, action

    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3

    set_new_target_arrow()


def set_new_target_arrow():
    global sx, sy, hx, hy, t,action
    global frame
    sx, sy = cx, cy  # p1: 시작점
    # hx, hy =50,50
    hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)  # p2: 끝점
    t = 0.0
    action = 1 if sx < hx else 0
    frame = 0


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(hx, hy)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame
    global cx, cy
    global t, action

    frame = (frame + 1) % 8


    if t <= 1.0:
        t += 0.001
        cx = (1 - t) * sx + t * hx  # cx는 시작점과 마지막점을 1-t : t비율로 섞음
        cy = (1 - t) * sy + t * hy
    else:
        cx,cy = hx,hy #캐릭터 위치를 목적지 위치와 정확히 일치시킴
        set_new_target_arrow()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()

while running:
    render_world()  # 월드의 현재 내용을 그린다.
    handle_events()  # 사용자 입력을 받아들인다.
    update_world()  # 월드안의 객체들의 상호작용을 계산하고, 그 결과를 update한다.

close_canvas()
