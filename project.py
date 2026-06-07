from graphics import *

def draw_artifact1(win):
    objects = []
    
    body = Oval(Point(135, 520), Point(225, 640))
    body.setFill("#b45309")  
    body.setOutline("#78350f")
    body.setWidth(2)
    body.draw(win)
    objects.append(body)

    bottom_sharp = Polygon(Point(142, 590), Point(218, 590), Point(180, 648))
    bottom_sharp.setFill("#b45309")
    bottom_sharp.setOutline("#b45309")  
    bottom_sharp.draw(win)
    objects.append(bottom_sharp)
    
    bottom_line1 = Line(Point(142, 590), Point(180, 648))
    bottom_line2 = Line(Point(218, 590), Point(180, 648))
    bottom_line1.setOutline("#78350f")
    bottom_line2.setOutline("#78350f")
    bottom_line1.setWidth(2)
    bottom_line2.setWidth(2)
    bottom_line1.draw(win)
    bottom_line2.draw(win)
    objects.append(bottom_line1)
    objects.append(bottom_line2)

    band_y1 = 545
    band_y2 = 570
    line_h1 = Line(Point(137, band_y1), Point(223, band_y1))
    line_h2 = Line(Point(135, band_y2), Point(225, band_y2))
    for lh in [line_h1, line_h2]:
        lh.setOutline("#451a03")
        lh.setWidth(2)
        lh.draw(win)
        objects.append(lh)

    for x_pos in range(142, 215, 6):
        pattern_line = Line(Point(x_pos, band_y1), Point(x_pos + 5, band_y2))
        pattern_line.setOutline("#451a03")
        pattern_line.draw(win)
        objects.append(pattern_line)

    for row in range(0, 3):  
        y_start = 575 + (row * 20)
        for x_left in range(140, 180, 8):
            if y_start + (x_left-140)//2 < 635:
                v_line1 = Line(Point(x_left, y_start), Point(x_left + 6, y_start + 12))
                v_line1.setOutline("#451a03")
                v_line1.draw(win)
                objects.append(v_line1)
        for x_right in range(220, 180, -8):
            if y_start + (220-x_right)//2 < 635:
                v_line2 = Line(Point(x_right, y_start), Point(x_right - 6, y_start + 12))
                v_line2.setOutline("#451a03")
                v_line2.draw(win)
                objects.append(v_line2)

    rim_inner = Oval(Point(145, 510), Point(215, 524))
    rim_inner.setFill("#78350f") 
    rim_inner.setOutline("#451a03")
    rim_inner.draw(win)
    objects.append(rim_inner)

    rim_top = Oval(Point(145, 513), Point(215, 525))
    rim_top.setFill("#b45309")
    rim_top.setOutline("#78350f")
    rim_top.setWidth(2)
    rim_top.draw(win)
    objects.append(rim_top)
    
    return objects

def draw_artifact2(win):
    objects = []
    body = Oval(Point(140, 530), Point(210, 640))
    body.setFill("#0d9488")  
    body.setOutline("#115e59")
    body.setWidth(2)
    body.draw(win)
    objects.append(body)
    
    spout = Polygon(Point(140, 560), Point(115, 535), Point(143, 575))
    spout.setFill("#0d9488")
    spout.setOutline("#115e59")
    spout.setWidth(2)
    spout.draw(win)
    objects.append(spout)
    
    handle = Circle(Point(215, 580), 20)
    handle.setOutline("#115e59")
    handle.setWidth(3)
    handle.draw(win)
    objects.append(handle)
    
    lid = Rectangle(Point(163, 518), Point(187, 530))
    lid.setFill("#0d9488")
    lid.setOutline("#115e59")
    lid.setWidth(2)
    lid.draw(win)
    objects.append(lid)
    
    return objects

def main():
    win = GraphWin("계명대학교 행소박물관 인터랙티브 평면도 (2F)", 900, 710)
    win.setBackground("#fafaf9")

    title = Text(Point(450, 40), "계명대학교 행소박물관 2F 안내")
    title.setSize(22)
    title.setStyle('bold')
    title.setTextColor("#0f172a")
    title.draw(win)

    subtitle = Text(Point(450, 75), "※ 평면도의 전시 구역을 클릭하면 그래픽 코드로 구현된 유물 시각화와 안내가 작동합니다.")
    subtitle.setSize(11)
    subtitle.setTextColor("#64748b")
    subtitle.draw(win)

    outer_wall = Rectangle(Point(150, 120), Point(750, 430))
    outer_wall.setFill("#ffffff")
    outer_wall.setOutline("#cbd5e1")
    outer_wall.setWidth(2)
    outer_wall.draw(win)

    center_lobby = Rectangle(Point(400, 120), Point(500, 430))
    center_lobby.setFill("#f1f5f9")
    center_lobby.setOutline("#94a3b8")
    center_lobby.draw(win)

    for i in range(0, 10):
        Line(Point(420, 240 + (i * 12)), Point(480, 240 + (i * 12))).draw(win)
    Text(Point(450, 220), "1F ↗").draw(win)
    Text(Point(450, 380), "중앙 홀").draw(win)

    room1 = Rectangle(Point(150, 120), Point(400, 430))
    room1.setFill("#e0f2fe")
    room1.setOutline("#0284c7")
    room1.setWidth(2)
    room1.draw(win)
    
    room1_text = Text(Point(275, 275), "제1전시실\n\n(시대별 선사 문화)")
    room1_text.setStyle('bold')
    room1_text.draw(win)

    room2 = Rectangle(Point(500, 120), Point(750, 430))
    room2.setFill("#fef3c7")
    room2.setOutline("#d97706")
    room2.setWidth(2)
    room2.draw(win)
    
    room2_text = Text(Point(625, 275), "제2전시실\n\n(고대 역사 및 도자)")
    room2_text.setStyle('bold')
    room2_text.draw(win)

    info_bg = Rectangle(Point(80, 470), Point(820, 670))
    info_bg.setFill("#0f172a")
    info_bg.draw(win)

    info_title = Text(Point(450, 495), "🔍 박물관 실시간 안내 시스템")
    info_title.setSize(14)
    info_title.setStyle('bold')
    info_title.setTextColor("#38bdf8")
    info_title.draw(win)

    info_desc = Text(Point(510, 580), "평면도 내부를 클릭하시면 해당 전시실의\n대표 유물 디자인과 상세 안내가 이곳에 나타납니다.")
    info_desc.setSize(11)
    info_desc.setTextColor("#94a3b8")
    info_desc.draw(win)

    current_artifacts = []

    while True:
        try:
            click_point = win.getMouse()
            x = click_point.getX()
            y = click_point.getY()

            for obj in current_artifacts:
                obj.undraw()
            current_artifacts.clear()

            if 150 <= x < 400 and 120 <= y <= 430:
                room1.setWidth(4)
                room2.setWidth(2)
                center_lobby.setOutline("#94a3b8")
                
                info_title.setText("🏛️ [제1전시실] 대표 유물: 김천 송죽리 빗살무늬토기")
                info_title.setTextColor("#38bdf8")
                info_desc.setText(
                    "• 대구·경북 지역 선사시대의 정착과 농경 문화를 보여주는 핵심 유물입니다.\n"
                    "• 토기 표면에 정교하게 새겨진 가로 밴드와 V자 격자 문양을 그래픽 코드로 구현했습니다.\n"
                    "• 본 전시실에는 연천 출토 주먹도끼 및 선사 시대 토기류가 함께 전시 중입니다."
                )
                current_artifacts = draw_artifact1(win)

            elif 500 < x <= 750 and 120 <= y <= 430:
                room1.setWidth(2)
                room2.setWidth(4)
                center_lobby.setOutline("#94a3b8")
                
                info_title.setText("🏺 [제2전시실] 대표 유물: 청자 상감참외모양 주전자")
                info_title.setTextColor("#fbbf24")
                info_desc.setText(
                    "• 고려 귀족들의 차·술 문화를 장식했던 전성기 비색 고려청자입니다.\n"
                    "• 참외 모양의 몸체와 주둥이, 부드러운 손잡이 곡선을 기하학적으로 묘사했습니다.\n"
                    "• 도자실 코너에서는 고려청자, 분청사기, 순백자의 연대별 발전상도 확인 가능합니다."
                )
                current_artifacts = draw_artifact2(win)

            elif 400 <= x <= 500 and 120 <= y <= 430:
                room1.setWidth(2)
                room2.setWidth(2)
                center_lobby.setOutline("#0f172a")
                
                info_title.setText("🏢 [중앙 공간] 1층-2층 연결 로비 및 관람 안내")
                info_title.setTextColor("#34d399")
                info_desc.setText(
                    "• 계명대학교 대형 종 복원품 og 대구읍성에서 실제 사용된 성벽돌이 전시되어 있습니다.\n"
                    "• 야간 개관 행사나 박물관 문화체험 프로그램 진행 시 메인 오리엔테이션 홀로 사용됩니다."
                )

        except GraphicsError:
            break

if __name__ == "__main__":
    main()
