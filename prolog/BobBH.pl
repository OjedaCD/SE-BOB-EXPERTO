%Base de hechos
es_problema(pantallaazul, pitidolargo).
es_problema(pantallaazul, sobrecalentamiento).
es_problema(pitidolargo, pitidocorto).
es_problema(sobrecalentamiento, temperaturacpualta).
es_problema(sobrecalentamiento, mensajeserror).
es_problema(temperaturacpualta, sedetiene).
es_problema(temperaturacpualta, mantenimiento).
es_problema(sedetiene, enciende).
es_problema(mensajeserror, reinicioscontinuos).

es_solucion(reinicioscontinuos, tecnico, no).
es_solucion(reinicioscontinuos, driversysoftware, si).
es_solucion(mantenimiento, suciedadypolvo, no).
es_solucion(mantenimiento, tecnico, si).
es_solucion(sedetiene, problemascpu, si).
es_solucion(mensajeserror, problemascpu, si).
es_solucion(pitidocorto, grafica, si).
es_solucion(pitidocorto, tecnico, no).
es_solucion(pitidolargo, ram, si).
es_solucion(enciende, cortocircuito,si).
es_solucion(enciende, fuentedepoder,no).
problema(P):- es_problema(P,H),writeln(H).

solucionsi(P):-es_solucion(P, R, si),writeln(R).
solucionno(P):-es_solucion(P, R, no),writeln(R).




