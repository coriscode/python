import pytest
from television import *

class Test:


    def setup_method(self):
        self.t = Television()

    def test_init(self):
        assert str(self.t) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.t.power()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 0"
        self.t.power()
        assert str(self.t) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.t.power()
        self.t.volume_up()
        self.t.mute()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_up(self):
        self.t.channel_up()
        assert str(self.t) == "Power = False, Channel = 0, Volume = 0"
        self.t.power()
        self.t.channel_up()
        assert str(self.t) == "Power = True, Channel = 1, Volume = 0"
        self.t.channel_up()
        self.t.channel_up()
        self.t.channel_up()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.t.channel_down()
        assert str(self.t) == "Power = False, Channel = 0, Volume = 0"
        self.t.power()
        self.t.channel_down()
        assert str(self.t) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        self.t.volume_up()
        assert str(self.t) == "Power = False, Channel = 0, Volume = 0"
        self.t.power()
        self.t.volume_up()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 1"
        self.t.mute()
        self.t.volume_up()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 2"
        self.t.volume_up()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 2"


    def test_volume_down(self):
        self.t.volume_down()
        assert str(self.t) == "Power = False, Channel = 0, Volume = 0"
        self.t.power()
        self.t.volume_up()
        self.t.volume_up()
        self.t.volume_down()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 1"
        self.t.volume_up()
        self.t.mute()
        self.t.volume_down()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 1"
        self.t.volume_down()
        self.t.volume_down()
        assert str(self.t) == "Power = True, Channel = 0, Volume = 0"



