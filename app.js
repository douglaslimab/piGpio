const btnGpio = document.getElementById('btn-gpio')
const btnUart = document.getElementById('btn-uart')
const btnSensors = document.getElementById('btn-sensors')

const gpio = document.getElementById('gpio')
const uart = document.getElementById('uart')
const sensors = document.getElementById('sensors')

btnGpio.addEventListener('click', function(){
    gpio.classList.remove('hide')
    uart.classList.add('hide')
    sensors.classList.add('hide')

    btnGpio.classList.add('pressed')
    btnUart.classList.remove('pressed')
    btnSensors.classList.remove('pressed')
})

btnUart.addEventListener('click', function(){
    uart.classList.remove('hide')
    gpio.classList.add('hide')
    sensors.classList.add('hide')

    btnUart.classList.add('pressed')
    btnGpio.classList.remove('pressed')
    btnSensors.classList.remove('pressed')
})

btnSensors.addEventListener('click', function(){
    sensors.classList.remove('hide')
    gpio.classList.add('hide')
    uart.classList.add('hide')

    btnSensors.classList.add('pressed')
    btnGpio.classList.remove('pressed')
    btnUart.classList.remove('pressed')
})