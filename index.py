gui = 1


if gui:
    from gui import Gui
    g = Gui()
    g.initialGui()

if not gui:
    from cli import CLI
    c = CLI()
