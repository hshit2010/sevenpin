import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# --- 1. HARDWARE PIN CONFIGURATION ---
# Direct-wired switches mapping to the RP2040 GPIO pins
keyboard.matrix = KeysScanner(
    pins=[
        board.D0,  # SW1 (Top-Left)
        board.D1,  # SW2 (Bottom-Left)
        board.D2,  # SW3 (Top-Middle)
        board.D3,  # SW4 (Bottom-Middle)
        board.D6,  # SW5 (Top-Right)
        board.D7,  # SW6 (Bottom-Right)
        board.D10  # SW7 (Encoder Push-Button)
    ],
    value_when_pressed=False,
    pull=True
)

# --- 2. ROTARY ENCODER CONFIGURATION ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Pins for Encoder A and B
encoder_handler.pins = ((board.D8, board.D9, None, False),) 

# Dial mapping: (Counter-Clockwise action, Clockwise action)
# Right-to-Left = Volume Up | Left-to-Right = Volume Down
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),)
]

# --- 3. KEYMAP (MACROS & SHORTCUTS) ---
# Maps directly to the 7 pins defined in the KeysScanner above
keyboard.keymap = [
    [
        KC.LCTRL(KC.C), # SW1: Copy 
        KC.LCTRL(KC.V), # SW2: Paste 
        KC.LCTRL(KC.X), # SW3: Cut 
        KC.LCTRL(KC.Z), # SW4: Undo 
        KC.LCTRL(KC.S), # SW5: Save 
        KC.LCTRL(KC.A), # SW6: Select All 
        KC.MUTE         # Encoder Button: Mute Audio
    ]
]

if __name__ == '__main__':
    keyboard.go()