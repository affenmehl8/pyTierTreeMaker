from mainWindow import MainWindow

if __name__ == '__main__':
    mainWindow = MainWindow(height=720, width=1280)

    mainWindow.add_node_to_tier(1, "testoooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    mainWindow.add_node_to_tier(2, "sest")
    mainWindow.add_node_to_tier(2, "spest")

    mainWindow.run()