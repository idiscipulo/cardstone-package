import configs

class  Card:
    def __init__(self, name: str="Default Name", cost: str="1YUMRG", desc: str="", tags: list=["SORCERY"], power: int=0, toughness: int=0):
        """Set base stats
        """
        self.name = name
        self.cost = cost
        self.desc = desc
        self.tags = tags
        self.power = power
        self.toughness = toughness
        
        """State based stuff
        """
        self.tapped = False

        if cost[0] not in "YUMRG":
            self.mana_value = int(cost[0])
            self.mana_value += len(cost[1:])
        else:
            self.mana_value = len(cost)

        """Set the color identity
        """
        colored_cost = set([x for x in cost if x in "YUMRG"])
        self.colors = list(colored_cost)

        """Format the description
        """
        self.desc_lines = self.generate_desc()

    def generate_desc(self):
        desc_len = configs.CARD_WIDTH - 2

        temp_desc = self.desc
        temp_desc = temp_desc.replace("{T}", "(T)")

        temp_desc_blocks = temp_desc.split("{br}")

        desc_lines = []
        for block in temp_desc_blocks:
            temp_block = block
            while len(temp_block) > desc_len:
                ind = temp_block[desc_len::-1].find(" ")
                ind = desc_len - ind
                
                desc_lines.append(temp_block[:ind])
                temp_block = temp_block[ind + 1:]
            desc_lines.append(temp_block)

        return desc_lines

    def draw(self, y: int, x: int, scr, colors):
        """Base color
        """
        if len(self.colors) == 1:
            if self.colors[0] == "Y":
                color = colors.WHITE_YELLOW
            elif self.colors[0] == "U":
                color = colors.WHITE_BLUE
            elif self.colors[0] == "M":
                color = colors.WHITE_MAGENTA
            elif self.colors[0] == "R":
                color = colors.WHITE_RED
            elif self.colors[0] == "G":
                color = colors.WHITE_GREEN
        else:
            color = colors.WHITE_CYAN

        for yy in range(configs.CARD_HEIGHT):
            scr.addstr(y + yy, x, " " * 22, color)

        """Tag line
        """
        tag_str = " ".join([x.capitalize() for x in self.tags])
        scr.addstr(y + 1, x + 1, tag_str, color)

        """Name bar
        """
        scr.addstr(y, x, " " * configs.CARD_WIDTH, colors.BLACK_WHITE)

        """Name
        """
        scr.addstr(y, x + 1, self.name, colors.BLACK_WHITE)

        """Cost
        """
        cost_len = len(self.cost)
        for n, c in enumerate(self.cost):
            if c not in "YUMRG":
                scr.addstr(y, x - 1 + configs.CARD_WIDTH - cost_len + n, c, colors.BLACK_WHITE)
            else:
                if c == "Y":
                    color = colors.YELLOW_WHITE
                elif c == "U":
                    color = colors.BLUE_WHITE
                elif c == "M":
                    color = colors.MAGENTA_WHITE
                elif c == "R":
                    color = colors.RED_WHITE
                elif c == "G":
                    color = colors.GREEN_WHITE
                
                scr.addstr(y, x - 1 + configs.CARD_WIDTH - cost_len + n, "●", color)

        """Description box
        """
        for yy in range(configs.CARD_HEIGHT - 3):
            scr.addstr(y + yy + 2, x + 1, " " * (configs.CARD_WIDTH - 2), colors.BLACK_WHITE)
        
        for n, desc in enumerate(self.desc_lines):
            scr.addstr(y + 2 + n, x + 1, f"{desc:<{configs.CARD_WIDTH - 2}}", colors.BLACK_WHITE)

        """Stats
        """
        if "MINION" in self.tags:
            stat_str = f"({self.power}/{self.toughness})"
            stat_len = len(stat_str)

            scr.addstr(y + configs.CARD_HEIGHT - 1, x + int(0.5 * configs.CARD_WIDTH) - int(0.5 * stat_len), f"{stat_str}", colors.BLACK_WHITE)

        """Tapped
        """
        if self.tapped:
            for yy in range(3):
                scr.addstr(y + yy + int(0.5 * configs.CARD_HEIGHT) - 1, x + int(0.5 * configs.CARD_WIDTH) - 5, " " * 10, colors.WHITE_BLACK)

            scr.addstr(y + int(0.5 * configs.CARD_HEIGHT), x + int(0.5 * configs.CARD_WIDTH) - 5, f"{'Tapped':^10}", colors.WHITE_BLACK)