# EJERCICIOS DE REFUERZO: CLASE 1 (LOGARITMOS Y POTENCIAS)
> **Alumno:** Alumno 1  
> **Contenido:** Práctica directa de los fundamentos de logaritmos y potencias.

---

## BLOQUE 1: CÁLCULO MENTAL DIRECTO
*Recuerda la pregunta clave de la clase: **"¿A qué número tengo que elevar la base para que me dé el número de dentro?"***

Calcula mentalmente:
1. $\log_2(16) =$
2. $\log_3(81) =$
3. $\log_5(125) =$
4. $\log_{10}(10000) =$
5. $\log_7(7) =$
6. $\log_4(1) =$

---

## BLOQUE 2: FRACCIONES Y RAÍCES EN EL ARGUMENTO
*Como los que hicimos en la pizarra con $\frac{1}{16}$ y $\sqrt[5]{27}$: el denominador pasa como potencia negativa y las raíces pasan como potencias fraccionarias $\sqrt[n]{A^m} = A^{m/n}$.*

Calcula el valor exacto:
7. $\log_2\left(\frac{1}{32}\right)$
8. $\log_3\left(\frac{1}{9}\right)$
9. $\log_5\left(\frac{1}{125}\right)$
10. $\log_3(\sqrt{27})$
11. $\log_2(\sqrt[3]{16})$
12. $\log_7(\sqrt[5]{49})$

---

## BLOQUE 3: CUANDO LA RAÍZ ESTÁ EN LA BASE
*Como el ejercicio de clase con $\log_{\sqrt{2}}(8)$: plantea la ecuación igualando las potencias $(\sqrt{b})^x = A$.*

13. $\log_{\sqrt{2}}(16)$
14. $\log_{\sqrt{3}}(9)$
15. $\log_{\sqrt{5}}(25)$
16. $\log_{\sqrt{2}}(\sqrt{8})$

---

## BLOQUE 4: PROPIEDADES Y LA TRAMPA DEL EXAMEN

17. Sabiendo que conocemos $\log 2$ y $\log 3$, descompón en factores primos y expresa en función de $\log 2$ y $\log 3$:
    - a) $\log(18)$
    - b) $\log(24)$
    - c) $\log\left(\frac{8}{9}\right)$

18. **La trampa que vimos en clase (Hoja 4 y 5):**  
    Calcula por separado estas dos expresiones y explica por qué **NO** dan el mismo resultado:
    - a) $\log_2(64^2)$
    - b) $(\log_2 64)^2$

19. **Cambio de base:**  
    Escribe cómo meterías en la calculadora los siguientes logaritmos usando la tecla $\ln$ o $\log$:
    - a) $\log_3(10)$
    - b) $\log_7(50)$

---

## BLOQUE 5: ECUACIONES EXPONENCIALES CON RAÍCES
*Exactamente como el ejercicio final de clase: $2^{x+1} = 4\sqrt{2}$. Pon todo en la misma base sumando o restando los exponentes.*

20. $2^{x-1} = 8\sqrt{2}$
21. $3^{x+2} = 9\sqrt{3}$
22. $5^{2x} = 25\sqrt[3]{5}$
23. $2^x = \frac{4}{\sqrt{2}}$

---

# SOLUCIONARIO PASO A PASO

### Bloque 1: Cálculo mental
1. $\log_2(16) = \mathbf{4}$ (porque $2^4 = 16$).
2. $\log_3(81) = \mathbf{4}$ (porque $3^4 = 81$).
3. $\log_5(125) = \mathbf{3}$ (porque $5^3 = 125$).
4. $\log_{10}(10000) = \mathbf{4}$ (porque $10^4 = 10000$).
5. $\log_7(7) = \mathbf{1}$ (porque $7^1 = 7$).
6. $\log_4(1) = \mathbf{0}$ (porque $4^0 = 1$).

### Bloque 2: Fracciones y raíces
7. $\log_2\left(\frac{1}{32}\right) = \log_2(2^{-5}) = \mathbf{-5}$.
8. $\log_3\left(\frac{1}{9}\right) = \log_3(3^{-2}) = \mathbf{-2}$.
9. $\log_5\left(\frac{1}{125}\right) = \log_5(5^{-3}) = \mathbf{-3}$.
10. $\log_3(\sqrt{27}) = \log_3\left(\sqrt{3^3}\right) = \log_3(3^{3/2}) = \mathbf{\frac{3}{2}}$.
11. $\log_2(\sqrt[3]{16}) = \log_2\left(\sqrt[3]{2^4}\right) = \log_2(2^{4/3}) = \mathbf{\frac{4}{3}}$.
12. $\log_7(\sqrt[5]{49}) = \log_7\left(\sqrt[5]{7^2}\right) = \log_7(7^{2/5}) = \mathbf{\frac{2}{5}}$.

### Bloque 3: Base con raíz
13. $\log_{\sqrt{2}}(16) \implies (\sqrt{2})^x = 16 \implies (2^{1/2})^x = 2^4 \implies \frac{x}{2} = 4 \implies \mathbf{x = 8}$.
14. $\log_{\sqrt{3}}(9) \implies (3^{1/2})^x = 3^2 \implies \frac{x}{2} = 2 \implies \mathbf{x = 4}$.
15. $\log_{\sqrt{5}}(25) \implies (5^{1/2})^x = 5^2 \implies \frac{x}{2} = 2 \implies \mathbf{x = 4}$.
16. $\log_{\sqrt{2}}(\sqrt{8}) \implies (2^{1/2})^x = (2^3)^{1/2} = 2^{3/2} \implies \frac{x}{2} = \frac{3}{2} \implies \mathbf{x = 3}$.

### Bloque 4: Propiedades y trampa
17. 
   - a) $\log(18) = \log(2 \cdot 3^2) = \log 2 + \log(3^2) = \mathbf{\log 2 + 2\log 3}$.
   - b) $\log(24) = \log(2^3 \cdot 3) = \log(2^3) + \log 3 = \mathbf{3\log 2 + \log 3}$.
   - c) $\log\left(\frac{8}{9}\right) = \log(2^3) - \log(3^2) = \mathbf{3\log 2 - 2\log 3}$.
18. 
   - a) $\log_2(64^2) = 2 \cdot \log_2(64) = 2 \cdot 6 = \mathbf{12}$. *(El exponente afecta solo al 64, por lo que baja multiplicando delante).*
   - b) $(\log_2 64)^2 = (6)^2 = \mathbf{36}$. *(El exponente eleva a todo el resultado del logaritmo).*  
   **Conclusión:** $12 \neq 36$. No se puede aplicar la propiedad si el exponente eleva al logaritmo entero.
19. 
   - a) $\log_3(10) = \mathbf{\frac{\ln(10)}{\ln(3)}} \approx 2.096$
   - b) $\log_7(50) = \mathbf{\frac{\ln(50)}{\ln(7)}} \approx 2.010$

### Bloque 5: Ecuaciones exponenciales con raíces
20. $2^{x-1} = 8\sqrt{2} \implies 2^{x-1} = 2^3 \cdot 2^{1/2} = 2^{3 + 1/2} = 2^{7/2}$  
    $$x - 1 = \frac{7}{2} \implies x = \frac{7}{2} + 1 \implies \mathbf{x = \frac{9}{2} = 4.5}$$

21. $3^{x+2} = 9\sqrt{3} \implies 3^{x+2} = 3^2 \cdot 3^{1/2} = 3^{2 + 1/2} = 3^{5/2}$  
    $$x + 2 = \frac{5}{2} \implies x = \frac{5}{2} - 2 \implies \mathbf{x = \frac{1}{2} = 0.5}$$

22. $5^{2x} = 25\sqrt[3]{5} \implies 5^{2x} = 5^2 \cdot 5^{1/3} = 5^{2 + 1/3} = 5^{7/3}$  
    $$2x = \frac{7}{3} \implies \mathbf{x = \frac{7}{6}}$$

23. $2^x = \frac{4}{\sqrt{2}} \implies 2^x = \frac{2^2}{2^{1/2}} = 2^{2 - 1/2} = 2^{3/2}$  
    $$\mathbf{x = \frac{3}{2} = 1.5}$$
