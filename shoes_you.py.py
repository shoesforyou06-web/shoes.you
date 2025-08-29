def generate_landing():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shoes_you - Байер одежды и обуви из Китая и Европы</title>
        <style>
            :root {
    --primary: #8A2432;    /* PANTONE 194 */
    --secondary: #3A6E8F;  /* PANTONE 548 */
    --accent1: #6A9A30;    /* PANTONE 563 */
    --accent2: #E6C35C;    /* PANTONE 585 */
    --light: #f8f9fa;
    --dark: #343a40;
}
            }
            
            * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Oswald', sans-serif;
    letter-spacing: 0.1px;
}
            
            body {
    background-color: #fff;
    color: var(--dark);
    line-height: 1.6;
    overflow-x: hidden;
    font-weight: 360;
}    
            /* Анимации */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(50px); }
    to { opacity: 1; transform: translateY(0); }
}


@keyframes slideInLeft {
    from { 
        opacity: 0; 
        transform: translateX(-100px) skewX(-15deg);
    }
    to { 
        opacity: 1; 
        transform: translateX(0) skewX(0);
    }
}

@keyframes slideInRight {
    from { 
        opacity: 0; 
        transform: translateX(100px) skewX(15deg);
    }
    to { 
        opacity: 1; 
        transform: translateX(0) skewX(0);
    }
}

@keyframes scaleIn {
    from { 
        opacity: 0; 
        transform: scale(0.8) rotate(-5deg);
    }
    to { 
        opacity: 1; 
        transform: scale(1) rotate(0);
    }
}

@keyframes bounceIn {
    0% { 
        opacity: 0; 
        transform: scale(0.3) translateY(100px);
    }
    50% { 
        opacity: 0.9; 
        transform: scale(1.05) translateY(-15px);
    }
    70% { 
        transform: scale(0.95) translateY(5px);
    }
    100% { 
        opacity: 1; 
        transform: scale(1) translateY(0);
    }
}

@keyframes flipIn {
    from { 
        opacity: 0; 
        transform: perspective(400px) rotate3d(1, 0, 0, 90deg);
        animation-timing-function: ease-in;
    }
    40% { 
        transform: perspective(400px) rotate3d(1, 0, 0, -20deg);
        animation-timing-function: ease-in;
    }
    60% { 
        opacity: 1; 
        transform: perspective(400px) rotate3d(1, 0, 0, 10deg);
    }
    80% { 
        transform: perspective(400px) rotate3d(1, 0, 0, -5deg);
    }
    to { 
        opacity: 1; 
        transform: perspective(400px);
    }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes glow {
    0% { box-shadow: 0 0 5px rgba(138, 36, 50, 0.5); }
    50% { box-shadow: 0 0 20px rgba(138, 36, 50, 0.8); }
    100% { box-shadow: 0 0 5px rgba(138, 36, 50, 0.5); }
}

@keyframes textShadow {
    0% { text-shadow: 0 0 0 rgba(0, 0, 0, 0); }
    50% { text-shadow: 0 0 10px rgba(138, 36, 50, 0.5); }
    100% { text-shadow: 0 0 0 rgba(0, 0, 0, 0); }
}

@keyframes typewriter {
    from { width: 100%; }
    to { width: 50%; }
}

@keyframes fadeInUp {
    from { 
        opacity: 0; 
        transform: translate3d(0, 40px, 0); 
    }
    to { 
        opacity: 1; 
        transform: translate3d(0, 0, 0); 
    }
}

@keyframes shake {
    70%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
    20%, 40%, 60%, 80% { transform: translateX(5px); }
}

/* Классы анимаций */
.animate-fade {
    opacity: 2;
    animation: fadeIn 1s ease forwards;
}

.animate-left {
    opacity: 0;
    animation: slideInLeft 1s ease forwards;
}

.animate-right {
    opacity: 0;
    animation: slideInRight 1s ease forwards;
}

.animate-scale {
    opacity: 0;
    animation: scaleIn 0.8s ease forwards;
}

.animate-bounce {
    opacity: 0;
    animation: bounceIn 1.2s ease forwards;
}

.animate-flip {
    opacity: 0;
    animation: flipIn 1.1s ease forwards;
    backface-visibility: visible !important;
}

.animate-pulse {
    animation: pulse 2s infinite;
}

.animate-float {
    animation: float 3s ease-in-out infinite;
}

.animate-glow {
    animation: glow 2s ease-in-out infinite;
}

.animate-text-shadow {
    animation: textShadow 3s ease-in-out infinite;
}

.animate-typewriter {
    overflow: hidden;
    white-space: nowrap;
    animation: typewriter 1.5s steps(40) forwards;
}

.animate-fade-up {
    opacity: 0;
    animation: fadeInUp 1s ease forwards;
}

.animate-shake {
    animation: shake 0.8s ease;
}

/* Задержки анимаций */
.delay-1 { animation-delay: 0.2s; }
.delay-2 { animation-delay: 0.4s; }
.delay-3 { animation-delay: 0.6s; }
.delay-4 { animation-delay: 0.8s; }
.delay-5 { animation-delay: 1s; }
.delay-6 { animation-delay: 1.2s; }
.delay-7 { animation-delay: 1.4s; }
.delay-8 { animation-delay: 1.6s; }
.delay-9 { animation-delay: 1.8s; }
.delay-10 { animation-delay: 2s; }
            
            @keyframes slideInLeft {
                from { opacity: 0; transform: translateX(-50px); }
                to { opacity: 1; transform: translateX(0); }
            }
            
            @keyframes slideInRight {
                from { opacity: 0; transform: translateX(50px); }
                to { opacity: 1; transform: translateX(0); }
            }
            
            .animate-fade {
                opacity: 0;
                animation: fadeIn 1s ease forwards;
            }
            
            .animate-left {
                opacity: 0;
                animation: slideInLeft 1s ease forwards;
            }
            
            .animate-right {
                opacity: 0;
                animation: slideInRight 1s ease forwards;
            }
            
            .delay-1 { animation-delay: 0.2s; }
            .delay-2 { animation-delay: 0.4s; }
            .delay-3 { animation-delay: 0.6s; }
            .delay-4 { animation-delay: 0.8s; }
            
            header {
                background-color:#660017 ;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 1000;
                animation: fadeIn 1s ease;
            }
            
            .container {
                width: 100%;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 15px;
            }
            
            .header-inner {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px 0;
            }
            
            .logo {
                height: 50px;
                animation: fadeIn 1s ease;
            }
            
            .nav-toggle {
                display: none;
                cursor: pointer;
                font-size: 24px;
            }
            
            .sidebar {
                width: 250px;
                position: fixed;
                top: 80px;
                left: 0;
                height: calc(100vh - 80px);
                background: var(--primary);
                padding: 20px;
                transform: translateX(-100%);
                transition: transform 0.3s ease;
                z-index: 999;
            }
            
            .sidebar.active {
                transform: translateX(0);
            }
            
            .sidebar a {
                display: block;
                color: white;
                padding: 12px 0;
                text-decoration: none;
                font-size: 18px;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                transition: all 0.2s;
            }
            
            .sidebar a:hover {
                color: var(--secondary);
                padding-left: 10px;
            }
            
            .main-content {
                margin-top: 80px;
                margin-left: 0;
                transition: margin-left 0.3s;
            }
            
            .main-content.shifted {
                margin-left: 250px;
            }
            .main-title {
        color: ##660017; /* бургундий для максимального контраста */
        text-shadow: 
            2px 2px 0 #000, 
            -2px -2px 0 #000, 
            2px -2px 0 #000, 
            -2px 2px 0 #000,
            0 0 15px rgba(229, 10, 20, 0.7); /* Объемная тень и красное свечение */
        font-weight: 900;
        font-size: 3.5rem;
        letter-spacing: 1px;
        line-height: 1.2;
    }
    
    .subtitle {
        color: #f8f8f8; /* Светлый серый для хорошей читаемости */
        text-shadow: 
            1px 1px 2px #000,
            0 0 10px rgba(0, 0, 0, 0); /* Легкая тень для контраста */
        font-weight: 600;
        font-size: 1.5rem;
        max-width: 800px;
        margin: 20px auto;
    }
    
    .btn {
        display: inline-block;
        background: linear-gradient(45deg, #660017, #B8070F);
        color: white;
        padding: 18px 42px;
        font-size: 1.2rem;
        font-weight: 800;
        text-decoration: none;
        border-radius: 50px;
        box-shadow: 0 5px 20px rgba(229, 10, 20, 0.5);
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.6);
        border: 2px solid rgba(255, 255, 255, 0.3);
        margin-top: 30px;
        transition: all 0.3s ease;
    }
    
    .btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(229, 10, 20, 0.7);
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
    }
            
            section {
                padding: 100px 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                opacity: 0;
                transform: translateY(50px);
                transition: opacity 1s ease, transform 1s ease;
            }
            
            section.visible {
                opacity: 1;
                transform: translateY(0);
            }
            

           .hero {
    background: url('images/2023.gif') no-repeat center center;
    background-size: cover;
    text-align: center;
    position: relative;
    /* Оптимизация производительности */
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
    backface-visibility: hidden;
    transform: translateZ(0);
}
         /* Стили для видео-фона */
/* Общие стили для видеофона на обеих страницах */
.section-video-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 1;
}

.bg-video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translateX(-50%) translateY(-50%);
    object-fit: cover;
}

.section-video-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4); /* Затемнение для читаемости текста */
    z-index: 2;
}

.video-overlay {
   position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); /* Увеличиваем затемнение для лучшей читаемости */
    z-index: 2;
}

/* Убедитесь, что контейнеры контента поверх видео */
.hero .container,
#benefits .container {
    position: relative;
    z-index: 2;
}

/* Убедитесь, что у секций нет фона, перекрывающего видео */
.hero,
#benefits {
    background: transparent;
    position: relative;
}

.hero .container {
    position: relative;
    z-index: 3;
    width: 100%;
    text-align: center;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
    .video-background {
        display: none; /* Скрываем GIF на мобильных */
    }
    
    .hero {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    }
}

/* Для устройств с ограниченными ресурсами */
@media (max-width: 1024px) and (prefers-reduced-motion: reduce) {
    .video-background {
        display: none;
    }
    
    .hero {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    }
} 
}


/* Добавьте затемнение для лучшей читаемости текста */
.hero::before {
    content: '';
    position: absolute;
    top: 1;
    left: 2;
    right: 3;
    bottom: 4;
    background: rgba(0, 0, 0, 0); /* Регулируйте прозрачность по необходимости */
    z-index: 1;
}

.hero .container {
    position: relative;
    z-index: 2;
}
      .hero h1 {
    font-size: 4.5rem;
    margin-bottom: 50px;
    color: #ffffff; /* Белый цвет для лучшего контраста */
    letter-spacing: 1.5px;
    font-weight:700; /* Более жирный шрифт */
    line-height: 3;
    
    /* Эффекты для объемности и лучшей читаемости */
    text-shadow: 
        2px 2px 0px rgba(0, 0, 0, 0.10),    /* Основная тень */
        4px 4px 0px rgba(0, 0, 0, 0.5),    /* Вторая тень для объема */
        0px 0px 10px rgba(0, 0, 0, 0.8),   /* Размытая тень для контраста */
        0px 0px 20px rgba(138, 36, 50, 0.6); /* Свечение основным цветом */
    
    /* Дополнительные эффекты для лучшей читаемости */
    background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    padding: 25px 35px;
    border-radius: 10px;
    display: inline-block;
    position: relative;
    z-index: 2;
}
/* Псевдоэлемент для дополнительного контраста */
.hero h1::before {
    content: '';
    position: absolute;
    top: -3px;
    left: -3px;
    right: -3px;
    bottom: -3px;
    background: rgba(0, 0, 0, 10);
    border-radius: 15px;
    z-index: -1;
    filter: blur(5px);
}
/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
    .hero h1 {
    font-size: 3.5rem;
    margin-bottom: 20px;
    color: #ffffff;
    letter-spacing: 1.5px;
    font-weight: 800; /* Еще более жирный шрифт */
    line-height: 1.2;
    
    /* Ярко выраженный объемный эффект */
    text-shadow: 
        0 1px 0 #ccc, 
        0 2px 0 #c9c9c9, 
        0 3px 0 #bbb, 
        0 4px 0 #b9b9b9, 
        0 5px 0 #aaa, 
        0 6px 1px rgba(0,0,0,.1), 
        0 0 5px rgba(0,0,0,.1), 
        0 1px 3px rgba(0,0,0,.3), 
        0 3px 5px rgba(0,0,0,.2), 
        0 5px 10px rgba(0,0,0,.25), 
        0 10px 10px rgba(0,0,0,.2), 
        0 20px 20px rgba(0,0,0,.15),
        0 0 15px rgba(255,255,255,0.5); /* Свечение */
    
    padding: 15px 25px;
    border-radius: 10px;
    display: inline-block;
    position: relative;
    z-index: 2;
}

/* Для мобильных устройств */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.2rem;
        padding: 10px 15px;
        text-shadow: 
            0 1px 0 #ccc, 
            0 2px 0 #c9c9c9, 
            0 3px 0 #bbb, 
            0 4px 0 #b9b9b9, 
            0 5px 0 #aaa, 
            0 6px 1px rgba(0,0,0,.1), 
            0 0 5px rgba(0,0,0,.1), 
            0 1px 3px rgba(0,0,0,.3), 
            0 3px 5px rgba(0,0,0,.2);
    }
}
    }      
            
}

.section-title {
    text-align: center;
    margin-bottom: 100px;
    color: var(--primary);
    letter-spacing: 1.2px;
    font-weight: 600;
}
            
           .hero p {
    font-size: 1.5rem;
    margin-bottom: 30px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.4;
    color: white;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
    font-weight: 500;
    padding: 10px 15px;
    background: rgba(0, 0, 0, 0.3);
    border-radius: 8px;
}

/* Для кнопок */
.hero .btn {
    background: rgba(138, 36, 50, 0.5);
    border: 2px solid #ffffff;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    font-weight: 600;
}

.hero .btn:hover {
    background: rgba(255, 255, 255, 0.9);
    color: var(--primary);
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
}
            }
            
            .btn {
                display: inline-block;
                background: var(--primary);
                color: white;
                padding: 15px 30px;
                border-radius: 50px;
                text-decoration: none;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
                transition: all 0.3s;
                border: 2px solid var(--primary);
                margin: 10px;
            }
            
            .btn {
    display: inline-block;
    background: var(--primary);
    color: white;
    padding: 15px 30px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    transition: all 0.3s;
    border: 2px solid var(--primary);
    margin: 10px;
}

.btn-outline {
    background: transparent;
    color: var(--primary);
}

.btn-outline:hover {
    background: var(--primary);
    color: white;
}
            
            .catalog {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 50px;
                margin-top: 50px;
            }
            
            .catalog-item {
                background: white;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                width: 250px;
                transition: transform 0.3s;
            }
            
            .catalog-item:hover {
                transform: translateY(-10px) scale(1.03);
            }
            
            .catalog-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    display: block;
}
            
            .catalog-item h3 {
                padding: 20px;
                text-align: center;
                background: var(--primary);
                color: white;
                margin: 0;
            }
            
            .section-title {
                text-align: center;
                margin-bottom: 60px;
                color: var(--primary);
            }
            
            .benefits-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
            }
            
            .benefit-card {
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                text-align: center;
                transition: transform 0.3s;
            }
            
            .benefit-card:hover {
                transform: translateY(-10px);
            }
           /* Стили для раздела преимуществ с видео-фоном */
.benefits-section {
    position: relative;
    overflow: hidden;
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 100px 0;
    background: transparent;
}

.benefits-video-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 1;
}

.benefits-video-bg video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translateX(-50%) translateY(-50%);
    object-fit: cover;
}

.benefits-video-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); /* Затемнение для улучшения читаемости текста */
    z-index: 2;
}

.benefits-section .container {
    position: relative;
    z-index: 3;
    width: 100%;
}

/* Обновление стилей карточек преимуществ для лучшей видимости на видео-фоне */
.benefit-card {
    background: rgba(255, 255, 255, 0.9); /* Полупрозрачный белый фон */
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transition: transform 0.3s, box-shadow 0.3s;
}

.benefit-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    background: rgba(255, 255, 255, 0.95); /* Меньшая прозрачность при наведении */
}

.benefit-header {
    background: rgba(138, 36, 50, 0.9); /* Полупрозрачный вариант основного цвета */
    color: white;
    padding: 20px;
    text-align: center;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
    .benefits-video-bg {
        display: none; /* Скрываем видео на мобильных */
    }
    
    .benefits-section {
        background: linear-gradient(135deg, var(--secondary) 0%, var(--accent1) 100%);
    }
    
    .benefit-card {
        background: rgba(255, 255, 255, 0.95); /* Меньшая прозрачность на мобильных */
    }
}

/* Для устройств с ограниченными ресурсами */
@media (max-width: 1024px) and (prefers-reduced-motion: reduce) {
    .benefits-video-bg {
        display: none;
    }
    
    
      /* Стили для раздела преимуществ с видео-фоном */
.benefits-section {
    position: relative;
    overflow: hidden;
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 100px 0;
}

.benefits-video-bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: 1;
}

.benefits-video-bg video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translateX(-50%) translateY(-50%);
    object-fit: cover;
}

.benefits-video-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); /* Затемнение для улучшения читаемости текста */
    z-index: 2;
}

.benefits-section .container {
    position: relative;
    z-index: 3;
    width: 100%;
}

/* Обновление стилей карточек преимуществ для лучшей видимости на видео-фоне */
.benefit-card {
    background: rgba(255, 255, 255, 0.9); /* Полупрозрачный белый фон */
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    transition: transform 0.3s, box-shadow 0.3s;
}

.benefit-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    background: rgba(255, 255, 255, 0.95); /* Меньшая прозрачность при наведении */
}

.benefit-header {
    background: rgba(138, 36, 50, 0.9); /* Полупрозрачный вариант основного цвета */
    color: white;
    padding: 20px;
    text-align: center;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
    .benefits-video-bg {
        display: none; /* Скрываем видео на мобильных */
    }
    
    .benefits-section {
        background: linear-gradient(135deg, var(--secondary) 0%, var(--accent1) 100%);
    }
    
    .benefit-card {
        background: rgba(255, 255, 255, 0.95); /* Меньшая прозрачность на мобильных */
    }
}

/* Для устройств с ограниченными ресурсами */
@media (max-width: 1024px) and (prefers-reduced-motion: reduce) {
    .benefits-video-bg {
        display: none;
    }
    
    .benefits-section {
        background: linear-gradient(135deg, var(--secondary) 0%, var(--accent1) 100%);
    }
}     
            }
            
            .bonuses {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 40px;
            }
            
            .bonus-col {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            }
            
            .bonus-col ul {
                list-style: none;
                padding: 20px 0;
            }
            
            .bonus-col li {
                padding: 10px 0;
                border-bottom: 1px dashed #eee;
            }
            
            .bonus-col h3 {
                color: var(--primary);
                margin-bottom: 20px;
            }
            
            .about-content {
                display: grid;
                grid-template-columns: 1fr 2fr;
                gap: 50px;
                align-items: center;
            }
            
            .profile-img {
    width: 100%;
    height: 300px;
    border-radius: 15px;
    object-fit: cover;
}
            /* Стили для раздела "О владельце" */
.profile-container {
    text-align: center;
    margin-bottom: 30px;
}

.profile-img-large {
    width: 300px;
    height: 300px;
    border-radius: 50%;
    object-fit: cover;
    border: 5px solid var(--primary);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    margin: 0 auto 20px;
    display: block;
}

.profile-title {
    text-align: center;
    margin-bottom: 30px;
}

.profile-title h3 {
    color: var(--primary);
    font-size: 2rem;
    margin-bottom: 20px;
}

.profile-title p {
    color: var(--dark);
    font-size: 1.2rem;
    font-style: italic;
}

.about-text {
    background: none;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

.about-text h3 {
    color: var(--primary);
    margin-bottom: 20px;
    border-bottom: 2px solid var(--accent2);
    padding-bottom: 10px;
}

.about-text p {
    margin-bottom: 20px;
    line-height: 1.6;
}

.about-content {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 50px;
    align-items: start;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 992px) {
    .about-content {
        grid-template-columns: 1fr;
    }
    
    .profile-img-large {
        width: 250px;
        height: 250px;
    }
    
    .about-text {
        padding: 20px;
    }
}

@media (max-width: 768px) {
    .profile-img-large {
        width: 200px;
        height: 200px;
    }
    
    .profile-title h3 {
        font-size: 1.5rem;
    }
    
    .profile-title p {
        font-size: 1rem;
    }
}
            .contact-wrapper {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 50px;
            }
            
            .contact-info {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            }
            
            .contact-form form {
                display: flex;
                flex-direction: column;
                gap: 20px;
            }
            
            .form-group input,
            .form-group textarea {
                width: 100%;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 8px;
                font-size: 16px;
                transition: all 0.3s;
            }
            
            .form-group input:focus,
            .form-group textarea:focus {
                outline: none;
                border-color: var(--primary);
                box-shadow: 0 0 0 3px rgba(106, 13, 173, 0.2);
            }
            
            .form-group textarea {
                height: 150px;
                resize: vertical;
            }
            
            footer {
                background: var(--dark);
                color: white;
                text-align: center;
                padding: 30px 0;
            }
            
            @media (max-width: 992px) {
                .about-content,
                .contact-wrapper {
                    grid-template-columns: 1fr;
                }
                
                .nav-toggle {
                    display: block;
                }
                
                .main-content.shifted {
                    margin-left: 0;
                }
                
               .hero h1 {
    font-size: 3.5rem;
    margin-bottom: 30px;
    color: var(--primary);
    letter-spacing: 1.5px;
    font-weight: 600;
    line-height: 1.2;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.hero p {
    font-size: 1.5rem;
    margin-bottom: 30px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.4;
    text-shadow: 1px 1px 1px rgba(0,0,0,0.1);
}

/* Улучшение отображения текста на мобильных устройствах */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.2rem;
        padding: 0 10px;
    }
    
    .hero p {
        font-size: 1.2rem;
        padding: 0 15px;
    }
}

/* Дополнительные гарантии от обрезания текста */
.container {
    overflow: visible !important;
}

.hero .container {
    position: relative;
    z-index: 3;
    width: 100%;
    overflow: visible;
}
                }
            }
        </style>
    </head>
    
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <body>
        <header>
            <div class="container">
                <div class="header-inner">
                    <img src="images/logo.png" alt="Shoes You" class="logo">
                    <div class="nav-toggle">☰</div>
                </div>
            </div>
        </header>

        <div class="sidebar" id="sidebar">
            <a href="#hero">Главная</a>
            <a href="#benefits">Преимущества</a>
            <a href="#about">О нас</a>
            <a href="#bonuses">Акции и бонусы</a>
            <a href="#contacts">Контакты</a>
            <a href="#rules">Правила заказа</a>
        </div>

        <div class="main-content" id="mainContent">

        <!-- Главный экран -->
        <section id="benefits" class="benefits-section visible">
    <!-- Используем тот же видеофон, что и на главной -->
    <div class="video-background">
        <video autoplay muted loop playsinline class="gif-background">
           <source src="images/media.mp4" type="video/mp4">  
            Ваш браузер не поддерживает видео-фон.
        </video>
        <div class="video-overlay"></div>
    </div>
    <div class="container">
         <h1 class="main-title">№ 1 telegram-канал байера по поиску товаров</h1>
            <h2 class="subtitle">Экспертный подбор одежды и обуви из Китая и Европы с гарантией качества и лучшими ценами</h2>
        <a href="https://t.me/shoes_you" class="btn animate-fade delay-1" target="_blank">Подробнее</a>
        
        <div class="catalog">
            <div class="catalog-item animate-left delay-1">
                <img src="images/zakaz.jpg" alt="Ваши заказы" class="catalog-img">
                <h3>Ваши заказы</h3>
                <a href="https://web.telegram.org/a/#-1001299905580" class="btn btn-outline" target="_blank">Перейти</a>
            </div>
            
            <div class="catalog-item animate-fade delay-2">
                 <img src="images/shoes.jpg" alt="Обувь" class="catalog-img">
                <h3>Обувь</h3>
                <a href="https://web.telegram.org/a/#-1001655516091" class="btn btn-outline" target="_blank">Перейти</a>
            </div>
            
            <div class="catalog-item animate-fade delay-3">
                <img src="images/clothes.jpg" alt="Одежда" class="catalog-img">
                <h3>Одежда</h3>
                <a href="https://web.telegram.org/a/#-1001299905580" class="btn btn-outline" target="_blank">Перейти</a>
            </div>
            
            <div class="catalog-item animate-right delay-4">
              <img src="images/bag1.jpg" alt="Сумки/Аксессуары" class="catalog-img">
                <h3>Сумки/Аксессуары</h3>
                <a href="https://web.telegram.org/a/#-1002437119342" class="btn btn-outline" target="_blank">Перейти</a>
            </div>
        </div>
    </div>
</section>
    <!-- Преимущества -->
    <div class="container">
        <h2 class="section-title animate-fade">5 Главных Преимуществ</h2>
        <p class="animate-fade delay-1" style="text-align: center; margin-bottom: 50px; font-size: 1.2rem;">Закажи и проверь нашу работу!</p>
        
        <div class="benefits-grid">
            <div class="benefit-card animate-left delay-2">
                <div class="benefit-header">
                    <h3>Стремительная Доставка</h3>
                </div>
                <div class="catalog">
                <img src="images/3.jpg" alt="Стремительная доставка" class="catalog-img">
                    <p>Надежная и предсказуемая экспресс-доставка премиум-класса с отслеживанием заказа с 1го дня.</p>
                </div>
            </div>
            
            <div class="benefit-card animate-fade delay-2">
                <div class="benefit-header">
                    <h3>Основательное Внимание к Деталям</h3>
                </div>
                <div class="benefit-content">
             <img src="images/4.jpg" alt="Основное внимание к деталям" class="catalog-img">
                    <p>Мы очень трепетно относимся как к качеству товара, проверяем перед отправкой.</p>
                </div>
            </div>
            
            <div class="benefit-card animate-fade delay-3">
                <div class="benefit-header">
                    <h3>Индивидуальный подход</h3>
                </div>
                <div class="benefit-content">
                <div class="catalog">
                <img src="images/otzuvy.jpg" alt="Ваши заказы" class="catalog-img">
            </div>
                    <p>Гибкие, персонализированные решения для постоянных клиентов.</p>
                    
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="benefit-card animate-fade delay-4">
                <div class="benefit-header">
                    <h3>Поддержка 24/7</h3>
                        </div>
                <div class="benefit-content">
                <div class="catalog">
            <div class="catalog-item animate-left delay-1">
                <img src="images/11.jpg" alt="Ваши заказы" class="catalog-img">
                                </div>
                <div class="benefit-content">
                    <p>Круглосуточная профессиональная помощь для вас в любой момент.</p>
                </div>
            </div>
            
            <div class="benefit-card animate-right delay-5">
                <div class="benefit-header">
                    <h3>Ваш Стилист Онлайн</h3>
                </div>
                <div class="benefit-content">
                    <p>Персональный эксперт-стилист курирует каждый заказ, гарантируя безупречный выбор и консультацию.</p>
                </div>
            </div>
        </div>
    </div>
</section>
           
            <!-- Акции и бонусы -->
            <section id="bonuses">
                <div class="container">
                    <h2 class="section-title animate-fade">Эксклюзивные бонусы для вас!</h1>
                    <div class="image"></h1>
                    <div class="bonuses">
                        <div class="bonus-col animate-left delay-1">
                            <h1>Наши услуги</h2>
                            <ul>
                                <h2>Индивидуальный заказ товара</h2>
                                <h2>Поиск и доставка товара</h2>
                                <h2>Консультация по товару</h2>
                                <h2>Круглосуточная поддержка бесплатно</h2>
                                <ul>
                        
                        <div class="bonus-col animate-right delay-1">
                            <h1>Программа лояльности</h1>
                            <p>Скидки для постоянных клиентов:</p>
                            <ul>
                                <h2>-10% при покупке от 3 товаров</h2>
                                <h2>-15% при покупке от 5 товаров</h2>
                                <h2>Специальные скидки в День Рождения!</h2>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

          <!-- О владельце -->
            <section class="hero" id="hero">
    <!-- Видео-фон -->
    <div class="video-background">
    <video autoplay muted loop playsinline class="video-bg">
        <source src="images/media.mp4" type="video/mp4">
        Ваш браузер не поддерживает видео-фон.
    </video>
    <div class="video-overlay"></div>
</div>
    <div class="container">
        <h2 class="section-title animate-fade">О владельце компании</h2>
        
        <div class="about-content">
            <div class="profile-container animate-left delay-1">
                <img src="images/photo1.jpg" alt="Екатерина Маликова" class="profile-img-large">
                <div class="profile-title">
                    <h3>Маликова Екатерина</h3>
                    <h3>Байер и генеральный директор компании Shoes_you</h3>
                </div>
            </div>
            
            <div class="about-text animate-left delay-1">
                <h3>Екатерина Маликова: Видение и Экспертиза во главе Shoes_you</h3>
                
                <p>Екатерина Маликова является бессменным Генеральным директором и ключевым байером компании Shoes_you с момента ее основания в 2015 году. Под ее стратегическим руководством и благодаря глубокой экспертизе в мире фэшн-индустрии, компания завоевала доверие сотен клиентов, ценящих индивидуальный подход и безупречный сервис.</p>
                
                <p>Shoes_you не просто находит товар – мы создаем возможности. Компания активно развивает партнерские отношения с лидерами мнений, сотрудничая с известными блогерами, и укрепляет свои позиции на рынке, регулярно участвуя в профильных показах и отраслевых событиях.</p>
                
                <p>Наша ключевая миссия: решать самые сложные задачи по поиску товаров различных категорий. Независимо от бренда, редкости модели или географической локации, команда Shoes_you готова взяться за поиск и доставить желаемое клиенту. Мы превращаем "невозможное" в "доставлено".</p>
                
                <p>Обращайтесь к Shoes_you – и доверьтесь профессионализму Екатерины Маликовой и ее команды.</p>
            </div>
        </div>
    </div>
</section> 
            <!-- Контакты -->
            <section id="contacts">
                <div class="container">
                    <h2 class="section-title animate-fade">Свяжитесь с нами!</h2>
                    <p class="animate-fade delay-1" style="text-align: center; margin-bottom: 50px; max-width: 800px; margin-left: auto; margin-right: auto;">
                        Предоставьте нам свой запрос, и мы поможем вам с заказом. Консультация по товару работает круглосуточно.
                    </p>
                    
                    <div class="contact-wrapper">
                        <div class="contact-info animate-left delay-2">
                            <h3>Контактная информация</h3>
                            <p style="margin: 20px 0;"><strong>Телефон:</strong> +7(977)368-09-59</p>
                            <p><strong>Email:</strong> shoesforyou06@gmail.com</p>
                        </div>
                        
                        <div class="contact-form animate-right delay-3">
                           <form id="contactForm" class="animate-fade-up delay-4">
                                <div class="form-group">
                                    <input type="text" placeholder="Ваше полное имя" required>
                                </div>
                                
                                <div class="form-group">
                                    <input type="email" placeholder="Ваш адрес электронной почты" required>
                                </div>
                                
                                <div class="form-group">
                                    <textarea placeholder="Ваши комментарии" required></textarea>
                                </div>
                                
                                <button type="submit" class="btn">Отправить запрос</button>
                            </form>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Правила заказа -->
            <!-- Правила заказа -->
<section id="rules" style="background-color: #f8f9fa;">
    <div class="container">
        <h2 class="section-title animate-fade">Правила оформления заказа</h2>
        
        <div class="rules-content animate-fade delay-1">
            <div class="pdf-preview">
                <div class="pdf-icon">
                    <svg viewBox="0 0 24 24" width="64" height="64">
                        <path fill="#e74c3c" d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z"/>
                        <path fill="#e74c3c" d="M7 18H9V16H7V18M9 14H7V10H9V14M10 14H12V16H10V14M12 14V12H14V14H12M12 12V10H14V12H12M12 8V10H10V8H12M10 10V12H8V10H10M8 10V8H10V10H8M10 12H12V10H10V12M12 12H14V10H12V12Z"/>
                    </svg>
                </div>
                <h3>Правила оформления заказа</h3>
                <p>Ознакомьтесь с полными правилами оформления заказов в нашем магазине</p>
                
                <div class="download-buttons">
                    <a href="images/ПРАВИЛА ОФОРМЛЕНИЯ ЗАКАЗА.pdf" class="btn-download" download>
                        <span>Скачать PDF</span>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                            <path d="M12 16L12 4M12 16L8 12M12 16L16 12" stroke="currentColor" stroke-width="2"/>
                            <path d="M4 20H20" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </a>
                    
                    <a href="documents/order_rules.pdf" class="btn-view" target="_blank">
                        <span>Посмотреть онлайн</span>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                            <path d="M14 5H20V11M20 5L11 14M10 19H4V13" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </a>
                </div>
                
                <div class="file-info">
                    <p><strong>Формат:</strong> PDF</p>
                    <p><strong>Размер:</strong> 1.2 MB</p>
                    <p><strong>Страниц:</strong> 3</p>
                </div>
            </div>
            
            <div class="rules-summary">
                <h3>Краткое содержание правил:</h3>
                <ul>
                    <li>Выбор товара и отправка запроса</li>
                    <li>Подтверждение наличия и стоимости</li>
                    <li>Оплата заказа (100% предоплата)</li>
                    <li>Производство товара (2-5 дней)</li>
                    <li>Контроль качества и фотоотчет</li>
                    <li>Организация доставки</li>
                    <li>Получение и проверка заказа</li>
                </ul>
                
                <div class="important-note">
                    <h4>Важно!</h4>
                    <p>При оформлении заказа вы автоматически соглашаетесь с правилами, изложенными в документе. Рекомендуем внимательно ознакомиться с полной версией перед совершением покупки.</p>
                </div>
            </div>
        </div>
    </div>
</section>

            <!-- Футер -->
            <footer>
                <div class="container">
                    <p>&copy; 2023 Shoes_you. Все права защищены.</p>
                    <p>Домен: https://shoesyou.su/</p>
                </div>
            </footer>
        </div>

        <script>
            // Мобильное меню
            document.querySelector('.nav-toggle').addEventListener('click', function() {
                document.getElementById('sidebar').classList.toggle('active');
                document.getElementById('mainContent').classList.toggle('shifted');
            });
            
            // Закрытие меню при клике на ссылку
            document.querySelectorAll('.sidebar a').forEach(link => {
                link.addEventListener('click', () => {
                    document.getElementById('sidebar').classList.remove('active');
                    document.getElementById('mainContent').classList.remove('shifted');
                });
            });
            
            // Обработка формы
            document.getElementById('contactForm').addEventListener('submit', function(e) {
                e.preventDefault();
                alert('Ваш запрос отправлен! Мы свяжемся с вами в ближайшее время.');
                this.reset();
            });
            
            // Плавная прокрутка к разделам
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    
                    const targetId = this.getAttribute('href');
                    if (targetId === '#') return;
                    
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        targetElement.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
            
            // Анимация появления элементов при прокрутке
            function checkVisibility() {
                const sections = document.querySelectorAll('section');
                
                sections.forEach(section => {
                    const sectionTop = section.getBoundingClientRect().top;
                    const windowHeight = window.innerHeight;
                    
                    if (sectionTop < windowHeight * 0.75) {
                        section.classList.add('visible');
                    }
                });
            }
            
            // Проверяем видимость при загрузке и прокрутке
            window.addEventListener('load', checkVisibility);
            window.addEventListener('scroll', checkVisibility);
            
            // Запускаем проверку видимости после загрузки
            setTimeout(checkVisibility, 100);
        </script>
            <!-- Другие скрипты -->
    
    <script>
        // Функция для управления видео-фоном в разделе преимуществ
      // Управление видео-фоном для всех секций
function initAllVideos() {
    const videos = document.querySelectorAll('.bg-video');
    const sections = document.querySelectorAll('.hero, #benefits, #about, #bonuses, #contacts, #rules');
    
    // Проверяем мобильное устройство
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    if (isMobile) {
        // На мобильных - скрываем видео и включаем градиентный фон
        videos.forEach(video => {
            video.style.display = 'none';
        });
        
        sections.forEach(section => {
            section.style.background = 'linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%)';
        });
    } else {
        // На десктопах - показываем видео
        videos.forEach(video => {
            video.style.display = 'block';
        });
        
        sections.forEach(section => {
            section.style.background = 'none';
        });
        
        // Пытаемся запустить все видео
        videos.forEach(video => {
            video.play().catch(error => {
                console.log("Автовоспроизведение видео предотвращено:", error);
            });
        });
    }
}

// Инициализация при загрузке
document.addEventListener('DOMContentLoaded', initAllVideos);
window.addEventListener('resize', initAllVideos);
        // Запускаем инициализацию при загрузке страницы
        document.addEventListener('DOMContentLoaded', initBenefitsVideo);

        // Также обновляем при изменении размера окна
        window.addEventListener('resize', initBenefitsVideo);
    <script>
    // ... ваш существующий JavaScript код ...
    
    // ВСТАВЬТЕ ЭТОТ КОД ПЕРЕД ЗАКРЫВАЮЩИМ ТЕГОМ SCRIPT
    // Функция для управления видео-фоном в разделе преимуществ
    function initBenefitsVideo() {
        const benefitsVideo = document.querySelector('.benefits-video-bg video');
        const benefitsSection = document.querySelector('.benefits-section');
        
        if (benefitsVideo && benefitsSection) {
            // Проверяем, является ли устройство мобильным
            const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
            
            if (isMobile) {
                // На мобильных устройствах скрываем видео и устанавливаем фоновый градиент
                benefitsVideo.style.display = 'none';
                benefitsSection.style.background = 'linear-gradient(135deg, var(--secondary) 0%, var(--accent1) 100%)';
            } else {
                // На десктопах обеспечиваем правильное отображение видео
                benefitsVideo.style.display = 'block';
                benefitsSection.style.background = 'none';
                
                // Попытка запуска видео (некоторые браузеры требуют этого)
                benefitsVideo.play().catch(error => {
                    console.log("Автовоспроизведение видео предотвращено:", error);
                });
            }
        }
    }

    // Запускаем инициализацию при загрузке страницы
    document.addEventListener('DOMContentLoaded', initBenefitsVideo);

    // Также обновляем при изменении размера окна
    window.addEventListener('resize', initBenefitsVideo);
    // КОНЕЦ ВСТАВКИ
    
</script>
    </body>
    </html>
    """
    
    # Сохранение в файл
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print("Лендинг успешно сгенерирован в файле index.html")

# Запуск генерации
generate_landing()
