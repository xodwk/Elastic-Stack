function vulnerableFunction(userInput) {
    // 취약점: XSS
    document.getElementById("output").innerHTML = userInput;
}

function secureFunction(userInput) {
    // 보안: HTML 엔코딩
    document.getElementById("output").textContent = userInput;
}
