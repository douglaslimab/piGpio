const btnGpio = document.getElementById('btn-gpio')
const gpio = document.getElementById('gpio')
const uart = document.getElementById('uart')
const sensors = document.getElementById('sensors')

btnGpio.addEventListener('click', function(){
    uart.classList.add('hide')
})