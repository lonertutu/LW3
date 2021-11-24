import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

luma_white_mercury = j.readIntensity("mercury_white.jpg", "white-mercury", "ртутная лампа", "белый лист")
luma_blue_tungsten = j.readIntensity("glow_lamp_blue.jpg", "blue-tungsten", "лампа накаливания", "синий лист")
luma_green_tungsten = j.readIntensity("glow_lamp_green.jpg", "green-tungsten", "лампа накаливания", "зеленый лист")
luma_red_tungsten = j.readIntensity("glow_lamp_red.jpg", "red-tungsten", "лампа накаливания", "красный лист")
luma_white_tungsten = j.readIntensity("glow_lamp_white.jpg", "white-tungsten", "лампа накаливания", "белый лист")
luma_yellow_tungsten = j.readIntensity("glow_lamp_yellow.jpg", "yellow-tungsten", "лампа накаливания", "желтый лист")

f = open("mean.txt", "r")
x = [1, 1, 1]
i = 0
x[2] = int(f.readline())
x[1] = int(f.readline())
x[0] = int(f.readline())
print(x)
y = [435.8328, 546.0735, 578.2] #пики интенсивности ртутной лампы


A = np.vstack([x, np.ones(len(x))]).T
cl, dy = np.linalg.lstsq(A, y, rcond=None)[0]  #метод наименьших квадратов для нахождения угла наклона cl

X = np.arange(y[0] - x[0] * cl, y[0] + cl * (600 - x[0]), cl)

fig, ax = plt.subplots(figsize=(16, 10), dpi = 200)
fig.suptitle("Отраженная интенсивность излучения лампы накаливания")
ax.set_xlabel("Длина волны [нм]")
ax.set_ylabel("Яркость")
ax.plot(X, luma_white_tungsten, "w", label = "белый лист")
ax.plot(X, luma_blue_tungsten, "blue", label = "синий лист")
ax.plot(X, luma_green_tungsten, "g", label = "зеленый лист")
ax.plot(X, luma_red_tungsten, "r", label = "красный лист")
ax.plot(X, luma_yellow_tungsten, "y", label = "желтый лист")
ax.grid(True, which = "major", linestyle = "-")
ax.minorticks_on()
ax.grid(True, which = "minor", linestyle = "--", alpha = 0.5)
ax.set_facecolor("grey")
legend = ax.legend(loc='upper right', fontsize='small')


fig.savefig("intensities.png")


plt.show()


albedo_white = luma_white_tungsten / luma_white_tungsten
albedo_blue = luma_blue_tungsten / luma_white_tungsten
albedo_red = luma_red_tungsten / luma_white_tungsten
albedo_green = luma_green_tungsten / luma_white_tungsten
albedo_yellow = luma_yellow_tungsten / luma_white_tungsten


fig1, ax1 = plt.subplots(figsize=(16, 10), dpi = 200)
fig1.suptitle("Альбедо поверхностей")
ax1.set_xlabel("Длина волны [нм]")
ax1.set_ylabel("Альбедо")
ax1.plot(X, albedo_white, "w", label = "белый лист")
ax1.plot(X, albedo_blue, "blue", label = "синий лист")
ax1.plot(X, albedo_green, "g", label = "зеленый лист")
ax1.plot(X, albedo_red, "r", label = "красный лист")
ax1.plot(X, albedo_yellow, "y", label = "желтый лист")
ax1.grid(True, which = "major", linestyle = "-")
ax1.minorticks_on()
ax1.grid(True, which = "minor", linestyle = "--", alpha = 0.5)
ax1.set_facecolor("grey")
legend = ax1.legend(loc='upper right', fontsize='small')


fig1.savefig("albedo.png")


plt.show()