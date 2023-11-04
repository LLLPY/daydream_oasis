
<BlogInfo id="1398" title="Python实现飞机大战小游戏(工具包文件)" author="白日梦想猿" pv=0 read_times=0 pre_cost_time=136 category="pygame" tag_list="['飞机大战', 'game']" create_time="2021.06.26 21:42:23.821740" update_time="2021.06.26 21:42:23" />


```python
import pygame
import random

# 定义屏幕常量
# SCREEN_RECT = pygame.Rect(0, 0, 1200, 1080)
SCREEN_RECT = pygame.Rect(0, 0, 1200, 800)
# 定义刷新的帧率的常量
FRAME_PER_SEC = 60
# 创建敌机的定时常量
CREAT_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1

# 背景音乐常量
BGM = pygame.USEREVENT + 2


class GameSprite(pygame.sprite.Sprite):
    """飞机大战的游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 当某一个子类的父类不是object基类时，一定要在初始化
        # 方法中，主动调用父类的初始化方法
        # 调用父类初始化方法
        super().__init__()

        # 定义对象的属性
        # 图像 从图像文件中加载数据，并传给image
        self.image = pygame.image.load(image_name)
        # 位置 调用get_rect（）方法，返回位置信息，并用变量rect记录
        self.rect = self.image.get_rect()
        # 速度 默认速度为1
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):  # 继承自精灵类
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类方法实现精灵创建
        super().__init__("./images/background2.jpg")

        # 2判断是否为交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    # 重写父类的方法
    def update(self):

        # 1.调用父类的方法实现（垂直方向的移动）
        super().update()

        # 2.判断是否移出屏幕，如果移出，将图像设置在屏幕的正上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 定义Enemy类
class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # self.image = pygame.image.load(path)

        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片

        a = random.randint(0, 2)

        if a == 0:
            super().__init__("./images/enemy1.png")

        elif a == 1:
            super().__init__("./images/enemy2.png")

        else:
            super().__init__("./images/enemy3.png")

        # super().__init__("enemies_list[0]")

        # super().__init__("./images/enemy2.png")

        # 2.指定敌机的初始速度 1~3
        self.speed = random.randint(1, 4)

        # 3.指定敌机的初始位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):

        # 1.调用父类的方法，保持垂直方向的飞行
        super().update()

        # 2判断是否飞出屏幕，如果飞出屏幕，kill该精灵
        if self.rect.y > SCREEN_RECT.height:
            # print("删除该敌机精灵")
            # 删除该敌机，释放内存
            self.kill()

    def __del__(self):
        # print("敌机挂了%s"%self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        # 1.调用父类方法，设置image，speed
        super().__init__("./images/hero.png", 0)

        # 2.英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        """控制英雄不能离开屏幕"""

        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        elif self.rect.y <= 0:
            self.rect.y = 0

        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        # print("发射子弹")

        for i in (0, 1, 2):
            # 一次性发射3颗子弹
            # 1.创建子弹精灵
            bullet = Bullet()

            # 设置子弹的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 把子弹精灵添加到子弹精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):

        # 调用父类方法，设置子弹的图片，速度

        super().__init__("./images/bullet1.png", -6)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_l]:  # 大招:
            super().__init__("./images/bullet2-4.png", -6)

    def update(self):

        # 调用父类方法，让子弹沿着垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        # 删除子弹
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
        # print("子弹被销毁")
```
    


