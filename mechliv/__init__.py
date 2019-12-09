#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import os
import json
import argparse
from os.path import expanduser
import signal
from pynput import keyboard
import pyaudio
import wave

from version import Version

if os.environ.get('TRAVIS') != 'true':
    import pygtk

    pygtk.require('2.0')
    import gtk

    import webbrowser

    try:
        import appindicator
    except ImportError:
        import appindicator_replacement as appindicator

    from appindicator_replacement import get_icon_filename


def play_sound():
    # define stream chunk
    chunk = 1024

    # open a wav format music
    f = wave.open(get_icon_filename('press.wav'), "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)

    # play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

        # stop stream
    stream.stop_stream()
    stream.close()


def on_press(key):
    pass


def on_release(key):
    play_sound()


# noinspection PyMethodMayBeStatic
class MechLivApp:
    UPDATE_URL = "https://github.com/artiya4u/mechliv#upgrade"
    ABOUT_URL = "https://github.com/artiya4u/mechliv"

    def __init__(self, args):
        # Load the database
        home = expanduser("~")
        with open(home + '/.mechliv.json', 'a+') as content_file:
            content_file.seek(0)
            content = content_file.read()
            try:
                self.db = set(json.loads(content))
            except ValueError:
                self.db = set()

        # create an indicator applet
        self.ind = appindicator.Indicator("MechLev", "mechliv", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_icon(get_icon_filename("icon.png"))

        # create a menu
        self.menu = gtk.Menu()

        # The default state is false, and it toggles when you click on it
        self.playState = args.play

        btnPlay = gtk.CheckMenuItem("Play Sound!")
        btnPlay.show()
        btnPlay.set_active(args.play)
        btnPlay.connect("activate", self.toggle_play)
        self.menu.append(btnPlay)

        # create items for the menu - refresh, quit and a separator
        menuSeparator = gtk.SeparatorMenuItem()
        menuSeparator.show()
        self.menu.append(menuSeparator)

        btnAbout = gtk.MenuItem("About")
        btnAbout.show()
        btnAbout.connect("activate", self.show_about)
        self.menu.append(btnAbout)

        if Version.new_available():
            btnUpdate = gtk.MenuItem("New Update Available")
            btnUpdate.show()
            btnUpdate.connect('activate', self.show_update)
            self.menu.append(btnUpdate)

        btnQuit = gtk.MenuItem("Quit")
        btnQuit.show()
        btnQuit.connect("activate", self.quit)
        self.menu.append(btnQuit)
        self.menu.show()
        self.ind.set_menu(self.menu)
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

    def toggle_play(self, widget):
        """Whether comments page is opened or not"""
        self.playState = not self.playState

    def show_update(self, widget):
        """Handle the update button"""
        webbrowser.open(MechLivApp.UPDATE_URL)
        # Remove the update button once clicked
        self.menu.remove(widget)

    def show_about(self, widget):
        """Handle the about btn"""
        webbrowser.open(MechLivApp.ABOUT_URL)

    # ToDo: Handle keyboard interrupt properly
    def quit(self, widget, data=None):
        """ Handler for the quit button"""
        l = list(self.db)
        home = expanduser("~")

        # truncate the file
        with open(home + '/.mechliv.json', 'w+') as file:
            file.write(json.dumps(l))

        gtk.main_quit()

    def run(self):
        signal.signal(signal.SIGINT, self.quit)
        gtk.main()
        return 0

    def open(self, widget, event=None, data=None):
        """Opens the link in the web browser"""
        # We disconnect and reconnect the event in case we have
        # to set it to active and we don't want the signal to be processed
        if not widget.get_active():
            widget.disconnect(widget.signal_id)
            widget.set_active(True)
            widget.signal_id = widget.connect('activate', self.open)

        self.db.add(widget.item_id)
        webbrowser.open(widget.url)

        if self.playState:
            webbrowser.open(widget.discussion_url)


def main():
    parser = argparse.ArgumentParser(description='Play mechanical keyboard sound in your System Tray.')
    parser.set_defaults(play=True)
    args = parser.parse_args()
    indicator = MechLivApp(args)
    indicator.run()


if __name__ == '__main__':
    main()
