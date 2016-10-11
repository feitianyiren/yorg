'''This module provides a menu.'''
from direct.gui.OnscreenImage import OnscreenImage
from ...gameobject.gameobject import Gui, Logic, GameObjectMdt


class MenuArgs(object):
    '''This class models the arguments of a menu.'''

    def __init__(self, font, text_fg, text_scale, btn_size, btn_color,
                 dial_color, background, rollover, click, social_path):
        self.font = font
        self.text_fg = text_fg
        self.text_scale = text_scale
        self.btn_size = btn_size
        self.btn_color = btn_color
        self.dial_color = dial_color
        self.background = background
        self.rollover = rollover
        self.click = click
        self.social_path = social_path


class MenuGui(Gui):
    '''The GUI component of a menu.'''

    def __init__(self, mdt, menu_args):
        Gui.__init__(self, mdt)
        self.menu_args = menu_args
        self.font = eng.font_mgr.load_font(menu_args.font)
        self.background = None
        self.background = OnscreenImage(scale=(1.77778, 1, 1.0),
                                        image=self.menu_args.background)
        self.background.setBin('background', 10)
        self.rollover = loader.loadSfx(menu_args.rollover)
        self.click = loader.loadSfx(menu_args.click)
        self.imgbtn_args = {
            'rolloverSound': self.rollover, 'clickSound': self.click}
        self.btn_args = {
            'scale': self.menu_args.text_scale,
            'text_font': self.font,
            'text_fg': self.menu_args.text_fg,
            'frameColor': self.menu_args.btn_color,
            'frameSize': self.menu_args.btn_size,
            'rolloverSound': self.rollover,
            'clickSound': self.click}

    def destroy(self):
        '''Destroys the page.'''
        Gui.destroy(self)
        self.background.destroy()


class MenuLogic(Logic):
    '''The logic component of a menu.'''

    def __init__(self, mdt):
        Logic.__init__(self, mdt)
        self.pages = []

    def push_page(self, page):
        '''Pushes a page.'''
        if self.pages:
            self.pages[-1].gui.hide()
            self.pages[-1].gui.detach(self.pages[-1])
        self.pages += [page]
        page.gui.attach(self.pop_page)

    def pop_page(self):
        '''Pops a page.'''
        page = self.pages.pop()
        page.gui.detach(self)
        page.destroy()
        self.pages[-1].gui.show()
        self.pages[-1].gui.attach(self.pop_page)

    def destroy(self):
        Logic.destroy(self)
        map(lambda page: page.destroy(), self.pages)
        self.pages = None


class Menu(GameObjectMdt):
    '''This class models a page.'''
    gui_cls = MenuGui
    logic_cls = MenuLogic

    def __init__(self, menu_args):
        self.fsm = self.fsm_cls(self)
        self.gfx = self.gfx_cls(self)
        self.phys = self.phys_cls(self)
        self.gui = self.gui_cls(self, menu_args)
        self.logic = self.logic_cls(self)
        self.audio = self.audio_cls(self)
        self.ai = self.ai_cls(self)
        self.event = self.event_cls(self)