
# O Bozolan'ie

Kompilator Bozolan konwertuje kod w języku Bozolan w kod pythona:

- Input:
```
{
    funkcja factorial(a) {
        jezeli (a<2) {
            zwroc a;p
        }
        zwroc a*factorial(a-1);p
    }

    wypisz factorial(4);p
}
```

- Output:
```python
def factorial(a):
    if (a)<(2) :
        return a

    return a*factorial(a-1)

print(factorial(4))
```# Bozolan
