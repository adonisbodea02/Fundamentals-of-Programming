def ReadSettingsLine(line):
    line = line.replace(' ', '')
    line = line.replace('"', '')
    line = line.split("=")
    return line
