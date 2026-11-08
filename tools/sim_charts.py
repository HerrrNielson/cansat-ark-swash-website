"""Diagramme für den Simulationsabschnitt auf flugergebnisse.html (6-DOF-SITL, Stand 08.11.2026).

Die Daten kommen aus der SITL im Haupt-Repo (cansat-ark-swash/firmware):

    pio run -e sitl
    mkdir sim-out
    .pio/build/sitl/program.exe nominal no_guidance target_north --csv sim-out
    .pio/build/sitl/program.exe --pitch-sweep > sim-out/pitch.csv

Dann im Website-Repo:

    python tools/sim_charts.py <pfad zu sim-out> assets/simulation

Schreibt flug.svg, zielanflug.svg und blattwinkel.svg. Zahlen im Text der Seite
(Sinkrate, Abstand zum Ziel …) stehen in der Ausgabe der SITL und müssen von Hand
nachgezogen werden.
"""
import csv
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

NAVY, ORANGE, BLUE, PURPLE, GRAY, WASH, GREEN = "#0b1f3a", "#ff6b1a", "#1e5aa8", "#4d1056", "#a9b4c2", "#f5f7fa", "#005300"
plt.rcParams.update({
    "font.family": "sans-serif", "font.size": 11,
    "axes.edgecolor": NAVY, "axes.labelcolor": NAVY, "axes.titlecolor": NAVY,
    "axes.titleweight": "bold", "axes.titlesize": 13,
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": NAVY, "ytick.color": NAVY,
    "figure.facecolor": WASH, "axes.facecolor": WASH, "savefig.facecolor": WASH,
    "grid.color": GRAY, "grid.alpha": 0.5, "legend.frameon": False,
    "svg.fonttype": "none", "svg.hashsalt": "swash",
})
src, out = sys.argv[1], sys.argv[2]


def load(name):
    with open(os.path.join(src, f"sitl_{name}.csv"), newline="") as f:
        rows = list(csv.DictReader(f))
    return {k: [float(r[k]) for r in rows] for k in rows[0]}


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(out, name), format="svg", metadata={"Date": None})
    plt.close(fig)
    print(name)


def rules_band(ax):
    ax.axhspan(8, 11, color=GREEN, alpha=0.08, lw=0)
    ax.text(0.01, 10.85, "Regeln: 8–11 m/s", transform=ax.get_yaxis_transform(), color=GREEN, fontsize=9, va="top")


# 1) Ein ganzer Flug
d = load("nominal")
t0 = 28.0
idx = [i for i, t in enumerate(d["t_s"]) if t >= t0]
t = [d["t_s"][i] - t0 for i in idx]
pick = lambda k: [d[k][i] for i in idx]  # noqa: E731
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(8, 5.6), height_ratios=[1.3, 1])
ax[0].plot(t, pick("alt_true_m"), color=NAVY, lw=2.2, label="Simulierter Flug")
ax[0].plot(t, pick("alt_est_m"), color=ORANGE, lw=1.4, ls="--", label="Schätzung der Firmware")
ax[0].set_ylabel("Höhe [m]")
ax[0].set_title("Ein simulierter Flug in 3D: Start, Gipfel, Rotorsinkflug, Landung")
ax[0].legend(loc="upper right")
ax[0].grid(True)
ax[1].plot(t, [-v for v in pick("vz_true_mps")], color=NAVY, lw=2.2, label="Simuliert")
ax[1].plot(t, [-v for v in pick("vz_est_mps")], color=ORANGE, lw=1.4, ls="--", label="Schätzung")
rules_band(ax[1])
ax[1].set_ylim(-2, 25)
ax[1].set_ylabel("Sinkrate [m/s]")
ax[1].set_xlabel("Zeit ab Start [s]")
ax[1].grid(True)
save(fig, "flug.svg")

# 2) Zielanflug: Bahn von oben
fig, ax = plt.subplots(figsize=(8, 5.4))
cases = [("no_guidance", "Ohne Zielanflug", GRAY, (0, 0)),
         ("nominal", "Ziel Startschiene", ORANGE, (0, 0)),
         ("target_north", "Ziel 300 m nördlich", BLUE, (0, 300))]
for name, label, color, target in cases:
    c = load(name)
    desc = [i for i, p in enumerate(c["phase_true"]) if p >= 3]
    asc = [i for i, p in enumerate(c["phase_true"]) if 1 <= p < 3]
    ax.plot([c["x_m"][i] for i in asc], [c["y_m"][i] for i in asc], color=NAVY, lw=1, alpha=0.35)
    ax.plot([c["x_m"][i] for i in desc], [c["y_m"][i] for i in desc], color=color, lw=2.4, label=label)
    end = desc[-1]
    ax.plot(c["x_m"][end], c["y_m"][end], "o", color=color, ms=7)
    if name != "no_guidance":
        ax.plot(*target, marker="X", color=NAVY, ms=11, mec=WASH, mew=1.2, zorder=5)
ax.plot([], [], color=NAVY, lw=1, alpha=0.35, label="Steigflug der Rakete")
ax.plot([], [], marker="X", color=NAVY, ls="none", ms=10, label="Ziel")
ax.annotate("", xy=(205, 238), xytext=(135, 238), arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.6))
ax.text(170, 252, "Wind aus Westen", color=NAVY, ha="center", fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-130, 230)
ax.set_ylim(-40, 330)
ax.set_xlabel("Osten [m]")
ax.set_ylabel("Norden [m]")
ax.set_title("Zielanflug: Bahn von oben gesehen")
ax.legend(loc="lower right", fontsize=9)
ax.grid(True)
save(fig, "zielanflug.svg")

# 3) Einstellwinkel
with open(os.path.join(src, "pitch.csv"), newline="") as f:
    rows = list(csv.DictReader(f))
pitch = [-float(r["pitch_deg"]) for r in rows]  # Teamkonvention: Vorderkante nach unten positiv
sink = [float(r["sink_mps"]) for r in rows]
rpm = [float(r["rpm"]) for r in rows]
fig, ax = plt.subplots(figsize=(8, 4.6))
rules_band(ax)
ax.plot(pitch, sink, color=NAVY, lw=2.4, marker="o", ms=3.5, label="Sinkrate")
ax.set_xlabel("Einstellwinkel der Blätter im Sinkflug [°] (Vorderkante nach unten)")
ax.set_ylabel("Sinkrate [m/s]", color=NAVY)
ax.set_ylim(0, 25)
ax.axvspan(-2.25, 1.25, color=PURPLE, alpha=0.07, lw=0)
ax.text(-0.5, 23.6, "Rotor reißt ab", color=PURPLE, ha="center", fontsize=9)
ax.axvline(4.5, color=ORANGE, lw=1, ls=":")
ax.text(4.7, 1.2, "im Flug 4,5°", color=ORANGE, fontsize=9)
ax.grid(True)
ax2 = ax.twinx()
ax2.plot(pitch, rpm, color=ORANGE, lw=1.8, ls="--", label="Drehzahl")
ax2.set_ylabel("Rotordrehzahl [U/min]", color=ORANGE)
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(ORANGE)
ax2.tick_params(axis="y", colors=ORANGE)
ax2.set_ylim(0, 7000)
ax.set_title("Einstellwinkel stellt die Sinkrate ein (Modell, 350 g)")
lines = ax.get_lines()[:1] + ax2.get_lines()
ax.legend(lines, [ln.get_label() for ln in lines], loc="lower right")
save(fig, "blattwinkel.svg")
