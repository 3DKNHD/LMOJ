# Pack de problemas LMOJ

Este directorio es el pack. Puedes versionarlo en un repo de GitHub aparte y
bajarlo en el juez con **Sync**.

## Qué ve el usuario

- `statement.md` y `samples/*.in|*.out` — públicos
- `meta.json` — límites y puntos

## Qué no debe copiar

- `secret/gen.py` — generador **único de este problema**
- `secret/sol.cpp` (o `sol.py`) — solución oficial, produce las salidas ocultas
- `secret/checker.py` — opcional

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

1. Repo GitHub cuya raíz sea este pack (una carpeta por problema).
2. En LMOJ: Sync → pega la URL `https://github.com/USUARIO/REPO.git`.
3. Cuando agregues problemas, `git push` y en el PC del juez dale otra vez a Sync.
