import math
from tkinter import *

import customtkinter
import vaRating as va

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("VA Disability Calculator")
        self.hasFocus = "btnOther"
        self.focusColor = ["#3a7ebf", "#0088FF"]
        self.noFocusColor = ["#3a7ebf", "#1f538d"]
        self.leftArm = []
        self.rightArm = []
        self.leftLeg = []
        self.rightLeg = []
        self.other = []

        self.bilateralFrame = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.bilateralFrame.pack(pady=10, padx=20, expand=True)

        self.btnLeftLeg = customtkinter.CTkButton(
            master=self.bilateralFrame, text="Left Leg", command=self.ll
        )
        self.btnLeftLeg.grid(row=0, column=0, pady=12, padx=10)

        self.btnRightLeg = customtkinter.CTkButton(
            master=self.bilateralFrame, text="Right Leg", command=self.rl
        )
        self.btnRightLeg.grid(row=0, column=1, pady=12, padx=10)

        self.btnLeftArm = customtkinter.CTkButton(
            master=self.bilateralFrame, text="Left Arm", command=self.la
        )
        self.btnLeftArm.grid(row=0, column=2, pady=12, padx=10)

        self.btnRightArm = customtkinter.CTkButton(
            master=self.bilateralFrame, text="Right Arm", command=self.ra
        )
        self.btnRightArm.grid(row=0, column=3, pady=12, padx=10)

        self.btnOther = customtkinter.CTkButton(
            master=self.bilateralFrame,
            text="Other",
            fg_color=self.focusColor,
            command=self.o,
        )
        self.btnOther.grid(row=0, column=4, pady=12, padx=10)

        self.percentageFrame = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.percentageFrame.pack(pady=10, padx=20, expand=True)

        self.btn10 = customtkinter.CTkButton(
            master=self.percentageFrame, text="10%", command=self.ten
        )
        self.btn10.grid(row=0, column=0, pady=12, padx=10)

        self.btn20 = customtkinter.CTkButton(
            master=self.percentageFrame, text="20%", command=self.twenty
        )
        self.btn20.grid(row=0, column=1, pady=12, padx=10)

        self.btn30 = customtkinter.CTkButton(
            master=self.percentageFrame, text="30%", command=self.thirty
        )
        self.btn30.grid(row=0, column=2, pady=12, padx=10)

        self.btn40 = customtkinter.CTkButton(
            master=self.percentageFrame, text="40%", command=self.forty
        )
        self.btn40.grid(row=0, column=3, pady=12, padx=10)

        self.btn50 = customtkinter.CTkButton(
            master=self.percentageFrame, text="50%", command=self.fifty
        )
        self.btn50.grid(row=0, column=4, pady=12, padx=10)

        self.btn60 = customtkinter.CTkButton(
            master=self.percentageFrame, text="60%", command=self.sixty
        )
        self.btn60.grid(row=1, column=0, pady=12, padx=10)

        self.btn70 = customtkinter.CTkButton(
            master=self.percentageFrame, text="70%", command=self.seventy
        )
        self.btn70.grid(row=1, column=1, pady=12, padx=10)

        self.btn80 = customtkinter.CTkButton(
            master=self.percentageFrame, text="80%", command=self.eighty
        )
        self.btn80.grid(row=1, column=2, pady=12, padx=10)

        self.btn90 = customtkinter.CTkButton(
            master=self.percentageFrame, text="90%", command=self.ninety
        )
        self.btn90.grid(row=1, column=3, pady=12, padx=10)

        self.btn100 = customtkinter.CTkButton(
            master=self.percentageFrame, text="100%", command=self.hundred
        )
        self.btn100.grid(row=1, column=4, pady=12, padx=10)

        self.demographicsFrame = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.demographicsFrame.pack(pady=10, padx=20, expand=True)

        self.marStatLabel = customtkinter.CTkLabel(
            master=self.demographicsFrame, text="Marital Status:"
        )
        self.marStatLabel.grid(row=0, column=0, pady=12, padx=10)

        self.maritalStatus = customtkinter.CTkOptionMenu(
            master=self.demographicsFrame,
            values=["S", "M"],
            command=self.updateRating,
        )
        self.maritalStatus.grid(row=0, column=1, pady=12, padx=10)

        self.under18Label = customtkinter.CTkLabel(
            master=self.demographicsFrame, text="Dependents under 18:"
        )
        self.under18Label.grid(row=0, column=3, pady=12, padx=10)

        self.under18 = customtkinter.CTkOptionMenu(
            master=self.demographicsFrame,
            values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            command=self.updateRating,
        )
        self.under18.grid(row=0, column=4, pady=12, padx=10)

        self.over18Label = customtkinter.CTkLabel(
            master=self.demographicsFrame, text="Dependents over 18:"
        )
        self.over18Label.grid(row=1, column=0, pady=12, padx=10)

        self.over18 = customtkinter.CTkOptionMenu(
            master=self.demographicsFrame,
            values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            command=self.updateRating,
        )
        self.over18.grid(row=1, column=1, pady=12, padx=10)

        self.depParentLabel = customtkinter.CTkLabel(
            master=self.demographicsFrame, text="Dependents Parents:"
        )
        self.depParentLabel.grid(row=1, column=3, pady=12, padx=10)

        self.depParent = customtkinter.CTkOptionMenu(
            master=self.demographicsFrame,
            values=["0", "1", "2"],
            command=self.updateRating,
        )
        self.depParent.grid(row=1, column=4, pady=12, padx=10)

        self.spouseAidLabel = customtkinter.CTkLabel(
            master=self.demographicsFrame,
            text="Does Spouse Require Aid and Attendance?",
        )
        self.spouseAidLabel.grid(row=2, column=0, columnspan=3, pady=12, padx=10)
        self.spouseAid = customtkinter.CTkOptionMenu(
            master=self.demographicsFrame, values=["N", "Y"], command=self.updateRating
        )
        self.spouseAid.grid(row=2, column=3, columnspan=2, pady=12, padx=10)

        self.ratingsFrame = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.ratingsFrame.pack(pady=10, padx=20, expand=True)

        self.ratingList = customtkinter.CTkLabel(
            master=self.ratingsFrame, text="", text_color="silver"
        )
        self.ratingList.grid(row=2, column=0, columnspan=5, pady=12, padx=10)

        self.rating = customtkinter.CTkLabel(
            master=self.ratingsFrame,
            text="0%",
            text_color="silver",
            font=customtkinter.CTkFont(size=24, weight="bold"),
        )
        self.rating.grid(row=3, column=0, columnspan=5, pady=12, padx=10)

        self.vaPayment = customtkinter.CTkLabel(
            master=self.ratingsFrame,
            text="",
            text_color="silver",
            font=customtkinter.CTkFont(size=24, weight="bold"),
        )
        self.vaPayment.grid(row=4, column=0, columnspan=5, pady=12, padx=10)

    def setButtonColor(self, btn):
        self.btnLeftLeg.configure(
            fg_color=self.focusColor if btn == "btnLeftLeg" else self.noFocusColor
        )
        self.btnRightLeg.configure(
            fg_color=self.focusColor if btn == "btnRightLeg" else self.noFocusColor
        )
        self.btnLeftArm.configure(
            fg_color=self.focusColor if btn == "btnLeftArm" else self.noFocusColor
        )
        self.btnRightArm.configure(
            fg_color=self.focusColor if btn == "btnRightArm" else self.noFocusColor
        )
        self.btnOther.configure(
            fg_color=self.focusColor if btn == "btnOther" else self.noFocusColor
        )

    def ll(self):
        self.setButtonColor("btnLeftLeg")
        self.hasFocus = "btnLeftLeg"

    def rl(self):
        self.setButtonColor("btnRightLeg")
        self.hasFocus = "btnRightLeg"

    def la(self):
        self.setButtonColor("btnLeftArm")
        self.hasFocus = "btnLeftArm"

    def ra(self):
        self.setButtonColor("btnRightArm")
        self.hasFocus = "btnRightArm"

    def o(self):
        self.setButtonColor("btnOther")
        self.hasFocus = "btnOther"

    def setPct(self, percentage):
        self.legBF = 0
        self.armBF = 0
        if percentage != 0:
            match self.hasFocus:
                case "btnLeftLeg":
                    self.leftLeg.append(percentage)
                case "btnRightLeg":
                    self.rightLeg.append(percentage)
                case "btnLeftArm":
                    self.leftArm.append(percentage)
                case "btnRightArm":
                    self.rightArm.append(percentage)
                case "btnOther":
                    self.other.append(percentage)
        self.compileLegRating(self.leftLeg, self.rightLeg)
        self.compileArmRating(self.leftArm, self.rightArm)
        if len(self.leftLeg) > 0 and len(self.rightLeg) > 0:
            self.legBF = va.GetRating(self.legRating) * 0.1
        if len(self.leftArm) > 0 and len(self.rightArm) > 0:
            self.armBF = va.GetRating(self.armRating) * 0.1
        totalRating = []
        for a in range(len(self.legRating)):
            totalRating.append(self.legRating[a])
        totalRating.append(self.legBF)
        for b in range(len(self.armRating)):
            totalRating.append(self.armRating[b])
        totalRating.append(self.armBF)
        for c in range(len(self.other)):
            totalRating.append(self.other[c])
        self.ratingList.configure(
            text=str(self.legRating + self.armRating + self.other)
            + " Bilateral Factor: "
            + str(round(self.legBF + self.armBF, 1))
            + "%"
        )
        roundedRating = round(math.floor(va.GetRating(totalRating)) / 10) * 10
        self.rating.configure(text="VA Rating: " + str(roundedRating) + "%")
        if self.spouseAid.get() == "Y":
            aaBool = True
        else:
            aaBool = False
        payment = va.GetPayment(
            roundedRating,
            self.maritalStatus.get(),
            int(self.under18.get()),
            int(self.over18.get()),
            int(self.depParent.get()),
            aaBool,
        )
        self.vaPayment.configure(text=payment)

    def ten(self):
        self.setPct(10)

    def twenty(self):
        self.setPct(20)

    def thirty(self):
        self.setPct(30)

    def forty(self):
        self.setPct(40)

    def fifty(self):
        self.setPct(50)

    def sixty(self):
        self.setPct(60)

    def seventy(self):
        self.setPct(70)

    def eighty(self):
        self.setPct(80)

    def ninety(self):
        self.setPct(90)

    def hundred(self):
        self.setPct(100)

    def updateRating(self, value):
        try:
            self.setPct(0)
        except UnboundLocalError:
            return

    def compileLegRating(self, ll, rl):
        self.legRating = []
        for i in range(len(ll)):
            self.legRating.append(ll[i])
        for j in range(len(rl)):
            self.legRating.append(rl[j])

    def compileArmRating(self, la, ra):
        self.armRating = []
        for i in range(len(la)):
            self.armRating.append(la[i])
        for j in range(len(ra)):
            self.armRating.append(ra[j])


if __name__ == "__main__":
    app = App()
    app.mainloop()
