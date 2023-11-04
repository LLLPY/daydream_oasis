
<BlogInfo id="449" title="Python实现飞机大战小游戏" author="白日梦想猿" pv=0 read_times=0 pre_cost_time="178" category="pygame" tag_list="['pygame', '              飞机大战']" create_time="2021.06.26 21:40:46.863614" update_time="2021.06.26 21:40:46" />


```python
import pygame as pygame

from plane_sprites import *
pygame.init()

try:
    # 加载背景音乐
    pygame.mixer_music.load("images/bgmusic.mp3")
    pygame.mixer.init()
    # 播放背景音乐
    pygame.mixer_music.play()
    pygame.mixer.music.set_endevent(BGM)
except:
    pass

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化...")

        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()

        # 3.调用私有方法，创建精灵和精灵组
        self.__creat_sprites()

        # 4.设置定时器事件 1s
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)  # 1000毫秒 = 1秒
        # 发射子弹的事件
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)  # 每隔0.5秒发射子弹

    # 定义精灵的私有方法
    def __creat_sprites(self):

        # 创建背景精灵
        bg1 = Background()
        bg2 = Background(is_alt=True)

        # 创建背景精灵组
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵
        # enemy1 = Enemy("./images/enemy1.png")
        # enemy2 = Enemy("./images/enemy2.png")

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        print("开始游戏...")
        a = True
        while a:
            # 6.暂停和继续
            self.break_continue()

            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)  # 代码每秒执行60次

            # 2.事件监听
            self.__event_handler()

            # 3.碰撞检测
            self._check_collide()

            # 4.更行/绘制精灵组
            self.__update_sprites()

            # 5.更新显示
            pygame.display.update()

    # 游戏暂停和继续
    def break_continue(self):
        pass
        # x = False
        # keys_pressed = pygame.key.get_pressed()
        # if keys_pressed[pygame.K_SPACE]:  # 暂停
        #     x = True
        #     while x:
        #         bk = pygame.image.load("images/brk.png")
        #         self.screen.blit(bk, (SCREEN_RECT.centerx, SCREEN_RECT.centery))
        #         pygame.display.update()
        #         if keys_pressed[pygame.K_KP_ENTER]:
        #             sta = pygame.image.load("images/sta.png")
        #             self.screen.blit(sta, (SCREEN_RECT.centerx, SCREEN_RECT.centery))
        #             pygame.display.update()
        #             break

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():  # 获取某一时发生的所有事情的监听列表

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()  # 使用类名.的方法调用静态方法

            elif event.type == CREAT_ENEMY_EVENT:
                # print("敌机出场")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)


            elif event.type == HERO_FIRE_EVENT:
                # print("发射子弹")
                self.hero.fire()

            elif event.type == BGM:
                pygame.mixer_music.load("images/bgmusic.mp3")
                pygame.mixer_music.play()
                pygame.mixer.music.set_endevent(BGM + 1)

            elif event.type == BGM + 1:
                pygame.mixer_music.load("images/bgmusic.mp3")
                pygame.mixer_music.play(-1)

            # elif event.type == pygame.MOUSEMOTION:
            #     # return the X and Y position of the mouse cursor
            #     pos = pygame.mouse.get_pos()
            #     mouse_x = pos[0]
            #     mouse_y = pos[1]
            #     self.hero.rect.centerx = mouse_x
            #     self.hero.rect.y = mouse_y - self.hero.rect.height / 2

        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        #    print("向右移动")

        # 使用键盘模块提供的方法获取键盘按钮 元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元祖中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            # print("向右移动")
            self.hero.rect.x += 3

        elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            # print("向左移动")
            self.hero.rect.x -= 3

        elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            # print("向上移动")
            self.hero.rect.y -= 3

        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            # print("向下移动")
            self.hero.rect.y += 3

        elif keys_pressed[pygame.K_ESCAPE]:
            PlaneGame.__game_over()

    # 碰撞检测
    def _check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)  # 返回值为敌机的列表

        # 判断列表是否有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    # 更新精灵组
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 游戏结束
    @staticmethod  # 静态方法
    def __game_over():
        print("游戏结束")

        pygame.quit()  # 卸载模块，释放内存
        exit()  # 终止游戏


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()

    while True:
        pass

```

    


