// Get progress bar that contains cart total as data attribute
let progressBar = document.getElementById("progress-bar");
console.log("progressbar: " + progressBar);

// Get cart total from data attribute
let total = Math.floor(progressBar.dataset.total)
console.log("total: " + total)

// Multiply total by two to get percentage of delivery threshold
percentage = total * 2
console.log("Percentage: " + percentage)

// Get inner div of progress bar
let percentageBar = document.getElementById("percentage");
console.log("percentageBar: " + percentageBar)

// Set percentage width of inner div to delivery threshold percentage
percentageBar.style.width = `${percentage}%`

// Pad free delivery span relative to percentage bar
document.getElementById("free-delivery").style.paddingLeft = `${percentage}%`;