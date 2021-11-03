import csv

def get_stats(name):

    '''
    Gets the stats of all NHL players with requested name from nhl_stats.csv

    Paramaters
    ----------
    name: string
        The name of NHL player

    Returns:
        list
            A list with the stats of every player with requested name
    '''

    file = open("nhl_stats.csv")
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        if row == []:
            continue
        rows.append(row)
    file.close()

    exists = False
    stat = []
    for item in rows:
        if item[0].lower() == name.lower():
            exists = True
            stat.append(item)
    if exists == False:
        stat.append("Player has not played a game this season!")

    return stat

def format_stats(stat):
    '''
    Formats the outuput of NHL player stats
    Parameters
    ----------
    stat: string
        The player name

    Returns
    -------
    string
            The player stats
    '''
    if stat[0] == "Player has not played a game this season!":
        output = "Player has not played a game this season!"
        return output
    for player in stat:
        count = 0
        output = ""
        for stats in player:
            count += 1
            if count == 1:
                output += stats
            elif count == 2:
                output += stats
                output += " years old"
            elif count == 4:
                if stats.lower() == "f":
                    output += "Forward"
                if stats.lower() == "c":
                    output += "Center"
                if stats.lower() == "rw":
                    output += "Right Wing"
                if stats.lower() == "lw":
                    output += "Left Wing"
                elif stats.lower() == "d":
                    output += "Defender"
            elif count == 5:
                output += stats
                output += " games played"
            elif count == 6:
                output += stats
                output += " goals"
            elif count == 7:
                output += stats
                output += " assists"
            elif count == 8:
                output += stats
                output += " points"
            elif count == 9:
                output += "+/- "
                output += stats
            elif count == 10:
                output += stats
                output += " PIM"
            else:
                continue
            if count != 26:
                output += ", "
        output += '\n'
    return output

