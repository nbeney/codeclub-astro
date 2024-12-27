const pages = [
    { 
        name: 'Home', 
        route: '/', 
        language: '', 
        description: 'Home page.', 
        status: '', 
        logo: null 
    },
    { 
        name: 'Guizero', 
        route: '/activities/guizero-based/', 
        language: 'python', 
        description: 'Desktop applications with <em>Guizero</em>.', 
        status: '', 
        logo: 'logo.jpg' 
    },
    { 
        name: 'Pygame Zero', 
        route: '/activities/pygame-zero-based/', 
        language: 'python', 
        description: 'Video games with <em>Pygame Zero</em>.', 
        status: '', 
        logo: 'logo.jpg' 
    },
    { 
        name: 'Adventurelib', 
        route: '/activities/adventurelib-based/', 
        language: 'python', 
        description: 'Text-based adventure games with <em>Adventurelib</em>.', 
        status: '', 
        logo: 'logo.jpg' 
    },
    { 
        name: 'P5', 
        route: '/activities/p5-based/', 
        language: 'python', 
        description: 'Animations or digital art with <em>p5py</em>.', 
        status: '', 
        logo: 'logo.jpg' 
    },
    {
        name: 'Scratch',
        route: '/activities/scratch-based/',
        language: '',
        description: 'Games, animations, stories, etc with <em>Scratch</em>.',
        status: 'not-ready',
        logo: 'logo.jpg'
    },
    {
        name: 'Web design',
        route: '/activities/web-based/',
        language: '',
        description: 'Web design with <em>HTML</em>, <em>CSS</em>, and <em>Javascript</em>.',
        status: 'not-ready',
        logo: 'logo.jpg'
    },
    {
        name: 'BBC Microbit',
        route: '/activities/microbit-based/',
        language: '',
        description: 'Discover physical computing with the <em>BBC Microbit</em>.',
        status: 'not-ready',
        logo: 'logo.jpg'
    },
    {
        name: 'Makecode Arcade',
        route: '/activities/arcade-based/',
        language: '',
        description: 'Retro video games with <em>MakeCode Arcade</em>.',
        status: 'not-ready',
        logo: 'logo.jpg'
    },
    {
        name: 'AI',
        route: '/activities/ai-based/',
        language: '',
        description: 'Artificial intelligence and machine learning.',
        status: 'not-ready',
        logo: 'logo.jpg'
    },
    {
        name: 'Music',
        route: '/activities/music-based/',
        language: '',
        description: 'Music with <em>Sonic Pi</em> and others.',
        status: 'not-ready',
        logo: 'logo.jpg'
    },
    {
        name: 'Python libraries',
        route: '/activities/python-libraries/index.html',
        language: '',
        description: 'Python libraries.',
        status: '',
        logo: null
    }
]

const pagesWithLogo = pages.filter(page => page.logo !== null);

const pagesReady = pages.filter(page => page.status !== 'not-ready');

export { pages, pagesWithLogo, pagesReady };
