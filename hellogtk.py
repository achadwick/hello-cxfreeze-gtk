# All copyrights and related or neighbouring rights waived under CC0.
# http://creativecommons.org/publicdomain/zero/1.0/
# To the extent possible under law, Andrew Chadwick has waived all
# copyright and related or neighboring rights to this program. This
# program is published from: United Kingdom.

"""Fairly minimal GTK3 and Cairo Hello World."""


import math

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import cairo


def main():
    t = Gtk.Label(
        label = "Hello, GTK!",
        hexpand = True,
        vexpand = False,
    )
    d = Gtk.DrawingArea(
        hexpand = True,
        vexpand = True,
    )
    d.set_size_request(300, 250)
    d.connect("draw", draw_cb)
    g = Gtk.Grid(
        row_spacing = 12,
        column_spacing = 12,
        border_width = 18,
    )
    g.attach(d, 0, 0, 1, 1)
    g.attach(t, 0, 1, 1, 1)
    w = Gtk.Window(
        title = "hello",
    )
    w.set_default_size(400, 300)
    w.add(g)
    w.connect("destroy", Gtk.main_quit)
    w.show_all()
    Gtk.main()


def draw_cb(da, cr):
    cr.set_source_rgb(0.3, 0.3, 0.4)
    cr.paint()
    cr.set_line_width(10)
    w = da.get_allocated_width()
    h = da.get_allocated_height()
    cr.arc(w/2.0, h/2.0, min(w, h)/2.0 - 20, 0, 2*math.pi)
    cr.set_source_rgb(0.8, 0.7, 0.2)
    cr.stroke()


if __name__ == "__main__":
    main()
