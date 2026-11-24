# Erzeugt ab-winkel-zeichnen.tex: Nachbau der beiden Vorlagen (Winkelmessung, Winkel mit vorgegebenem Winkelmaß zeichnen).
# Alle Positionen kommen aus pos.json (aus dem Foto entzerrt), in cm von oben links.
import json, math
P = json.load(open('pos.json'))
A, B = P['46'], P['21']

def q(p, dx=0, dy=0):
    return f"({p[0] + dx:.2f},{-(p[1] + dy):.2f})"

def ang(V, E1, E2, F=None):
    s = f"\\draw[strich] {q(E1)} -- {q(V)} -- {q(E2)};\n"
    if F: s += f"\\feld{{{q(F)}}}\n"
    return s + f"\\fill[punkt] {q(V)} circle (0.045);\n"

def txt(p, t, extra=''):
    return f"\\node[anchor=west, inner sep=0{extra}] at {q(p)} {{{t}}};\n"

def num(p, t):
    return f"\\node[anchor=west, inner sep=0, text=blau] at {q(p)} {{{t}}};\n"

def box(p, n):
    return f"\\node[nrbox] at {q(p)} {{{n}}};\n"

head = r"""% Nachbau zweier Arbeitsblätter: Vorderseite Winkelmessung, Rückseite Winkel mit vorgegebenem Winkelmaß zeichnen.
% Kompilieren mit xelatex. Schrift Andika liegt im Ordner fonts.
\documentclass{article}
\usepackage[a4paper, margin=0cm]{geometry}
\usepackage{fontspec}
\setmainfont{Andika}[Path=fonts/, Extension=.ttf, UprightFont=*-Regular, BoldFont=*-Bold]
\usepackage{tikz}
\usetikzlibrary{calc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\definecolor{blau}{HTML}{2D4B7C}
\definecolor{rand}{HTML}{8C9AB5}
\definecolor{rot}{HTML}{C0392B}
\definecolor{feldgrau}{HTML}{C9CCD2}
\definecolor{gelb}{HTML}{F2C037}
\definecolor{geo}{HTML}{E9EFF5}
\definecolor{gruen}{HTML}{C9DFA8}
\definecolor{stiftblau}{HTML}{2F67B1}
\definecolor{stiftgruen}{HTML}{2E8B57}
\definecolor{holz}{HTML}{EBCB9C}
\tikzset{
  strich/.style={line width=1.05pt, line cap=round},
  punkt/.style={rot},
  nrbox/.style={draw, line width=0.5pt, minimum size=0.36cm, inner sep=0, font=\fontsize{8.5}{9}\selectfont\bfseries},
  % Geodreieck wie auf der Vorlage: Gradskala entlang der kurzen Seiten, gelber runder Skalenring innen, Griff, Hilfslinien
  pics/geodreieck/.style={code={
    \fill[geo, fill opacity=0.85] (-8,0) -- (8,0) -- (0,8) -- cycle;
    \foreach \h in {0.9,1.4,...,3.9} {\pgfmathsetmacro\w{sqrt(max(3.95*3.95-\h*\h,0))} \draw[black!40, line width=0.2pt] (-\w,\h) -- (\w,\h);}
    \draw[black!40, line width=0.25pt] (0,0) -- (0,3.95) (0,0) -- (45:3.95) (0,0) -- (135:3.95);
    \fill[gelb] (4.75,0) arc (0:180:4.75) -- (-3.95,0) arc (180:0:3.95) -- cycle;
    \draw[black!55, line width=0.25pt] (4.75,0) arc (0:180:4.75) (3.95,0) arc (0:180:3.95);
    \foreach \t in {1,...,179} {\pgfmathsetmacro\l{mod(\t,10)==0 ? 0.3 : (mod(\t,5)==0 ? 0.2 : 0.12)} \draw[line width=0.15pt] (\t:4.75) -- (\t:{4.75-\l});}
    \foreach \k in {10,20,...,170} {\pgfmathtruncatemacro\m{180-\k} \pgfmathsetmacro\r{\k-90} \node[font=\fontsize{3.8}{4}\selectfont, inner sep=0, rotate=\r] at (\k:4.2) {\m};}
    \fill[black!82, rounded corners=0.3] (-1.9,1.2) rectangle (1.9,1.8);
    \foreach \t in {3,...,177} {\pgfmathsetmacro\l{mod(\t,10)==0 ? 0.55 : (mod(\t,5)==0 ? 0.38 : 0.22)}
      \pgfmathsetmacro\ra{(8-0.12*1.4142)/(abs(cos(\t))+sin(\t))} \pgfmathsetmacro\rb{(8-(0.12+\l)*1.4142)/(abs(cos(\t))+sin(\t))}
      \draw[line width=0.15pt] (\t:\ra) -- (\t:\rb);}
    \foreach \k in {10,20,...,170} {\pgfmathsetmacro\r{(8-1.05*1.4142)/(abs(cos(\k))+sin(\k))} \pgfmathsetmacro\w{\k-90} \node[font=\fontsize{4.2}{4.5}\selectfont, inner sep=0, rotate=\w] at (\k:\r) {\k};}
    \foreach \i in {-75,...,75} {\pgfmathsetmacro\l{mod(\i,10)==0 ? 0.36 : (mod(\i,5)==0 ? 0.25 : 0.15)} \draw[line width=0.15pt] (\i/10,0) -- (\i/10,\l);}
    \foreach \i in {-7,...,7} {\pgfmathtruncatemacro\n{abs(\i)} \node[font=\fontsize{4}{4.5}\selectfont, inner sep=0] at (\i,0.55) {\n};}
    \draw[black!60, line width=0.5pt] (-8,0) -- (8,0) -- (0,8) -- cycle;
  }},
  % kleines Hilfsgeodreieck wie in Aufgabe 1
  pics/geohint/.style={code={
    \draw[gelb!70, line width=1.4pt] (4.3,0) arc (0:180:4.3);
    \draw[black!45, line width=0.35pt] (-8,0) -- (8,0) -- (0,8) -- cycle; \draw[black!45, line width=0.35pt] (0,0) -- (0,8);
  }}
}
% Antwortfeld
\newcommand{\feld}[1]{\fill[feldgrau, rounded corners=1.5pt] ($#1+(-0.6,-0.3)$) rectangle ($#1+(0.6,0.3)$);}
% Stift: Spitze, Richtung zum Ende, Farbe, Länge, Breite (cm)
\newcommand{\stift}[5]{\begin{scope}[shift={#1}, rotate=#2]
  \fill[#3] (0.55,-#5/2) rectangle (#4,#5/2);
  \fill[#3!70!black] (0.55,-#5/2) rectangle (#4,-#5/6);
  \fill[holz] (0,0) -- (0.55,-#5/2) -- (0.55,#5/2) -- cycle;
  \fill[#3!60!black] (0,0) -- (0.18,-#5/6) -- (0.18,#5/6) -- cycle;
  \draw[black!70, line width=0.3pt] (0,0) -- (0.55,-#5/2) -- (#4,-#5/2) -- (#4,#5/2) -- (0.55,#5/2) -- cycle;
\end{scope}}
\begin{document}
\fontsize{10.9}{13}\selectfont
"""

# ---------- Vorderseite: Winkelmessung ----------
s = r"""\null
\begin{tikzpicture}[remember picture, overlay, shift={(current page.north west)}]
\draw[rand, line width=1.1pt] (1.2,-0.6) -- (1.2,-29.1);
\draw[blau, line width=0.5pt] (1.2,-2.2) -- (20.4,-2.2);
\draw[blau, line width=0.5pt] (1.2,-27.6) -- (20.4,-27.6);
"""
s += txt(A['kopf'], 'Winkelmessung')
s += "\\node[anchor=west, inner sep=0, text=black!75] at (2.45,-28.35) {46}; \\node[anchor=west, inner sep=0, text=black!75] at (3.75,-28.35) {sechsundvierzig};\n"
s += txt(A['teile1'], 'So heißen die Teile') + txt(A['teile2'], 'eines Winkels:')
s += f"\\draw[strich] {q(A['tA'])} -- {q(A['tV'])} -- {q(A['tB'])};\n"
s += txt(A['schenkel'], 'Schenkel') + txt(A['scheitel'], 'Scheitel')
o = A['arrO']
s += f"\\draw[-stealth, line width=0.55pt] {q(o, 0, -0.02)} -- {q(o, -0.12, -0.02)} .. controls {q(o, -0.32, -0.02)} and {q(o, -0.4, -0.12)} .. {q(o, -0.42, -0.42)};\n"
s += f"\\draw[-stealth, line width=0.55pt] {q(o, 0, 0.06)} -- {q(o, -0.12, 0.06)} .. controls {q(o, -0.32, 0.06)} and {q(o, -0.4, 0.16)} .. {q(o, -0.42, 0.48)};\n"
so, st = A['sArrO'], A['sArrT']
s += f"\\draw[-stealth, line width=0.55pt] {q(so)} -- {q((st[0] + 0.25, so[1]))} .. controls {q((st[0], so[1]))} .. {q(st)};\n"
# großes Geodreieck mit Winkel
g0 = (A['g0'][0], (A['gL'][1] + A['gR'][1]) / 2)
u = (A['gR'][0] - A['gL'][0]) / 16
s += f"\\begin{{scope}}[shift={{{q(g0)}}}, x={u:.3f}cm, y={u:.3f}cm]\n\\pic {{geodreieck}};\n"
s += f"\\draw[strich] (0,0) -- ({(A['s1'][0] - g0[0]) / u:.2f},0); \\draw[strich] (0,0) -- (40:{math.hypot(A['s2'][0] - g0[0], A['s2'][1] - g0[1]) / u:.2f});\n"
s += "\\fill[punkt] (0,0) circle (0.07);\n\\end{scope}\n"
# Kreis 3 dort, wo der zweite Schenkel die Skala schneidet
s += f"\\begin{{scope}}[shift={{{q(g0)}}}, x={u:.3f}cm, y={u:.3f}cm]\\draw[line width=0.6pt, black!80] (40:5.25) circle (0.68); \\node[anchor=west, inner sep=0] at ($(40:5.25)+(0.95,0.1)$) {{3.}};\\end{{scope}}\n"
s += f"\\node[inner sep=0, text=rot] at {q(A['l1'])} {{1.}};\n\\node[inner sep=0, text=blau] at {q(A['l2'])} {{2.}};\n"
# Anleitung
s += txt(A['misst'], 'So misst man einen Winkel:')
s += num((3.15, A['n1'][1]), '\\textcolor{rot}{1.}') + txt((3.77, A['t1'][1]), 'Lege den Nullpunkt des Geodreiecks auf den Scheitel des Winkels.')
s += num((3.15, A['n2'][1]), '2.') + txt((3.77, A['t2'][1]), 'Drehe das Geodreieck, bis seine Kante auf dem Schenkel des Winkels liegt')
s += txt((3.77, A['t2b'][1]), 'und dabei der andere Schenkel unter dem Geodreieck ist.')
s += num((3.15, A['n3'][1]), '3.') + txt((3.77, A['t3'][1]), 'Lies die Winkelskala des Geodreiecks dort ab, wo der andere Schenkel sie schneidet.')
s += txt((3.77, A['t3b'][1]), 'Nimm die Skala, die beim ersten Schenkel bei 0 beginnt.')
# Aufgabe 1
s += box((2.55, A['a1'][1]), '1') + txt((3.12, A['a1'][1]), 'Miss und notiere die spitzen Winkel. Spitze Winkel sind kleiner als 90°.')
for k in 'abcd':
    s += ang(A[k + 'V'], A[k + 'A'], A[k + 'B'], A[k + 'F'])
# Aufgabe 2
s += box((2.6, A['a2'][1]), '2') + txt((3.17, A['a2'][1]), 'Miss und notiere die stumpfen Winkel. Stumpfe Winkel sind größer als 90°')
s += txt((3.17, A['a2b'][1]), 'und kleiner als 180°.')
s += ang(A['eV'], A['eA'], A['eB'], A['eF']) + ang(A['fV'], A['fA'], A['fB'], A['fF']) + ang(A['gV'], A['gA2'], A['gB'], A['gF'])
s += "\\end{tikzpicture}\n\\newpage\n"

# ---------- Rückseite: Winkel mit vorgegebenem Winkelmaß zeichnen ----------
t = r"""\null
\begin{tikzpicture}[remember picture, overlay, shift={(current page.north west)}]
\draw[rand, line width=0.7pt] (19.8,-0.6) -- (19.8,-29.1); \draw[rand, line width=0.7pt] (20.05,-0.6) -- (20.05,-29.1);
\draw[blau, line width=0.5pt] (0.6,-2.2) -- (19.8,-2.2);
\draw[blau, line width=0.5pt] (0.6,-27.6) -- (19.8,-27.6);
"""
t += txt(B['kopf'], 'Winkel mit vorgegebenem Winkelmaß zeichnen')
t += "\\node[anchor=east, inner sep=0, text=black!75] at (17.3,-28.35) {einundzwanzig}; \\node[anchor=east, inner sep=0, text=black!75] at (18.6,-28.35) {21};\n"
t += txt(B['intro'], r'So zeichnest du einen Winkel, der eine bestimmte Größe hat. Hier sind es \textbf{30°}.')
# Bild 1: Geodreieck auf der Linie, Stift an der 30
u1 = (B['f1R'][0] - B['f1L'][0]) / 16
n1 = (B['f1N'][0], (B['f1L'][1] + B['f1R'][1]) / 2)
t += f"\\draw[strich] {q((B['f1L'][0], n1[1]))} -- {q((B['f1E'][0], n1[1]))};\n"
t += f"\\begin{{scope}}[shift={{{q(n1)}}}, x={u1:.3f}cm, y={u1:.3f}cm]\n\\pic {{geodreieck}};\n\\fill[punkt] (0,0) circle (0.12);\n"
t += "\\stift{(30:6.2)}{98}{stiftblau}{6.3}{0.85}\n\\end{scope}\n"
# Bild 2: Geodreieck mit der langen Kante auf der Verbindung von Punkt und Markierung, Stift zieht an der Kante entlang
BL, R, Pp = B['g2BL'], B['g2R'], B['g2P']
u2 = math.hypot(R[0] - BL[0], R[1] - BL[1]) / 16
rot = math.degrees(math.atan2(-(R[1] - BL[1]), R[0] - BL[0]))
M = ((BL[0] + R[0]) / 2, (BL[1] + R[1]) / 2)
t += f"\\draw[strich] {q(Pp)} -- {q((B['g2L'][0], Pp[1]))};\n"
t += f"\\begin{{scope}}[shift={{{q(M)}}}, rotate={rot:.1f}, x={u2:.3f}cm, y={u2:.3f}cm]\n\\pic[transform shape] {{geodreieck}};\n\\end{{scope}}\n"
t += f"\\draw[strich] {q(Pp)} -- {q(B['g2T'])};\n\\fill[punkt] {q(Pp)} circle (0.05);\n"
pd = math.degrees(math.atan2(-(B['g2E'][1] - B['g2T'][1]), B['g2E'][0] - B['g2T'][0]))
pl = math.hypot(B['g2E'][0] - B['g2T'][0], B['g2E'][1] - B['g2T'][1])
t += f"\\stift{{{q(B['g2T'])}}}{{{pd:.1f}}}{{stiftgruen}}{{{pl:.2f}}}{{0.3}}\n"
# Anleitung
t += num((1.65, B['n1'][1]), '\\textcolor{rot}{1.}') + txt((2.15, B['t1'][1]), 'Lege das Geodreieck mit der Null an')
t += txt((2.15, B['t1b'][1]), 'den Punkt, wo der Winkel entstehen soll.') + txt((2.15, B['t1c'][1]), 'Die Kante muss auf der Linie liegen.')
t += num((1.65, B['n2'][1]), '2.') + txt((2.15, B['t2'][1]), r'Markiere die Stelle, an der \textbf{30} auf der')
t += txt((2.15, B['t2b'][1]), 'Skala steht.')
t += num((10.6, B['n3'][1]), '3.') + txt((11.1, B['t3'][1]), 'Verbinde den Punkt mit der Markierung.')
t += txt((11.1, B['t3b'][1]), 'Du darfst über die Markierung hinaus') + txt((11.1, B['t3c'][1]), 'verlängern.')
# Aufgabe 1
t += box((1.75, B['a1'][1]), '1') + txt((2.3, B['a1'][1]), 'Zeichne Winkel mit den vorgegebenen Winkelmaßen.')
for v, e, a, c in [('v40', 'e40', 'h40a', 'h40c'), ('v20', 'e20', 'h20a', 'h20b')]:
    V, E, H1, H2 = B[v], B[e], B[a], B[c]
    uh = math.hypot(H2[0] - H1[0], H2[1] - H1[1]) / 16
    d = math.degrees(math.atan2(-(H2[1] - H1[1]), H2[0] - H1[0]))
    # Spitze des Hilfsgeodreiecks auf der richtigen Seite der Linie
    apex = B['h40b'] if v == 'v40' else B['h20c']
    side = (H2[0] - H1[0]) * (-(apex[1] - H1[1])) - (-(H2[1] - H1[1])) * (apex[0] - H1[0])
    r = d if side > 0 else d + 180
    t += f"\\begin{{scope}}[shift={{{q(V)}}}, rotate={r:.1f}, x={uh:.3f}cm, y={uh:.3f}cm]\\pic[transform shape] {{geohint}};\\end{{scope}}\n"
    t += f"\\draw[strich] {q(V)} -- {q(E)};\n\\fill[punkt] {q(V)} circle (0.045);\n"
t += f"\\node[inner sep=0] at {q(B['l40'])} {{40°}};\n\\node[inner sep=0] at {q(B['l20'])} {{20°}};\n"
# Aufgabe 2
t += box((1.75, B['a2'][1]), '2') + txt((2.3, B['a2'][1]), 'Zeichne Winkel mit den angegebenen Winkelmaßen.')
t += txt((2.3, B['a2b'][1]), 'Überlege zuerst, wie du das Geodreieck anlegen musst.')
for v, e, l, n in [('v10', 'e10', 'l10', '10°'), ('v100', 'e100', 'l100', '100°')]:
    t += f"\\draw[strich] {q(B[v])} -- {q(B[e])};\n\\fill[punkt] {q(B[v])} circle (0.045);\n\\node[inner sep=0] at {q(B[l])} {{{n}}};\n"
t += "\\end{tikzpicture}\n\\end{document}\n"

open('ab-winkel-zeichnen.tex', 'w').write(head + s + t)
