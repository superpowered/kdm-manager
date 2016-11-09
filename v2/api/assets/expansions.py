#!/usr/bin/python2.7

from datetime import datetime

promo_and_misc = {
    "beta_challenge_scenarios": {
        "__released__": datetime(2016,2,1),
        "name": "Beta Challenge Scenarios",
        "special_rules": [
            {
            "name": "Survival Limit Warning!",
            "bg_color": "F87217",
            "font_color": "FFF",
            "desc": "Survival Limit is not automatically enforced by the Manager when Beta Challenge Scenarios content is enabled.",
            },
        ],
    },
    "white_box": {
        "__released__": datetime(2016,8,16),
        "name": "White Box",
    },
}

mar_2016_expansions = {
    "gorm": {
        "name": "Gorm",
        "always_available": ["Gormery", "Gormchymist", "Nigredo"],
        "timeline_add": [
            {"ly": 1, "type": "story_event", "name": "The Approaching Storm"},
            {"ly": 2, "type": "settlement_event", "name": "Gorm Climate"},
        ],
    },
    "dung_beetle_knight": {
        "name": "Dung Beetle Knight",
        "always_available": ["Wet Resin Crafter","Subterranean Agriculture"],
        "timeline_add": [
            {"ly": 8, "type": "story_event", "name": "Rumbling in the Dark"},
        ],
    },
    "lion_knight": {
        "name": "Lion Knight",
        "always_available": ["Stoic Statue"],
        "timeline_add": [
            {"ly": 6, "type": "story_event", "name": "An Uninvited Guest"},
            {"ly": 8, "type": "story_event", "name": "Places, Everyone!"},
            {"ly": 12, "type": "story_event", "name": "Places, Everyone!"},
            {"ly": 16, "type": "story_event", "name": "Places, Everyone!"},
        ],
    },
    "lion_god": {
        "name": "Lion God",
        "always_available": ["The Knowledge Worm"],
        "timeline_add": [
            {"ly": 13, "type": "story_event", "name": "The Silver City"},
        ],
    },
    "sunstalker": {
        "name": "Sunstalker",
        "always_available": ["The Sun", "Sun Language", "Umbilical Bank"],
        "survivor_attribs": ["Purified","Sun Eater","Child of the Sun"],
        "timeline_add": [
            {"ly": 8, "type": "story_event", "name": "Promise Under the Sun", "excluded_campaign": "People of the Sun"},
        ],
    },
    "lonely_tree": {
        "name": "Lonely Tree",
        "always_available_nemesis": True,
    },
    "flower_knight": {
        "name": "Flower Knight",
        "timeline_add": [
            {"ly": 5, "type": "story_event", "name": "A Crone's Tale", "excluded_campaign": "The Bloom People"}
        ],
    },
}