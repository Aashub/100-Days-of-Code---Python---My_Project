const canvas = document.getElementById("binaryCanvas");
const ctx = canvas.getContext("2d");

// =============================
// SETTINGS
// =============================
const FONT_SIZE = 12;
const FONT = `${FONT_SIZE}px monospace`;
const SPACING_X = 10;
const SPACING_Y = 13;

const FIELD_SCALE = 1.5;
const SPEED = 1.5;

let particles = [];
let fieldWidth = 0;
let fieldHeight = 0;
let move = 0;

const ANGLE = Math.PI / 4;
const COS_A = Math.cos(ANGLE);
const SIN_A = Math.sin(ANGLE);

// =============================
// PRE-COMPUTED COLOR CACHE
// =============================

const colorCache = [];
for (let i = 0; i <= 100; i++) {
    const darkness = i / 100;
    // Visibility outside the wave
    const baseOpacity = 0.15;
    // Stronger wave
    const opacity = baseOpacity + darkness * 0.85;
    // Light gray → white
    const shade = Math.floor(140 + darkness * 115);
    colorCache.push(
        `rgba(${shade},${shade},${shade},${opacity.toFixed(3)})`
    );

}

// =============================

function resizeCanvas() {
    canvas.width = canvas.offsetWidth || window.innerWidth;
    canvas.height = canvas.offsetHeight || window.innerHeight;
    createBinaryField();
}

window.addEventListener("resize", resizeCanvas);

// =============================

function createBinaryField() {
    particles = [];

    const diagonal = Math.sqrt(
        canvas.width * canvas.width +
        canvas.height * canvas.height
    );

    const rows = Math.ceil((diagonal * FIELD_SCALE) / SPACING_Y);
    fieldHeight = rows * SPACING_Y;

    const cols = Math.ceil((diagonal * FIELD_SCALE) / SPACING_X);
    fieldWidth = cols * SPACING_X;

    for (let row = 0; row < rows; row++) {
        const rowOffset =
            Math.sin(row * 0.28) * 40 +
            Math.sin(row * 0.09) * 25 +
            (Math.random() - 0.5) * 12;

        for (let col = 0; col < cols; col++) {
            const x = col * SPACING_X - fieldWidth / 2 + rowOffset;
            const y = row * SPACING_Y - fieldHeight / 2;

            particles.push({
                x,
                y,
                value: Math.random() > 0.5 ? "1" : "0",
            });
        }
    }
}

// =============================

function updateBinaryValues() {
    const changes = Math.floor(particles.length * 0.001);
    for (let i = 0; i < changes; i++) {
        const index = Math.floor(Math.random() * particles.length);
        particles[index].value = Math.random() > 0.5 ? "1" : "0";
    }
}

// =============================

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.save();
    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.font = FONT;

    // We want text baselines consistent for optimal rendering
    ctx.textBaseline = "middle";

    const BAND_WIDTH = 500;
    const WAVE_SPACING = 900;
    const diagHalf = Math.max(canvas.width, canvas.height);

    // 1. Create empty batches for our 101 possible colors
    const batches = Array.from({ length: 101 }, () => []);

    // 2. Sort particles into color batches
    const len = particles.length;
    for (let i = 0; i < len; i++) {
        const p = particles[i];
        const worldX = p.x;

        let worldY = p.y + move;
        worldY = ((worldY + fieldHeight / 2) % fieldHeight);
        if (worldY < 0) worldY += fieldHeight;
        worldY -= fieldHeight / 2;

        const currentX = worldX * COS_A - worldY * SIN_A;
        const currentY = worldX * SIN_A + worldY * COS_A;

        // Cull offscreen particles
        if (currentX < -diagHalf || currentX > diagHalf ||
            currentY < -diagHalf || currentY > diagHalf) {
            continue;
        }

        const wavePosition = (currentX - currentY) + move;
        let distance = ((wavePosition % WAVE_SPACING) + WAVE_SPACING) % WAVE_SPACING;
        distance = Math.min(distance, WAVE_SPACING - distance);

        let darkness = 1 - distance / BAND_WIDTH;
        darkness = Math.max(0, Math.min(darkness, 1));
        darkness = Math.pow(darkness, 1.4);

        const colorIndex = Math.floor(darkness * 100);

        // Push raw values into the flat batch array to avoid creating objects
        batches[colorIndex].push(p.value, currentX, currentY);
    }

    // 3. Draw the batches (This is where the massive performance gain happens)
    for (let i = 0; i <= 100; i++) {
        const batch = batches[i];
        if (batch.length === 0) continue;

        // Set the color EXACTLY ONCE per shade level
        ctx.fillStyle = colorCache[i];

        // Loop through the flat array (value, x, y, value, x, y...)
        for (let j = 0; j < batch.length; j += 3) {
            // Removed Math.round() so 0.5 speed glides smoothly
            ctx.fillText(batch[j], batch[j+1], batch[j+2]);
        }
    }

    ctx.restore();
}

// =============================

let lastTime = 0;

function animate(time) {
    if (!lastTime) lastTime = time;

    // Smooth delta calculation to prevent micro-stutters on 144Hz monitors
    let delta = (time - lastTime) / 16.67;
    if (delta > 2) delta = 2;

    lastTime = time;

    move -= SPEED * delta;

    updateBinaryValues();
    draw();
    requestAnimationFrame(animate);
}

// =============================
resizeCanvas();
requestAnimationFrame(animate);