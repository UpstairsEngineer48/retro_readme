from dataclasses import dataclass


@dataclass(slots=True)
class Rectangle:
    x: int
    y: int
    width: int
    height: int


@dataclass(slots=True)
class Point:
    x: int
    y: int


class LayoutEngine:
    """
    Computes the geometry of the handheld.
    No SVG should be generated here.
    """

    CANVAS_WIDTH = 1130
    CANVAS_HEIGHT = 900

    DEVICE_X = 40
    DEVICE_Y = 40
    DEVICE_WIDTH = 520
    DEVICE_HEIGHT = 820

    BORDER = 18

    LCD_MARGIN_TOP = 70

    LCD_WIDTH = 424
    LCD_HEIGHT = 520

    CONTROL_TOP = 610

    def device(self) -> Rectangle:
        return Rectangle(
            self.DEVICE_X,
            self.DEVICE_Y,
            self.DEVICE_WIDTH,
            self.DEVICE_HEIGHT,
        )

    def inner_bezel(self) -> Rectangle:
        return Rectangle(
            self.DEVICE_X + self.BORDER,
            self.DEVICE_Y + self.BORDER,
            self.DEVICE_WIDTH - self.BORDER * 2,
            self.DEVICE_HEIGHT - self.BORDER * 2,
        )

    def lcd(self) -> Rectangle:
        lcd_x = self.DEVICE_X + (
            self.DEVICE_WIDTH - self.LCD_WIDTH
        ) // 2

        lcd_y = self.DEVICE_Y + self.LCD_MARGIN_TOP

        return Rectangle(
            lcd_x,
            lcd_y,
            self.LCD_WIDTH,
            self.LCD_HEIGHT,
        )

    def controls_area(self) -> Rectangle:
        return Rectangle(
            self.DEVICE_X + 30,
            self.DEVICE_Y + self.CONTROL_TOP,
            self.DEVICE_WIDTH - 60,
            170,
        )

    def speaker_area(self) -> Rectangle:
        width = 200

        x = self.DEVICE_X + (
            self.DEVICE_WIDTH - width
        ) // 2

        return Rectangle(
            x,
            self.DEVICE_Y + 30,
            width,
            20,
        )

    def dpad_area(self) -> Rectangle:
        return Rectangle(
            self.DEVICE_X + 50,
            self.DEVICE_Y + 645,
            110,
            110,
        )

    def buttons_area(self) -> Rectangle:
        return Rectangle(
            self.DEVICE_X + 305,
            self.DEVICE_Y + 655,
            130,
            90,
        )

    def led_position(self) -> Point:
        return Point(
            self.DEVICE_X + 52,
            self.DEVICE_Y + 40,
        )

    def status_bar(self) -> Rectangle:
        lcd = self.lcd()

        return Rectangle(
            lcd.x,
            lcd.y,
            lcd.width,
            36,
        )

    def content(self) -> Rectangle:
        lcd = self.lcd()

        return Rectangle(
            lcd.x,
            lcd.y + 45,
            lcd.width,
            lcd.height - 45,
        )


    def menu(self) -> Rectangle:
        content = self.content()

        return Rectangle(
            content.x + 35,
            content.y + 25,
            content.width - 70,
            content.height,
        )
    

    def footer(self) -> Rectangle:
        lcd = self.lcd()

        return Rectangle(
            lcd.x + 18,
            lcd.y + lcd.height - 52,
            lcd.width - 36,
            34,
        )
    
    def content_start_y(self) -> int:
        return self.menu().y + 105


    def content_line_height(self) -> int:
        return 42


    def content_label_x(self) -> int:
        return self.menu().x


    def content_value_x(self) -> int:
        return self.menu().x + 110
    
    def page_indicator_x(self) -> int:
        menu = self.menu()

        return menu.x + menu.width // 2

    def page_indicator_y(self) -> int:
        return self.content_start_y() - 28