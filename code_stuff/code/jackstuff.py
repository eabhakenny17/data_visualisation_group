from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

workbook = Path(
    r"C:\Users\jackp\Downloads"
    r"\PAQ_L_Visualisation_Ready.xlsx"
)

# Visualisation 1
sheet = "Clean Data - gpt"
dataS = "s time per year"
y_column0 = "# of people"
y_column1 = []
x_column1 = []

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[dataS],
).dropna(subset=[dataS])

loopcount = 29
i = 1
j = 1

while i < loopcount:
    while j < dataS:
        if(((i * 240 )- 240) < j < (i * 240)):
            y_value += 1
            j+=1
    y_column1.append(y_value)
    x_column1.append(((i * 240) - 240) + " - " + (i * 240))
    i+=1

plt.barh(y_column1, x_column1)
plt.ylabel("# of people")
plt.xlabel("Time spent per 240 hours")
plt.title("Number of people per sitting time")
plt.tight_layout()
plt.show()

# Visualisation 2
sheet = "Clean Data - gpt"
dataS = "v hours per year"
y_column0 = "# of people"
y_column1 = []
x_column1 = []

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[dataS],
).dropna(subset=[dataS])

loopcount = 28
for i in range(loopcount):
    y_value = sum(1 for j in dataS if((i * 36 )- 36) < j < (i * 36))
    y_column1.append(y_value)
    x_column1.append(((i * 36) - 36) + " - " + (i * 36))
y_column1.append(sum(1 for i in dataS if i > 1008))
x_column1.append(">1008")

plt.barh(x_column1, y_column1)
plt.ylabel("# of people")
plt.xlabel("Time spent per 36 hours")
plt.title("Number of people per vigorous activity time")
plt.tight_layout()
plt.show()

# Visualisation 3
sheet = "Clean Data - gpt"
dataS = "m hours per year"
y_column0 = "# of people"
y_column1 = []
x_column1 = []

data = pd.read_excel(
    workbook,
    sheet_name=sheet,
    usecols=[dataS],
).dropna(subset=[dataS])

loopcount = 28
for i in range(loopcount):
    y_value = sum(1 for j in dataS if((i * 36 )- 36) < j < (i * 36))
    y_column1.append(y_value)
    x_column1.append(((i * 36) - 36) + " - " + (i * 36))
y_column1.append(sum(1 for i in dataS if i > 1008))
x_column1.append(">1008")

plt.barh(x_column1, y_column1)
plt.ylabel("# of people")
plt.xlabel("Time spent per 36 hours")
plt.title("Number of people per moderate activity time")
plt.tight_layout()
plt.show()

# Visualisation 4
