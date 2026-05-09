import core

class Humanize(core.module.Module):
    """Makes your AI avoid common AI language patterns"""

    settings = {
        "use_texting_style": {
            "default": False,
            "description": "Makes your AI write as if it's texting you like on a messaging app such as Telegram or Discord"
        },
        "use_casual_language": {
            "default": True,
            "description": "Makes your AI avoid using formal language"
        },
        "fix_emoji_overuse": {
            "default": False,
            "description": "Attempts to make your AI only use emojis for emotional concepts. Might confuse your AI!"
        },
        "forbid_emojis": {
            "default": False,
            "description": "Completely forbid the use of emojis"
        },
        "forbid_em_dash": {
            "default": False,
            "description": "Forbid the use of Em dashes (—), one of the most telltale signs of AI"
        },
        "forbid_lists": {
            "default": False,
            "description": "Forbid your AI from describing things using lists"
        },
        "forbid_tables": False,
        "forbid_headers_in_lists": True,
        "forbid_not_just_x_its_y": True,
        "forbid_rule_of_three": True,
        "write_only_lowercase": False,
        "use_chat_slang": False,
    }

    async def on_system_prompt(self):
        prompt = ""

        if self.config.get("use_texting_style"):
            prompt += "Write as if you're texting in an instant messaging app such as Telegram, Whatsapp or Discord. Limit your replies to only one paragraph.\n"

        if self.config.get("use_casual_language"):
            prompt += "In your replies, ONLY use casual, informal language.\n"

        if self.config.get("forbid_emojis"):
            prompt += "NEVER use emojis.\n"
        elif self.config.get("fix_emoji_overuse"):
            prompt += "ONLY use emojis for emotions, NEVER for any other concepts.\n"

        if self.config.get("use_chat_slang"):
            prompt += "Use chat slang and acronyms.\n"

        if self.config.get("write_only_lowercase"):
            prompt += "Write only in lowercase.\n"

        if self.config.get("forbid_em_dash"):
            prompt += "NEVER use Em dashes (—) in your writing.\n"

        if self.config.get("forbid_lists"):
            prompt += "NEVER use lists in your writing\n"

        if self.config.get("forbid_tables"):
            prompt += "NEVER output tables.\n"

        if self.config.get("forbid_headers_in_lists"):
            prompt += "When writing lists, NEVER put **bold headers** at the start of a list item.\n"

        if self.config.get("forbid_not_just_x_its_y"):
            prompt += "NEVER use negative parallelism (It's not (just) X, (but) (also) Y) in your writing\n"

        return prompt if prompt else None
