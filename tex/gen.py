PRE = r"""\documentclass[14pt,a4paper]{extarticle}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[scaled]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{amsmath}
\usepackage{sansmath}
\sansmath
\usepackage[a4paper,margin=2cm]{geometry}
\usepackage{tikz}
\usetikzlibrary{angles,quotes,patterns}
\usepackage{array}
\pagestyle{empty}
% Zweite Seite: 5-mm-Kästchen, 1 cm Rand
\newcommand{\kaestchen}{\newpage\null\begin{tikzpicture}[remember picture,overlay]
\begin{scope}[shift={(current page.south west)}]\draw[step=5mm, black!45, line width=0.3pt] (1cm,1cm) grid (20cm,28.5cm);\draw[black!45, line width=0.3pt] (1cm,1cm) rectangle (20cm,28.5cm);\end{scope}
\end{tikzpicture}}
\setlength{\parindent}{0pt}
\hyphenpenalty=10000

% Nur Schwarz und Grau, die Blätter werden schwarz-weiß kopiert.
% Merkblock: Begriff und Text links, Zeichnung rechts.
\newcommand{\bl}{0.5}
\newcommand{\block}[3]{%
\begin{minipage}[c]{\bl\textwidth}\raggedright{\Large\bfseries #1\par}\medskip #2\end{minipage}\hfill
\begin{minipage}[c]{\dimexpr0.97\textwidth-\bl\textwidth\relax}\centering #3\end{minipage}\par}
"""
LUECKE = r"""{\Large\bfseries Aufgaben im Heft\par}
\medskip
Buch S.\,\rule{1.5cm}{0.4pt} Nr.\,\rule{5cm}{0.4pt}
"""
files = {}

# ---------- Stufenwinkel und Wechselwinkel ----------
files['ab-stufenwinkel-wechselwinkel'] = PRE + r"""
% Die Tabelle beim Wechselwinkel braucht etwas mehr Breite.
\renewcommand{\bl}{0.58}
% Zwei Parallelen g und h, geschnitten von f. Winkelflächen werden als Argument übergeben.
\newcommand{\parfig}[1]{%
\begin{tikzpicture}[scale=1.4]
  \coordinate (G) at (0.866,1.5); \coordinate (H) at (-0.866,-1.5);
  #1
  \draw[thick] (-2.1,1.5) -- (2.1,1.5) node[right] {$g$};
  \draw[thick] (-2.1,-1.5) -- (2.1,-1.5) node[right] {$h$};
  \draw[thick] (-1.5,-2.6) -- (1.5,2.6) node[above right] {$f$};
\end{tikzpicture}}
\newcommand{\wk}[5]{\fill[#4] (#1) -- ++(#2:0.6) arc (#2:#3:0.6) -- cycle; \node at ([shift={({(#2+#3)/2}:0.98)}]#1) {\large$#5$};}

\begin{document}

{\LARGE\bfseries Stufenwinkel und Wechselwinkel\par}
\vspace{0.9cm}

\block{Stufenwinkel}{%
Die Gerade $f$ schneidet die Parallelen $g$ und $h$. Stufenwinkel liegen an beiden Kreuzungen an der gleichen Stelle. Sie sind gleich groß.
\[\alpha_1 = \alpha_2\]
Umgekehrt: Sind Stufenwinkel gleich groß, dann sind $g$ und $h$ parallel.}{%
\parfig{\wk{G}{0}{60}{gray!40}{\alpha_1}\wk{H}{0}{60}{gray!40}{\alpha_2}}}

\vspace{1cm}

\block{Wechselwinkel}{%
Wechselwinkel liegen auf verschiedenen Seiten von $f$ und an verschiedenen Parallelen. Sie sind gleich groß.
\[\alpha_1 = \gamma_2\]
Kennst du einen Winkel, kannst du alle acht angeben.\par\medskip
Beispiel: $\alpha_1 = 60^\circ$\par\smallskip
\begin{tabular}{@{}ll@{}}
$\gamma_1 = 60^\circ$ & Scheitelwinkel zu $\alpha_1$\\[2pt]
$\alpha_2 = 60^\circ$ & Stufenwinkel zu $\alpha_1$\\[2pt]
$\gamma_2 = 60^\circ$ & Wechselwinkel zu $\alpha_1$\\[2pt]
$\beta_1 = 180^\circ - 60^\circ = 120^\circ$ & Nebenwinkel zu $\alpha_1$
\end{tabular}}{%
\parfig{\wk{G}{0}{60}{gray!40}{\alpha_1}\wk{G}{180}{240}{gray!20}{\gamma_1}\wk{G}{60}{180}{pattern=north east lines, pattern color=gray}{\beta_1}\wk{H}{0}{60}{gray!20}{\alpha_2}\wk{H}{180}{240}{gray!40}{\gamma_2}}}

\vspace{1cm}

{\Large\bfseries Aufgaben im Heft\par}
\medskip
Buch S.\,49 Nr.\,6, 7, 8, 9, 10, 11\par\smallskip
Buch S.\,50 Nr.\,7, 8, 9, 10, 11

\kaestchen
\end{document}
"""

# ---------- Winkelsumme ----------
files['ab-winkelsumme'] = PRE + r"""
\renewcommand{\bl}{0.47}
\begin{document}

{\LARGE\bfseries Winkelsumme im Dreieck und Viereck\par}
\vspace{0.9cm}

\block{Dreieck}{%
Die drei Innenwinkel eines Dreiecks sind zusammen $180^\circ$ groß.
\[
\begin{array}{r@{\;=\;}l@{\quad}l}
\alpha + \beta + \gamma & 180^\circ & \mid -\alpha - \beta\\[2pt]
\gamma & \rlap{$180^\circ - \alpha - \beta$} &
\end{array}
\]
Beispiel: $\alpha = 50^\circ$, $\beta = 60^\circ$\par\smallskip
$\gamma = 180^\circ - 50^\circ - 60^\circ = 70^\circ$}{%
\begin{tikzpicture}[scale=2.1]
  \coordinate (A) at (0,0); \coordinate (B) at (4,0); \coordinate (C) at (2.369,2.824);
  \pic[fill=gray!20, angle radius=1.0cm, "\large$\alpha$", angle eccentricity=1.6] {angle=B--A--C};
  \pic[fill=gray!35, angle radius=1.0cm, "\large$\beta$", angle eccentricity=1.6] {angle=C--B--A};
  \pic[fill=gray!55, angle radius=1.0cm, "\large$\gamma$", angle eccentricity=1.6] {angle=A--C--B};
  \draw[thick] (A) -- (B) -- (C) -- cycle;
\end{tikzpicture}}

\vspace{1cm}

\block{Viereck}{%
Die vier Innenwinkel eines Vierecks sind zusammen $360^\circ$ groß. Eine Diagonale teilt das Viereck in zwei Dreiecke: $2 \cdot 180^\circ = 360^\circ$.
\[
\begin{array}{r@{\;=\;}l@{\quad}l}
\alpha + \beta + \gamma + \delta & 360^\circ & \mid -\alpha - \beta - \gamma\\[2pt]
\delta & \rlap{$360^\circ - \alpha - \beta - \gamma$} &
\end{array}
\]
Beispiel: $\alpha = 80^\circ$, $\beta = 100^\circ$, $\gamma = 70^\circ$\par\smallskip
$\delta = 360^\circ - 80^\circ - 100^\circ - 70^\circ = 110^\circ$}{%
\begin{tikzpicture}[scale=1.8]
  \coordinate (A) at (0,0); \coordinate (B) at (4,0); \coordinate (C) at (4.562,3.190); \coordinate (D) at (0.434,2.462);
  \pic[fill=gray!20, angle radius=0.9cm, "\large$\alpha$", angle eccentricity=1.6] {angle=B--A--D};
  \pic[fill=gray!35, angle radius=0.9cm, "\large$\beta$", angle eccentricity=1.6] {angle=C--B--A};
  \pic[fill=gray!55, angle radius=0.9cm, "\large$\gamma$", angle eccentricity=1.6] {angle=D--C--B};
  \pic[pattern=north east lines, pattern color=gray, angle radius=0.9cm, "\large$\delta$", angle eccentricity=1.6] {angle=A--D--C};
  \draw[thick, dashed, gray] (A) -- (C);
  \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
\end{tikzpicture}}

\vspace{1cm}

{\Large\bfseries Aufgaben im Heft\par}
\medskip
Buch S.\,65 Nr.\,1, 2, 3\par\smallskip
Buch S.\,66 Nr.\,1, 2, 3, 4\par\smallskip
Buch S.\,67 Nr.\,1, 2, 3, 4, 5
\kaestchen
\end{document}
"""

# ---------- Mittelsenkrechte und Winkelhalbierende ----------
files['ab-mittelsenkrechte-winkelhalbierende'] = PRE + r"""
\renewcommand{\bl}{0.46}
\begin{document}

{\LARGE\bfseries Mittelsenkrechte und Winkelhalbierende\par}
\vspace{0.9cm}

\block{Mittelsenkrechte}{%
Jeder Punkt auf der Mittelsenkrechten von $AB$ ist von $A$ und $B$ gleich weit entfernt. Sie geht durch die Mitte $M$ von $AB$ und steht senkrecht auf $AB$.\par\medskip
\begin{tabular}{@{}l@{\ }>{\raggedright\arraybackslash}p{0.88\linewidth}@{}}
1. & Kreis um $A$, Radius mehr als die halbe Strecke\\
2. & Kreis um $B$ mit gleichem Radius\\
3. & Gerade durch die beiden Schnittpunkte
\end{tabular}\par\medskip
Mit dem Geodreieck: Mitte von $AB$ messen, Senkrechte durch $M$ zeichnen.}{%
\begin{tikzpicture}[scale=2.4]
  \draw[gray, thick, dashed] (25:2) arc (25:57:2); \draw[gray, thick, dashed] (-25:2) arc (-25:-57:2);
  \draw[gray, thick, dashed] ([shift={(3,0)}]155:2) arc (155:123:2); \draw[gray, thick, dashed] ([shift={(3,0)}]205:2) arc (205:237:2);
  \draw[very thick] (1.5,-1.9) -- (1.5,1.9);
  \draw (1.75,0) arc (0:90:0.25); \fill (1.5,0) ++(45:0.11) circle (1pt);
  \draw[thick] (0,0) -- (3,0);
  \fill (0,0) circle (1.6pt) node[left] {$A$}; \fill (3,0) circle (1.6pt) node[right] {$B$}; \fill (1.5,0) circle (1.6pt) node[below right] {$M$};
\end{tikzpicture}}

\vspace{1cm}

\block{Winkelhalbierende}{%
Jeder Punkt auf der Winkelhalbierenden ist von beiden Schenkeln gleich weit entfernt. Sie teilt den Winkel in zwei gleich große Teile.\par\medskip
\begin{tabular}{@{}l@{\ }>{\raggedright\arraybackslash}p{0.88\linewidth}@{}}
1. & Kreis um $S$, er schneidet beide Schenkel\\
2. & Um beide Schnittpunkte je ein Kreis mit gleichem Radius\\
3. & Gerade von $S$ durch den neuen Schnittpunkt
\end{tabular}\par\medskip
Mit dem Geodreieck: Winkel messen, halbieren, Hälfte antragen.}{%
\begin{tikzpicture}[scale=2.0]
  \draw[gray, thick, dashed] (-8:1.5) arc (-8:78:1.5);
  \draw[gray, thick, dashed] ([shift={(1.5,0)}]55:1.5) arc (55:85:1.5);
  \draw[gray, thick, dashed] ([shift={(0.513,1.410)}]-15:1.5) arc (-15:15:1.5);
  \draw[very thick] (0,0) -- (35:3.6);
  \draw[thick] (0,0) -- (4,0); \draw[thick] (0,0) -- (70:3.3);
  \fill (0,0) circle (1.6pt) node[left] {$S$};
  \node at (17.5:1.12) {$35^\circ$}; \node at (52.5:1.12) {$35^\circ$};
\end{tikzpicture}}

\vspace{1cm}

""" + LUECKE + r"""
\kaestchen
\end{document}
"""

# ---------- Umkreis und Inkreis ----------
files['ab-umkreis-inkreis'] = PRE + r"""
\renewcommand{\bl}{0.46}
\begin{document}

{\LARGE\bfseries Umkreis und Inkreis\par}
\vspace{0.9cm}

\block{Umkreis}{%
Der Umkreis geht durch alle drei Ecken. Sein Mittelpunkt $U$ ist der Schnittpunkt der Mittelsenkrechten. $U$ ist von allen Ecken gleich weit entfernt.\par\medskip
\begin{tabular}{@{}l@{\ }>{\raggedright\arraybackslash}p{0.88\linewidth}@{}}
1. & Mittelsenkrechten von zwei Seiten zeichnen\\
2. & Ihr Schnittpunkt ist $U$\\
3. & Kreis um $U$ durch eine Ecke
\end{tabular}\par\medskip
Hat das Dreieck einen stumpfen Winkel, liegt $U$ außerhalb.}{%
\begin{tikzpicture}[scale=1.4]
  \coordinate (A) at (0,0); \coordinate (B) at (5,0); \coordinate (C) at (1.8,3.2); \coordinate (U) at (2.5,0.7);
  \draw[very thick] (U) circle (2.596);
  \draw[gray, thick] (2.5,-2.2) -- (2.5,3.4);
  \draw[gray, thick] (3.4,1.6) ++(-2.2,-2.2) -- ++(4.4,4.4);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \fill (U) circle (2pt) node[below right] {$U$};
  \node[below left] at (A) {$A$}; \node[below right] at (B) {$B$}; \node[above] at (C) {$C$};
\end{tikzpicture}}

\vspace{1cm}

\block{Inkreis}{%
Der Inkreis berührt alle drei Seiten. Sein Mittelpunkt $W$ ist der Schnittpunkt der Winkelhalbierenden. $W$ ist von allen Seiten gleich weit entfernt.\par\medskip
\begin{tabular}{@{}l@{\ }>{\raggedright\arraybackslash}p{0.88\linewidth}@{}}
1. & Winkelhalbierende von zwei Winkeln zeichnen\\
2. & Ihr Schnittpunkt ist $W$\\
3. & Senkrechte von $W$ auf eine Seite: das ist der Radius\\
4. & Kreis um $W$
\end{tabular}\par\medskip
Der Radius reicht bis zur Seite, nicht bis zur Ecke.}{%
\begin{tikzpicture}[scale=1.4]
  \coordinate (A) at (0,0); \coordinate (B) at (5,0); \coordinate (C) at (1.8,3.2); \coordinate (W) at (2.073,1.212);
  \draw[very thick] (W) circle (1.212);
  \draw[gray, thick] (A) -- (30.32:3.3);
  \draw[gray, thick] (B) -- ++(157.5:3.6);
  \draw[thick] (W) -- (2.073,0);
  \draw (2.073,0) ++(0.23,0) arc (0:90:0.23); \fill (2.073,0) ++(45:0.1) circle (1pt);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \fill (W) circle (2pt) node[above right] {$W$};
  \node[below left] at (A) {$A$}; \node[below right] at (B) {$B$}; \node[above] at (C) {$C$};
\end{tikzpicture}}

\vspace{1cm}

""" + LUECKE + r"""
\kaestchen
\end{document}
"""

# ---------- Dreiecke konstruieren ----------
files['ab-dreiecke-konstruieren'] = PRE + r"""
\renewcommand{\bl}{0.48}
\newcommand{\basis}{\draw[thick] (0,0) -- (6,0); \fill (0,0) circle (2.5pt) node[below left] {$A$}; \fill (6,0) circle (2.5pt) node[below right] {$B$}; \node[below] at (3,0) {$c$};}
\begin{document}

{\LARGE\bfseries Dreiecke konstruieren\par}
\medskip
Ein Dreieck ist eindeutig festgelegt durch:
\vspace{0.6cm}

\block{SSS: drei Seiten}{%
Beispiel: $c = 6$\,cm, $b = 4$\,cm, $a = 5$\,cm\par\smallskip
\begin{tabular}{@{}l@{\ }>{\raggedright\arraybackslash}p{0.88\linewidth}@{}}
1. & Seite $c$ zeichnen\\
2. & Kreis um $A$ mit Radius $b$\\
3. & Kreis um $B$ mit Radius $a$\\
4. & Der Schnittpunkt ist $C$
\end{tabular}}{%
\begin{tikzpicture}[scale=1.15]
  \draw[gray, thick, dashed] (42:4) arc (42:70:4);
  \draw[gray, thick, dashed] ([shift={(6,0)}]125:5) arc (125:152:5);
  \draw[thick] (0,0) -- (2.25,3.307) -- (6,0);
  \basis
  \fill (2.25,3.307) circle (2.5pt) node[above] {$C$};
  \node[left] at (1.1,1.8) {$b$}; \node[right] at (4.2,1.8) {$a$};
\end{tikzpicture}}

\vspace{1cm}

\block{SWS: zwei Seiten und der Winkel dazwischen}{%
Beispiel: $c = 6$\,cm, $\alpha = 50^\circ$, $b = 4$\,cm\par\smallskip
\begin{tabular}{@{}l@{\ }>{\raggedright\arraybackslash}p{0.88\linewidth}@{}}
1. & Seite $c$ zeichnen\\
2. & Winkel $\alpha$ in $A$ antragen\\
3. & Auf dem Schenkel $b$ abtragen: das ist $C$\\
4. & $C$ mit $B$ verbinden
\end{tabular}}{%
\begin{tikzpicture}[scale=1.15]
  \fill[gray!35] (0,0) -- (1,0) arc (0:50:1) -- cycle; \node at (25:1.6) {$\alpha$};
  \draw[thin] (0,0) -- (50:5.4);
  \draw[gray, thick, dashed] (44:4) arc (44:56:4);
  \draw[thick] (0,0) -- (2.571,3.064) -- (6,0);
  \basis
  \fill (2.571,3.064) circle (2.5pt) node[above right] {$C$};
  \node[left] at (1.1,1.8) {$b$};
\end{tikzpicture}}

\vspace{1cm}

\block{WSW: eine Seite und die beiden Winkel daran}{%
Beispiel: $c = 6$\,cm, $\alpha = 50^\circ$, $\beta = 60^\circ$\par\smallskip
\begin{tabular}{@{}l@{\ }>{\raggedright\arraybackslash}p{0.88\linewidth}@{}}
1. & Seite $c$ zeichnen\\
2. & Winkel $\alpha$ in $A$ antragen\\
3. & Winkel $\beta$ in $B$ antragen\\
4. & Die Schenkel schneiden sich in $C$
\end{tabular}}{%
\begin{tikzpicture}[scale=1.15]
  \fill[gray!35] (0,0) -- (1,0) arc (0:50:1) -- cycle; \node at (25:1.6) {$\alpha$};
  \fill[gray!35] (6,0) -- ++(180:1) arc (180:120:1) -- cycle; \node at ([shift={(6,0)}]150:1.6) {$\beta$};
  \draw[thin] (0,0) -- (50:6.3); \draw[thin] (6,0) -- ++(120:5.6);
  \draw[thick] (0,0) -- (3.555,4.236) -- (6,0);
  \basis
  \fill (3.555,4.236) circle (2.5pt) node[above] {$C$};
\end{tikzpicture}}

\vspace{1cm}

""" + LUECKE + r"""
\kaestchen
\end{document}
"""

# ---------- Wiederholung ----------
# ab-winkel-zeichnen ist ein eigenes Dokument (Nachbau der Vorlagen), siehe ab-winkel-zeichnen.tex, mit xelatex

files['ab-wiederholung'] = PRE + r"""
\renewcommand{\bl}{0.55}
\usepackage{enumitem}
\setlist[enumerate]{nosep,leftmargin=1.5em}
\begin{document}

{\LARGE\bfseries Wiederholung\par}
\vspace{0.3cm}

\block{Parallel und senkrecht}{%
Parallele Geraden haben überall den gleichen Abstand und schneiden sich nie: $f \parallel g$\par\medskip
Senkrechte Geraden bilden einen rechten Winkel: $f \perp h$}{%
\begin{tikzpicture}[scale=0.85]
  \draw[thick] (-2.2,0.8) -- (2.2,0.8) node[right] {$f$};
  \draw[thick] (-2.2,-0.8) -- (2.2,-0.8) node[right] {$g$};
  \draw[very thick, gray] (-0.8,-1.6) -- (-0.8,1.7) node[above] {$h$};
  \draw (-0.8,0.8) rectangle (-0.5,1.1);
\end{tikzpicture}}

\vspace{0.3cm}

\block{Teile eines Winkels}{%
Ein Winkel hat einen Scheitelpunkt $S$, zwei Schenkel und einen Winkelbogen. Man benennt ihn mit einem griechischen Buchstaben: $\alpha$ (Alpha), $\beta$ (Beta), $\gamma$ (Gamma), $\delta$ (Delta).}{%
\begin{tikzpicture}[scale=0.85]
  \coordinate (S) at (0,0); \coordinate (A) at (3.4,0); \coordinate (B) at (50:3.2);
  \pic[fill=gray!30, draw=black, thick, angle radius=0.9cm, "\large$\alpha$", angle eccentricity=0.6] {angle=A--S--B};
  \draw[thick] (S) -- (A) node[below left] {Schenkel};
  \draw[thick] (S) -- (B) node[left=4pt] {Schenkel};
  \fill (S) circle (2.5pt) node[below] {$S$};
  \node[right] at (25:1.05) {Winkelbogen};
\end{tikzpicture}}

\vspace{0.3cm}

{\Large\bfseries Winkelarten\par}
\medskip
\newcommand{\wa}[1]{\begin{tikzpicture}[scale=0.42]\fill[gray!35] (0,0) -- (0:0.9) arc (0:#1:0.9) -- cycle;\draw[thick] (1.6,0) -- (0,0) -- (#1:1.6);\fill (0,0) circle (2pt);\end{tikzpicture}}
\begin{tabular}{@{}*{4}{>{\centering\arraybackslash}p{3.85cm}}@{}}
\wa{50} & \begin{tikzpicture}[scale=0.42]\draw (0.62,0) arc (0:90:0.62); \fill (45:0.27) circle (1.6pt);\draw[thick] (1.6,0) -- (0,0) -- (0,1.6);\fill (0,0) circle (2pt);\end{tikzpicture} & \wa{130} & \wa{250}\\
spitz & rechter Winkel & stumpf & überstumpf\\
$0^\circ<\alpha<90^\circ$ & $\alpha = 90^\circ$ & $90^\circ<\alpha<180^\circ$ & $180^\circ<\alpha<360^\circ$
\end{tabular}

\vspace{0.3cm}

\block{Winkel messen}{%
\begin{enumerate}
\item Nullpunkt des Geodreiecks auf den Scheitelpunkt.
\item 0-Linie auf einen Schenkel. Zu kurze Schenkel vorher verlängern.
\item Auf der Skala ablesen, die an diesem Schenkel bei $0^\circ$ beginnt. Mit der Winkelart prüfen.
\end{enumerate}}{%
\begin{tikzpicture}[scale=0.9]
  \fill[gray!8] (2.2,0) arc (0:180:2.2) -- cycle; \draw[gray] (2.2,0) arc (0:180:2.2) -- cycle;
  \foreach \a in {0,10,...,180} \draw[gray] (\a:2.2) -- (\a:2.02);
  \foreach \a in {0,30,...,180} \node[font=\scriptsize] at (\a:1.8) {\a};
  \foreach \a/\b in {0/180,30/150,60/120,90/90,120/60,150/30,180/0} \node[gray, font=\tiny] at (\a:1.45) {\b};
  \fill[gray!35] (0,0) -- (0:0.6) arc (0:50:0.6) -- cycle;
  \draw[thick] (0,0) -- (2.8,0); \draw[thick] (0,0) -- (50:1.2); \draw[thick, dashed, gray] (50:1.2) -- (50:2.7);
  \node[font=\bfseries] at (50:2.6) {$50^\circ$};
\end{tikzpicture}}

\vspace{0.3cm}

\block{Winkel zeichnen}{%
\begin{enumerate}
\item Einen Schenkel zeichnen, Scheitelpunkt $S$ markieren.
\item Geodreieck anlegen: Nullpunkt auf $S$, 0-Linie auf den Schenkel.
\item Bei der Gradzahl einen Punkt markieren. Richtige Skala!
\item $S$ mit dem Punkt verbinden, Winkelbogen zeichnen, beschriften.
\end{enumerate}}{%
\begin{tikzpicture}[scale=0.9]
  \coordinate (S) at (0,0); \coordinate (A) at (3.2,0); \coordinate (B) at (40:3);
  \draw[thick] (S) -- (A); \draw[thick] (S) -- (B);
  \pic[fill=gray!30, draw=black, thick, angle radius=0.9cm, "$40^\circ$", angle eccentricity=1.55] {angle=A--S--B};
  \fill (0,0) circle (2.5pt) node[below] {$S$};
  \fill (40:2.4) circle (2.5pt);
\end{tikzpicture}}

\vspace{0.3cm}

{\Large\bfseries Aufgaben im Heft\par}
\medskip
Buch S.\,225 Nr.\,74 \qquad S.\,232 Nr.\,92, 93, 94 \qquad S.\,233 Nr.\,95, 96
\kaestchen
\end{document}
"""

for name, src in files.items():
    open(name + '.tex', 'w', encoding='utf8').write(src)
print(list(files))
