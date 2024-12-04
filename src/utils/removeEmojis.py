# Copyright (c) 2024 bilive.

import re
import sys
import os

regex = r"(?:[0-9#*]️⃣|[☝✊-✍🎅🏂🏇👂👃👆-👐👦👧👫-👭👲👴-👶👸👼💃💅💏💑💪🕴🕺🖐🖕🖖🙌🙏🛀🛌🤌🤏🤘-🤟🤰-🤴🤶🥷🦵🦶🦻🧒🧓🧕🫃-🫅🫰🫲-🫸][🏻-🏿]?|⛓(?:️‍💥)?|[⛹🏋🏌🕵](?:️‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|❤(?:️‍[🔥🩹])?|🇦[🇨-🇬🇮🇱🇲🇴🇶-🇺🇼🇽🇿]|🇧[🇦🇧🇩-🇯🇱-🇴🇶-🇹🇻🇼🇾🇿]|🇨[🇦🇨🇩🇫-🇮🇰-🇵🇷🇺-🇿]|🇩[🇪🇬🇯🇰🇲🇴🇿]|🇪[🇦🇨🇪🇬🇭🇷-🇺]|🇫[🇮-🇰🇲🇴🇷]|🇬[🇦🇧🇩-🇮🇱-🇳🇵-🇺🇼🇾]|🇭[🇰🇲🇳🇷🇹🇺]|🇮[🇨-🇪🇱-🇴🇶-🇹]|🇯[🇪🇲🇴🇵]|🇰[🇪🇬-🇮🇲🇳🇵🇷🇼🇾🇿]|🇱[🇦-🇨🇮🇰🇷-🇻🇾]|🇲[🇦🇨-🇭🇰-🇿]|🇳[🇦🇨🇪-🇬🇮🇱🇴🇵🇷🇺🇿]|🇴🇲|🇵[🇦🇪-🇭🇰-🇳🇷-🇹🇼🇾]|🇶🇦|🇷[🇪🇴🇸🇺🇼]|🇸[🇦-🇪🇬-🇴🇷-🇹🇻🇽-🇿]|🇹[🇦🇨🇩🇫-🇭🇯-🇴🇷🇹🇻🇼🇿]|🇺[🇦🇬🇲🇳🇸🇾🇿]|🇻[🇦🇨🇪🇬🇮🇳🇺]|🇼[🇫🇸]|🇽🇰|🇾[🇪🇹]|🇿[🇦🇲🇼]|🍄(?:‍🟫)?|🍋(?:‍🟩)?|[🏃🚶🧎](?:‍(?:[♀♂]️(?:‍➡️)?|➡️)|[🏻-🏿](?:‍(?:[♀♂]️(?:‍➡️)?|➡️))?)?|[🏄🏊👮👰👱👳👷💁💂💆💇🙅-🙇🙋🙍🙎🚣🚴🚵🤦🤵🤷-🤹🤽🤾🦸🦹🧍🧏🧔🧖-🧝](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|🏳(?:️‍(?:⚧️|🌈))?|🏴(?:‍☠️|󠁧(?:󠁢(?:󠁥󠁮󠁧|󠁳󠁣󠁴)󠁿)?)?|🐈(?:‍⬛)?|🐕(?:‍🦺)?|🐦(?:‍[⬛🔥])?|🐻(?:‍❄️)?|👁(?:️‍🗨️)?|👨(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?👨|👦(?:‍👦)?|👧(?:‍[👦👧])?|[👨👩]‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳])|🏻(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏼-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏼(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏽-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏽(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏼🏾🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏾(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏽🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏿(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏾]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?)?|👩(?:‍(?:[⚕⚖✈]️|❤️‍(?:[👨👩]|💋‍[👨👩])|👦(?:‍👦)?|👧(?:‍[👦👧])?|👩‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳])|🏻(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏼-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏼(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏽-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏽(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏼🏾🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏾(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏽🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏿(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏾]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?)?|[👯🤼🧞🧟](?:‍[♀♂]️)?|😮(?:‍💨)?|😵(?:‍💫)?|😶(?:‍🌫️)?|🙂(?:‍[↔↕]️)?|🧑(?:‍(?:[⚕⚖✈]️|🤝‍🧑|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]|(?:🧑‍)?🧒(?:‍🧒)?)|🏻(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?🧑[🏼-🏿]|🤝‍🧑[🏻-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏼(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?🧑[🏻🏽-🏿]|🤝‍🧑[🏻-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏽(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?🧑[🏻🏼🏾🏿]|🤝‍🧑[🏻-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏾(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?🧑[🏻-🏽🏿]|🤝‍🧑[🏻-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?|🏿(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?🧑[🏻-🏾]|🤝‍🧑[🏻-🏿]|[🦯🦼🦽](?:‍➡️)?|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?)?|[©®‼⁉™ℹ↔-↙↩↪⌚⌛⌨⏏⏩-⏳⏸-⏺Ⓜ▪▫▶◀◻-◾☀-☄☎☑☔☕☘☠☢☣☦☪☮☯☸-☺♀♂♈-♓♟♠♣♥♦♨♻♾♿⚒-⚗⚙⚛⚜⚠⚡⚧⚪⚫⚰⚱⚽⚾⛄⛅⛈⛎⛏⛑⛔⛩⛪⛰-⛵⛷⛸⛺⛽✂✅✈✉✏✒✔✖✝✡✨✳✴❄❇❌❎❓-❕❗❣➕-➗➡➰➿⤴⤵⬅-⬇⬛⬜⭐⭕〰〽㊗㊙🀄🃏🅰🅱🅾🅿🆎🆑-🆚🈁🈂🈚🈯🈲-🈺🉐🉑🌀-🌡🌤-🍃🍅-🍊🍌-🎄🎆-🎓🎖🎗🎙-🎛🎞-🏁🏅🏆🏈🏉🏍-🏰🏵🏷-🐇🐉-🐔🐖-🐥🐧-🐺🐼-👀👄👅👑-👥👪👹-👻👽-💀💄💈-💎💐💒-💩💫-📽📿-🔽🕉-🕎🕐-🕧🕯🕰🕳🕶-🕹🖇🖊-🖍🖤🖥🖨🖱🖲🖼🗂-🗄🗑-🗓🗜-🗞🗡🗣🗨🗯🗳🗺-😭😯-😴😷-🙁🙃🙄🙈-🙊🚀-🚢🚤-🚳🚷-🚿🛁-🛅🛋🛍-🛒🛕-🛗🛜-🛥🛩🛫🛬🛰🛳-🛼🟠-🟫🟰🤍🤎🤐-🤗🤠-🤥🤧-🤯🤺🤿-🥅🥇-🥶🥸-🦴🦷🦺🦼-🧌🧐🧠-🧿🩰-🩼🪀-🪈🪐-🪽🪿-🫂🫎-🫛🫠-🫨]|🫱(?:🏻(?:‍🫲[🏼-🏿])?|🏼(?:‍🫲[🏻🏽-🏿])?|🏽(?:‍🫲[🏻🏼🏾🏿])?|🏾(?:‍🫲[🏻-🏽🏿])?|🏿(?:‍🫲[🏻-🏾])?)?)+"
def remove_emojis(danmaku_file):
    """Removes emojis from a given ASS danmaku file
    Args:
        danmaku_file: str, the path of ass danmaku file
    """
    try:
        with open(danmaku_file, 'r', encoding='utf-8') as file:
            originalFile = file.read()

        result = re.sub(regex, "", originalFile, 0, re.MULTILINE)
        if result:
            print(f"The emojis of {danmaku_file} are removed.")
            with open(danmaku_file, 'w', encoding='utf-8') as output_file:
                output_file.write(result)
    except FileNotFoundError:
        print("file not exists.")
    except UnicodeDecodeError:
        print("The file encoding may be inconsistent with the specified UTF-8 encoding.")

if __name__ == '__main__':
    # Read and define variables
    parser = argparse.ArgumentParser(description='Remove emojis')
    parser.add_argument('ass_path', type=str, help='Path to the ass file')
    args = parser.parse_args()
    remove_emojis(args.ass_path)