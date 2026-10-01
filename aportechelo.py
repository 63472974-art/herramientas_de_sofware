```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flores Amarillas 🌻</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            height: 100vh;
            overflow: hidden;
            background: linear-gradient(to bottom, #0b1026, #172554);
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
        }

        .mensaje {
            position: absolute;
            top: 40px;
            color: #ffd700;
            font-size: 35px;
            text-align: center;
            text-shadow: 0 0 15px #ffd700;
            z-index: 10;
        }

        .jardin {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 70%;
        }

        .flor {
            position: absolute;
            bottom: 0;
            width: 20px;
            height: 250px;
        }

        .tallo {
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 8px;
            height: 200px;
            background: linear-gradient(to right, #176b36, #36a852);
            border-radius: 10px;
            transform: translateX(-50%);
        }

        .hoja {
            position: absolute;
            width: 60px;
            height: 25px;
            background: #299447;
            border-radius: 100% 0 100% 0;
        }

        .hoja.izquierda {
            left: -40px;
            bottom: 80px;
            transform: rotate(-25deg);
        }

        .hoja.derecha {
            right: -40px;
            bottom: 120px;
            transform: rotate(25deg) scaleX(-1);
        }

        .cabeza {
            position: absolute;
            top: -20px;
            left: 50%;
            width: 120px;
            height: 120px;
            transform: translateX(-50%);
        }

        .petalo {
            position: absolute;
            width: 45px;
            height: 70px;
            background: #ffd700;
            border-radius: 50%;
            left: 38px;
            top: 25px;
            transform-origin: center bottom;
            box-shadow: 0 0 10px #ffc400;
        }

        .petalo:nth-child(1)  { transform: rotate(0deg) translateY(-35px); }
        .petalo:nth-child(2)  { transform: rotate(45deg) translateY(-35px); }
        .petalo:nth-child(3)  { transform: rotate(90deg) translateY(-35px); }
        .petalo:nth-child(4)  { transform: rotate(135deg) translateY(-35px); }
        .petalo:nth-child(5)  { transform: rotate(180deg) translateY(-35px); }
        .petalo:nth-child(6)  { transform: rotate(225deg) translateY(-35px); }
        .petalo:nth-child(7)  { transform: rotate(270deg) translateY(-35px); }
        .petalo:nth-child(8)  { transform: rotate(315deg) translateY(-35px); }

        .centro {
            position: absolute;
            width: 45px;
            height: 45px;
            background: #8b4513;
            border-radius: 50%;
            top: 38px;
            left: 38px;
            z-index: 2;
            box-shadow: 0 0 15px #5c2e0b;
        }

        .flor:nth-child(1) {
            left: 15%;
            transform: scale(.8);
        }

        .flor:nth-child(2) {
            left: 35%;
            transform: scale(1.1);
        }

        .flor:nth-child(3) {
            left: 55%;
            transform: scale(.7);
        }

        .flor:nth-child(4) {
            left: 75%;
            transform: scale(.9);
        }

        .flor {
            animation: mover 3s ease-in-out infinite alternate;
        }

        @keyframes mover {
            from {
                transform: rotate(-2deg);
            }
            to {
                transform: rotate(2deg);
            }
        }

        .brillo {
            position: absolute;
            width: 8px;
            height: 8px;
            background: #fff;
            border-radius: 50%;
            box-shadow: 0 0 15px #fff;
            animation: subir 5s linear infinite;
        }

        @keyframes subir {
            0% {
                bottom: -20px;
                opacity: 0;
            }

            30% {
                opacity: 1;
            }

            100% {
                bottom: 100%;
                opacity: 0;
            }
        }
    </style>
</head>

<body>

    <div class="mensaje">
        🌻 Flores Amarillas 🌻
    </div>

    <div class="jardin">

        <div class="flor">
            <div class="tallo"></div>
            <div class="hoja izquierda"></div>
            <div class="hoja derecha"></div>

            <div class="cabeza">
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="centro"></div>
            </div>
        </div>

        <div class="flor">
            <div class="tallo"></div>
            <div class="hoja izquierda"></div>
            <div class="hoja derecha"></div>

            <div class="cabeza">
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="centro"></div>
            </div>
        </div>

        <div class="flor">
            <div class="tallo"></div>
            <div class="hoja izquierda"></div>
            <div class="hoja derecha"></div>

            <div class="cabeza">
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="centro"></div>
            </div>
        </div>

        <div class="flor">
            <div class="tallo"></div>
            <div class="hoja izquierda"></div>
            <div class="hoja derecha"></div>

            <div class="cabeza">
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="petalo"></div>
                <div class="centro"></div>
            </div>
        </div>

    </div>

    <script>
        // Crear pequeñas luces flotantes
        function crearBrillo() {
            const brillo = document.createElement("div");
            brillo.classList.add("brillo");

            brillo.style.left = Math.random() * 100 + "%";
            brillo.style.animationDuration =
                (3 + Math.random() * 5) + "s";

            document.body.appendChild(brillo);

            setTimeout(() => {
                brillo.remove();
            }, 8000);
        }

        setInterval(crearBrillo, 400);
    </script>

</body>
</html>
```
