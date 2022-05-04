from Constants import DEBUG

if DEBUG:
    from time import time

def CreateAnimation(imgs):
    print('TODO: CreateAnimation')
    anim = None
    return anim

def SaveAnimation(anim):
    print('TODO: SaveAnimation')
    return None

def ShowAnimation(anim):
    from gi.repository import Gtk as gtk
    from gi.repository.Gdk import KEY_q
    from gi.repository.Gdk import KEY_Q
    from gi.repository.Gdk import RGBA
    
    #creating window
    window = gtk.Window(title="Animation")
    state = window.get_state()
    window.override_background_color(state, RGBA(1, 1, 1, 1))

    #assign closing events
    def on_key_press(self, event):
        if event.keyval == KEY_q or event.keyval == KEY_Q :
            window.close()

    window.connect("key-press-event", on_key_press)
    window.connect("destroy", gtk.main_quit)

    #exhibits animation in gtk window
    img = gtk.Image.new()
    img.set_from_file('bar_test.gif')
    window.add(img)

    #showing window and starting gtk main loop
    window.show_all()
    gtk.main()

    return None
