# You import all the IOs of your board
import board
import busio
# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import simple_key_sequence

# This is the main instance of your keyboard
i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=100000)
mcp = MCP23017(i2c, address=0x20)
keyboard = KMKKeyboard()

# Encoder Configuration
encoder_handler.pins = ((mcp.get_pin(1), mcp.get_pin(0), mcp.get_pin(2)), ((mcp.get_pin(3), mcp.get_pin4), mcp.get_pin(5)))  # Define pins for encoders
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE)),  # Encoder 1 - Volume Control
    ((KC.LEFT, KC.RIGHT, KC.LALT(KC.TAB)))  # Encoder 2 - App Switching
]

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

OPEN_VSCODE = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("code"), KC.ENTER))
OPEN_GITHUB = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("github-desktop"), KC.ENTER))
OPEN_TERMIUS = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("termius"), KC.ENTER))
OPEN_KICAD = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("kicad"), KC.ENTER))
OPEN_FUSION360 = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("fusion360"), KC.ENTER))
OPEN_STEAM = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("steam"), KC.ENTER))
OPEN_DISCORD = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("discord"), KC.ENTER))
OPEN_NOTEPAD = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("notepad-plus-plus"), KC.ENTER))
OPEN_VMWARE = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("vmware"), KC.ENTER))
OPEN_CHROME = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("google-chrome"), KC.ENTER))
OPEN_SPOTIFY = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("spotify"), KC.ENTER))


# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    []
    []
    []
    []
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()