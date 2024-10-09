let score = 0;
let increment = 1;
let increment2 = 0;
let score1 = 0;
let score2 = 0;
let score3 = 0;
let score4 = 0;
let score5 = 0;
let score6 = 0;

function initializeScore(key) {
    if (localStorage.getItem(key) === null) {
        localStorage.setItem(key, 0);
        return 0;
    }
    return parseInt(localStorage.getItem(key));
}

function updateLocalStorage() {
    localStorage.setItem("score", score);
    localStorage.setItem("score1", score1);
    localStorage.setItem("score2", score2);
    localStorage.setItem("score3", score3);
    localStorage.setItem("score4", score4);
    localStorage.setItem("score5", score5);
    localStorage.setItem("score6", score6);
    localStorage.setItem("increment", increment);
    localStorage.setItem("increment2", increment2);
}

function updateDisplay() {
    document.getElementById("score").innerText = `SCORE : ${score}`;
    document.getElementById("nomb1").innerText = `${score1}`;
    document.getElementById("nomb2").innerText = `${score2}`;
    document.getElementById("nomb3").innerText = `${score3}`;
    document.getElementById("nombmachine").innerText = `${score4}`;
    document.getElementById("nombboudinieresexy").innerText = `${score5}`;
    document.getElementById("nombgrandmaitreboudinier").innerText = `${score6}`;
    document.getElementById("click").innerText = `B/C : ${increment}`;
    document.getElementById("auto").innerText = `B/S : ${increment2}`;
}

function addScore() {
    score += increment2; 
    updateDisplay();    
    updateLocalStorage();
}

score1 = initializeScore("score1");  
score2 = initializeScore("score2");
score3 = initializeScore("score3");
score = initializeScore("score");
increment = initializeScore("increment");
increment2 = initializeScore("increment2");

updateLocalStorage();
updateDisplay();

setInterval(addScore,1000);

document.getElementById("reset").addEventListener("click", () => {
    localStorage.clear();
    score = 0;
    increment = 1;
    increment2 = 0;
    score1 = 0;
    score2 = 0;
    score3 = 0;
    updateDisplay();
    updateLocalStorage();
});

document.getElementById("boudinimage").addEventListener("click", () => {
    score += increment;
    updateDisplay();
    updateLocalStorage();
});

document.getElementById("boudiniere").addEventListener("click", () => {
    if (score >=100) {
        score1 += 1;
        increment +=1;
        score -= 100;
        updateDisplay();
        updateLocalStorage();
}});

document.getElementById("boudinieresexyimage").addEventListener("click", () => {
    if (score >=10000) {
        score5 += 1;
        increment +=200;
        score -= 10000;
        updateDisplay();
        updateLocalStorage();
}});

document.getElementById("grandmaitreboudinierimage").addEventListener("click", () => {
    if (score >=1000000) {
        score6 += 1;
        increment +=5000;
        score -= 1000000;
        updateDisplay();
        updateLocalStorage();
    
}});

document.getElementById("machine").addEventListener("click", () => {
    if (score >=500) {
        score4 += 1;
        increment2 +=1;
        score -= 500;
        updateDisplay();
        updateLocalStorage();
}});


document.getElementById("boucherie").addEventListener("click", () => {
    if (score >=50000) {
        score2 += 1;
        increment2 +=200;
        score -= 50000;
        updateDisplay();
        updateLocalStorage();
}});

document.getElementById("usine").addEventListener("click", () => {
    if (score >=5000000) {
        score3 += 1;
        increment2 +=5000;
        score -= 5000000;
        updateDisplay();
        updateLocalStorage();
}});

document.getElementById("p2").addEventListener("click", () => {
    score+=1000000;
});