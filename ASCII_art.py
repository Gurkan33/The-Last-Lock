alphabet = {
    "A":{ 
        "line1": " █████╗ ",
        "line2": "██╔══██╗",
        "line3": "███████║",
        "line4": "██║  ██║",
        "line5": "██║  ██║",
        "line6": "╚═╝  ╚═╝"
    },
    "B":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "C":{ 
        "line1": " ██████╗",
        "line2": "██╔════╝",
        "line3": "██║     ",
        "line4": "██║     ",
        "line5": "╚██████╗",
        "line6": " ╚═════╝"
    },
    "D":{ 
        "line1": "███████╗ ",
        "line2": "██╔═══██╗",
        "line3": "██║   ██║",
        "line4": "██║   ██║",
        "line5": "███████╔╝",
        "line6": "╚══════╝ "
    },
    "E":{ 
        "line1": "███████╗",
        "line2": "██╔════╝",
        "line3": "█████╗  ",
        "line4": "██╔══╝  ",
        "line5": "███████╗",
        "line6": "╚══════╝"
    },
    "F":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "G":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "H":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "I":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "J":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "K":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "L":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "M":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "N":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "O":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "P":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "Q":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "R":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "S":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "T":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "U":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "V":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "W":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "X":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "Y":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    },
    "Z":{ 
        "line1": "",
        "line2": "",
        "line3": "",
        "line4": "",
        "line5": "",
        "line6": ""
    }
}

def ASCII_art_text(text):
   text_list = list(text.upper())
   for i in range (0, 6):
      for j in range(0, len(text_list)):
         print(alphabet[text_list[j]][list(alphabet[text_list[j]])[i]], end="")
      print()
ASCII_art_text("ACDE")