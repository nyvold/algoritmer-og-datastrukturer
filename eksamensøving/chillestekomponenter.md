egen oppgave:
chilleste komponenter:
filmer har en rating, lag komponentgrafen til følgende graf og finn chilleste komponenten. altså komponenten med best rating:

graf G: noder med rating er filmnoder og noder uten rating er actornoder
D: M, E, T
M(6): D, E
E: M, T, A
T(8): D, E
A(8): E, S, G
G: A, B
B(7): G, C
C: B, H, P
H(5): C, O
O: H, P, Y
Y(9): O, S
S: Y, A
P(10): O, C


kosarjus for å finne komponenter:
gjør dfs på grafen også dfs på reverserte grafen med stack fra første dfs

stack: y, o, h, p, c, b, g, s, a, e, t, d, m
priqueue: 
visited: d, t, e, a, g, b, c, h, o, y, p, s, m

stack: y, o, h, p, c, b, g, s, a, e, t, d, m


ny graf:
D: T, M
M: D
T: E
E: M, A
A: S
S: Y
Y: 
O: Y, H, P
H: 
C: H, P
P: 
C: H, P
B: C, G
G: A, B

jeg vil finne de chilleste komponentene til denne grafen.
for å jgøre det må jeg finne alle sterkt sammenhengende komponenter og se hvilken som er billigst.

Egen algoritme:
starte der det er intuitivt, 


visited: D, T, M, E, A, S, Y, O, H, P, C, B, G
SCC:(DMTE), (A), (S), (Y), (OH), (P), (C), (BG)
D: G(M, T, E, A, S, Y) Gr(M, E, T) union av disse blir (M, T, E) og dette er en SCC
A: G(S, Y) Gr(E, T, D, M, G, B) union av disse blir ingenting, så A er en SCC
S: Gr(A, E, T, D, M, G, B) G(Y) union av disse blir ingenting, så S er en SCC
Y: når ingenting, Y er egen SCC
O: G(Y, H, P) Gr(H, C, B, G), union av disse blir (H), så OH blir SCC
P: når ingenting, P blir egen SCC
C: G(P, H, O, Y) Gr(B, G), når ingenting, C er egne SCC
B: G(, GC, P, H, O, Y) Gr(G), union av disse blir, BG, dette er SCC
G: G(B, C, P, H, O, Y) Gr(B)

så for å finne chilleste komponent av disse sterkt sammenhengende komponentene jeg har funnet.
SCC:(DMTE), (A), (S), (Y), (OH), (P), (C), (BG)
costSCC: {(DMTE):28, (A):, (S), (Y), (OH), (P), (C), (BG)}
