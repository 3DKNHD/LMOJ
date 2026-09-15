# Pack de problemas LMOJ

Este directorio es el pack: vive en el mismo repo que el juez.
**Sync** hace `git pull` del `origin` de este clone. Problemas nuevos
llegan con enunciado, samples, `secret/` **y** `editorial.md`.

## Qué ve el usuario (en la web)

- `statement.md` y `samples/*.in|*.out` — públicos
- `editorial.md` — tutorial (el juez lo muestra en /editorial)
- `meta.json` — límites y puntos

## Qué no muestra la web (sí está en el git)

- `secret/gen.py` — generador **único de este problema**
- `secret/sol.cpp` (o `sol.py`) — solución oficial, produce las salidas ocultas
- `secret/checker.py` — opcional

El juez necesita esos archivos para generar casos. Quien clone el repo
puede abrirlos en disco; la GUI no los sirve. No subas tokens, envíos
de usuarios ni `data/` / `workspace/`.

No pongas casos ocultos como `.in` en el repo. El juez llama `generate()` y
cachea los tests fuera de `problems/` (`data/cache/`).

## meta.json

```json
{
  "code": "aplusb",
  "name": "A más B",
  "points": 1,
  "timeLimit": 1.0,
  "memoryLimit": 256,
  "tags": ["implementación"],
  "partial": false
}
```

## gen.py

```python
def generate():
    yield "bordes", "1 2\n"
    yield "max", "...\n"
```

Cada `yield` es un caso oculto. Nombres distintos. Nada de un generador genérico
copiado de otro problema: ataca los bordes de **este** enunciado.

## Publicar actualizaciones

1. Agrega la carpeta del problema (con `editorial.md` si hay tutorial).
2. `git push` al origin de este repo.
3. En cada máquina: **Sync** o `./lmoj sync`.
