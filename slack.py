from talon.voice import Context, Key
from .utils import text

ctx = Context("slack", bundle="com.tinyspeck.slackmacgap")

keymap = {
    # Channel
    "channel": Key("cmd-k"),
    "channel <dgndictation>": [Key("cmd-k"), text],
    "([channel] unread last | gopreev)": Key("alt-shift-up"),
    "([channel] unread next | goneck)": Key("alt-shift-down"),
    "(slack | lack) [channel] info": Key("cmd-shift-i"),
    "channel up": Key("alt-up"),
    "channel down": Key("alt-down"),
    # Navigation
    "(move | next) focus": Key("ctrl-`"),
    "[next] (section | zone)": Key("f6"),
    "(previous | last) (section | zone)": Key("shift-f6"),
    "direct messages": Key("cmd-shift-k"),
    "(slack | lack) threads": Key("cmd-shift-t"),
    "(slack | lack) (history [next] | back | backward)": Key("cmd-["),
    "(slack | lack) forward": Key("cmd-]"),
    "[next] (element | bit)": Key("tab"),
    "(previous | last) (element | bit)": Key("shift-tab"),
    "(my stuff | activity)": Key("cmd-shift-m"),
    "directory": Key("cmd-shift-e"),
    "(starred [items] | stars)": Key("cmd-shift-s"),
    "unread [messages]": Key("cmd-j"),
    "(go | undo | toggle) full": Key("ctrl-cmd-f"),
    "(slack | lack) (find | search)": Key("cmd-f"),
    # Messaging
    "grab left": Key("shift-up"),
    "grab right": Key("shift-down"),
    "add line": Key("shift-enter"),
    "(slaw | slapper)": [Key("cmd-right"), Key("shift-enter")],
    "(react | reaction)": Key("cmd-shift-\\"),
    "user": Key("@"),
    "tag channel": Key("#"),
    "(insert command | commandify)": Key("cmd-shift-c"),
    "insert code": [
        "``````",
        Key("left left left"),
        Key("shift-enter"),
        Key("shift-enter"),
        Key("up"),
    ],
    "(bullet | bulleted) list": Key("cmd-shift-8"),
    "(number | numbered) list": Key("cmd-shift-7"),
    "(quotes | quotation)": Key("cmd-shift->"),
    "bold": Key("cmd-b"),
    "(italic | italicize)": Key("cmd-i"),
    "(strike | strikethrough)": Key("cmd-shift-x"),
    "mark all read": Key("shift-esc"),
    "mark channel read": Key("esc"),
    "(clear | scrap | scratch)": Key("cmd-a backspace"),
    # Files and Snippets
    "upload": Key("cmd-u"),
    "snippet": Key("cmd-shift-enter"),
    # Calls
    "([toggle] mute | unmute)": Key("m"),
    "([toggle] video)": Key("v"),
    "invite": Key("a"),
    # Miscellaneous
    "shortcuts": Key("cmd-/"),
}

ctx.keymap(keymap)
