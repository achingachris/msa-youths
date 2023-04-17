console.log("Hello from script.js");

function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const sec = seconds % 60;
    return `${hours}h ${minutes}m ${sec}s`;
  }
  
  function updateCountdown(remainingTime, timeRemainingElement) {
    if (remainingTime <= 0) {
      clearInterval(interval);
      timeRemainingElement.innerHTML = "You can now vote again!";
    } else {
      timeRemainingElement.innerHTML = formatTime(remainingTime);
      remainingTime--;
    }
  }
  
  function startCountdown(remainingTime) {
    const timeRemainingElement = document.getElementById("time-remaining");
    const interval = setInterval(() => updateCountdown(remainingTime, timeRemainingElement), 1000);
    updateCountdown(remainingTime, timeRemainingElement);
  }
  