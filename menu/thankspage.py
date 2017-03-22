from direct.gui.OnscreenText import OnscreenText
from yorg.utils import Utils
from yyagl.engine.gui.page import PageGui
from panda3d.core import TextNode


class ThanksPageGui(PageGui):

    def build_page(self):
        menu_gui = self.menu.gui
        t_a = menu_gui.text_args
        t_a['fg'] = menu_gui.menu_args.text_bg
        t_a['scale'] = .06
        txt = OnscreenText(
            text=_('Thanks to: ') + Utils().get_thanks(1)[0], pos=(.05, .05),
            align=TextNode.A_left, parent=base.a2dBottomLeft, **t_a)
        self.add_widget(txt)
        PageGui.build_page(self)