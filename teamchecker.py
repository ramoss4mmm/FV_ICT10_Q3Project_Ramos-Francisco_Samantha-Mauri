from pyscript import document, display
import random

def intramsteam(e): #e for event handling
    document.getElementById('output1').innerHTML = ''
    registered = document.getElementById("registered").checked
    not_registered = document.getElementById("notregistered").checked
    med_yes = document.getElementById("medyes").checked
    med_no = document.getElementById("medno").checked
    level = document.getElementById("level").value
    teams = {"Blue Bears": "blue_bears.png", "Red Bulldogs": "red_bulldogs.png", "Yellow Tigers": "yellow_tigers.png", "Green Hornets": "green_hornets.png"}

    # use .checked instead of .value as it tells us if a checkbox if checked or not

    if level not in ["7", "8", "9", "10"]:
        display("You must be in grades 7-10 to join the Intramurals.", target="output1")
        return

    if not registered: # checks if the user is not registered by using the if statement and the not operator
        display("Please register online to join the Intramurals.", target="output1")

    elif not med_yes: # checks if the user does not have a medical clearance by using the elif statement and the not operator
        display("Please secure a medical clearance from the clinic.", target="output1")

    else: # default block, shows the intramurals team
        intrams_teams = random.choice(list(teams.keys())) # picks a team randomly
        team_img = teams[intrams_teams]
        summary = f"""
        Congratulations!<br>
        You are eligible to join the Intramurals.<br>
        Your assigned team is: <strong>{intrams_teams}</strong><br><br>

        <center><img src="{team_img}" width="200"></center>
        """
        # displays the users team in the output1
        document.getElementById("output1").innerHTML = summary
