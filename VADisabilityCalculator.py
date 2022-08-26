import math

import PySimpleGUI as sg

import vaRating as va

sg.theme("DarkGrey15")
sg.set_options(font="Arial 12")

focusColor = ("black", "DeepSkyBlue2")
noFocusColor = (sg.theme_button_color_text(), sg.theme_button_color_background())


def windowVACalculator():

    layout = [
        [
            sg.Button("Left Leg", size=(10, 1), button_color=noFocusColor),
            sg.Button("Right Leg", size=(10, 1), button_color=noFocusColor),
            sg.Button("Left Arm", size=(10, 1), button_color=noFocusColor),
            sg.Button("Right Arm", size=(10, 1), button_color=noFocusColor),
            sg.Button("Other", size=(10, 1), button_color=focusColor),
        ],
        [sg.HSeparator(pad=(5, 5), color=sg.theme_button_color_background())],
        [
            sg.Button("10%", size=(10, 1)),
            sg.Button("20%", size=(10, 1)),
            sg.Button("30%", size=(10, 1)),
            sg.Button("40%", size=(10, 1)),
            sg.Button("50%", size=(10, 1)),
        ],
        [
            sg.Button("60%", size=(10, 1)),
            sg.Button("70%", size=(10, 1)),
            sg.Button("80%", size=(10, 1)),
            sg.Button("90%", size=(10, 1)),
            sg.Button("100%", size=(10, 1)),
        ],
        [sg.Text("", key="Disabilities", enable_events=True)],
        [sg.Text("", key="lblRawRating")],
        [sg.Text("", key="rawRating")],
        [sg.Text("", key="lblRating")],
        [sg.Text("", key="Rating", font="Arial 24")],
        [sg.Text("", key="lblBilateral")],
        [sg.Button("Get Rating"), sg.Button("Reset")],
        [sg.HSeparator(pad=(5, 5), color=sg.theme_button_color_background())],
        [
            sg.Text(
                "Number of dependent children under 18:",
                size=(40, 1),
                key="lblUnder18",
                visible=False,
            ),
            sg.InputText(
                "0", key="under18", size=(2, 1), visible=False, enable_events=True
            ),
        ],
        [
            sg.Text(
                "Number of dependent children over 18:",
                size=(40, 1),
                key="lblOver18",
                visible=False,
            ),
            sg.InputText(
                "0", key="over18", size=(2, 1), visible=False, enable_events=True
            ),
        ],
        [
            sg.Text(
                "Marital Status:",
                key="lblMarStatus",
                visible=False,
            ),
            sg.Combo(
                ["M", "S"],
                key="marStatus",
                default_value="S",
                visible=False,
                enable_events=True,
            ),
        ],
        [
            sg.Text(
                "Spouse requires Aid and Attendance (A/A):",
                key="lblSpouseAid",
                visible=False,
            ),
            sg.Combo(["Y", "N"], key="spouseAid", default_value="N", visible=False),
        ],
        [
            sg.Text(
                "Number of dependent parents:",
                key="lblDepParents",
                visible=False,
            ),
            sg.Combo(
                ["0", "1", "2"], key="depParents", default_value="0", visible=False
            ),
        ],
        [sg.Button("Get Payment", key="Get Payment", visible=False)],
        [sg.Text(key="lblPayment")],
        [sg.Text(key="payment", font="Arial 24")],
    ]

    return sg.Window(
        "VA Rating and Disability Calculator", layout, element_justification="c"
    )


hasFocus = "Other"
blLeftLeg = []
blRightLeg = []
blLeftArm = []
blRightArm = []
otherRating = []
disabilities = ""
paymentEnabled = False


window = windowVACalculator()


def setupPayment():
    paymentEnabled = True
    window["lblUnder18"].update(visible=True)
    window["under18"].update(visible=True)
    window["lblOver18"].update(visible=True)
    window["over18"].update(visible=True)
    window["lblMarStatus"].update(visible=True)
    window["marStatus"].update(visible=True)
    window["lblDepParents"].update(visible=True)
    window["depParents"].update(visible=True)
    window["depParents"].update(visible=True)
    window["Get Payment"].update(visible=True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in ("Left Leg", "Right Leg", "Left Arm", "Right Arm"):
        window["Left Leg"].update(button_color=noFocusColor)
        window["Right Leg"].update(button_color=noFocusColor)
        window["Left Arm"].update(button_color=noFocusColor)
        window["Right Arm"].update(button_color=noFocusColor)
        window["Other"].update(button_color=noFocusColor)
        window[event].update(button_color=focusColor)
        hasFocus = event

    if event == "Other":
        window["Left Leg"].update(button_color=noFocusColor)
        window["Right Leg"].update(button_color=noFocusColor)
        window["Left Arm"].update(button_color=noFocusColor)
        window["Right Arm"].update(button_color=noFocusColor)
        window["Other"].update(button_color=focusColor)

    if event == "Disabilities":
        hasFocus = "Other"
        blLeftLeg = []
        blRightLeg = []
        blLeftArm = []
        blRightArm = []
        otherRating = []
        disabilities = ""
        window["Disabilities"].update(disabilities)
        window["Left Leg"].update(button_color=noFocusColor)
        window["Right Leg"].update(button_color=noFocusColor)
        window["Left Arm"].update(button_color=noFocusColor)
        window["Right Arm"].update(button_color=noFocusColor)
        window["Other"].update(button_color=focusColor)

    if event in ("10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"):
        match event:
            case "10%":
                rating = 10
            case "20%":
                rating = 20
            case "30%":
                rating = 30
            case "40%":
                rating = 40
            case "50%":
                rating = 50
            case "60%":
                rating = 60
            case "70%":
                rating = 70
            case "80%":
                rating = 80
            case "90%":
                rating = 90
            case "100%":
                rating = 100
        disabilities += "(" + str(rating) + "%"

        match hasFocus:
            case "Left Leg":
                blLeftLeg.append(rating)
                disabilities += " LL) "
            case "Right Leg":
                blRightLeg.append(rating)
                disabilities += " RL) "
            case "Left Arm":
                blLeftArm.append(rating)
                disabilities += " LA) "
            case "Right Arm":
                blRightArm.append(rating)
                disabilities += " RA) "
            case "Other":
                otherRating.append(rating)
                disabilities += ") "
        window["Disabilities"].update(disabilities)

    if event == "Reset":
        window.close()
        window = windowVACalculator()
        hasFocus = "Other"
        blLeftLeg = []
        blRightLeg = []
        blLeftArm = []
        blRightArm = []
        otherRating = []
        disabilities = ""
        paymentEnabled = False

    if event == "Get Rating":
        bilateralFactor = 0
        bilateralRating = []
        legRating = [blLeftLeg[i] for i in range(0, len(blLeftLeg))]
        for i in range(0, len(blRightLeg)):
            legRating.append(blRightLeg[i])
        armRating = [blLeftArm[i] for i in range(0, len(blLeftArm))]
        for i in range(0, len(blRightArm)):
            armRating.append(blRightArm[i])

        combinedRating = [legRating[i] for i in range(0, len(legRating))]
        for i in range(0, len(armRating)):
            combinedRating.append(armRating[i])
        for i in range(0, len(otherRating)):
            combinedRating.append(otherRating[i])

        if len(blLeftLeg) > 0 and len(blRightLeg) > 0:
            bilateralRating = [blLeftLeg[i] for i in range(0, len(blLeftLeg))]
            for i in range(0, len(blRightLeg)):
                bilateralRating.append(blRightLeg[i])
        if len(blLeftArm) > 0 and len(blRightArm) > 0:
            bilateralRating = [blLeftArm[i] for i in range(0, len(blLeftArm))]
            for i in range(0, len(blRightArm)):
                bilateralRating.append(blRightArm[i])
        if len(bilateralRating) > 0:
            bilateralFactor = round(va.GetRating(bilateralRating) / 10, 1)
            window["lblBilateral"].update(
                "(a bilateral factor of " + str(bilateralFactor) + " has been applied)"
            )
        rawRating = va.GetRating(combinedRating) + bilateralFactor
        totalRating = math.floor(rawRating)
        window["lblRawRating"].update("Total Calculated Rating:")
        window["rawRating"].update(str(int(round(rawRating, 0))) + "%")
        window["lblRating"].update("VA Rounded Rating:")
        rating = round(totalRating / 10) * 10
        window["Rating"].update(str(rating) + "%")
        if not paymentEnabled:
            setupPayment()

    if event == "marStatus" and values[event] == "M":
        window["lblSpouseAid"].update(visible=True)
        window["spouseAid"].update(visible=True)

    if (
        event in ("under18", "over18")
        and values[event]
        and values[event][-1] not in ("0123456789")
    ):
        window[event].update(values[event][:-1])

    if event == "Get Payment":
        marStatus = values["marStatus"]
        under18 = int(values["under18"])
        over18 = int(values["over18"])
        depParents = int(values["depParents"])
        if values["spouseAid"] == "Y":
            spouseAid = True
        else:
            spouseAid = False

        payment = va.GetPayment(
            rating, marStatus, under18, over18, depParents, spouseAid
        )
        window["lblPayment"].update("Monthly Payment Amount:")
        window["payment"].update("$" + str(payment))

window.close()
