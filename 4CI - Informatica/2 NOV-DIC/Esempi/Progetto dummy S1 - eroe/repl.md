# Sessione REPL - trascrizione

Esempio per S1: la REPL risponde subito a ogni riga. Le righe che iniziano con `>>>` sono quelle scritte; le altre sono la risposta di Python.

```python
>>> 2 + 2
4
>>> "ciao" * 3
'ciaociaociao'
>>> 7 / 2
3.5
>>> 7 // 2
3
>>> type(5)
<class 'int'>
>>> x = 10
>>> x + 5
15
>>> x = "dieci"
>>> x + 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int("17") + 3
20
>>> "17" + "3"
'173'
>>> True + 1
2
```

**Da prevedere prima di eseguire** (PRIMM):

- `"17" + "3"` dà `20` o `'173'`?
- Dopo `x = "dieci"`, che cosa succede con `x + 5`?
